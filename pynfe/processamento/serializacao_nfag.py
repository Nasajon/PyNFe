from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from typing import Any, Dict, Optional, TYPE_CHECKING, List

from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from pynfe.entidades.nfag import (
    NotaFiscalAgua,
    NotaFiscalAguaAgencia,
    NotaFiscalAguaAgenciaConsumo,
    NotaFiscalAguaAgenciaHistorico,
    NotaFiscalAguaFatura,
    NotaFiscalAguaItem,
    NotaFiscalAguaItemCOFINS,
    NotaFiscalAguaItemImposto,
    NotaFiscalAguaItemMedicao,
    NotaFiscalAguaItemPIS,
    NotaFiscalAguaMedidor,
    NotaFiscalAguaSubstituicao,
    NotaFiscalAguaTarifa,
)
from pynfe.entidades.ibs_cbs import IBS_CBS
from pynfe.utils import obter_codigo_por_municipio, so_numeros
from pynfe.utils.ibs_cbs_indicadores import IBSCBSIndicadores
from pynfe.utils.flags import CODIGOS_ESTADOS

from pynfe_nasajon.pynfe.utils.nfag.dfe_tipos_basicos_v1_00 import (
    Tcibs,
    TdevTrib,
    Tdif,
    TestornoCred,
    Tibscbstot,
    Tmonofasia,
    Tred,
    TtribCompraGov,
    TtribNfag,
    TtribRegular,
)
from pynfe_nasajon.pynfe.utils.nfag.nfag_tipos_basico_v1_00 import (
    CofinsCst,
    PisCst,
    ProdIndDevolucao,
    Tfaixa,
    TcategAg,
    TgrMedAg,
    Tligacao,
    TmedidaAg,
    TmotNaoLeitura,
    TmotSubAg,
    Tnfag,
    TendeEmi,
    TfatNfag,
    TfinNfag,
    TorigemQtdAg,
    TtpEmis,
    TumedAg,
    TumedItemAg,
)
from pynfe_nasajon.pynfe.utils.nfag.tipos_geral_nfag_v1_00 import (
    Tamb,
    TcodUfIbge,
    TmodNfag,
    TufSemEx,
)
from pynfe_nasajon.pynfe.utils.nfag.nfag_v1_00 import Nfag

if TYPE_CHECKING:
    from pynfe_nasajon.pynfe.utils.nfag.evento_nfag_v1_00 import EventoNfag


NFAG_NAMESPACE = "http://www.portalfiscal.inf.br/nfag"
XMLDSIG_NAMESPACE = "http://www.w3.org/2000/09/xmldsig#"


