# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Optional
import random
from decimal import Decimal

from pynfe import get_version
from pynfe.entidades.cliente import Cliente
from pynfe.entidades.emitente import Emitente
from pynfe.utils import so_numeros
from pynfe.utils.flags import CODIGOS_ESTADOS

from .base import Entidade
from .ibs_cbs import IBS_CBS


class NotaFiscalGasInstalacao(Entidade):
    id = str()
    codigo_cliente = str()
    tipo = str()
    numero_contrato = str()
    classe_consumo = str()
    classe_detalhe = str()
    latitude_gps = str()
    longitude_gps = str()
    codigo_roteiro_leitura = str()


class NotaFiscalGas(Entidade):
    """
    Entidade para preenchimento dos dados da NFGas.
    Esta classe serve como insumo para a SerializacaoNFGas.
    """

    # Código numérico aleatório que compõe a chave de acesso
    codigo_numerico_aleatorio = str()

    # Digito verificador do codigo numerico aleatorio
    dv_codigo_numerico_aleatorio = str()

    # Modelo NFGas
    modelo = 76

    # Serie (obrigatorio)
    serie = str()

    # Numero NFGas (obrigatorio)
    numero = str()

    # Data da Emissao (obrigatorio)
    data_emissao: datetime = None

    # UF do emitente
    uf = str()

    # Município de ocorrência do fato gerador
    municipio_fato_gerador = str()

    # Ambiente
    ambiente = "2"  # 1-Produção; 2-Homologação

    # Tipo de emissão
    tipo_emissao = "1"  # 1 - Normal; 2 - Contingência Off Line

    # Site autorizador
    site_autoriz = "0"

    # Finalidade de emissão
    finalidade = "0"  # 0 - Normal; 3 - Substituição

    # Tipo de faturamento
    tipo_faturamento = "1"  # 1-Normal; 2-Agregado; 3-Agregador

    # Versão do processo de emissão
    versao_processo_emissao = get_version()

    # Emitente
    emitente: Emitente = None

    # Destinatário
    destinatario: Cliente = None

    # Itens (detalhamento)
    itens = None

    # Totais
    total = None

    # Grupo de faturamento e agência (opcionais)
    g_fat: Optional["NotaFiscalGasFatura"] = None
    g_agencia: Optional["NotaFiscalGasAgencia"] = None

    # Autorizados XML (lista de objetos autXML do schema)
    autorizados_xml = None

    # Informações adicionais
    informacoes_adicionais = None

    # Responsável técnico
    responsavel_tecnico = None

    # Contingência
    data_contingencia = None
    justificativa_contingencia = None

    # Compras Governo
    compra_governo = None

    # Instalação (opcional para tpFat=3)
    instalacao: Optional[NotaFiscalGasInstalacao] = None

    def __init__(self, *args, **kwargs):
        super(NotaFiscalGas, self).__init__(*args, **kwargs)

        if self.itens is None:
            self.itens = []
        if self.autorizados_xml is None:
            self.autorizados_xml = []

    def __str__(self):
        return " ".join([str(self.identificador_unico)])

    def _codigo_numerico_aleatorio(self):
        if not self.codigo_numerico_aleatorio:
            self.codigo_numerico_aleatorio = str(random.randint(0, 9999999)).zfill(7)
        return self.codigo_numerico_aleatorio

    def _dv_codigo_numerico(self, key):
        if not len(key) == 43:
            raise ValueError(
                f"Chave de acesso deve ter 43 caracteres antes de calcular o DV, chave: {key}"
            )

        weights = [2, 3, 4, 5, 6, 7, 8, 9]
        weights_size = len(weights)
        key_numbers = [int(k) for k in key]
        key_numbers.reverse()

        key_sum = 0
        for i, key_number in enumerate(key_numbers):
            i = i % weights_size
            key_sum += key_number * weights[i]

        remainder = key_sum % 11
        if remainder == 0 or remainder == 1:
            self.dv_codigo_numerico_aleatorio = "0"
            return "0"
        self.dv_codigo_numerico_aleatorio = str(11 - remainder)
        return str(self.dv_codigo_numerico_aleatorio)

    @property
    def identificador_unico(self):
        key = "%(uf)s%(ano)s%(mes)s%(cnpj)s%(mod)s%(serie)s%(nNF)s%(tpEmis)s%(nSiteAutoriz)s%(cNF)s" % {
            "uf": CODIGOS_ESTADOS[self.uf],
            "ano": self.data_emissao.strftime("%y"),
            "mes": self.data_emissao.strftime("%m"),
            "cnpj": so_numeros(self.emitente.cnpj).zfill(14),
            "mod": str(self.modelo).zfill(2),
            "serie": str(self.serie).zfill(3),
            "nNF": str(self.numero).zfill(9),
            "tpEmis": str(self.tipo_emissao),
            "nSiteAutoriz": str(self.site_autoriz),
            "cNF": self._codigo_numerico_aleatorio(),
        }
        return "NFGas%(uf)s%(ano)s%(mes)s%(cnpj)s%(mod)s%(serie)s%(nNF)s%(tpEmis)s%(nSiteAutoriz)s%(cNF)s%(cDV)s" % {
            "uf": CODIGOS_ESTADOS[self.uf],
            "ano": self.data_emissao.strftime("%y"),
            "mes": self.data_emissao.strftime("%m"),
            "cnpj": so_numeros(self.emitente.cnpj).zfill(14),
            "mod": str(self.modelo).zfill(2),
            "serie": str(self.serie).zfill(3),
            "nNF": str(self.numero).zfill(9),
            "tpEmis": str(self.tipo_emissao),
            "nSiteAutoriz": str(self.site_autoriz),
            "cNF": str(self.codigo_numerico_aleatorio),
            "cDV": self._dv_codigo_numerico(key),
        }

    def adicionar_item(self, **kwargs):
        obj = NotaFiscalGasItem(**kwargs)
        self.itens.append(obj)
        if self.total is None:
            self.total = NotaFiscalGasTotal()
        total = self.total

        def _decimal_or_zero(value):
            if isinstance(value, Decimal):
                return value
            if value in (None, ""):
                return Decimal(0)
            return Decimal(value)

        total.v_prod += _decimal_or_zero(obj.valor_total)

        if obj.imposto:
            if obj.imposto.icms:
                icms = obj.imposto.icms
                total.icms_v_bc += _decimal_or_zero(icms.base_calculo)
                total.icms_v_icms += _decimal_or_zero(icms.valor)
                total.icms_v_icmsdeson += _decimal_or_zero(icms.valor_desonerado)
                total.icms_v_fcp += _decimal_or_zero(icms.valor_fcp)
                total.icms_v_bcst += _decimal_or_zero(icms.base_calculo_st)
                total.icms_v_st += _decimal_or_zero(icms.valor_st)
                total.icms_v_fcpst += _decimal_or_zero(icms.valor_fcpst)

            if obj.imposto.pis:
                total.v_pis += _decimal_or_zero(obj.imposto.pis.valor)
            if obj.imposto.cofins:
                total.v_cofins += _decimal_or_zero(obj.imposto.cofins.valor)

            ret_pis = _decimal_or_zero(obj.imposto.retencao_pis_valor)
            ret_cofins = _decimal_or_zero(obj.imposto.retencao_cofins_valor)
            ret_csll = _decimal_or_zero(obj.imposto.retencao_csll_valor)
            ret_irrf = _decimal_or_zero(obj.imposto.retencao_irrf_valor)
            total.ret_v_pis += ret_pis
            total.ret_v_cofins += ret_cofins
            total.ret_v_csll += ret_csll
            total.ret_v_irrf += ret_irrf

            total.v_tx_reg += _decimal_or_zero(obj.imposto.taxa_regulatoria_valor)

            if obj.imposto.ibs_cbs:
                ibs_cbs = obj.imposto.ibs_cbs
                ibs_uf = ibs_cbs.ibs_uf
                ibs_mun = ibs_cbs.ibs_mun
                cbs = ibs_cbs.cbs

                total.ibs_v_bcibscbs += _decimal_or_zero(ibs_cbs.base_calculo)

                if ibs_uf:
                    total.ibs_uf_v_dif += _decimal_or_zero(ibs_uf.valor_diferimento)
                    total.ibs_uf_v_dev_trib += _decimal_or_zero(ibs_uf.valor_devolucao)
                    total.ibs_uf_v_ibsuf += _decimal_or_zero(ibs_uf.valor)

                if ibs_mun:
                    total.ibs_mun_v_dif += _decimal_or_zero(ibs_mun.valor_diferimento)
                    total.ibs_mun_v_dev_trib += _decimal_or_zero(ibs_mun.valor_devolucao)
                    total.ibs_mun_v_ibsmun += _decimal_or_zero(ibs_mun.valor)

                total.ibs_v_ibs += _decimal_or_zero(
                    (ibs_uf.valor if ibs_uf else None)
                ) + _decimal_or_zero((ibs_mun.valor if ibs_mun else None))

                if cbs:
                    total.cbs_v_dif += _decimal_or_zero(cbs.valor_diferimento)
                    total.cbs_v_dev_trib += _decimal_or_zero(cbs.valor_devolucao)
                    total.cbs_v_cbs += _decimal_or_zero(cbs.valor)
        else:
            ret_pis = Decimal(0)
            ret_cofins = Decimal(0)
            ret_csll = Decimal(0)
            ret_irrf = Decimal(0)

        total.v_nf += _decimal_or_zero(obj.valor_total) - (
            ret_pis + ret_cofins + ret_csll + ret_irrf
        )
        return obj


