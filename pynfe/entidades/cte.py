# -*- coding: utf-8 -*-
from datetime import datetime
import random
from decimal import Decimal

from pynfe import get_version

# from pynfe.utils import so_numeros, memoize
from pynfe.entidades.cliente import Cliente
from pynfe.entidades.emitente import Emitente
from pynfe.entidades.pessoa import Pessoa
from pynfe.utils import so_numeros
from pynfe.utils.flags import CODIGOS_ESTADOS, CTE_STATUS

from .base import Entidade


class CTe(Entidade):

    status = CTE_STATUS[0]

    # Código numérico aleatório que compõe a chave de acesso
    codigo_numerico_aleatorio = ''

    # Digito verificador do codigo numerico aleatorio
    dv_codigo_numerico_aleatorio = ''

    # Nota Fisca eletronica
    # - Modelo (formato: NN)
    modelo = 57

    # - Serie (obrigatorio - formato: NNN)
    serie = ''

    # - Numero NF (obrigatorio)
    numero = ''

    # - Data da Emissao (obrigatorio)
    data_emissao: datetime = None

    # - Natureza da Operacao (obrigatorio)
    natureza_operacao = ''

    # - Tipo do Documento (obrigatorio - seleciona de lista) - NF_TIPOS_DOCUMENTO
    tipo_cte = 0

    # - Processo de emissão da NF-e (obrigatorio - seleciona de lista) - NF_PROCESSOS_EMISSAO
    processo_emissao = 0

    # - Versao do processo de emissão da NF-e
    versao_processo_emissao = get_version()

    # - Forma de emissao (obrigatorio - seleciona de lista) - NF_FORMAS_EMISSAO
    forma_emissao = 1

    cfop = ''

    # - Emitente
    emitente: Emitente = None

    # - Destinatario
    #  - Identificacao (seleciona de Clientes)
    cliente: Cliente = None

    tipo_impressao_dacte = 1

    uf_envio = ''

    municipio_envio = ''

    uf_inicio = ''

    municipio_inicio = ''

    uf_fim = ''

    municipio_fim = ''

    modal = "0"

    tipo_servico = 0

    retira = 1 # 1 - Não, 0 - Sim

    indicador_ie = 0

    tipo_tomador = 0

    tomador: Pessoa = None

    observacao = ''

    remetente: Pessoa = None

    expedidor: Pessoa = None

    recebidor: Pessoa = None

    valor_total_prestacao = Decimal(0)
    valor_receber_prestacao = Decimal(0)
    valor_total_tributos = None

    icms_modalidade = ""

    icms_valor_base_calculo = Decimal(0)
    icms_valor = Decimal(0)
    icms_aliquota = Decimal(0)
    icms_percentual_reducao_bc = Decimal(0)
    valor_carga = Decimal(0)
    carga_predominante = ""

    rodoviario_registro = ''
    fatura_numero = ''
    fatura_valor_original = Decimal(0)
    fatura_valor_desconto = Decimal(0)
    fatura_valor_liquido = Decimal(0)

    compra_gov_ente = 0
    compra_gov_redutor = Decimal(0)

    def __init__(self, *args, **kwargs):
        self.prestacao_componentes: list[CTeComponente] = []
        self.cargas: list[CTeCarga] = []
        self.duplicatas: list[CTeDuplicata] = []
        self.nfes: list[CTeNFe] = []
        self.ibs_cbs: IBS_CBS_CTE = None
        

        super(CTe, self).__init__(*args, **kwargs)

    def __str__(self):
        return " ".join([str(self.modelo), self.serie, self.numero_nf])

    def adicionar_duplicata(self, **kwargs):
        """Adiciona uma instancia de Duplicata"""
        obj = CTeDuplicata(**kwargs)
        self.duplicatas.append(obj)
        return obj
    
    def adicionar_carga(self, **kwargs):
        """Adiciona uma instancia de Duplicata"""
        obj = CTeCarga(**kwargs)
        self.cargas.append(obj)
        return obj

    def adicionar_prestacao_componente(self, **kwargs):
        """Adiciona uma instancia de Duplicata"""
        obj = CTeComponente(**kwargs)
        self.prestacao_componentes.append(obj)
        return obj
    
    def adicionar_nfe(self, **kwargs):
        """Adiciona uma instancia de Duplicata"""
        obj = CTeNFe(**kwargs)
        self.nfes.append(obj)
        return obj

    def _codigo_numerico_aleatorio(self):
        if not self.codigo_numerico_aleatorio:
            self.codigo_numerico_aleatorio = str(random.randint(0, 99999999)).zfill(8)
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
            # cycle though weights
            i = i % weights_size
            key_sum += key_number * weights[i]

        remainder = key_sum % 11
        if remainder == 0 or remainder == 1:
            self.dv_codigo_numerico_aleatorio = "0"
            return "0"
        self.dv_codigo_numerico_aleatorio = str(11 - remainder)
        return str(self.dv_codigo_numerico_aleatorio)

    @property
    # @memoize
    def identificador_unico(self):
        # Monta 'Id' da tag raiz <infNFe>
        # Ex.: NFe35080599999090910270550010000000011518005123
        key = "%(uf)s%(ano)s%(mes)s%(cnpj)s%(mod)s%(serie)s%(nCT)s%(tpEmis)s%(cCT)s" % {
            "uf": CODIGOS_ESTADOS[self.emitente.endereco_uf],
            "ano": self.data_emissao.strftime("%y"),
            "mes": self.data_emissao.strftime("%m"),
            "cnpj": so_numeros(self.emitente.cnpj).zfill(14),
            "mod": self.modelo,
            "serie": str(self.serie).zfill(3),
            "nCT": str(self.numero).zfill(9),
            "tpEmis": str(self.forma_emissao),
            "cCT": self._codigo_numerico_aleatorio(),
        }
        return "CTe%(uf)s%(ano)s%(mes)s%(cnpj)s%(mod)s%(serie)s%(nCT)s%(tpEmis)s%(cCT)s%(cDV)s" % {
            "uf": CODIGOS_ESTADOS[self.emitente.endereco_uf],
            "ano": self.data_emissao.strftime("%y"),
            "mes": self.data_emissao.strftime("%m"),
            "cnpj": so_numeros(self.emitente.cnpj).zfill(14),
            "mod": self.modelo,
            "serie": str(self.serie).zfill(3),
            "nCT": str(self.numero).zfill(9),
            "tpEmis": str(self.forma_emissao),
            "cCT": str(self.codigo_numerico_aleatorio),
            "cDV": self._dv_codigo_numerico(key),
        }
    
class CTeDuplicata(Entidade):
    numero = ''
    valor = Decimal(0)
    vencimento: datetime = None

    def __init__(self, *args, **kwargs):

      super(CTeDuplicata, self).__init__(*args, **kwargs)

class CTeCarga(Entidade):
    codigo_unidade = ''
    tipo_medida = ''
    quantidade = Decimal(0)

    def __init__(self, *args, **kwargs):

      super(CTeCarga, self).__init__(*args, **kwargs)

class CTeComponente(Entidade):
    nome = ''
    valor = Decimal(0)

    def __init__(self, *args, **kwargs):

      super(CTeComponente, self).__init__(*args, **kwargs)

class CTeNFe(Entidade):
    chave = ''

    def __init__(self, *args, **kwargs):

      super(CTeNFe, self).__init__(*args, **kwargs)


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


class IBS_CBS_CTE(Entidade):
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

    def __init__(self, *args, **kwargs):
        super(IBS_CBS_CTE, self).__init__(*args, **kwargs)