class SerializacaoNFAg:
    """Serializacao XML para NFAg usando xsdata."""

    def __init__(self, pretty_print: bool = False) -> None:
        config = SerializerConfig(
            xml_declaration=False,
            pretty_print=pretty_print,
        )
        self._serializer = XmlSerializer(config=config)

    def gerar(self, nfag: "Nfag") -> str:
        """Serializa o XML da NFAg."""
        if isinstance(nfag, NotaFiscalAgua):
            payload = self._build_nfag_from_nota(nfag)
        else:
            payload = nfag
        return self._serialize(payload)

    def registrar_evento(self, evento: "EventoNfag") -> str:
        """Serializa o XML do pedido de registro de evento da NFAg."""
        return self._serialize(evento)

    def _serialize(self, payload: Any, ns_map: Optional[Dict[str, str]] = None) -> str:
        if ns_map is None:
            ns_map = {
                None: NFAG_NAMESPACE,
                "ds": XMLDSIG_NAMESPACE,
            }
        return self._serializer.render(payload, ns_map=ns_map)

    def _build_nfag_from_nota(self, nota: NotaFiscalAgua) -> Nfag:
        if not nota.emitente or not nota.destinatario:
            raise ValueError("emitente e destinatario sao obrigatorios para gerar NFAg.")

        # Necessário chamar o id aqui para preencher o número aleatório e digito verificador, que são usados no ide
        id=nota.identificador_unico

        det_list = self._build_det_list(nota)
        total = self._build_total(nota)

        ide = self._build_ide(nota)
        emit = self._build_emit(nota)
        dest = self._build_dest(nota)
        ligacao = self._build_ligacao(nota)

        inf_nfag = Tnfag.InfNfag(
            ide=ide,
            emit=emit,
            dest=dest,
            ligacao=ligacao,
            g_sub=self._build_g_sub(nota.g_substituicao),
            g_med=self._build_g_med_list(nota.g_medidores),
            g_fat_conjunto=self._build_g_fat_conjunto(nota.g_fat_conjunto_chave),
            det=det_list,
            total=total,
            g_fat=self._build_g_fat(nota.g_fat),
            g_agencia=self._build_g_agencia(nota.g_agencia),
            g_quali_agua=None,
            aut_xml=nota.autorizados_xml or [],
            inf_adic=nota.informacoes_adicionais,
            inf_paa=None,
            g_resp_tec=nota.responsavel_tecnico,
            versao="1.00",
            id=id,
        )

        return Nfag(
            inf_nfag=inf_nfag,
            signature=None,  # A assinatura deve ser adicionada posteriormente
            inf_nfag_supl=None,  # Suplementar pode ser adicionado posteriormente
        )

    def _build_g_sub(
        self, g_sub: Optional[NotaFiscalAguaSubstituicao]
    ) -> Optional[Tnfag.InfNfag.GSub]:
        if g_sub is None:
            return None
        if isinstance(g_sub, Tnfag.InfNfag.GSub):
            return g_sub
        return Tnfag.InfNfag.GSub(
            ch_nfag=str(g_sub.chave_nfag_referenciada),
            mot_sub=self._enum_value(TmotSubAg, str(g_sub.motivo_substituicao)),
        )

    def _build_g_med_list(self, medidores) -> List[Tnfag.InfNfag.GMed]:
        medidores = medidores or []
        g_med_list: List[Tnfag.InfNfag.GMed] = []
        for medidor in medidores:
            if isinstance(medidor, Tnfag.InfNfag.GMed):
                g_med_list.append(medidor)
                continue
            if not isinstance(medidor, NotaFiscalAguaMedidor):
                raise ValueError("Medidores devem ser NotaFiscalAguaMedidor ou GMed.")
            g_med_list.append(
                Tnfag.InfNfag.GMed(
                    id_medidor=str(medidor.identificacao_medidor),
                    d_med_ant=str(medidor.data_leitura_anterior),
                    d_med_atu=str(medidor.data_leitura_atual),
                    n_med=str(medidor.numero_referencia_medicao),
                )
            )
        return g_med_list

    def _build_g_fat_conjunto(self, chave_nfag) -> Optional[Tnfag.InfNfag.GFatConjunto]:
        if not chave_nfag:
            return None
        if isinstance(chave_nfag, Tnfag.InfNfag.GFatConjunto):
            return chave_nfag
        return Tnfag.InfNfag.GFatConjunto(ch_nfag_fat=str(chave_nfag))

    def _build_g_fat(self, g_fat: Optional[NotaFiscalAguaFatura]) -> Optional[Tnfag.InfNfag.GFat]:
        if g_fat is None:
            return None
        if isinstance(g_fat, Tnfag.InfNfag.GFat):
            return g_fat

        ender_corresp = None
        if g_fat.endereco_correspondencia:
            ender = g_fat.endereco_correspondencia
            ender_corresp = self._build_endereco(
                ender.logradouro,
                ender.numero,
                ender.complemento,
                ender.bairro,
                ender.codigo_municipio,
                ender.municipio,
                ender.cep,
                ender.uf,
                ender.telefone,
                ender.email,
            )

        g_pix = None
        if g_fat.pix:
            g_pix = Tnfag.InfNfag.GFat.GPix(url_qrcode_pix=g_fat.pix.url_qrcode_pix)

        return Tnfag.InfNfag.GFat(
            compet_fat=str(g_fat.competencia_faturamento),
            d_venc_fat=str(g_fat.data_vencimento),
            d_apres_fat=str(g_fat.data_apresentacao) if g_fat.data_apresentacao else None,
            d_prox_leitura=str(g_fat.data_proxima_leitura),
            n_fat=str(g_fat.numero_fatura) if g_fat.numero_fatura else None,
            cod_barras=str(g_fat.codigo_barras),
            cod_deb_auto=str(g_fat.codigo_debito_automatico)
            if g_fat.codigo_debito_automatico
            else None,
            cod_banco=str(g_fat.codigo_banco) if g_fat.codigo_banco and not g_fat.codigo_debito_automatico else None,
            cod_agencia=str(g_fat.codigo_agencia) if g_fat.codigo_agencia and not g_fat.codigo_debito_automatico else None,
            ender_corresp=ender_corresp,
            g_pix=g_pix,
        )

    def _build_g_agencia(
        self, g_agencia: Optional[NotaFiscalAguaAgencia]
    ) -> Tnfag.InfNfag.GAgencia:
        if g_agencia is None:
            raise ValueError("g_agencia e obrigatorio para gerar NFAg.")
        if isinstance(g_agencia, Tnfag.InfNfag.GAgencia):
            return g_agencia

        g_hist_cons = []
        for historico in g_agencia.historicos or []:
            if isinstance(historico, Tnfag.InfNfag.GAgencia.GHistCons):
                g_hist_cons.append(historico)
                continue
            if not isinstance(historico, NotaFiscalAguaAgenciaHistorico):
                raise ValueError("Historicos devem ser NotaFiscalAguaAgenciaHistorico.")

            g_cons = []
            for consumo in historico.consumos or []:
                if isinstance(consumo, Tnfag.InfNfag.GAgencia.GHistCons.GCons):
                    g_cons.append(consumo)
                    continue
                if not isinstance(consumo, NotaFiscalAguaAgenciaConsumo):
                    raise ValueError("Consumos devem ser NotaFiscalAguaAgenciaConsumo.")

                g_cons.append(
                    Tnfag.InfNfag.GAgencia.GHistCons.GCons(
                        compet_fat=str(consumo.competencia_faturamento),
                        u_med=self._enum_value(TumedAg, str(consumo.unidade_medida)),
                        qtd_dias=str(consumo.quantidade_dias).zfill(5),
                        med_diaria=self._fmt_qty(consumo.media_diaria)
                        if consumo.media_diaria is not None
                        else None,
                        consumo=self._fmt_money(consumo.consumo)
                        if consumo.consumo is not None
                        else None,
                        vol_fat=self._fmt_money(consumo.volume_faturado),
                    )
                )

            g_hist_cons.append(
                Tnfag.InfNfag.GAgencia.GHistCons(
                    x_historico=str(historico.nome_historico),
                    g_cons=g_cons,
                    med_mensal=self._fmt_qty(historico.media_mensal),
                )
            )

        return Tnfag.InfNfag.GAgencia(
            econ=str(g_agencia.economia_agua) if g_agencia.economia_agua else None,
            econ_acumulada=str(g_agencia.economia_agua_acumulada)
            if g_agencia.economia_agua_acumulada
            else None,
            s_prestador=str(g_agencia.selo_prestador) if g_agencia.selo_prestador else None,
            d_emiss_selo=str(g_agencia.data_emissao_selo)
            if g_agencia.data_emissao_selo
            else None,
            s_regulador=str(g_agencia.selo_regulador) if g_agencia.selo_regulador else None,
            n_agencia_atend=str(g_agencia.nome_agencia_atendimento),
            ender_agencia_atend=str(g_agencia.endereco_agencia_atendimento),
            g_hist_cons=g_hist_cons,
        )

    def _build_ligacao(self, nota: NotaFiscalAgua) -> Tnfag.InfNfag.Ligacao:
        if isinstance(nota.ligacao_id, Tnfag.InfNfag.Ligacao):
            return nota.ligacao_id

        if not nota.ligacao_id:
            raise ValueError("ligacao_id e obrigatorio para gerar NFAg.")
        if not nota.ligacao_tipo:
            raise ValueError("ligacao_tipo e obrigatorio para gerar NFAg.")
        if nota.ligacao_latitude_gps is None or nota.ligacao_longitude_gps is None:
            raise ValueError("ligacao_latitude_gps e ligacao_longitude_gps sao obrigatorios.")

        return Tnfag.InfNfag.Ligacao(
            id_ligacao=str(nota.ligacao_id),
            id_cod_cliente=str(nota.ligacao_codigo_cliente)
            if nota.ligacao_codigo_cliente
            else None,
            tp_ligacao=self._enum_value(Tligacao, str(nota.ligacao_tipo)),
            lat_gps=str(nota.ligacao_latitude_gps),
            long_gps=str(nota.ligacao_longitude_gps),
            cod_roteiro_leitura=str(nota.ligacao_codigo_roteiro_leitura)
            if nota.ligacao_codigo_roteiro_leitura
            else None,
        )

    def _build_ide(self, nota: NotaFiscalAgua) -> Tnfag.InfNfag.Ide:
        tz = datetime.now().astimezone().strftime("%z")
        tz = "{}:{}".format(tz[:-2], tz[-2:])

        uf = nota.uf or (nota.emitente.endereco_uf if nota.emitente else None)
        if not uf:
            raise ValueError("UF e obrigatoria para gerar NFAg.")

        c_mun_fg = self._codigo_municipio(
            nota.municipio_fato_gerador,
            nota.uf or nota.emitente.endereco_uf,
            nota.emitente.endereco_cod_municipio if nota.emitente else None,
            nota.emitente.endereco_municipio if nota.emitente else None,
        )

        return Tnfag.InfNfag.Ide(
            c_uf=self._enum_value(TcodUfIbge, str(CODIGOS_ESTADOS[uf])),
            tp_amb=self._enum_value(Tamb, str(nota.ambiente)),
            mod=self._enum_value(TmodNfag, str(nota.modelo)),
            serie=str(nota.serie),
            n_nf=str(nota.numero),
            c_nf=str(nota.codigo_numerico_aleatorio),
            c_dv=nota.identificador_unico[-1],
            dh_emi=nota.data_emissao.strftime("%Y-%m-%dT%H:%M:%S") + tz,
            tp_emis=self._enum_value(TtpEmis, str(nota.tipo_emissao)),
            n_site_autoriz=str(nota.site_autoriz),
            c_mun_fg=str(c_mun_fg),
            fin_nfag=self._enum_value(TfinNfag, str(nota.finalidade)),
            tp_fat=self._enum_value(TfatNfag, str(nota.tipo_faturamento)),
            ver_proc=str(nota.versao_processo_emissao),
            dh_cont=nota.data_contingencia,
            x_just=nota.justificativa_contingencia,
            g_compra_gov=nota.compra_governo,
        )

    def _build_emit(self, nota: NotaFiscalAgua) -> Tnfag.InfNfag.Emit:
        emit = nota.emitente
        ender_emit = self._build_endereco(
            emit.endereco_logradouro,
            emit.endereco_numero,
            emit.endereco_complemento,
            emit.endereco_bairro,
            emit.endereco_cod_municipio,
            emit.endereco_municipio,
            emit.endereco_cep,
            emit.endereco_uf,
            emit.endereco_telefone,
            None,
        )

        return Tnfag.InfNfag.Emit(
            cnpj=so_numeros(emit.cnpj).zfill(14),
            ie=so_numeros(emit.inscricao_estadual),
            x_nome=emit.razao_social,
            x_fant=emit.nome_fantasia or None,
            ender_emit=ender_emit,
        )

    def _build_dest(self, nota: NotaFiscalAgua) -> Tnfag.InfNfag.Dest:
        dest = nota.destinatario
        ender_dest = self._build_endereco(
            dest.endereco_logradouro,
            dest.endereco_numero,
            dest.endereco_complemento,
            dest.endereco_bairro,
            dest.endereco_cod_municipio,
            dest.endereco_municipio,
            dest.endereco_cep,
            dest.endereco_uf,
            dest.endereco_telefone,
            dest.email,
        )

        return Tnfag.InfNfag.Dest(
            x_nome=dest.razao_social,
            cnpj=so_numeros(dest.numero_documento).zfill(14)
            if dest.tipo_documento == "CNPJ"
            else None,
            cpf=so_numeros(dest.numero_documento).zfill(11)
            if dest.tipo_documento == "CPF"
            else None,
            id_outros=None,
            ie=so_numeros(dest.inscricao_estadual) if dest.inscricao_estadual else None,
            im=dest.inscricao_municipal or None,
            c_nis=None,
            nb=None,
            x_nome_adicional=None,
            ender_dest=ender_dest,
        )

    def _build_endereco(
        self,
        logradouro: str,
        numero: str,
        complemento: str,
        bairro: str,
        codigo_municipio: str,
        municipio: str,
        cep: str,
        uf: str,
        telefone: str,
        email: Optional[str],
    ) -> TendeEmi:
        c_mun = self._codigo_municipio(codigo_municipio, uf, codigo_municipio, municipio)
        return TendeEmi(
            x_lgr=logradouro,
            nro=str(numero),
            x_cpl=complemento or None,
            x_bairro=bairro,
            c_mun=str(c_mun),
            x_mun=municipio,
            cep=so_numeros(cep).zfill(8),
            uf=self._enum_value(TufSemEx, str(uf)),
            fone=so_numeros(telefone) if telefone else None,
            email=email or None,
        )

    def _codigo_municipio(
        self,
        valor: Optional[str],
        uf: Optional[str],
        codigo_fallback: Optional[str],
        municipio_fallback: Optional[str],
    ) -> str:
        if valor and str(valor).isdigit() and len(str(valor)) == 7:
            return str(valor)
        if codigo_fallback and str(codigo_fallback).isdigit():
            return str(codigo_fallback).zfill(7)
        if municipio_fallback and uf:
            return str(obter_codigo_por_municipio(municipio_fallback, uf))
        raise ValueError("Codigo do municipio invalido para NFAg.")

    def _build_det_list(self, nota: NotaFiscalAgua) -> List[Tnfag.InfNfag.Det]:
        if not nota.itens:
            raise ValueError("Informe pelo menos um item para a NFAg.")

        det_list: List[Tnfag.InfNfag.Det] = []
        for idx, item in enumerate(nota.itens, start=1):
            if isinstance(item, Tnfag.InfNfag.Det):
                det_list.append(item)
                continue

            if not isinstance(item, NotaFiscalAguaItem):
                raise ValueError("Itens devem ser NotaFiscalAguaItem ou Det.")

            det_list.append(self._build_det_from_item(item, idx))

        return det_list

    def _build_det_from_item(self, item: NotaFiscalAguaItem, idx: int) -> Tnfag.InfNfag.Det:
        n_item = str(item.numero_item or idx)

        g_tarif = []
        for tarifa in item.tarifas or []:
            if isinstance(tarifa, Tnfag.InfNfag.Det.GTarif):
                g_tarif.append(tarifa)
                continue
            if not isinstance(tarifa, NotaFiscalAguaTarifa):
                raise ValueError("Tarifas devem ser NotaFiscalAguaTarifa.")
            g_tarif.append(
                Tnfag.InfNfag.Det.GTarif(
                    d_ini_tarif=str(tarifa.data_inicio_tarifa),
                    d_fim_tarif=str(tarifa.data_fim_tarifa) if tarifa.data_fim_tarifa else None,
                    n_ato=str(tarifa.numero_ato),
                    ano_ato=str(tarifa.ano_ato),
                    tp_faixa_cons=self._enum_value(Tfaixa, str(tarifa.faixa_consumo))
                    if tarifa.faixa_consumo is not None
                    else None,
                )
            )

        g_medicao = None
        if item.medicao:
            if isinstance(item.medicao, Tnfag.InfNfag.Det.Prod.GMedicao):
                g_medicao = item.medicao
            elif isinstance(item.medicao, NotaFiscalAguaItemMedicao):
                g_medida = None
                if (
                    item.medicao.unidade_medida
                    or item.medicao.valor_medido is not None
                    or item.medicao.tipo_grandeza_medida
                    or item.medicao.valor_medicao_anterior is not None
                    or item.medicao.valor_medicao_atual is not None
                ):
                    g_medida = TmedidaAg(
                        tp_gr_med=self._enum_value(
                            TgrMedAg, str(item.medicao.tipo_grandeza_medida)
                        )
                        if item.medicao.tipo_grandeza_medida
                        else None,
                        u_med=self._enum_value(TumedAg, str(item.medicao.unidade_medida)),
                        v_med_ant=self._fmt_qty(item.medicao.valor_medicao_anterior)
                        if item.medicao.valor_medicao_anterior is not None
                        else None,
                        v_med_atu=self._fmt_qty(item.medicao.valor_medicao_atual)
                        if item.medicao.valor_medicao_atual is not None
                        else None,
                        v_med=self._fmt_qty(item.medicao.valor_medido),
                    )
                g_medicao = Tnfag.InfNfag.Det.Prod.GMedicao(
                    n_med=str(item.medicao.numero_medicao),
                    g_medida=g_medida,
                    tp_mot_nao_leitura=self._enum_value(
                        TmotNaoLeitura, str(item.medicao.motivo_nao_leitura)
                    )
                    if item.medicao.motivo_nao_leitura is not None
                    else None,
                )

        prod = Tnfag.InfNfag.Det.Prod(
            ind_origem_qtd=self._enum_value(
                TorigemQtdAg, str(item.ind_origem_quantidade or "2")
            ),
            g_medicao=g_medicao,
            c_prod=str(item.codigo or "0"),
            x_prod=str(item.descricao or "Item"),
            c_class=str(item.classificacao_item or "0000000"),
            tp_categoria=self._enum_value(TcategAg, str(item.categoria_ligacao))
            if item.categoria_ligacao
            else None,
            x_categoria=str(item.categoria_detalhe) if item.categoria_detalhe else None,
            q_economias=str(item.quantidade_economias) if item.quantidade_economias else None,
            u_med=self._enum_value(TumedItemAg, str(item.unidade_medida or "1")),
            q_faturada=self._fmt_qty(item.quantidade_faturada),
            v_item=self._fmt_money(item.valor_unitario),
            fator_poluicao=self._fmt_money(item.fator_poluicao)
            if item.fator_poluicao is not None
            else None,
            v_prod=self._fmt_money(item.valor_total),
            ind_devolucao=self._enum_value(ProdIndDevolucao, "1")
            if item.indicador_devolucao
            else None,
        )

        imposto = self._build_imposto(item)

        return Tnfag.InfNfag.Det(
            g_tarif=g_tarif,
            prod=prod,
            imposto=imposto,
            g_proc_ref=None,
            inf_ad_prod=item.informacoes_adicionais or None,
            n_item=n_item,
            ch_nfag_ant=item.chave_nfag_anterior or None,
            n_item_ant=str(item.numero_item_anterior) if item.numero_item_anterior else None,
        )

    def _build_imposto(self, item: NotaFiscalAguaItem) -> Tnfag.InfNfag.Det.Imposto:
        data: Optional[NotaFiscalAguaItemImposto] = item.imposto
        if data is None:
            raise ValueError("imposto e obrigatorio para os itens da NFAg.")

        ibscbs = self._build_ibscbs(data.ibs_cbs)
        if ibscbs is None:
            raise ValueError("imposto.ibs_cbs e obrigatorio quando informado imposto do item.")

        imposto = Tnfag.InfNfag.Det.Imposto(ibscbs=ibscbs)

        pis = self._build_pis(data.pis)
        if pis:
            imposto.pis = pis

        cofins = self._build_cofins(data.cofins)
        if cofins:
            imposto.cofins = cofins

        ret_trib = self._build_ret_trib(data)
        if ret_trib:
            imposto.ret_trib = ret_trib

        tfs = self._build_tfs(data.tfs_base_calculo, data.tfs_aliquota, data.tfs_valor)
        if tfs:
            imposto.tfs = tfs

        tfu = self._build_tfu(data.tfu_base_calculo, data.tfu_aliquota, data.tfu_valor)
        if tfu:
            imposto.tfu = tfu

        return imposto

    def _build_ibscbs(self, data: Optional[IBS_CBS]) -> Optional[TtribNfag]:
        if data is None:
            return None

        if not data.modalidade:
            raise ValueError("imposto.ibs_cbs.modalidade (CST) e obrigatorio.")
        if not data.classificacao:
            raise ValueError("imposto.ibs_cbs.classificacao (cClassTrib) e obrigatorio.")

        cst = data.modalidade
        c_class_trib = data.classificacao

        indicadores_cst = IBSCBSIndicadores.obter_por_cst(str(cst))
        indicadores_classtrib = IBSCBSIndicadores.obter_por_classificacao(
            str(c_class_trib)
        )

        def grupo_permitido(*chaves):
            return IBSCBSIndicadores.grupo_permitido(
                chaves, indicadores_cst, indicadores_classtrib
            )

        if data.monofasico:
            raise ValueError("imposto.ibs_cbs.monofasico nao e suportado para NFAg.")

        g_ibscbs = None
        if grupo_permitido("ind_gIBSCBS"):
            self._validar_ibscbs_padrao(data)
            g_ibscbs = self._build_ibscbs_padrao(data, grupo_permitido)
        elif grupo_permitido("ind_gIBSCBSMono"):
            raise ValueError("imposto.ibs_cbs.monofasico nao e suportado para NFAg.")

        estorno = None
        if data.estorno and grupo_permitido("ind_gEstornoCred"):
            estorno = TestornoCred(
                v_ibsest_cred=self._fmt_money(data.estorno.valor_ibs),
                v_cbsest_cred=self._fmt_money(data.estorno.valor_cbs),
            )

        return TtribNfag(
            cst=str(cst),
            c_class_trib=str(c_class_trib),
            g_ibscbs=g_ibscbs,
            g_estorno_cred=estorno,
        )

    def _build_ibscbs_padrao(self, data: IBS_CBS, grupo_permitido) -> Tcibs:
        ibs_uf = data.ibs_uf
        ibs_mun = data.ibs_mun
        cbs = data.cbs

        g_ibsuf = Tcibs.GIbsuf(
            p_ibsuf=self._fmt_money(ibs_uf.aliquota),
            v_ibsuf=self._fmt_money(ibs_uf.valor),
            g_dif=self._build_dif(ibs_uf) if grupo_permitido("ind_gDif") else None,
            g_dev_trib=self._build_dev_trib(ibs_uf),
            g_red=self._build_red(ibs_uf) if grupo_permitido("ind_gRed") else None,
        )
        g_ibsmun = Tcibs.GIbsmun(
            p_ibsmun=self._fmt_money(ibs_mun.aliquota),
            v_ibsmun=self._fmt_money(ibs_mun.valor),
            g_dif=self._build_dif(ibs_mun) if grupo_permitido("ind_gDif") else None,
            g_dev_trib=self._build_dev_trib(ibs_mun),
            g_red=self._build_red(ibs_mun) if grupo_permitido("ind_gRed") else None,
        )
        g_cbs = Tcibs.GCbs(
            p_cbs=self._fmt_money(cbs.aliquota),
            v_cbs=self._fmt_money(cbs.valor),
            g_dif=self._build_dif(cbs) if grupo_permitido("ind_gDif") else None,
            g_dev_trib=self._build_dev_trib(cbs),
            g_red=self._build_red(cbs) if grupo_permitido("ind_gRed") else None,
        )

        g_trib_regular = None
        if data.trib_reg and grupo_permitido("ind_gTribRegular"):
            reg = data.trib_reg
            g_trib_regular = TtribRegular(
                cstreg=str(reg.modalidade),
                c_class_trib_reg=str(reg.classificacao),
                p_aliq_efet_reg_ibsuf=self._fmt_money(reg.aliquota_ibs_uf),
                v_trib_reg_ibsuf=self._fmt_money(reg.valor_ibs_uf),
                p_aliq_efet_reg_ibsmun=self._fmt_money(reg.aliquota_ibs_mun),
                v_trib_reg_ibsmun=self._fmt_money(reg.valor_ibs_mun),
                p_aliq_efet_reg_cbs=self._fmt_money(reg.aliquota_cbs),
                v_trib_reg_cbs=self._fmt_money(reg.valor_cbs),
            )

        g_trib_compra_gov = None
        if data.compra_gov:
            gov = data.compra_gov
            g_trib_compra_gov = TtribCompraGov(
                p_aliq_ibsuf=self._fmt_money(gov.aliquota_ibs_uf),
                v_trib_ibsuf=self._fmt_money(gov.valor_ibs_uf),
                p_aliq_ibsmun=self._fmt_money(gov.aliquota_ibs_mun),
                v_trib_ibsmun=self._fmt_money(gov.valor_ibs_mun),
                p_aliq_cbs=self._fmt_money(gov.aliquota_cbs),
                v_trib_cbs=self._fmt_money(gov.valor_cbs),
            )

        v_ibs = Decimal(str(ibs_uf.valor or 0)) + Decimal(str(ibs_mun.valor or 0))

        return Tcibs(
            v_bc=self._fmt_money(data.base_calculo),
            g_ibsuf=g_ibsuf,
            g_ibsmun=g_ibsmun,
            v_ibs=self._fmt_money(v_ibs),
            g_cbs=g_cbs,
            g_trib_regular=g_trib_regular,
            g_trib_compra_gov=g_trib_compra_gov,
        )

    def _validar_ibscbs_padrao(self, data: IBS_CBS) -> None:
        if data.base_calculo is None:
            raise ValueError("imposto.ibs_cbs.base_calculo e obrigatorio.")
        if not data.ibs_uf:
            raise ValueError("imposto.ibs_cbs.ibs_uf e obrigatorio.")
        if not data.ibs_mun:
            raise ValueError("imposto.ibs_cbs.ibs_mun e obrigatorio.")
        if not data.cbs:
            raise ValueError("imposto.ibs_cbs.cbs e obrigatorio.")

    def _build_ibscbs_mono(self, data) -> Tmonofasia:
        g_padrao = None
        if data.padrao:
            padrao = data.padrao
            g_padrao = Tmonofasia.GMonoPadrao(
                q_bcmono=self._fmt_qty4(padrao.quantidade_base_calculo),
                ad_rem_ibs=self._fmt_money(padrao.aliquota_ibs),
                ad_rem_cbs=self._fmt_money(padrao.aliquota_cbs),
                v_ibsmono=self._fmt_money(padrao.valor_ibs),
                v_cbsmono=self._fmt_money(padrao.valor_cbs),
            )

        g_reten = None
        if data.retencao:
            reten = data.retencao
            g_reten = Tmonofasia.GMonoReten(
                q_bcmono_reten=self._fmt_qty4(reten.quantidade_base_calculo),
                ad_rem_ibsreten=self._fmt_money(reten.aliquota_ibs),
                v_ibsmono_reten=self._fmt_money(reten.valor_ibs),
                ad_rem_cbsreten=self._fmt_money(reten.aliquota_cbs),
                v_cbsmono_reten=self._fmt_money(reten.valor_cbs),
            )

        g_ret = None
        if data.retida:
            ret = data.retida
            g_ret = Tmonofasia.GMonoRet(
                q_bcmono_ret=self._fmt_qty4(ret.quantidade_base_calculo),
                ad_rem_ibsret=self._fmt_money(ret.aliquota_ibs),
                v_ibsmono_ret=self._fmt_money(ret.valor_ibs),
                ad_rem_cbsret=self._fmt_money(ret.aliquota_cbs),
                v_cbsmono_ret=self._fmt_money(ret.valor_cbs),
            )

        g_dif = None
        if data.diferimento:
            dif = data.diferimento
            g_dif = Tmonofasia.GMonoDif(
                p_dif_ibs=self._fmt_money(dif.aliquota_ibs),
                v_ibsmono_dif=self._fmt_money(dif.valor_ibs),
                p_dif_cbs=self._fmt_money(dif.aliquota_cbs),
                v_cbsmono_dif=self._fmt_money(dif.valor_cbs),
            )

        return Tmonofasia(
            g_mono_padrao=g_padrao,
            g_mono_reten=g_reten,
            g_mono_ret=g_ret,
            g_mono_dif=g_dif,
            v_tot_ibsmono_item=self._fmt_money(data.valor_total_ibs),
            v_tot_cbsmono_item=self._fmt_money(data.valor_total_cbs),
        )

    def _build_dif(self, data) -> Optional[Tdif]:
        if data.aliquota_diferimento is None and data.valor_diferimento is None:
            return None
        return Tdif(
            p_dif=self._fmt_money(data.aliquota_diferimento),
            v_dif=self._fmt_money(data.valor_diferimento),
        )

    def _build_dev_trib(self, data) -> Optional[TdevTrib]:
        if data.valor_devolucao is None:
            return None
        return TdevTrib(v_dev_trib=self._fmt_money(data.valor_devolucao))

    def _build_red(self, data) -> Optional[Tred]:
        if data.percentual_reducao is None and data.aliquota_efetiva is None:
            return None
        return Tred(
            p_red_aliq=self._fmt_money(data.percentual_reducao),
            p_aliq_efet=self._fmt_money(data.aliquota_efetiva),
        )

    def _build_pis(
        self, data: Optional[NotaFiscalAguaItemPIS]
    ) -> Optional[Tnfag.InfNfag.Det.Imposto.Pis]:
        if data is None:
            return None
        cst = data.modalidade.value[1] if hasattr(data.modalidade, "value") else data.modalidade
        if str(cst) not in {"01", "02", "06", "07", "08", "09", "49"}:
            raise ValueError(f"CST do PIS invalido para NFAg: {cst}.")
        return Tnfag.InfNfag.Det.Imposto.Pis(
            cst=self._enum_value(PisCst, str(cst)),
            v_bc=self._fmt_money(data.base_calculo),
            p_pis=self._fmt_money(data.aliquota),
            v_pis=self._fmt_money(data.valor),
        )

    def _build_cofins(
        self, data: Optional[NotaFiscalAguaItemCOFINS]
    ) -> Optional[Tnfag.InfNfag.Det.Imposto.Cofins]:
        if data is None:
            return None
        cst = data.modalidade.value[1] if hasattr(data.modalidade, "value") else data.modalidade
        if str(cst) not in {"01", "02", "06", "07", "08", "09", "49"}:
            raise ValueError(f"CST do COFINS invalido para NFAg: {cst}.")
        return Tnfag.InfNfag.Det.Imposto.Cofins(
            cst=self._enum_value(CofinsCst, str(cst)),
            v_bc=self._fmt_money(data.base_calculo),
            p_cofins=self._fmt_money(data.aliquota),
            v_cofins=self._fmt_money(data.valor),
        )

    def _build_ret_trib(
        self, data: NotaFiscalAguaItemImposto
    ) -> Optional[Tnfag.InfNfag.Det.Imposto.RetTrib]:
        valores = (
            data.retencao_pis_valor,
            data.retencao_cofins_valor,
            data.retencao_csll_valor,
            data.retencao_irrf_valor,
        )
        if all(valor is None for valor in valores):
            return None

        return Tnfag.InfNfag.Det.Imposto.RetTrib(
            v_ret_pis=self._fmt_money(data.retencao_pis_valor),
            v_ret_cofins=self._fmt_money(data.retencao_cofins_valor),
            v_ret_csll=self._fmt_money(data.retencao_csll_valor),
            v_irrf=self._fmt_money(data.retencao_irrf_valor),
        )

    def _build_tfs(self, base_calculo, aliquota, valor) -> Optional[Tnfag.InfNfag.Det.Imposto.Tfs]:
        if valor is None:
            return None
        return Tnfag.InfNfag.Det.Imposto.Tfs(
            v_bctfs=self._fmt_money(base_calculo),
            p_tfs=self._fmt_money(aliquota),
            v_tfs=self._fmt_money(valor),
        )

    def _build_tfu(self, base_calculo, aliquota, valor) -> Optional[Tnfag.InfNfag.Det.Imposto.Tfu]:
        if valor is None:
            return None
        return Tnfag.InfNfag.Det.Imposto.Tfu(
            v_bctfu=self._fmt_money(base_calculo),
            p_tfu=self._fmt_money(aliquota),
            v_tfu=self._fmt_money(valor),
        )

    def _build_total(self, nota: NotaFiscalAgua) -> Tnfag.InfNfag.Total:
        if isinstance(nota.total, Tnfag.InfNfag.Total):
            return nota.total

        total = nota.total

        v_ret_trib_tot = Tnfag.InfNfag.Total.VRetTribTot(
            v_ret_pis=self._fmt_money(total.ret_v_pis if total else None),
            v_ret_cofins=self._fmt_money(total.ret_v_cofins if total else None),
            v_ret_csll=self._fmt_money(total.ret_v_csll if total else None),
            v_irrf=self._fmt_money(total.ret_v_irrf if total else None),
        )

        ibs_uf = Tibscbstot.GIbs.GIbsuf(
            v_dif=self._fmt_money(total.ibs_uf_v_dif if total else None),
            v_dev_trib=self._fmt_money(total.ibs_uf_v_dev_trib if total else None),
            v_ibsuf=self._fmt_money(total.ibs_uf_v_ibsuf if total else None),
        )
        ibs_mun = Tibscbstot.GIbs.GIbsmun(
            v_dif=self._fmt_money(total.ibs_mun_v_dif if total else None),
            v_dev_trib=self._fmt_money(total.ibs_mun_v_dev_trib if total else None),
            v_ibsmun=self._fmt_money(total.ibs_mun_v_ibsmun if total else None),
        )
        g_ibs = Tibscbstot.GIbs(
            g_ibsuf=ibs_uf,
            g_ibsmun=ibs_mun,
            v_ibs=self._fmt_money(total.ibs_v_ibs if total else None),
        )
        g_cbs = Tibscbstot.GCbs(
            v_dif=self._fmt_money(total.cbs_v_dif if total else None),
            v_dev_trib=self._fmt_money(total.cbs_v_dev_trib if total else None),
            v_cbs=self._fmt_money(total.cbs_v_cbs if total else None),
        )
        ibscbs = Tibscbstot(
            v_bcibscbs=self._fmt_money(total.ibs_v_bcibscbs if total else None),
            g_ibs=g_ibs,
            g_cbs=g_cbs,
        )

        v_nf = total.v_nf if total else None
        v_ibs = total.ibs_v_ibs if total else None
        v_cbs = total.cbs_v_cbs if total else None
        if nota.data_emissao and nota.data_emissao.year == 2026:
            v_tot_dfe = v_nf
        else:
            v_tot_dfe = (
                Decimal(str(v_nf or 0))
                + Decimal(str(v_ibs or 0))
                + Decimal(str(v_cbs or 0))
            )

        return Tnfag.InfNfag.Total(
            v_prod=self._fmt_money(total.v_prod if total else None),
            v_ret_trib_tot=v_ret_trib_tot,
            v_cofins=self._fmt_money(total.v_cofins if total else None),
            v_pis=self._fmt_money(total.v_pis if total else None),
            v_tfs=self._fmt_money(total.v_tfs if total else None),
            v_tfu=self._fmt_money(total.v_tfu if total else None),
            v_nf=self._fmt_money(total.v_nf if total else None),
            ibscbstot=ibscbs,
            v_tot_dfe=self._fmt_money(v_tot_dfe),
        )

    def _fmt_money(self, value: Optional[Any]) -> str:
        if value is None:
            value = Decimal("0")
        if not isinstance(value, Decimal):
            value = Decimal(str(value))
        return f"{value:.2f}"

    def _fmt_qty(self, value: Optional[Any]) -> str:
        if value is None:
            value = Decimal("0")
        if not isinstance(value, Decimal):
            value = Decimal(str(value))
        return f"{value:.2f}"

    def _fmt_qty4(self, value: Optional[Any]) -> str:
        if value is None:
            value = Decimal("0")
        if not isinstance(value, Decimal):
            value = Decimal(str(value))
        return f"{value:.4f}"

    def _enum_value(self, enum_cls, value):
        if isinstance(value, enum_cls):
            return value
        return enum_cls(str(value))
