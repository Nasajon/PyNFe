from decimal import Decimal
from pynfe.entidades.base import Entidade


class IBSComponente(Entidade):
    """Componente de IBS UF ou IBS Mun"""
    aliquota = Decimal(0)
    valor = Decimal(0)
    aliquota_diferimento = Decimal(0)
    valor_diferimento = Decimal(0)
    valor_devolucao = Decimal(0)
    percentual_reducao = Decimal(0)
    aliquota_efetiva = Decimal(0)

    def __init__(self, *args, **kwargs):
        super(IBSComponente, self).__init__(*args, **kwargs)


class CBSComponente(Entidade):
    """Componente de CBS"""
    aliquota = Decimal(0)
    valor = Decimal(0)
    aliquota_diferimento = Decimal(0)
    valor_diferimento = Decimal(0)
    valor_devolucao = Decimal(0)
    percentual_reducao = Decimal(0)
    aliquota_efetiva = Decimal(0)

    def __init__(self, *args, **kwargs):
        super(CBSComponente, self).__init__(*args, **kwargs)


class TribucaoRegular(Entidade):
    """Tributação Regular"""
    modalidade = ''
    classificacao = ''
    aliquota_ibs_uf = Decimal(0)
    valor_ibs_uf = Decimal(0)
    aliquota_ibs_mun = Decimal(0)
    valor_ibs_mun = Decimal(0)
    aliquota_cbs = Decimal(0)
    valor_cbs = Decimal(0)

    def __init__(self, *args, **kwargs):
        super(TribucaoRegular, self).__init__(*args, **kwargs)


class TribucaoCompraGov(Entidade):
    """Tributação Compra Governo"""
    aliquota_ibs_uf = Decimal(0)
    valor_ibs_uf = Decimal(0)
    aliquota_ibs_mun = Decimal(0)
    valor_ibs_mun = Decimal(0)
    aliquota_cbs = Decimal(0)
    valor_cbs = Decimal(0)

    def __init__(self, *args, **kwargs):
        super(TribucaoCompraGov, self).__init__(*args, **kwargs)


class Estorno(Entidade):
    """Estorno de Crédito"""
    valor_ibs = Decimal(0)
    valor_cbs = Decimal(0)

    def __init__(self, *args, **kwargs):
        super(Estorno, self).__init__(*args, **kwargs)


class Transferencia(Entidade):
    """Transferência de Crédito"""
    valor_ibs = Decimal(0)
    valor_cbs = Decimal(0)

    def __init__(self, *args, **kwargs):
        super(Transferencia, self).__init__(*args, **kwargs)


class AjusteCompetencia(Entidade):
    """Ajuste de competência"""
    competencia_apuracao = None
    valor_ibs = Decimal(0)
    valor_cbs = Decimal(0)

    def __init__(self, *args, **kwargs):
        super(AjusteCompetencia, self).__init__(*args, **kwargs)


class IBS_CBS_MonofasicoOperacao(Entidade):
    """Dados de uma operação monofásica padrão/retenção/retida"""
    quantidade_base_calculo = Decimal(0)
    aliquota_ibs = Decimal(0)
    aliquota_cbs = Decimal(0)
    valor_ibs = Decimal(0)
    valor_cbs = Decimal(0)

    def __init__(self, *args, **kwargs):
        super(IBS_CBS_MonofasicoOperacao, self).__init__(*args, **kwargs)


class IBS_CBS_MonofasicoDiferimento(Entidade):
    """Dados do diferimento monofásico"""
    aliquota_ibs = Decimal(0)
    aliquota_cbs = Decimal(0)
    valor_ibs = Decimal(0)
    valor_cbs = Decimal(0)

    def __init__(self, *args, **kwargs):
        super(IBS_CBS_MonofasicoDiferimento, self).__init__(*args, **kwargs)


class IBS_CBS_Monofasico(Entidade):
    """Totais e detalhamento monofásico"""
    valor_total_ibs = Decimal(0)
    valor_total_cbs = Decimal(0)
    valor_ibs = Decimal(0)
    valor_cbs = Decimal(0)
    padrao: IBS_CBS_MonofasicoOperacao = None
    retencao: IBS_CBS_MonofasicoOperacao = None
    retida: IBS_CBS_MonofasicoOperacao = None
    diferimento: IBS_CBS_MonofasicoDiferimento = None

    def __init__(self, *args, **kwargs):
        super(IBS_CBS_Monofasico, self).__init__(*args, **kwargs)


class CreditoPresumidoIBS(Entidade):
    """Dados do crédito presumido para IBS"""
    aliquota_ibs = Decimal(0)
    valor_ibs = Decimal(0)
    valor_ibs_condicao_suspensiva = Decimal(0)

    def __init__(self, *args, **kwargs):
        super(CreditoPresumidoIBS, self).__init__(*args, **kwargs)


class CreditoPresumidoCBS(Entidade):
    """Dados do crédito presumido para CBS"""
    aliquota_cbs = Decimal(0)
    valor_cbs = Decimal(0)
    valor_cbs_condicao_suspensiva = Decimal(0)

    def __init__(self, *args, **kwargs):
        super(CreditoPresumidoCBS, self).__init__(*args, **kwargs)


class CreditoPresumido(Entidade):
    """Crédito presumido por operação"""
    base_calculo = Decimal(0)
    classificacao = ''
    ibs: CreditoPresumidoIBS = None
    cbs: CreditoPresumidoCBS = None

    def __init__(self, *args, **kwargs):
        super(CreditoPresumido, self).__init__(*args, **kwargs)


class CreditoPresumidoZFM(Entidade):
    """Crédito presumido da Zona Franca de Manaus"""
    competencia_apuracao = None
    tipo = ''
    valor_ibs = Decimal(0)

    def __init__(self, *args, **kwargs):
        super(CreditoPresumidoZFM, self).__init__(*args, **kwargs)


class IBS_CBS(Entidade):
    """Imposto IBS/CBS"""
    modalidade = ''
    classificacao = ''
    base_calculo = Decimal(0)
    ibs_uf: IBSComponente = None
    ibs_mun: IBSComponente = None
    cbs: CBSComponente = None
    trib_reg: TribucaoRegular = None
    compra_gov: TribucaoCompraGov = None
    estorno: Estorno = None
    transferencia: Transferencia = None
    ajuste_competencia: AjusteCompetencia = None
    monofasico: IBS_CBS_Monofasico = None
    credito_presumido: CreditoPresumido = None
    credito_presumido_zfm: CreditoPresumidoZFM = None

    def __init__(self, *args, **kwargs):
        super(IBS_CBS, self).__init__(*args, **kwargs)
