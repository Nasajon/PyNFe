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


class NotaFiscalAgua(Entidade):
    """
    Entidade para preenchimento dos dados da NFAg.
    Esta classe serve como insumo para a SerializacaoNFAg.
    """

    # Codigo numerico aleatorio que compoe a chave de acesso
    codigo_numerico_aleatorio = str()

    # Digito verificador do codigo numerico aleatorio
    dv_codigo_numerico_aleatorio = str()

    # Modelo NFAg
    modelo = 75

    # Serie (obrigatorio)
    serie = str()

    # Numero NFAg (obrigatorio)
    numero = str()

    # Data da Emissao (obrigatorio)
    data_emissao: datetime = None

    # UF do emitente
    uf = str()

    # Municipio de ocorrencia do fato gerador
    municipio_fato_gerador = str()

    # Ambiente
    ambiente = "2"  # 1-Producao; 2-Homologacao

    # Tipo de emissao
    tipo_emissao = "1"  # 1 - Normal; 2 - Contingencia Off Line

    # Site autorizador
    site_autoriz = "0"

    # Finalidade de emissao
    finalidade = "0"  # 0 - Normal; 3 - Substituicao

    # Tipo de faturamento
    tipo_faturamento = "1"  # 1-Normal; 2-Terceiro; 3-Conjunto

    # Versao do processo de emissao
    versao_processo_emissao = get_version()

    # Emitente
    emitente: Emitente = None

    # Destinatario
    destinatario: Cliente = None

    # Itens (detalhamento)
    itens = None

    # Totais
    total = None

    # Grupos opcionais
    g_fat: Optional["NotaFiscalAguaFatura"] = None
    g_agencia: Optional["NotaFiscalAguaAgencia"] = None
    g_medidores = None
    g_fat_conjunto_chave = None
    g_substituicao = None

    # Autorizados XML (lista de objetos autXML do schema)
    autorizados_xml = None

    # Informacoes adicionais
    informacoes_adicionais = None

    # Responsavel tecnico
    responsavel_tecnico = None

    # Contingencia
    data_contingencia = None
    justificativa_contingencia = None

    # Compras Governo
    compra_governo = None

    # Ligacao (obrigatorio)
    ligacao_id = None
    ligacao_codigo_cliente = None
    ligacao_tipo = None
    ligacao_latitude_gps = None
    ligacao_longitude_gps = None
    ligacao_codigo_roteiro_leitura = None

    def __init__(self, *args, **kwargs):
        super(NotaFiscalAgua, self).__init__(*args, **kwargs)

        if self.itens is None:
            self.itens = []
        if self.autorizados_xml is None:
            self.autorizados_xml = []
        if self.g_medidores is None:
            self.g_medidores = []

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
        return "NFAG%(uf)s%(ano)s%(mes)s%(cnpj)s%(mod)s%(serie)s%(nNF)s%(tpEmis)s%(nSiteAutoriz)s%(cNF)s%(cDV)s" % {
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
        obj = NotaFiscalAguaItem(**kwargs)
        self.itens.append(obj)
        if self.total is None:
            self.total = NotaFiscalAguaTotal()
        total = self.total

        def _decimal_or_zero(value):
            if isinstance(value, Decimal):
                return value
            if value in (None, ""):
                return Decimal(0)
            return Decimal(value)

        total.v_prod += _decimal_or_zero(obj.valor_total)
        
        
        if obj.imposto:
            if obj.imposto.pis:
                total.v_pis += _decimal_or_zero(obj.imposto.pis.valor)
            if obj.imposto.cofins:
                total.v_cofins += _decimal_or_zero(obj.imposto.cofins.valor)
            if obj.imposto.tfs_valor is not None:
                total.v_tfs += _decimal_or_zero(obj.imposto.tfs_valor)
            if obj.imposto.tfu_valor is not None:
                total.v_tfu += _decimal_or_zero(obj.imposto.tfu_valor)
            if obj.imposto.ibs_cbs:
                ibs = obj.imposto.ibs_cbs
                total.ibs_uf_v_ibsuf += _decimal_or_zero(
                    ibs.ibs_uf.valor if ibs.ibs_uf else None
                )
                total.ibs_mun_v_ibsmun += _decimal_or_zero(
                    ibs.ibs_mun.valor if ibs.ibs_mun else None
                )
                total.cbs_v_cbs += _decimal_or_zero(ibs.cbs.valor if ibs.cbs else None)
                total.ibs_v_ibs += _decimal_or_zero(
                    (ibs.ibs_uf.valor if ibs.ibs_uf else 0)
                    + (ibs.ibs_mun.valor if ibs.ibs_mun else 0)
                )
            ret_pis = _decimal_or_zero(obj.imposto.retencao_pis_valor)
            ret_cofins = _decimal_or_zero(obj.imposto.retencao_cofins_valor)
            ret_csll = _decimal_or_zero(obj.imposto.retencao_csll_valor)
            ret_irrf = _decimal_or_zero(obj.imposto.retencao_irrf_valor)

            total.ret_v_pis += ret_pis
            total.ret_v_cofins += ret_cofins
            total.ret_v_csll += ret_csll
            total.ret_v_irrf += ret_irrf
        else:
            ret_pis = Decimal(0)
            ret_cofins = Decimal(0)
            ret_csll = Decimal(0)
            ret_irrf = Decimal(0)

        total.v_nf += _decimal_or_zero(obj.valor_total) - (
            ret_pis + ret_cofins + ret_csll + ret_irrf
        )

class NotaFiscalAguaLigacao(Entidade):
    """Dados da ligacao da NFAg."""

    codigo_ligacao = None
    codigo_cliente = None
    tipo_ligacao = None
    latitude_gps = None
    longitude_gps = None
    codigo_roteiro_leitura = None


class NotaFiscalAguaSubstituicao(Entidade):
    """Dados de substituicao da NFAg."""

    chave_nfag_referenciada = None
    motivo_substituicao = None


class NotaFiscalAguaMedidor(Entidade):
    """Dados do medidor."""

    identificacao_medidor = None
    data_leitura_anterior = None
    data_leitura_atual = None
    numero_referencia_medicao = None


class NotaFiscalAguaTarifa(Entidade):
    """Dados de tarifa por periodo."""

    data_inicio_tarifa = None
    data_fim_tarifa = None
    numero_ato = None
    ano_ato = None
    faixa_consumo = None


class NotaFiscalAguaItemMedicao(Entidade):
    """Informacoes de medicao relacionadas ao item."""

    numero_medicao = None
    unidade_medida = None
    valor_medido = None
    motivo_nao_leitura = None


class NotaFiscalAguaItem(Entidade):
    """Detalhamento de itens da NFAg."""

    numero_item = None
    codigo = None
    descricao = None
    classificacao_item = None
    categoria_ligacao = None
    categoria_detalhe = None
    quantidade_economias = None
    unidade_medida = None
    quantidade_faturada = None
    valor_unitario = None
    valor_total = None
    ind_origem_quantidade = None
    fator_poluicao = None
    indicador_devolucao = None
    medicao: Optional[NotaFiscalAguaItemMedicao] = None
    tarifas = None
    imposto: Optional["NotaFiscalAguaItemImposto"] = None
    informacoes_adicionais = None
    chave_nfag_anterior = None
    numero_item_anterior = None

    def __init__(self, *args, **kwargs):
        super(NotaFiscalAguaItem, self).__init__(*args, **kwargs)
        if self.tarifas is None:
            self.tarifas = []


class NotaFiscalAguaItemPIS(Entidade):
    modalidade = None
    base_calculo = None
    aliquota = None
    valor = None


class NotaFiscalAguaItemCOFINS(Entidade):
    modalidade = None
    base_calculo = None
    aliquota = None
    valor = None


class NotaFiscalAguaItemImposto(Entidade):
    ibs_cbs: Optional[IBS_CBS] = None
    pis: Optional[NotaFiscalAguaItemPIS] = None
    cofins: Optional[NotaFiscalAguaItemCOFINS] = None

    retencao_pis_valor = None
    retencao_cofins_valor = None
    retencao_csll_valor = None
    retencao_irrf_valor = None

    tfs_base_calculo = None
    tfs_aliquota = None
    tfs_valor = None

    tfu_base_calculo = None
    tfu_aliquota = None
    tfu_valor = None


class NotaFiscalAguaTotal(Entidade):
    v_prod = Decimal(0)
    v_cofins = Decimal(0)
    v_pis = Decimal(0)
    v_tfs = Decimal(0)
    v_tfu = Decimal(0)
    v_nf = Decimal(0)

    ret_v_pis = Decimal(0)
    ret_v_cofins = Decimal(0)
    ret_v_csll = Decimal(0)
    ret_v_irrf = Decimal(0)

    ibs_v_bcibscbs = Decimal(0)
    ibs_uf_v_dif = Decimal(0)
    ibs_uf_v_dev_trib = Decimal(0)
    ibs_uf_v_ibsuf = Decimal(0)
    ibs_mun_v_dif = Decimal(0)
    ibs_mun_v_dev_trib = Decimal(0)
    ibs_mun_v_ibsmun = Decimal(0)
    ibs_v_ibs = Decimal(0)
    cbs_v_dif = Decimal(0)
    cbs_v_dev_trib = Decimal(0)
    cbs_v_cbs = Decimal(0)


class NotaFiscalAguaFaturaEndereco(Entidade):
    logradouro = None
    numero = None
    complemento = None
    bairro = None
    codigo_municipio = None
    municipio = None
    cep = None
    uf = None
    telefone = None
    email = None


class NotaFiscalAguaFaturaPix(Entidade):
    url_qrcode_pix = None


class NotaFiscalAguaFatura(Entidade):
    competencia_faturamento = None
    data_vencimento = None
    data_apresentacao = None
    data_proxima_leitura = None
    numero_fatura = None
    codigo_barras = None
    codigo_debito_automatico = None
    codigo_banco = None
    codigo_agencia = None
    endereco_correspondencia: Optional[NotaFiscalAguaFaturaEndereco] = None
    pix: Optional[NotaFiscalAguaFaturaPix] = None


class NotaFiscalAguaAgenciaConsumo(Entidade):
    competencia_faturamento = None
    unidade_medida = None
    quantidade_dias = None
    media_diaria = None
    consumo = None
    volume_faturado = None


class NotaFiscalAguaAgenciaHistorico(Entidade):
    nome_historico = None
    consumos = None
    media_mensal = None

    def __init__(self, *args, **kwargs):
        super(NotaFiscalAguaAgenciaHistorico, self).__init__(*args, **kwargs)
        if self.consumos is None:
            self.consumos = []


class NotaFiscalAguaAgencia(Entidade):
    economia_agua = None
    economia_agua_acumulada = None
    selo_prestador = None
    data_emissao_selo = None
    selo_regulador = None
    nome_agencia_atendimento = None
    endereco_agencia_atendimento = None
    historicos = None

    def __init__(self, *args, **kwargs):
        super(NotaFiscalAguaAgencia, self).__init__(*args, **kwargs)
        if self.historicos is None:
            self.historicos = []
