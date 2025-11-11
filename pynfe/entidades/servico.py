"""
    @author: Junior Tada, Leonardo Tada
"""
from .base import Entidade
from decimal import Decimal


class Servico(Entidade):
    valor_servico = Decimal()
    iss_retido = int()
    """ http://www1.receita.fazenda.gov.br/sistemas/nfse/tabelas-de-codigos.htm
        Lista com códigos dos serviços
    """
    item_lista = str()
    # descrição da atividade
    discriminacao = str()
    """
        1 – Exigível;
        2 – Não incidência;
        3 – Isenção;
        4 – Exportação;
        5 – Imunidade;
        6 – Exigibilidade Suspensa por Decisão Judicial;
        7 – Exigibilidade Suspensa por ProcessoAdministrativo
    """
    exigibilidade = int()
    # Lista com todos os codigos divididos por estados na pasta data/MunIBGE
    codigo_municipio = str()
    municipio_incidencia = str()
    codigo_cnae = int()
    codigo_tributacao_nacional = str()
    codigo_tributacao_municipal = str()
    tributacao_issqn = str()
    tipo_retencao_issqn = str()
    cst_pis_cofins = str()
    tipo_retencao_pis_cofins = str()
    codigo_nbs = str()
    # Dados opcionais
    valor_deducoes = Decimal()
    valor_pis = Decimal()
    valor_cofins = Decimal()
    valor_inss = Decimal()
    valor_ir = Decimal()
    valor_csll = Decimal()
    valor_iss = Decimal()
    valor_iss_retido = Decimal()
    valor_liquido = Decimal()
    outras_retencoes = Decimal()
    base_calculo = Decimal()
    aliquota = Decimal()
    desconto_incondicionado = Decimal()
    desconto_condicionado = Decimal()
    total_tributos_federais = Decimal()
    total_tributos_estaduais = Decimal()
    total_tributos_municipais = Decimal()
    base_calculo_pis_cofins = Decimal()
    aliquota_pis = Decimal()
    aliquota_cofins = Decimal()
    valor_cp = Decimal()
    valor_irrf = Decimal()

    def __str__(self):
        return self.discriminacao