class NotaFiscalGasItem(Entidade):
    numero_item = int()
    codigo = str()
    descricao = str()
    quantidade = Decimal()
    unidade = str()
    valor_unitario = Decimal()
    valor_total = Decimal()
    valor_total_dfe = Decimal()

    # Campos específicos do layout NFGas
    ind_origem_qtd = str()  # 1..7
    c_class = str()  # 7 dígitos
    cfop = str()
    u_med = str()  # 1..2

    # GMedicao (para ind_origem_qtd = 1 ou 5)
    g_medicao_n_med = str()
    g_medicao_n_contrat = str()
    g_medicao_u_med = str()
    g_medicao_v_med = Decimal()
    g_medicao_tp_mot_nao_leitura = str()
    g_medicao_x_mot_nao_leitura = str()

    # Impostos do item (NFGas)
    imposto: Optional["NotaFiscalGasItemImposto"] = None


class NotaFiscalGasItemICMS(Entidade):
    modalidade = None
    origem = None
    sem_cst = False

    base_calculo = Decimal()
    aliquota = Decimal()
    valor = Decimal()
    percentual_reducao_bc = Decimal()

    modalidade_bc = str()
    modalidade_bc_st = str()

    base_calculo_st = Decimal()
    aliquota_st = Decimal()
    valor_st = Decimal()
    percentual_mva_st = Decimal()
    percentual_reducao_bc_st = Decimal()

    base_calculo_fcp = Decimal()
    percentual_fcp = Decimal()
    valor_fcp = Decimal()

    base_calculo_fcpst = Decimal()
    percentual_fcpst = Decimal()
    valor_fcpst = Decimal()

    valor_desonerado = Decimal()
    codigo_beneficio = str()
    motivo_desoneracao = None

    ind_deduz_desoneracao = False
    valor_st_desonerado = Decimal()
    motivo_desoneracao_st = None

    base_calculo_st_retido = Decimal()
    aliquota_st_retido = Decimal()
    valor_substituto = Decimal()
    valor_st_retido = Decimal()

    base_calculo_fcpst_retido = Decimal()
    percentual_fcpst_retido = Decimal()
    valor_fcpst_retido = Decimal()

    percentual_reducao_bc_efetiva = Decimal()
    base_calculo_efetiva = Decimal()
    aliquota_efetiva = Decimal()
    valor_efetivo = Decimal()


