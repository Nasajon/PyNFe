from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from typing import Any, Dict, Optional, TYPE_CHECKING, List

from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from pynfe.entidades.nfgas import (
    NotaFiscalGas,
    NotaFiscalGasFatura,
    NotaFiscalGasAgencia,
    NotaFiscalGasItem,
    NotaFiscalGasItemICMS,
    NotaFiscalGasItemImposto,
    NotaFiscalGasItemCOFINS,
    NotaFiscalGasItemPIS,
)
from pynfe.entidades.ibs_cbs import IBS_CBS
from pynfe.utils import obter_codigo_por_municipio, so_numeros
from pynfe.utils.flags import CODIGOS_ESTADOS

from pynfe_nasajon.pynfe.utils.nfgas.dfe_tipos_basicos_v1_00 import (
    Tcibs,
    TdevTrib,
    Tdif,
    TestornoCred,
    Tibscbstot,
    Tmonofasia,
    Tred,
    TtribCompraGov,
    TtribNfgas,
    TtribRegular,
)
from pynfe_nasajon.pynfe.utils.nfgas.nfgas_tipos_basico_v1_00 import (
    CofinsCst,
    Icms00Cst,
    Icms10Cst,
    Icms20Cst,
    Icms40Cst,
    Icms51Cst,
    Icms60Cst,
    Icms70Cst,
    Icms70IndDeduzDeson,
    Icms70ModBc,
    Icms70ModBcst,
    Icms70MotDesIcms,
    Icms70MotDesIcmsst,
    Icms90Cst,
    ImpostoIndSemCst,
    ImpostoOrig,
    PisCst,
    Tclasse,
    Tligacao,
    Tnfgas,
    TendeEmi,
    TfatNf,
    TfinNf,
    Tmedida,
    TmotNaoLeitura,
    TorigemQtd,
    TtpEmis,
    Tumed,
    TumedItem,
)
from pynfe_nasajon.pynfe.utils.nfgas.tipos_geral_nfgas_v1_00 import (
    Tamb,
    TcodUfIbge,
    TmodNf,
    TufSemEx,
)
from pynfe_nasajon.pynfe.utils.nfgas.nfgas_v1_00 import Nfgas

if TYPE_CHECKING:
    from pynfe_nasajon.pynfe.utils.nfgas.evento_nfgas_v1_00 import EventoNfgas


NFGAS_NAMESPACE = "http://www.portalfiscal.inf.br/nfgas"
XMLDSIG_NAMESPACE = "http://www.w3.org/2000/09/xmldsig#"


