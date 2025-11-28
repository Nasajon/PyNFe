from decimal import Decimal
from typing import Optional
from datetime import datetime


# Estruturas para IBS/CBS (NFS-e Nacional)
class IBS_CBS_ReferenciaNFSe:
    def __init__(self, chave: str):
        self.chave = chave


class IBS_CBS_Destinatario:
    def __init__(
        self,
        tipo_documento: str,
        numero_documento: str,
        razao_social: str,
        endereco_cep: Optional[str] = None,
        endereco_municipio: Optional[str] = None,
        endereco_uf: Optional[str] = None,
        endereco_logradouro: Optional[str] = None,
        endereco_numero: Optional[str] = None,
        endereco_complemento: Optional[str] = None,
        endereco_bairro: Optional[str] = None,
    ):
        self.tipo_documento = tipo_documento
        self.numero_documento = numero_documento
        self.razao_social = razao_social
        self.endereco_cep = endereco_cep
        self.endereco_municipio = endereco_municipio
        self.endereco_uf = endereco_uf
        self.endereco_logradouro = endereco_logradouro
        self.endereco_numero = endereco_numero
        self.endereco_complemento = endereco_complemento
        self.endereco_bairro = endereco_bairro


class IBS_CBS_Imovel:
    def __init__(
        self,
        inscricao_imobiliaria: str,
        cib: str,
        endereco_cep: str,
        endereco_logradouro: str,
        endereco_numero: str,
        endereco_bairro: str,
        endereco_complemento: Optional[str] = None,
    ):
        self.inscricao_imobiliaria = inscricao_imobiliaria
        self.cib = cib
        self.endereco_cep = endereco_cep
        self.endereco_logradouro = endereco_logradouro
        self.endereco_numero = endereco_numero
        self.endereco_complemento = endereco_complemento
        self.endereco_bairro = endereco_bairro


class IBS_CBS_Fornecedor:
    def __init__(self, tipo_documento: str, numero_documento: str, razao_social: str):
        self.tipo_documento = tipo_documento
        self.numero_documento = numero_documento
        self.razao_social = razao_social


class IBS_CBS_Documento:
    def __init__(
        self,
        tipo_documento: str,
        chave: str,
        data_emissao: datetime,
        data_competencia: datetime,
        tipo_valor: str,
        valor: Decimal,
        fornecedor: Optional[IBS_CBS_Fornecedor] = None,
    ):
        self.tipo_documento = tipo_documento
        self.chave = chave
        self.data_emissao = data_emissao
        self.data_competencia = data_competencia
        self.tipo_valor = tipo_valor
        self.valor = valor
        self.fornecedor = fornecedor


class IBS_CBS_TribRegular:
    def __init__(self, cst: str, codigo_classificacao_tributaria: str):
        self.cst = cst
        self.codigo_classificacao_tributaria = codigo_classificacao_tributaria


class IBS_CBS_Diferimento:
    def __init__(
        self,
        percentual_diferimento_uf: Decimal,
        percentual_diferimento_municipal: Decimal,
        percentual_diferimento_cbs: Decimal,
    ):
        self.percentual_diferimento_uf = percentual_diferimento_uf
        self.percentual_diferimento_municipal = percentual_diferimento_municipal
        self.percentual_diferimento_cbs = percentual_diferimento_cbs


class IBS_CBS_Tributos:
    def __init__(
        self,
        cst: str,
        codigo_classificacao_tributaria: str,
        codigo_credito_presumido: Optional[str] = None,
        trib_regular: Optional[IBS_CBS_TribRegular] = None,
        diferimento: Optional[IBS_CBS_Diferimento] = None,
    ):
        self.cst = cst
        self.codigo_classificacao_tributaria = codigo_classificacao_tributaria
        self.codigo_credito_presumido = codigo_credito_presumido
        self.trib_regular = trib_regular
        self.diferimento = diferimento


class IBS_CBS_NFSE:
    def __init__(
        self,
        codigo_indicador_operacao: str,
        indicador_destinatario: str,
        tributos: IBS_CBS_Tributos,
        destinatario: Optional[IBS_CBS_Destinatario] = None,
        imovel: Optional[IBS_CBS_Imovel] = None,
    ):
        self.codigo_indicador_operacao = codigo_indicador_operacao
        self.indicador_destinatario = indicador_destinatario
        self.referencias_nfse = []
        self.destinatario = destinatario
        self.imovel = imovel
        self.documentos_reembolso_repasse = []
        self.tributos = tributos

    def adicionar_referencia_nfse(self, referencia: IBS_CBS_ReferenciaNFSe):
        self.referencias_nfse.append(referencia)

    def adicionar_documento_reembolse_repasse(self, documento: IBS_CBS_Documento):
        self.documentos_reembolso_repasse.append(documento)