class NotaFiscalGasItemPIS(Entidade):
    modalidade = None
    base_calculo = Decimal()
    aliquota = Decimal()
    valor = Decimal()


class NotaFiscalGasItemCOFINS(Entidade):
    modalidade = None
    base_calculo = Decimal()
    aliquota = Decimal()
    valor = Decimal()


class NotaFiscalGasItemImposto(Entidade):
    ibs_cbs: Optional[IBS_CBS] = None
    pis: Optional[NotaFiscalGasItemPIS] = None
    cofins: Optional[NotaFiscalGasItemCOFINS] = None
    icms: Optional[NotaFiscalGasItemICMS] = None

    retencao_pis_valor = Decimal()
    retencao_cofins_valor = Decimal()
    retencao_csll_valor = Decimal()
    retencao_irrf_valor = Decimal()

    taxa_regulatoria_valor = Decimal()
    taxa_regulatoria_aliquota = Decimal()
    taxa_regulatoria_base_calculo = Decimal()


class NotaFiscalGasTotal(Entidade):
    valor_total = Decimal()
    valor_tributos = Decimal()

    icms_v_bc = Decimal()
    icms_v_icms = Decimal()
    icms_v_icmsdeson = Decimal()
    icms_v_fcp = Decimal()
    icms_v_bcst = Decimal()
    icms_v_st = Decimal()
    icms_v_fcpst = Decimal()

    ret_v_pis = Decimal()
    ret_v_cofins = Decimal()
    ret_v_csll = Decimal()
    ret_v_irrf = Decimal()

    ibs_uf_v_dif = Decimal()
    ibs_uf_v_dev_trib = Decimal()
    ibs_uf_v_ibsuf = Decimal()

    ibs_mun_v_dif = Decimal()
    ibs_mun_v_dev_trib = Decimal()
    ibs_mun_v_ibsmun = Decimal()

    ibs_v_ibs = Decimal()

    cbs_v_dif = Decimal()
    cbs_v_dev_trib = Decimal()
    cbs_v_cbs = Decimal()

    ibs_v_bcibscbs = Decimal()

    v_prod = Decimal()
    v_cofins = Decimal()
    v_pis = Decimal()
    v_tx_reg = Decimal()
    v_nf = Decimal()
    v_tot_dfe = Decimal()