class SerializacaoNFGas:
    """Serialização XML para NFGas usando xsdata."""

    def __init__(self, pretty_print: bool = False) -> None:
        config = SerializerConfig(
            xml_declaration=False,
            pretty_print=pretty_print,
        )
        self._serializer = XmlSerializer(config=config)

    def gerar(self, nfgas: "Nfgas") -> str:
        """Serializa o XML da NFGas."""
        if isinstance(nfgas, NotaFiscalGas):
            payload = self._build_nfgas_from_nota(nfgas)
        else:
            payload = nfgas
        return self._serialize(payload)

    def registrar_evento(self, evento: "EventoNfgas") -> str:
        """Serializa o XML do pedido de registro de evento da NFGas."""
        return self._serialize(evento)

    def _serialize(self, payload: Any, ns_map: Optional[Dict[str, str]] = None) -> str:
        if ns_map is None:
            ns_map = {
                None: NFGAS_NAMESPACE,
                "ds": XMLDSIG_NAMESPACE,
            }
        return self._serializer.render(payload, ns_map=ns_map)

    def _build_nfgas_from_nota(self, nota: NotaFiscalGas) -> Nfgas:
        if not nota.emitente or not nota.destinatario:
            raise ValueError("emitente e destinatario são obrigatórios para gerar NFGas.")

        det_list = self._build_det_list(nota)
        total = self._build_total(nota)

        ide = self._build_ide(nota)
        emit = self._build_emit(nota)
        dest = self._build_dest(nota)

        inf_nfgas = Tnfgas.InfNfgas(
            ide=ide,
            emit=emit,
            dest=dest,
            instalacao=self._build_instalacao(nota),
            det=det_list,
            total=total,
            g_fat=self._build_g_fat(nota.g_fat),
            g_agencia=self._build_g_agencia(nota.g_agencia),
            aut_xml=nota.autorizados_xml or [],
            inf_adic=nota.informacoes_adicionais,
            g_resp_tec=nota.responsavel_tecnico,
            versao="1.00",
            id=nota.identificador_unico,
        )

        return Nfgas(
            inf_nfgas=inf_nfgas,
            signature=None,  # A assinatura deve ser adicionada posteriormente
            inf_nfgas_supl=None,  # Suplementar pode ser adicionado posteriormente
        )

    def _build_g_fat(
        self, g_fat: Optional[NotaFiscalGasFatura]
    ) -> Optional[Tnfgas.InfNfgas.GFat]:
        if g_fat is None:
            return None
        if isinstance(g_fat, Tnfgas.InfNfgas.GFat):
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
            g_pix = Tnfgas.InfNfgas.GFat.GPix(
                url_qrcode_pix=g_fat.pix.url_qrcode_pix
            )

        return Tnfgas.InfNfgas.GFat(
            compet_fat=str(g_fat.competencia_faturamento),
            d_venc_fat=str(g_fat.data_vencimento),
            d_apres_fat=str(g_fat.data_apresentacao)
            if g_fat.data_apresentacao
            else None,
            d_prox_leitura=str(g_fat.data_proxima_leitura),
            n_fat=str(g_fat.numero_fatura) if g_fat.numero_fatura else None,
            cod_barras=str(g_fat.codigo_barras),
            cod_deb_auto=str(g_fat.codigo_debito_automatico)
            if g_fat.codigo_debito_automatico
            else None,
            cod_banco=str(g_fat.codigo_banco) if g_fat.codigo_banco else None,
            cod_agencia=str(g_fat.codigo_agencia) if g_fat.codigo_agencia else None,
            ender_corresp=ender_corresp,
            g_pix=g_pix,
            inf_ad_fat=str(g_fat.informacoes_adicionais)
            if g_fat.informacoes_adicionais
            else None,
        )

    def _build_g_agencia(
        self, g_agencia: Optional[NotaFiscalGasAgencia]
    ) -> Optional[Tnfgas.InfNfgas.GAgencia]:
        if g_agencia is None:
            return None
        if isinstance(g_agencia, Tnfgas.InfNfgas.GAgencia):
            return g_agencia

        g_hist_cons = []
        for historico in g_agencia.historicos or []:
            g_cons = []
            for consumo in historico.consumos or []:
                g_cons.append(
                    Tnfgas.InfNfgas.GAgencia.GHistCons.GCons(
                        compet_fat=str(consumo.competencia_faturamento),
                        u_med=self._enum_value(Tumed, str(consumo.unidade_medida)),
                        qtd_dias=str(consumo.quantidade_dias),
                        med_diaria=str(consumo.media_diaria)
                        if consumo.media_diaria
                        else None,
                        consumo=str(consumo.consumo) if consumo.consumo else None,
                        v_fat=str(consumo.valor_faturado),
                    )
                )
            g_hist_cons.append(
                Tnfgas.InfNfgas.GAgencia.GHistCons(
                    x_historico=str(historico.nome_historico),
                    g_cons=g_cons,
                    med_mensal=str(historico.media_mensal),
                )
            )

        return Tnfgas.InfNfgas.GAgencia(
            nome_agencia_atend=str(g_agencia.nome_agencia_atendimento)
            if g_agencia.nome_agencia_atendimento
            else None,
            ender_agencia_atend=str(g_agencia.endereco_agencia_atendimento)
            if g_agencia.endereco_agencia_atendimento
            else None,
            sitio_agencia_atend=str(g_agencia.sitio_agencia_atendimento)
            if g_agencia.sitio_agencia_atendimento
            else None,
            g_hist_cons=g_hist_cons,
            inf_ad_reg=str(g_agencia.informacoes_adicionais_reguladora)
            if g_agencia.informacoes_adicionais_reguladora
            else None,
        )

    def _build_instalacao(self, nota: NotaFiscalGas) -> Optional[Tnfgas.InfNfgas.Instalacao]:
        fields = (
            nota.instalacao_id,
            nota.instalacao_codigo_cliente,
            nota.instalacao_tipo,
            nota.instalacao_numero_contrato,
            nota.instalacao_classe_consumo,
            nota.instalacao_classe_detalhe,
            nota.instalacao_latitude_gps,
            nota.instalacao_longitude_gps,
            nota.instalacao_codigo_roteiro_leitura,
        )
        if not any(field is not None for field in fields):
            return None

        if not nota.instalacao_id:
            raise ValueError("instalacao_id é obrigatório quando informado o grupo de instalação.")
        if not nota.instalacao_tipo:
            raise ValueError("instalacao_tipo é obrigatório quando informado o grupo de instalação.")
        if not nota.instalacao_classe_consumo:
            raise ValueError(
                "instalacao_classe_consumo é obrigatório quando informado o grupo de instalação."
            )

        if (nota.instalacao_latitude_gps is None) != (nota.instalacao_longitude_gps is None):
            raise ValueError("instalacao_latitude_gps e instalacao_longitude_gps devem ser informados juntos.")

        return Tnfgas.InfNfgas.Instalacao(
            id_instalacao=str(nota.instalacao_id),
            id_cod_cliente=str(nota.instalacao_codigo_cliente)
            if nota.instalacao_codigo_cliente
            else None,
            tp_instalacao=self._enum_value(Tligacao, str(nota.instalacao_tipo)),
            n_contrato=str(nota.instalacao_numero_contrato)
            if nota.instalacao_numero_contrato
            else None,
            tp_classe=self._enum_value(Tclasse, str(nota.instalacao_classe_consumo)),
            x_classe=str(nota.instalacao_classe_detalhe)
            if nota.instalacao_classe_detalhe
            else None,
            lat_gps=str(nota.instalacao_latitude_gps)
            if nota.instalacao_latitude_gps
            else None,
            long_gps=str(nota.instalacao_longitude_gps)
            if nota.instalacao_longitude_gps
            else None,
            cod_roteiro_leitura=str(nota.instalacao_codigo_roteiro_leitura)
            if nota.instalacao_codigo_roteiro_leitura
            else None,
        )

    def _build_ide(self, nota: NotaFiscalGas) -> Tnfgas.InfNfgas.Ide:
        tz = datetime.now().astimezone().strftime("%z")
        tz = "{}:{}".format(tz[:-2], tz[-2:])

        uf = nota.uf or (nota.emitente.endereco_uf if nota.emitente else None)
        if not uf:
            raise ValueError("UF é obrigatória para gerar NFGas.")

        c_mun_fg = self._codigo_municipio(
            nota.municipio_fato_gerador,
            nota.uf or nota.emitente.endereco_uf,
            nota.emitente.endereco_cod_municipio if nota.emitente else None,
            nota.emitente.endereco_municipio if nota.emitente else None,
        )

        return Tnfgas.InfNfgas.Ide(
            c_uf=self._enum_value(TcodUfIbge, str(CODIGOS_ESTADOS[uf])),
            tp_amb=self._enum_value(Tamb, str(nota.ambiente)),
            mod=self._enum_value(TmodNf, str(nota.modelo)),
            serie=str(nota.serie),
            n_nf=str(nota.numero),
            c_nf=str(nota.codigo_numerico_aleatorio),
            c_dv=nota.identificador_unico[-1],
            dh_emi=nota.data_emissao.strftime("%Y-%m-%dT%H:%M:%S") + tz,
            tp_emis=self._enum_value(TtpEmis, str(nota.tipo_emissao)),
            n_site_autoriz=str(nota.site_autoriz),
            c_mun_fg=str(c_mun_fg),
            fin_nfgas=self._enum_value(TfinNf, str(nota.finalidade)),
            tp_fat=self._enum_value(TfatNf, str(nota.tipo_faturamento)),
            ver_proc=str(nota.versao_processo_emissao),
            dh_cont=nota.data_contingencia,
            x_just=nota.justificativa_contingencia,
            g_compra_gov=nota.compra_governo,
        )

    def _build_emit(self, nota: NotaFiscalGas) -> Tnfgas.InfNfgas.Emit:
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

        return Tnfgas.InfNfgas.Emit(
            cnpj=so_numeros(emit.cnpj).zfill(14),
            ie=so_numeros(emit.inscricao_estadual),
            x_nome=emit.razao_social,
            x_fant=emit.nome_fantasia or None,
            ender_emit=ender_emit,
        )

    def _build_dest(self, nota: NotaFiscalGas) -> Tnfgas.InfNfgas.Dest:
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

        return Tnfgas.InfNfgas.Dest(
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
        raise ValueError("Código do município inválido para NFGas.")

    def _build_det_list(self, nota: NotaFiscalGas) -> List[Tnfgas.InfNfgas.Det]:
        if not nota.itens:
            raise ValueError("Informe pelo menos um item para a NFGas.")

        det_list: List[Tnfgas.InfNfgas.Det] = []
        for idx, item in enumerate(nota.itens, start=1):
            if isinstance(item, Tnfgas.InfNfgas.Det):
                det_list.append(item)
                continue

            if not isinstance(item, NotaFiscalGasItem):
                raise ValueError("Itens devem ser NotaFiscalGasItem ou Det.")

            det_list.append(self._build_det_from_item(item, idx, nota))

        return det_list

    def _build_det_from_item(
        self, item: NotaFiscalGasItem, idx: int, nota: NotaFiscalGas
    ) -> Tnfgas.InfNfgas.Det:
        n_item = str(item.numero_item or idx)

        if str(nota.tipo_faturamento) == "3":
            g_agregadora = Tnfgas.InfNfgas.Det.GAgregadora(
                c_class=str(item.c_class or "0000000"),
                v_tot_dfe=self._fmt_money(item.valor_total_dfe or item.valor_total),
            )
            return Tnfgas.InfNfgas.Det(
                g_agregadora=g_agregadora,
                n_item=n_item,
            )

        ind_origem_qtd = item.ind_origem_qtd or "2"
        g_medicao = None
        if str(ind_origem_qtd) in ("1", "5"):
            if not item.g_medicao_n_med:
                raise ValueError("g_medicao_n_med é obrigatório quando ind_origem_qtd é 1 ou 5.")
            g_medida = None
            if item.g_medicao_u_med or item.g_medicao_v_med:
                g_medida = Tmedida(
                    u_med=self._enum_value(Tumed, str(item.g_medicao_u_med or "1")),
                    v_med=self._fmt_qty(item.g_medicao_v_med),
                )
            g_medicao = Tnfgas.InfNfgas.Det.GNormal.Prod.GMedicao(
                n_med=str(item.g_medicao_n_med),
                n_contrat=str(item.g_medicao_n_contrat)
                if item.g_medicao_n_contrat
                else None,
                g_medida=g_medida,
                tp_mot_nao_leitura=self._enum_value(
                    TmotNaoLeitura, str(item.g_medicao_tp_mot_nao_leitura)
                )
                if item.g_medicao_tp_mot_nao_leitura
                else None,
                x_mot_nao_leitura=item.g_medicao_x_mot_nao_leitura or None,
            )

        prod = Tnfgas.InfNfgas.Det.GNormal.Prod(
            ind_origem_qtd=self._enum_value(TorigemQtd, item.ind_origem_qtd or "2"),
            g_medicao=g_medicao,
            c_prod=str(item.codigo or "0"),
            x_prod=str(item.descricao or "Item"),
            c_class=str(item.c_class or "0000000"),
            cfop=str(item.cfop) if item.cfop else None,
            u_med=self._enum_value(TumedItem, item.u_med or "1"),
            q_faturada=self._fmt_qty(item.quantidade),
            v_item=self._fmt_money(item.valor_unitario),
            v_prod=self._fmt_money(item.valor_total),
        )

        imposto = self._build_imposto(item)

        g_normal = Tnfgas.InfNfgas.Det.GNormal(prod=prod, imposto=imposto)

        return Tnfgas.InfNfgas.Det(
            g_normal=g_normal,
            n_item=n_item,
        )

    def _build_imposto(
        self, item: NotaFiscalGasItem
    ) -> Tnfgas.InfNfgas.Det.GNormal.Imposto:
        data: Optional[NotaFiscalGasItemImposto] = item.imposto
        if data is None:
            return Tnfgas.InfNfgas.Det.GNormal.Imposto()

        ibscbs = self._build_ibscbs(data.ibs_cbs)
        if ibscbs is None:
            raise ValueError("imposto.ibs_cbs é obrigatório quando informado imposto do item.")

        imposto = Tnfgas.InfNfgas.Det.GNormal.Imposto(ibscbs=ibscbs)

        icms = self._build_icms(data.icms)
        if icms:
            setattr(imposto, icms["campo"], icms["valor"])

        if data.icms and data.icms.origem is not None:
            origem = (
                data.icms.origem.value[1]
                if hasattr(data.icms.origem, "value")
                else data.icms.origem
            )
            imposto.orig = self._enum_value(ImpostoOrig, str(origem))

        if data.icms and data.icms.sem_cst:
            imposto.ind_sem_cst = ImpostoIndSemCst.VALUE_1

        pis = self._build_pis(data.pis)
        if pis:
            imposto.pis = pis

        cofins = self._build_cofins(data.cofins)
        if cofins:
            imposto.cofins = cofins

        ret_trib = self._build_ret_trib(data)
        if ret_trib:
            imposto.ret_trib = ret_trib

        tx_reg = self._build_tx_reg(data.taxa_regulatoria_valor, data.taxa_regulatoria_aliquota, data.taxa_regulatoria_base_calculo)
        if tx_reg:
            imposto.tx_reg = tx_reg

        return imposto

    def _build_ibscbs(self, data: Optional[IBS_CBS]) -> Optional[TtribNfgas]:
        if data is None:
            return None

        if not data.modalidade:
            raise ValueError("imposto.ibs_cbs.modalidade (CST) é obrigatório.")
        if not data.classificacao:
            raise ValueError("imposto.ibs_cbs.classificacao (cClassTrib) é obrigatório.")

        cst = data.modalidade
        c_class_trib = data.classificacao

        g_ibscbsmono = None
        g_ibscbs = None

        if data.monofasico:
            g_ibscbsmono = self._build_ibscbs_mono(data.monofasico)
        else:
            g_ibscbs = self._build_ibscbs_padrao(data)

        estorno = None
        if data.estorno:
            estorno = TestornoCred(
                v_ibsest_cred=self._fmt_money(data.estorno.valor_ibs),
                v_cbsest_cred=self._fmt_money(data.estorno.valor_cbs),
            )

        return TtribNfgas(
            cst=str(cst),
            c_class_trib=str(c_class_trib),
            g_ibscbs=g_ibscbs,
            g_ibscbsmono=g_ibscbsmono,
            g_estorno_cred=estorno,
        )

    def _build_ibscbs_padrao(self, data: IBS_CBS) -> Tcibs:
        if not data.ibs_uf:
            raise ValueError("imposto.ibs_cbs.ibs_uf é obrigatório.")
        if not data.ibs_mun:
            raise ValueError("imposto.ibs_cbs.ibs_mun é obrigatório.")
        if not data.cbs:
            raise ValueError("imposto.ibs_cbs.cbs é obrigatório.")

        ibs_uf = data.ibs_uf
        ibs_mun = data.ibs_mun
        cbs = data.cbs

        g_ibsuf = Tcibs.GIbsuf(
            p_ibsuf=self._fmt_money(ibs_uf.aliquota),
            v_ibsuf=self._fmt_money(ibs_uf.valor),
            g_dif=self._build_dif(ibs_uf),
            g_dev_trib=self._build_dev_trib(ibs_uf),
            g_red=self._build_red(ibs_uf),
        )
        g_ibsmun = Tcibs.GIbsmun(
            p_ibsmun=self._fmt_money(ibs_mun.aliquota),
            v_ibsmun=self._fmt_money(ibs_mun.valor),
            g_dif=self._build_dif(ibs_mun),
            g_dev_trib=self._build_dev_trib(ibs_mun),
            g_red=self._build_red(ibs_mun),
        )
        g_cbs = Tcibs.GCbs(
            p_cbs=self._fmt_money(cbs.aliquota),
            v_cbs=self._fmt_money(cbs.valor),
            g_dif=self._build_dif(cbs),
            g_dev_trib=self._build_dev_trib(cbs),
            g_red=self._build_red(cbs),
        )

        g_trib_regular = None
        if data.trib_reg:
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

    def _build_icms(self, data: Optional[NotaFiscalGasItemICMS]) -> Optional[dict]:
        if data is None or not data.modalidade:
            return None

        cst = data.modalidade.value[1] if hasattr(data.modalidade, "value") else data.modalidade

        def require(value, nome):
            if value is None:
                raise ValueError(f"imposto.icms.{nome} é obrigatório para CST {cst}.")
            return value

        if cst == "00":
            return {
                "campo": "icms00",
                "valor": Tnfgas.InfNfgas.Det.GNormal.Imposto.Icms00(
                    cst=Icms00Cst.VALUE_00,
                    v_bc=self._fmt_money(require(data.base_calculo, "base_calculo")),
                    p_icms=self._fmt_money(require(data.aliquota, "aliquota")),
                    v_icms=self._fmt_money(require(data.valor, "valor")),
                    p_fcp=self._fmt_money(data.percentual_fcp)
                    if data.percentual_fcp is not None
                    else None,
                    v_fcp=self._fmt_money(data.valor_fcp)
                    if data.valor_fcp is not None
                    else None,
                ),
            }

        if cst == "10":
            return {
                "campo": "icms10",
                "valor": Tnfgas.InfNfgas.Det.GNormal.Imposto.Icms10(
                    cst=Icms10Cst.VALUE_10,
                    v_bcst=self._fmt_money(require(data.base_calculo_st, "base_calculo_st")),
                    p_icmsst=self._fmt_money(require(data.aliquota_st, "aliquota_st")),
                    v_icmsst=self._fmt_money(require(data.valor_st, "valor_st")),
                    p_fcpst=self._fmt_money(data.percentual_fcpst)
                    if data.percentual_fcpst is not None
                    else None,
                    v_fcpst=self._fmt_money(data.valor_fcpst)
                    if data.valor_fcpst is not None
                    else None,
                ),
            }

        if cst == "20":
            return {
                "campo": "icms20",
                "valor": Tnfgas.InfNfgas.Det.GNormal.Imposto.Icms20(
                    cst=Icms20Cst.VALUE_20,
                    p_red_bc=self._fmt_money(
                        require(data.percentual_reducao_bc, "percentual_reducao_bc")
                    ),
                    v_bc=self._fmt_money(require(data.base_calculo, "base_calculo")),
                    p_icms=self._fmt_money(require(data.aliquota, "aliquota")),
                    v_icms=self._fmt_money(require(data.valor, "valor")),
                    v_icmsdeson=self._fmt_money(data.valor_desonerado)
                    if data.valor_desonerado is not None
                    else None,
                    c_benef=data.codigo_beneficio or None,
                    p_fcp=self._fmt_money(data.percentual_fcp)
                    if data.percentual_fcp is not None
                    else None,
                    v_fcp=self._fmt_money(data.valor_fcp)
                    if data.valor_fcp is not None
                    else None,
                ),
            }

        if cst in ("40", "41"):
            return {
                "campo": "icms40",
                "valor": Tnfgas.InfNfgas.Det.GNormal.Imposto.Icms40(
                    cst=self._enum_value(Icms40Cst, str(cst)),
                    v_icmsdeson=self._fmt_money(data.valor_desonerado)
                    if data.valor_desonerado is not None
                    else None,
                    c_benef=data.codigo_beneficio or None,
                ),
            }

        if cst == "51":
            return {
                "campo": "icms51",
                "valor": Tnfgas.InfNfgas.Det.GNormal.Imposto.Icms51(
                    cst=Icms51Cst.VALUE_51,
                    v_icmsdeson=self._fmt_money(data.valor_desonerado)
                    if data.valor_desonerado is not None
                    else None,
                    c_benef=data.codigo_beneficio or None,
                ),
            }

        if cst == "60":
            return {
                "campo": "icms60",
                "valor": Tnfgas.InfNfgas.Det.GNormal.Imposto.Icms60(
                    cst=Icms60Cst.VALUE_60,
                    v_bcstret=self._fmt_money(data.base_calculo_st_retido)
                    if data.base_calculo_st_retido is not None
                    else None,
                    p_icmsstret=self._fmt_money(data.aliquota_st_retido)
                    if data.aliquota_st_retido is not None
                    else None,
                    v_icmssubstituto=self._fmt_money(data.valor_substituto)
                    if data.valor_substituto is not None
                    else None,
                    v_icmsstret=self._fmt_money(data.valor_st_retido)
                    if data.valor_st_retido is not None
                    else None,
                    v_bcfcpstret=self._fmt_money(data.base_calculo_fcpst_retido)
                    if data.base_calculo_fcpst_retido is not None
                    else None,
                    p_fcpstret=self._fmt_money(data.percentual_fcpst_retido)
                    if data.percentual_fcpst_retido is not None
                    else None,
                    v_fcpstret=self._fmt_money(data.valor_fcpst_retido)
                    if data.valor_fcpst_retido is not None
                    else None,
                    p_red_bcefet=self._fmt_money(data.percentual_reducao_bc_efetiva)
                    if data.percentual_reducao_bc_efetiva is not None
                    else None,
                    v_bcefet=self._fmt_money(data.base_calculo_efetiva)
                    if data.base_calculo_efetiva is not None
                    else None,
                    p_icmsefet=self._fmt_money(data.aliquota_efetiva)
                    if data.aliquota_efetiva is not None
                    else None,
                    v_icmsefet=self._fmt_money(data.valor_efetivo)
                    if data.valor_efetivo is not None
                    else None,
                    v_icmsdeson=self._fmt_money(data.valor_desonerado)
                    if data.valor_desonerado is not None
                    else None,
                    c_benef=data.codigo_beneficio or None,
                ),
            }

        if cst == "70":
            mod_bc = require(data.modalidade_bc, "modalidade_bc")
            mod_bcst = require(data.modalidade_bc_st, "modalidade_bc_st")
            return {
                "campo": "icms70",
                "valor": Tnfgas.InfNfgas.Det.GNormal.Imposto.Icms70(
                    cst=Icms70Cst.VALUE_70,
                    mod_bc=self._enum_value(Icms70ModBc, str(mod_bc)),
                    p_red_bc=self._fmt_money(
                        require(data.percentual_reducao_bc, "percentual_reducao_bc")
                    ),
                    v_bc=self._fmt_money(require(data.base_calculo, "base_calculo")),
                    p_icms=self._fmt_money(require(data.aliquota, "aliquota")),
                    v_icms=self._fmt_money(require(data.valor, "valor")),
                    v_bcfcp=self._fmt_money(data.base_calculo_fcp)
                    if data.base_calculo_fcp is not None
                    else None,
                    p_fcp=self._fmt_money(data.percentual_fcp)
                    if data.percentual_fcp is not None
                    else None,
                    v_fcp=self._fmt_money(data.valor_fcp)
                    if data.valor_fcp is not None
                    else None,
                    mod_bcst=self._enum_value(Icms70ModBcst, str(mod_bcst)),
                    p_mvast=self._fmt_money(data.percentual_mva_st)
                    if data.percentual_mva_st is not None
                    else None,
                    p_red_bcst=self._fmt_money(data.percentual_reducao_bc_st)
                    if data.percentual_reducao_bc_st is not None
                    else None,
                    v_bcst=self._fmt_money(require(data.base_calculo_st, "base_calculo_st")),
                    p_icmsst=self._fmt_money(require(data.aliquota_st, "aliquota_st")),
                    v_icmsst=self._fmt_money(require(data.valor_st, "valor_st")),
                    v_bcfcpst=self._fmt_money(data.base_calculo_fcpst)
                    if data.base_calculo_fcpst is not None
                    else None,
                    p_fcpst=self._fmt_money(data.percentual_fcpst)
                    if data.percentual_fcpst is not None
                    else None,
                    v_fcpst=self._fmt_money(data.valor_fcpst)
                    if data.valor_fcpst is not None
                    else None,
                    v_icmsdeson=self._fmt_money(data.valor_desonerado)
                    if data.valor_desonerado is not None
                    else None,
                    mot_des_icms=self._build_motivo_deson(
                        data.motivo_desoneracao, Icms70MotDesIcms
                    ),
                    ind_deduz_deson=self._build_ind_deduz_deson(
                        data.ind_deduz_desoneracao
                    ),
                    v_icmsstdeson=self._fmt_money(data.valor_st_desonerado)
                    if data.valor_st_desonerado is not None
                    else None,
                    mot_des_icmsst=self._build_motivo_deson(
                        data.motivo_desoneracao_st,
                        Icms70MotDesIcmsst,
                    ),
                ),
            }

        if cst == "90":
            return {
                "campo": "icms90",
                "valor": Tnfgas.InfNfgas.Det.GNormal.Imposto.Icms90(
                    cst=Icms90Cst.VALUE_90,
                    v_bc=self._fmt_money(data.base_calculo)
                    if data.base_calculo is not None
                    else None,
                    p_icms=self._fmt_money(data.aliquota)
                    if data.aliquota is not None
                    else None,
                    v_icms=self._fmt_money(data.valor)
                    if data.valor is not None
                    else None,
                    v_icmsdeson=self._fmt_money(data.valor_desonerado)
                    if data.valor_desonerado is not None
                    else None,
                    c_benef=data.codigo_beneficio or None,
                    p_fcp=self._fmt_money(data.percentual_fcp)
                    if data.percentual_fcp is not None
                    else None,
                    v_fcp=self._fmt_money(data.valor_fcp)
                    if data.valor_fcp is not None
                    else None,
                ),
            }

        raise ValueError(f"CST de ICMS inválido para NFGas: {cst}.")

    def _build_motivo_deson(self, motivo, enum_cls):
        if motivo is None:
            return None
        value = motivo.value[1] if hasattr(motivo, "value") else motivo
        return self._enum_value(enum_cls, str(value))

    def _build_ind_deduz_deson(self, valor) -> Optional[Icms70IndDeduzDeson]:
        if valor is None:
            return None
        return self._enum_value(Icms70IndDeduzDeson, "1" if valor else "0")

    def _build_pis(
        self, data: Optional[NotaFiscalGasItemPIS]
    ) -> Optional[Tnfgas.InfNfgas.Det.GNormal.Imposto.Pis]:
        if data is None:
            return None
        cst = data.modalidade.value[1] if hasattr(data.modalidade, "value") else data.modalidade
        if str(cst) not in {"01", "02", "06", "07", "08", "09", "49"}:
            raise ValueError(f"CST do PIS inválido para NFGas: {cst}.")
        return Tnfgas.InfNfgas.Det.GNormal.Imposto.Pis(
            cst=self._enum_value(PisCst, str(cst)),
            v_bc=self._fmt_money(data.base_calculo),
            p_pis=self._fmt_money(data.aliquota),
            v_pis=self._fmt_money(data.valor),
        )

    def _build_cofins(
        self, data: Optional[NotaFiscalGasItemCOFINS]
    ) -> Optional[Tnfgas.InfNfgas.Det.GNormal.Imposto.Cofins]:
        if data is None:
            return None
        cst = data.modalidade.value[1] if hasattr(data.modalidade, "value") else data.modalidade
        if str(cst) not in {"01", "02", "06", "07", "08", "09", "49"}:
            raise ValueError(f"CST do COFINS inválido para NFGas: {cst}.")
        return Tnfgas.InfNfgas.Det.GNormal.Imposto.Cofins(
            cst=self._enum_value(CofinsCst, str(cst)),
            v_bc=self._fmt_money(data.base_calculo),
            p_cofins=self._fmt_money(data.aliquota),
            v_cofins=self._fmt_money(data.valor),
        )

    def _build_ret_trib(
        self, data
    ) -> Optional[Tnfgas.InfNfgas.Det.GNormal.Imposto.RetTrib]:
        valores = (
            data.retencao_pis_valor,
            data.retencao_cofins_valor,
            data.retencao_csll_valor,
            data.retencao_irrf_valor,
        )
        if all(valor is None for valor in valores):
            return None

        return Tnfgas.InfNfgas.Det.GNormal.Imposto.RetTrib(
            v_ret_pis=self._fmt_money(data.retencao_pis_valor),
            v_ret_cofins=self._fmt_money(data.retencao_cofins_valor),
            v_ret_csll=self._fmt_money(data.retencao_csll_valor),
            v_irrf=self._fmt_money(data.retencao_irrf_valor),
        )

    def _build_tx_reg(
        self, valor, aliquota, base_calculo
    ) -> Optional[Tnfgas.InfNfgas.Det.GNormal.Imposto.TxReg]:
        if valor is None:
            return None
        return Tnfgas.InfNfgas.Det.GNormal.Imposto.TxReg(
            v_taxa=self._fmt_money(valor),
            p_taxa=self._fmt_money(aliquota),
            v_bc=self._fmt_money(base_calculo)
        )

    def _build_total(self, nota: NotaFiscalGas) -> Tnfgas.InfNfgas.Total:
        if isinstance(nota.total, Tnfgas.InfNfgas.Total):
            return nota.total

        total = nota.total

        icmstot = Tnfgas.InfNfgas.Total.Icmstot(
            v_bc=self._fmt_money(total.icms_v_bc if total else None),
            v_icms=self._fmt_money(total.icms_v_icms if total else None),
            v_icmsdeson=self._fmt_money(total.icms_v_icmsdeson if total else None),
            v_fcp=self._fmt_money(total.icms_v_fcp if total else None),
            v_bcst=self._fmt_money(total.icms_v_bcst if total else None),
            v_st=self._fmt_money(total.icms_v_st if total else None),
            v_fcpst=self._fmt_money(total.icms_v_fcpst if total else None),
        )

        v_ret_trib_tot = Tnfgas.InfNfgas.Total.VRetTribTot(
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
            v_dev_trib=self._fmt_money(
                total.cbs_v_dev_trib if total else None
            ),
            v_cbs=self._fmt_money(total.cbs_v_cbs if total else None),
        )
        ibscbs = Tibscbstot(
            v_bcibscbs=self._fmt_money(
                total.ibs_v_bcibscbs if total else None
            ),
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

        return Tnfgas.InfNfgas.Total(
            v_prod=self._fmt_money(total.v_prod if total else None),
            icmstot=icmstot,
            v_ret_trib_tot=v_ret_trib_tot,
            v_cofins=self._fmt_money(total.v_cofins if total else None),
            v_pis=self._fmt_money(total.v_pis if total else None),
            v_tx_reg=self._fmt_money(total.v_tx_reg if total else None),
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