class NotaFiscalGasFaturaEndereco(Entidade):
    logradouro = str()
    numero = str()
    complemento = str()
    bairro = str()
    codigo_municipio = str()
    municipio = str()
    cep = str()
    uf = str()
    telefone = str()
    email = str()


class NotaFiscalGasFaturaPix(Entidade):
    url_qrcode_pix = str()


class NotaFiscalGasFatura(Entidade):
    competencia_faturamento = str()
    data_vencimento = str()
    data_apresentacao = str()
    data_proxima_leitura = str()
    numero_fatura = str()
    codigo_barras = str()
    codigo_debito_automatico = str()
    codigo_banco = str()
    codigo_agencia = str()
    endereco_correspondencia: Optional[NotaFiscalGasFaturaEndereco] = None
    pix: Optional[NotaFiscalGasFaturaPix] = None
    informacoes_adicionais = str()


class NotaFiscalGasAgenciaConsumo(Entidade):
    competencia_faturamento = str()
    unidade_medida = str()
    quantidade_dias = str()
    media_diaria = str()
    consumo = str()
    valor_faturado = str()


class NotaFiscalGasAgenciaHistorico(Entidade):
    nome_historico = str()
    consumos: list[NotaFiscalGasAgenciaConsumo] = None
    media_mensal = str()

    def __init__(self, *args, **kwargs):
        super(NotaFiscalGasAgenciaHistorico, self).__init__(*args, **kwargs)
        if self.consumos is None:
            self.consumos = []


class NotaFiscalGasAgencia(Entidade):
    nome_agencia_atendimento = str()
    endereco_agencia_atendimento = str()
    sitio_agencia_atendimento = str()
    historicos: list[NotaFiscalGasAgenciaHistorico] = None
    informacoes_adicionais_reguladora = str()

    def __init__(self, *args, **kwargs):
        super(NotaFiscalGasAgencia, self).__init__(*args, **kwargs)
        if self.historicos is None:
            self.historicos = []
