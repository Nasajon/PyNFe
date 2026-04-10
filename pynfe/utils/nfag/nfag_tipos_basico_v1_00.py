from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from pynfe_nasajon.pynfe.utils.nfag.dfe_tipos_basicos_v1_00 import (
    TcompraGovReduzido,
    Tibscbstot,
    TtribNfag,
)
from pynfe_nasajon.pynfe.utils.nfag.tipos_geral_nfag_v1_00 import (
    Tamb,
    TcodUfIbge,
    TmodNfag,
    Tuf,
    TufSemEx,
)
from pynfe_nasajon.pynfe.utils.nfag.xmldsig_core_schema_v1_01 import Signature

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfag"


class CofinsCst(Enum):
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_49 = "49"


class PisCst(Enum):
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_49 = "49"


class TcategAg(Enum):
    """
    Tipo Categoria.
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_04 = "04"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_99 = "99"


@dataclass(kw_only=True)
class TempresaSoft:
    """
    Tipo Dados da Empresa de Software.

    :ivar cnpj: CNPJ da pessoa jurídica desenvolvedora do sistema
        utilizado na emissão do documento fiscal eletrônico Informar o
        CNPJ da pessoa jurídica desenvolvedora do sistema utilizado na
        emissão do documento fiscal eletrônico.
    :ivar cpf: CPF da pessoa física desenvolvedora do sistema utilizado
        na emissão do documento fiscal eletrônico No caso de pessoa
        física, informar o CPF do desenvolvedor do sistema utilizado na
        emissão do documento fiscal eletrônico.
    :ivar x_contato: Nome da pessoa a ser contatada Informar o nome da
        pessoa a ser contatada na empresa desenvolvedora do sistema
        utilizado na emissão do documento fiscal eletrônico. No caso de
        pessoa física, informar o respectivo nome.
    :ivar email: Email da pessoa jurídica/física a ser contatada
    :ivar fone: Telefone da pessoa jurídica/física a ser contatada
        Preencher com o Código DDD + número do telefone.
    """

    class Meta:
        name = "TEmpresaSoft"

    cnpj: None | str = field(
        default=None,
        metadata={
            "name": "CNPJ",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"[A-Z0-9]{12}[0-9]{2}",
        },
    )
    cpf: None | str = field(
        default=None,
        metadata={
            "name": "CPF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"[0-9]{11}",
        },
    )
    x_contato: str = field(
        metadata={
            "name": "xContato",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "min_length": 2,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    email: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[^@]+@[^\.]+\..+",
        }
    )
    fone: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"[0-9]{7,12}",
        }
    )


class Tfaixa(Enum):
    """
    Tipo de tarifa de aplicação.
    """

    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class TfatNfag(Enum):
    """
    Tipo de Faturamento da NFAg.
    """

    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class TfinNfag(Enum):
    """
    Finalidade da NFAg.
    """

    VALUE_0 = "0"
    VALUE_3 = "3"


class TgrMedAg(Enum):
    """
    Tipo Grupo Medida.
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_99 = "99"


class Tligacao(Enum):
    """
    Tipo Ligação.
    """

    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class TmotNaoLeitura(Enum):
    """
    Tipo motivo não leitura.
    """

    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class TmotSubAg(Enum):
    """
    Tipo Motivo Substituição.
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"


class TorigemQtdAg(Enum):
    """
    Tipo do indicador de origem da quantidade faturada.
    """

    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"
    VALUE_7 = "7"


class TprocessoAg(Enum):
    """
    Tipo de processo judicial.
    """

    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"


@dataclass(kw_only=True)
class TrespTec:
    """
    Tipo Dados da Responsável Técnico.

    :ivar cnpj: CNPJ da pessoa jurídica responsável técnica pelo sistema
        utilizado na emissão do documento fiscal eletrônico Informar o
        CNPJ da pessoa jurídica desenvolvedora do sistema utilizado na
        emissão do documento fiscal eletrônico.
    :ivar x_contato: Nome da pessoa a ser contatada Informar o nome da
        pessoa a ser contatada na empresa desenvolvedora do sistema
        utilizado na emissão do documento fiscal eletrônico. No caso de
        pessoa física, informar o respectivo nome.
    :ivar email: Email da pessoa jurídica a ser contatada
    :ivar fone: Telefone da pessoa jurídica a ser contatada Preencher
        com o Código DDD + número do telefone.
    :ivar id_csrt: Identificador do código de segurança do responsável
        técnico Identificador do CSRT utilizado para geração do hash
    :ivar hash_csrt: Hash do token do código de segurança do responsável
        técnico O hashCSRT é o resultado das funções SHA-1 e base64 do
        token CSRT fornecido pelo fisco + chave de acesso do DF-e.
        (Implementação em futura NT) Observação: 28 caracteres são
        representados no schema como 20 bytes do tipo base64Binary
    """

    class Meta:
        name = "TRespTec"

    cnpj: str = field(
        metadata={
            "name": "CNPJ",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"[A-Z0-9]{12}[0-9]{2}",
        }
    )
    x_contato: str = field(
        metadata={
            "name": "xContato",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "min_length": 2,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    email: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[^@]+@[^\.]+\..+",
        }
    )
    fone: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"[0-9]{7,12}",
        }
    )
    id_csrt: None | str = field(
        default=None,
        metadata={
            "name": "idCSRT",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "pattern": r"[0-9]{3}",
        },
    )
    hash_csrt: None | bytes = field(
        default=None,
        metadata={
            "name": "hashCSRT",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "length": 20,
            "format": "base64",
        },
    )


class TumedAg(Enum):
    """
    Tipo da unidade básica de medida.
    """

    VALUE_1 = "1"
    VALUE_2 = "2"


class TumedItemAg(Enum):
    """
    Tipo da unidade básica de medida.
    """

    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_5 = "5"
    VALUE_6 = "6"


class TtpEmis(Enum):
    """
    Tipo de emissão da NFAg.
    """

    VALUE_1 = "1"
    VALUE_2 = "2"


class GProcRefIndDevolucao(Enum):
    VALUE_1 = "1"


class ProdIndDevolucao(Enum):
    VALUE_1 = "1"


@dataclass(kw_only=True)
class TendeEmi:
    """
    Tipo Dados do Endereço.

    :ivar x_lgr: Logradouro
    :ivar nro: Número
    :ivar x_cpl: Complemento
    :ivar x_bairro: Bairro
    :ivar c_mun: Código do município (utilizar a tabela do IBGE)
    :ivar x_mun: Nome do município
    :ivar cep: CEP Informar zeros não significativos
    :ivar uf: Sigla da UF
    :ivar fone: Telefone
    :ivar email: Endereço de E-mail
    """

    class Meta:
        name = "TEndeEmi"

    x_lgr: str = field(
        metadata={
            "name": "xLgr",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "min_length": 2,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    nro: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    x_cpl: None | str = field(
        default=None,
        metadata={
            "name": "xCpl",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        },
    )
    x_bairro: str = field(
        metadata={
            "name": "xBairro",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "min_length": 2,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    c_mun: str = field(
        metadata={
            "name": "cMun",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    x_mun: str = field(
        metadata={
            "name": "xMun",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "min_length": 2,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    cep: str = field(
        metadata={
            "name": "CEP",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )
    uf: TufSemEx = field(
        metadata={
            "name": "UF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        }
    )
    fone: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"[0-9]{7,12}",
        },
    )
    email: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[^@]+@[^\.]+\..+",
        },
    )


@dataclass(kw_only=True)
class Tendereco:
    """
    Tipo Dados do Endereço.

    :ivar x_lgr: Logradouro
    :ivar nro: Número
    :ivar x_cpl: Complemento
    :ivar x_bairro: Bairro
    :ivar c_mun: Código do município (utilizar a tabela do IBGE),
        informar 9999999 para operações com o exterior.
    :ivar x_mun: Nome do município, informar EXTERIOR para operações com
        o exterior.
    :ivar cep: CEP Informar os zeros não significativos
    :ivar uf: Sigla da UF, informar EX para operações com o exterior.
    :ivar c_pais: Código do país Utilizar a tabela do BACEN
    :ivar x_pais: Nome do país
    :ivar fone: Telefone
    :ivar email: Endereço de E-mail
    """

    class Meta:
        name = "TEndereco"

    x_lgr: str = field(
        metadata={
            "name": "xLgr",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    nro: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    x_cpl: None | str = field(
        default=None,
        metadata={
            "name": "xCpl",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        },
    )
    x_bairro: str = field(
        metadata={
            "name": "xBairro",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    c_mun: str = field(
        metadata={
            "name": "cMun",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    x_mun: str = field(
        metadata={
            "name": "xMun",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    cep: None | str = field(
        default=None,
        metadata={
            "name": "CEP",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        },
    )
    uf: Tuf = field(
        metadata={
            "name": "UF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        }
    )
    c_pais: None | str = field(
        default=None,
        metadata={
            "name": "cPais",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"[0-9]{1,4}",
        },
    )
    x_pais: None | str = field(
        default=None,
        metadata={
            "name": "xPais",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        },
    )
    fone: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"[0-9]{7,12}",
        },
    )
    email: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[^@]+@[^\.]+\..+",
        },
    )


@dataclass(kw_only=True)
class TmedidaAg:
    """
    Tipo de dados de medida.

    :ivar tp_gr_med: Tipo de grandeza medida 01 - Água Tratada; 02 -
        Esgoto tratado; 03 - Esgoto coletado; 04 - Resíduos sólidos; 05
        - Água de reuso; 06 - Esgoto Estatico 07 - Captação de agua
        bruta 08 - Recebimento e tratamento de chorume 99 - Outros
    :ivar n_unid_consumo: Número da unidade de consumo
    :ivar v_unid_consumo: Volume por unidade de consumo em m3
    :ivar u_med: Unidade Básica de Medida 1 - m3; 2 - Litros; 5 -
        Unidade 6 - ton
    :ivar v_med_ant: Valor da medição (leitura) anterior
    :ivar v_med_atu: Valor da medição (leitura) atual
    :ivar v_const: Indicar o fator de multiplicação do medidor
    :ivar v_med: Valor da medição (vMedAtu – vMedAnt) * vConst
    """

    class Meta:
        name = "TMedidaAG"

    tp_gr_med: TgrMedAg = field(
        metadata={
            "name": "tpGrMed",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        }
    )
    n_unid_consumo: None | str = field(
        default=None,
        metadata={
            "name": "nUnidConsumo",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "length": 15,
        },
    )
    v_unid_consumo: None | str = field(
        default=None,
        metadata={
            "name": "vUnidConsumo",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"[0-9]{1,13}(\.[0-9]{2,4})?",
        },
    )
    u_med: TumedItemAg = field(
        metadata={
            "name": "uMed",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        }
    )
    v_med_ant: str = field(
        metadata={
            "name": "vMedAnt",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"[0-9]{1,13}(\.[0-9]{2,4})?",
        }
    )
    v_med_atu: str = field(
        metadata={
            "name": "vMedAtu",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"[0-9]{1,13}(\.[0-9]{2,4})?",
        }
    )
    v_const: None | str = field(
        default=None,
        metadata={
            "name": "vConst",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"[0-9]{1,13}(\.[0-9]{2,6})?",
        },
    )
    v_med: str = field(
        metadata={
            "name": "vMed",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"[0-9]{1,13}(\.[0-9]{2,4})?",
        }
    )


@dataclass(kw_only=True)
class TprotNfag:
    """
    Tipo Protocolo de status resultado do processamento da NFAg.

    :ivar inf_prot: Dados do protocolo de status
    :ivar inf_fisco: Mensagem do Fisco
    :ivar signature:
    :ivar versao:
    """

    class Meta:
        name = "TProtNFAg"

    inf_prot: TprotNfag.InfProt = field(
        metadata={
            "name": "infProt",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        }
    )
    inf_fisco: None | TprotNfag.InfFisco = field(
        default=None,
        metadata={
            "name": "infFisco",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    signature: None | Signature = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    versao: str = field(
        metadata={
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"1\.00",
        }
    )

    @dataclass(kw_only=True)
    class InfProt:
        """
        :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
            Homologação
        :ivar ver_aplic: Versão do Aplicativo que processou a NFAg
        :ivar ch_nfag: Chave de acesso da NFAg
        :ivar dh_recbto: Data e hora de processamento, no formato AAAA-
            MM-DDTHH:MM:SS TZD.
        :ivar n_prot: Número do Protocolo de Status da NFAg.
        :ivar dig_val: Digest Value da NFAg processado. Utilizado para
            conferir a integridade da NFAg original.
        :ivar c_stat: Código do status da NFAg
        :ivar x_motivo: Descrição literal do status da NFAg
        :ivar id:
        """

        tp_amb: Tamb = field(
            metadata={
                "name": "tpAmb",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
            }
        )
        ver_aplic: str = field(
            metadata={
                "name": "verAplic",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        ch_nfag: str = field(
            metadata={
                "name": "chNFAg",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "max_length": 44,
                "white_space": "preserve",
                "pattern": r"[0-9]{6}[A-Z0-9]{12}[0-9]{26}",
            }
        )
        dh_recbto: str = field(
            metadata={
                "name": "dhRecbto",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
            }
        )
        n_prot: None | str = field(
            default=None,
            metadata={
                "name": "nProt",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"[0-9]{16}",
            },
        )
        dig_val: None | bytes = field(
            default=None,
            metadata={
                "name": "digVal",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "format": "base64",
            },
        )
        c_stat: str = field(
            metadata={
                "name": "cStat",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"[0-9]{3,4}",
            }
        )
        x_motivo: str = field(
            metadata={
                "name": "xMotivo",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "min_length": 1,
                "max_length": 255,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        id: None | str = field(
            default=None,
            metadata={
                "name": "Id",
                "type": "Attribute",
            },
        )

    @dataclass(kw_only=True)
    class InfFisco:
        """
        :ivar c_msg: Código do status da mensagem do fisco
        :ivar x_msg: Mensagem do Fisco
        """

        c_msg: str = field(
            metadata={
                "name": "cMsg",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"[0-9]{3,4}",
            }
        )
        x_msg: str = field(
            metadata={
                "name": "xMsg",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "min_length": 1,
                "max_length": 255,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )


@dataclass(kw_only=True)
class Tnfag:
    """
    Tipo Nota Fiscal de Agua.

    :ivar inf_nfag: Informações da NFAg
    :ivar inf_nfag_supl: Informações suplementares da NFAg
    :ivar signature:
    """

    class Meta:
        name = "TNFAg"

    inf_nfag: Tnfag.InfNfag = field(
        metadata={
            "name": "infNFAg",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        }
    )
    inf_nfag_supl: Tnfag.InfNfagSupl = field(
        metadata={
            "name": "infNFAgSupl",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        }
    )
    signature: Signature = field(
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )

    @dataclass(kw_only=True)
    class InfNfag:
        """
        :ivar ide: Identificação da NFAg
        :ivar emit: Identificação do Emitente do documento fiscal
        :ivar dest: Identificação do destinatário
        :ivar ligacao: Dados da Ligação
        :ivar g_sub: Grupo de informações da substituição
        :ivar g_med: Grupo de informações dos Medidores
        :ivar g_fat_conjunto: Grupo de Informações do Faturamento
            conjunto
        :ivar det: Detalhamento de Produtos e Serviços
        :ivar total: Dados dos totais da NFAg
        :ivar g_fat: Grupo de informações de controle da Fatura
            Obrigatorio para tpFat 1 e 3 Vedado para tpFat 2
        :ivar g_agencia: Grupo de informações da Agência reguladora
        :ivar g_quali_agua: Informações sobre a qualidade de água
        :ivar aut_xml: Autorizados para download do XML do DF-e Informar
            CNPJ ou CPF. Preencher os zeros não significativos.
        :ivar inf_adic: Informações Adicionais
        :ivar inf_paa: Grupo de Informação do Provedor de Assinatura e
            Autorização
        :ivar g_resp_tec: Informações do Responsável Técnico pela
            emissão do DF-e
        :ivar versao: Versão do leiaute
        :ivar id: Identificador da tag a ser assinada Informar a chave
            de acesso da NFAg e precedida do literal "NFAg"
        """

        ide: Tnfag.InfNfag.Ide = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
            }
        )
        emit: Tnfag.InfNfag.Emit = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
            }
        )
        dest: Tnfag.InfNfag.Dest = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
            }
        )
        ligacao: Tnfag.InfNfag.Ligacao = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
            }
        )
        g_sub: None | Tnfag.InfNfag.GSub = field(
            default=None,
            metadata={
                "name": "gSub",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
            },
        )
        g_med: list[Tnfag.InfNfag.GMed] = field(
            default_factory=list,
            metadata={
                "name": "gMed",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "max_occurs": 99,
            },
        )
        g_fat_conjunto: None | Tnfag.InfNfag.GFatConjunto = field(
            default=None,
            metadata={
                "name": "gFatConjunto",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
            },
        )
        det: list[Tnfag.InfNfag.Det] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "min_occurs": 1,
                "max_occurs": 990,
            },
        )
        total: Tnfag.InfNfag.Total = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
            }
        )
        g_fat: None | Tnfag.InfNfag.GFat = field(
            default=None,
            metadata={
                "name": "gFat",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
            },
        )
        g_agencia: Tnfag.InfNfag.GAgencia = field(
            metadata={
                "name": "gAgencia",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
            }
        )
        g_quali_agua: None | Tnfag.InfNfag.GQualiAgua = field(
            default=None,
            metadata={
                "name": "gQualiAgua",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
            },
        )
        aut_xml: list[Tnfag.InfNfag.AutXml] = field(
            default_factory=list,
            metadata={
                "name": "autXML",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "max_occurs": 10,
            },
        )
        inf_adic: None | Tnfag.InfNfag.InfAdic = field(
            default=None,
            metadata={
                "name": "infAdic",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
            },
        )
        inf_paa: None | Tnfag.InfNfag.InfPaa = field(
            default=None,
            metadata={
                "name": "infPAA",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
            },
        )
        g_resp_tec: None | TrespTec = field(
            default=None,
            metadata={
                "name": "gRespTec",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
            },
        )
        versao: str = field(
            metadata={
                "type": "Attribute",
                "white_space": "preserve",
                "pattern": r"1\.00",
            }
        )
        id: str = field(
            metadata={
                "name": "Id",
                "type": "Attribute",
                "pattern": r"NFAG[0-9]{6}[A-Z0-9]{12}[0-9]{26}",
            }
        )

        @dataclass(kw_only=True)
        class Ide:
            """
            :ivar c_uf: Código da UF do emitente da NFAg Código da UF do
                emitente do Documento Fiscal. Utilizar a Tabela do IBGE
                de código de unidades da federação.
            :ivar tp_amb: Tipo do Ambiente 1 - Produção; 2 - Homologação
            :ivar mod: Modelo da NFAg Utilizar o código 75 para
                identificação da NFag
            :ivar serie: Série do documento fiscal Informar a série do
                documento fiscal (informar zero para série única).
            :ivar n_nf: Número do documento fiscal Número que identifica
                o documento fiscal 1 a 999999999.
            :ivar c_nf: Código numérico que compõe a Chave de Acesso.
                Código aleatório gerado pelo emitente, com o objetivo de
                evitar acessos indevidos ao documento.
            :ivar c_dv: Digito verificador da chave de acesso Informar o
                dígito  de controle da chave de acesso documento fiscal,
                que deve ser calculado com a aplicação do algoritmo
                módulo 11 (base 2,9) da chave de acesso.
            :ivar dh_emi: Data e hora de emissão do documento fiscal
                Formato AAAA-MM-DDTHH:MM:DD TZD
            :ivar tp_emis: Forma de emissão do Documento Fiscal 1 -
                Normal ; 2 - Contingência Off Line
            :ivar n_site_autoriz: Identificação do número do Site do
                Autorizador de recepção da NFAg Se o autorizador da NFAg
                possuir apenas um site deverá ser informado com Zero
                (0), em caso de Autorizador trabalhar com múltiplos
                sites indicar o número do site para qual foi endereçada
                a NFAg (1 a 9). Observação: O ambiente autorizador que
                trabalhar com mais de um Site deverá divulgar para cada
                endereço de site qual número correspondente de
                nSiteAutoriz o contribuinte pode usar
            :ivar c_mun_fg: Código do município de ocorrência do fato
                gerador
            :ivar fin_nfag: Finalidade de emissão da NFAg 0 - NFAg
                normal; 3 - NFAg substituição;
            :ivar tp_fat: Tipo de Faturamento da NFAg 1 - Faturamento
                Normal; 2 - Faturamento por terceiro; 3 - Faturamento
                conjunto 1- Faturamento Normal; 2 - Faturamento por
                terceiro; 3 - Faturamento conjunto
            :ivar ver_proc: Versão do processo de emissão Informar a
                versão do aplicativo emissor de NFAg
            :ivar dh_cont: Data e Hora da entrada em contingência
                Informar a data e hora no formato AAAA-MM-DDTHH:MM:SS
            :ivar x_just: Justificativa da entrada em contingência
            :ivar g_compra_gov: Grupo de Compras Governamentais
            """

            c_uf: TcodUfIbge = field(
                metadata={
                    "name": "cUF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                }
            )
            tp_amb: Tamb = field(
                metadata={
                    "name": "tpAmb",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                }
            )
            mod: TmodNfag = field(
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                }
            )
            serie: str = field(
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"0|[1-9]{1}[0-9]{0,2}",
                }
            )
            n_nf: str = field(
                metadata={
                    "name": "nNF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"[1-9]{1}[0-9]{0,8}",
                }
            )
            c_nf: str = field(
                metadata={
                    "name": "cNF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{7}",
                }
            )
            c_dv: str = field(
                metadata={
                    "name": "cDV",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{1}",
                }
            )
            dh_emi: str = field(
                metadata={
                    "name": "dhEmi",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            tp_emis: TtpEmis = field(
                metadata={
                    "name": "tpEmis",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                }
            )
            n_site_autoriz: str = field(
                metadata={
                    "name": "nSiteAutoriz",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{1}",
                }
            )
            c_mun_fg: str = field(
                metadata={
                    "name": "cMunFG",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{7}",
                }
            )
            fin_nfag: TfinNfag = field(
                metadata={
                    "name": "finNFAg",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                }
            )
            tp_fat: TfatNfag = field(
                metadata={
                    "name": "tpFat",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                }
            )
            ver_proc: str = field(
                metadata={
                    "name": "verProc",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            dh_cont: None | str = field(
                default=None,
                metadata={
                    "name": "dhCont",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                },
            )
            x_just: None | str = field(
                default=None,
                metadata={
                    "name": "xJust",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "min_length": 15,
                    "max_length": 256,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                },
            )
            g_compra_gov: None | TcompraGovReduzido = field(
                default=None,
                metadata={
                    "name": "gCompraGov",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                },
            )

        @dataclass(kw_only=True)
        class Emit:
            """
            :ivar cnpj: CNPJ do emitente Informar zeros não
                significativos
            :ivar ie: Inscrição Estadual do emitente
            :ivar x_nome: Razão social ou Nome do emitente
            :ivar x_fant: Nome fantasia do emitente
            :ivar ender_emit: Endereço do emitente
            """

            cnpj: str = field(
                metadata={
                    "name": "CNPJ",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"[A-Z0-9]{12}[0-9]{2}",
                }
            )
            ie: None | str = field(
                default=None,
                metadata={
                    "name": "IE",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}",
                },
            )
            x_nome: str = field(
                metadata={
                    "name": "xNome",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            x_fant: None | str = field(
                default=None,
                metadata={
                    "name": "xFant",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "min_length": 1,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                },
            )
            ender_emit: TendeEmi = field(
                metadata={
                    "name": "enderEmit",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                }
            )

        @dataclass(kw_only=True)
        class Dest:
            """
            :ivar x_nome: Razão social ou Nome do destinatário
            :ivar cnpj: Número do CNPJ Informar os zeros não
                significativos.
            :ivar cpf: Número do CPF Informar os zeros não
                significativos.
            :ivar id_outros: Identificação do destinatário outros
                Identificação do destinatário não obrigado a inscrição
                do CPF tais como estrangeiro, indígena (informar código
                do RANI) e quilombola; ou destinatário que a
                distribuidora não possui a informação (nestes casos
                orienta-se informar "00000").
            :ivar ie: Inscrição Estadual do destinatário
            :ivar im: Inscrição Municipal
            :ivar c_nis: Número da Identificação Social - NIS
            :ivar nb: Número do Benefício
            :ivar x_nome_adicional: Nome de destinatário adicional
                Exemplo: Nome do Conjuge, Companheira(o)
            :ivar ender_dest: Endereço do destinatário / acessante
            """

            x_nome: str = field(
                metadata={
                    "name": "xNome",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            cnpj: None | str = field(
                default=None,
                metadata={
                    "name": "CNPJ",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0}|[A-Z0-9]{12}[0-9]{2}",
                },
            )
            cpf: None | str = field(
                default=None,
                metadata={
                    "name": "CPF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                },
            )
            id_outros: None | str = field(
                default=None,
                metadata={
                    "name": "idOutros",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "min_length": 2,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"([!-ÿ]{0}|[!-ÿ]{2,20})?",
                },
            )
            ie: None | str = field(
                default=None,
                metadata={
                    "name": "IE",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0,14}|ISENTO",
                },
            )
            im: None | str = field(
                default=None,
                metadata={
                    "name": "IM",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "min_length": 1,
                    "max_length": 15,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                },
            )
            c_nis: None | str = field(
                default=None,
                metadata={
                    "name": "cNIS",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "min_length": 1,
                    "max_length": 15,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{15}",
                },
            )
            nb: None | str = field(
                default=None,
                metadata={
                    "name": "NB",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "min_length": 1,
                    "max_length": 10,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{10}",
                },
            )
            x_nome_adicional: None | str = field(
                default=None,
                metadata={
                    "name": "xNomeAdicional",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                },
            )
            ender_dest: TendeEmi = field(
                metadata={
                    "name": "enderDest",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                }
            )

        @dataclass(kw_only=True)
        class Ligacao:
            """
            :ivar id_ligacao: Código único de Identificação da Ligação
            :ivar id_cod_cliente: Código de Identificação do Cliente
                para empresa emitente
            :ivar tp_ligacao: Tipo de Ligação 1 - Agua 2 - Esgoto 3 -
                Agua e esgoto
            :ivar lat_gps: Latitude do ponto geográfico da localização
                da captura
            :ivar long_gps: Longitude do ponto geográfico da localização
                da captura
            :ivar cod_roteiro_leitura: Roteiro da Leitura para uso
                operacional Identificador interno da concessionária para
                a roteirização do leiturista, utilizado no DANFE para
                facilitar a identificação da rota de entrega da fatura
            """

            id_ligacao: str = field(
                metadata={
                    "name": "idLigacao",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"([!-ÿ]{0}|[!-ÿ]{1,15})?",
                }
            )
            id_cod_cliente: None | str = field(
                default=None,
                metadata={
                    "name": "idCodCliente",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "min_length": 2,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"([!-ÿ]{0}|[!-ÿ]{2,20})?",
                },
            )
            tp_ligacao: Tligacao = field(
                metadata={
                    "name": "tpLigacao",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                }
            )
            lat_gps: str = field(
                metadata={
                    "name": "latGPS",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"[0-9]\.[0-9]{6}|[1-8][0-9]\.[0-9]{6}|90\.[0-9]{6}|-[0-9]\.[0-9]{6}|-[1-8][0-9]\.[0-9]{6}|-90\.[0-9]{6}",
                }
            )
            long_gps: str = field(
                metadata={
                    "name": "longGPS",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"[0-9]\.[0-9]{6}|[1-9][0-9]\.[0-9]{6}|1[0-7][0-9]\.[0-9]{6}|180\.[0-9]{6}|-[0-9]\.[0-9]{6}|-[1-9][0-9]\.[0-9]{6}|-1[0-7][0-9]\.[0-9]{6}|-180\.[0-9]{6}",
                }
            )
            cod_roteiro_leitura: None | str = field(
                default=None,
                metadata={
                    "name": "codRoteiroLeitura",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "min_length": 2,
                    "max_length": 100,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                },
            )

        @dataclass(kw_only=True)
        class GSub:
            """
            :ivar ch_nfag: Chave de acesso da NFAg referenciada
            :ivar mot_sub: Motivo da substituição 01 – Erro de Leitura
                02 – Erro de Preço ou Erro de Tarifa; 03 – Decisão
                Judicial 04 – Erro Cadastral; 05 - Erro de Tributação 06
                - Decisão da Reguladora; 07 - Acúmulo de Consumo; 08 -
                Correção de Vazamento Interno 09 - Alteração de
                vencimento
            """

            ch_nfag: str = field(
                metadata={
                    "name": "chNFAg",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "max_length": 44,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{6}[A-Z0-9]{12}[0-9]{26}",
                }
            )
            mot_sub: TmotSubAg = field(
                metadata={
                    "name": "motSub",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                }
            )

        @dataclass(kw_only=True)
        class GMed:
            """
            :ivar id_medidor: Identificação do medidor Caso não tenha
                medidor informar "000000"  quando necessite informar
                datas de leitura para geranção do documento auxilair
            :ivar d_med_ant: Data da leitura anterior Formato AAAA-MM-DD
                Em caso da 1a leitura do hidrometro, informar a data de
                instalação do hidrômetro
            :ivar d_med_atu: Data da leitura atual Formato AAAA-MM-DD
            :ivar n_med: Número de referência para informar nos produtos
                a relação com a medição
            """

            id_medidor: str = field(
                metadata={
                    "name": "idMedidor",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "min_length": 2,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"([!-ÿ]{0}|[!-ÿ]{2,20})?",
                }
            )
            d_med_ant: str = field(
                metadata={
                    "name": "dMedAnt",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"((((20|19|18)(([02468][048])|([13579][26]))-02-29))|((20|19|18)[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                }
            )
            d_med_atu: str = field(
                metadata={
                    "name": "dMedAtu",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"((((20|19|18)(([02468][048])|([13579][26]))-02-29))|((20|19|18)[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                }
            )
            n_med: str = field(
                metadata={
                    "name": "nMed",
                    "type": "Attribute",
                    "min_length": 2,
                    "max_length": 2,
                    "white_space": "preserve",
                    "pattern": r"(0[1-9]|1[0-9]|99)",
                }
            )

        @dataclass(kw_only=True)
        class GFatConjunto:
            """
            :ivar ch_nfag_fat: Chave de acesso da NFAg faturada em
                conjunto Obrigatorio para tpFat 3 Vedado para tpFat 1 e
                2
            """

            ch_nfag_fat: str = field(
                metadata={
                    "name": "chNFAgFat",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "max_length": 44,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{6}[A-Z0-9]{12}[0-9]{26}",
                }
            )

        @dataclass(kw_only=True)
        class Det:
            """
            :ivar g_tarif: Grupo de Tarifas por Período
            :ivar prod: Dados do Produto ou Serviço
            :ivar imposto: Tributos incidentes no Produto ou Serviço
            :ivar g_proc_ref: Grupo Processo referenciado Este grupo
                somente deverá ser preenchido quando houver processo
                judicial ou administrativo que altere valores.
            :ivar inf_ad_prod: Informações adicionais do produto (norma
                referenciada, informações complementares, etc)
            :ivar n_item: Número do item da NFAg
            :ivar ch_nfag_ant: Chave de Acesso da NFag anterior Informar
                chave de acesso de referencia anterior TAG OPCIONAL,
                DEVE SER INFORMADA APENAS NOS CASOS PREVISTOS DE NOTA
                ANTERIOR REFERENCIADA
            :ivar n_item_ant: Número do item da NFAg anterior Informar
                nro do item da chave de acesso de referencia anterior
                TAG OPCIONAL, DEVE SER INFORMADA APENAS NOS CASOS
                PREVISTOS DE NOTA ANTERIOR REFERENCIADA
            """

            g_tarif: list[Tnfag.InfNfag.Det.GTarif] = field(
                default_factory=list,
                metadata={
                    "name": "gTarif",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "max_occurs": 6,
                },
            )
            prod: Tnfag.InfNfag.Det.Prod = field(
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                }
            )
            imposto: Tnfag.InfNfag.Det.Imposto = field(
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                }
            )
            g_proc_ref: None | Tnfag.InfNfag.Det.GProcRef = field(
                default=None,
                metadata={
                    "name": "gProcRef",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                },
            )
            inf_ad_prod: None | str = field(
                default=None,
                metadata={
                    "name": "infAdProd",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "min_length": 1,
                    "max_length": 500,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                },
            )
            n_item: str = field(
                metadata={
                    "name": "nItem",
                    "type": "Attribute",
                    "white_space": "preserve",
                    "pattern": r"[1-9]{1}[0-9]{0,1}|[1-8]{1}[0-9]{2}|[9]{1}[0-8]{1}[0-9]{1}|[9]{1}[9]{1}[0]{1}",
                }
            )
            ch_nfag_ant: None | str = field(
                default=None,
                metadata={
                    "name": "chNFAgAnt",
                    "type": "Attribute",
                    "max_length": 44,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{6}[A-Z0-9]{12}[0-9]{26}",
                },
            )
            n_item_ant: None | str = field(
                default=None,
                metadata={
                    "name": "nItemAnt",
                    "type": "Attribute",
                    "white_space": "preserve",
                    "pattern": r"[1-9]{1}[0-9]{0,3}",
                },
            )

            @dataclass(kw_only=True)
            class GTarif:
                """
                :ivar d_ini_tarif: Data de início da aplicação da tarifa
                    Data de início da aplicação da tarifa no período
                    considerado para o faturamento ( Formato AAAA-MM-DD)
                :ivar d_fim_tarif: Data de fim da aplicação da tarifa
                    Data de fim da aplicação da tarifa no período
                    considerado para o faturamento (Formato AAAA-MM-DD)
                :ivar n_ato: Número do Ato
                :ivar ano_ato: Ano do Ato (AAAA)
                :ivar tp_faixa_cons: Faixa Prevista de Consumo 1 -
                    minimo 2 - médio 3 - máximo
                """

                d_ini_tarif: str = field(
                    metadata={
                        "name": "dIniTarif",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                        "white_space": "preserve",
                        "pattern": r"((((20|19|18)(([02468][048])|([13579][26]))-02-29))|((20|19|18)[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                    }
                )
                d_fim_tarif: None | str = field(
                    default=None,
                    metadata={
                        "name": "dFimTarif",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                        "white_space": "preserve",
                        "pattern": r"((((20|19|18)(([02468][048])|([13579][26]))-02-29))|((20|19|18)[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                    },
                )
                n_ato: str = field(
                    metadata={
                        "name": "nAto",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                        "min_length": 4,
                        "max_length": 4,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                ano_ato: str = field(
                    metadata={
                        "name": "anoAto",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                        "min_length": 4,
                        "max_length": 4,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{4}",
                    }
                )
                tp_faixa_cons: None | Tfaixa = field(
                    default=None,
                    metadata={
                        "name": "tpFaixaCons",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                    },
                )

            @dataclass(kw_only=True)
            class Prod:
                """
                :ivar ind_origem_qtd: Indicador da origem da quantidade
                    faturada 1 - Media; 2 - Medido; 3 - Contratada; 4 -
                    Calculada ou estimado; 5 - Residual Calculado; 6 -
                    Sem quantidade 7 - Por Faixa;
                :ivar g_medicao: Grupo para referenciar qual medição e
                    medida estão relacionadas ao item
                :ivar c_prod: Código do produto ou serviço.
                :ivar x_prod: Descrição do produto ou serviço
                :ivar c_class: Código de classificação Tabela de
                    Classificação de Item da NFAg (validar por RV)
                :ivar tp_categoria: Categoria da ligação 01 - Comercial
                    02 - Consumo Próprio 04 - Industrial 06 -
                    Residencial 07 - Rural 08 - Serviço Público 09 -
                    Social 10 - Mista 11 - Resid.Comercial 12 - Resid
                    Industrial 99 - Outras
                :ivar x_categoria: Detalhamento da Categoria
                :ivar q_economias: Quantidade de economias Informar a
                    série do documento fiscal (informar zero para série
                    única).
                :ivar u_med: Unidade Básica de Medida 1 - m3; 2 -
                    Litros; 5 - Unidade 6 - ton
                :ivar q_faturada: Quantidade Faturada Informar a
                    quantidade de comercialização do produto .
                :ivar v_item: Valor unitário do item O valor unitário do
                    item no caso de energia elétrica corresponde ao
                    valor da tarifa e dos tributos que devam compor a
                    base de cálculo. O item pode estar acrescido do
                    adicional da bandeira tarifária ou o adicional de
                    bandeira poderá ser lançado como um item específico.
                    Este campo também corresponde ao preço médio efetivo
                    relativo ao consumo ativo do período, quando
                    aplicáveis os termos do inciso I da clausula
                    primeira do Convênio ICMS 77/11 (DEVEC).
                :ivar fator_poluicao: Fator de poluição Se informado
                    multipla ao valor do vItem Obrigatoriamente &gt; 1.
                :ivar v_prod: Valor total do item
                :ivar ind_devolucao: Indicador de devolução do valor do
                    item 1 – Devolução do valor do item
                """

                ind_origem_qtd: TorigemQtdAg = field(
                    metadata={
                        "name": "indOrigemQtd",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                    }
                )
                g_medicao: None | Tnfag.InfNfag.Det.Prod.GMedicao = field(
                    default=None,
                    metadata={
                        "name": "gMedicao",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                    },
                )
                c_prod: str = field(
                    metadata={
                        "name": "cProd",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                        "min_length": 1,
                        "max_length": 60,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                x_prod: str = field(
                    metadata={
                        "name": "xProd",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                        "min_length": 1,
                        "max_length": 120,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                c_class: str = field(
                    metadata={
                        "name": "cClass",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                        "min_length": 7,
                        "max_length": 7,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{7}",
                    }
                )
                tp_categoria: None | TcategAg = field(
                    default=None,
                    metadata={
                        "name": "tpCategoria",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                    },
                )
                x_categoria: None | str = field(
                    default=None,
                    metadata={
                        "name": "xCategoria",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                        "min_length": 1,
                        "max_length": 200,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    },
                )
                q_economias: None | str = field(
                    default=None,
                    metadata={
                        "name": "qEconomias",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                        "min_length": 1,
                        "max_length": 5,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    },
                )
                u_med: TumedItemAg = field(
                    metadata={
                        "name": "uMed",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                    }
                )
                q_faturada: str = field(
                    metadata={
                        "name": "qFaturada",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{1,11}(\.[0-9]{2,4})?",
                    }
                )
                v_item: str = field(
                    metadata={
                        "name": "vItem",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{1,13}(\.[0-9]{2,10})?",
                    }
                )
                fator_poluicao: None | str = field(
                    default=None,
                    metadata={
                        "name": "fatorPoluicao",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{1,11}(\.[0-9]{2,4})?",
                    },
                )
                v_prod: str = field(
                    metadata={
                        "name": "vProd",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{1,13}(\.[0-9]{2,10})?",
                    }
                )
                ind_devolucao: None | ProdIndDevolucao = field(
                    default=None,
                    metadata={
                        "name": "indDevolucao",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                        "white_space": "preserve",
                    },
                )

                @dataclass(kw_only=True)
                class GMedicao:
                    """
                    :ivar n_med: Referência para a medição ao qual se
                        refere o item
                    :ivar g_medida: Grupo de medida
                    :ivar tp_mot_nao_leitura: Tipo Motivo da não leitura
                        1 - Consumidor; 2 - Distribuidora; 3 -
                        Independente do Consumidor e distribuidora;
                    """

                    n_med: str = field(
                        metadata={
                            "name": "nMed",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfag",
                            "min_length": 2,
                            "max_length": 2,
                            "white_space": "preserve",
                            "pattern": r"(0[1-9]|1[0-9]|20)",
                        }
                    )
                    g_medida: None | TmedidaAg = field(
                        default=None,
                        metadata={
                            "name": "gMedida",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfag",
                        },
                    )
                    tp_mot_nao_leitura: None | TmotNaoLeitura = field(
                        default=None,
                        metadata={
                            "name": "tpMotNaoLeitura",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfag",
                        },
                    )

            @dataclass(kw_only=True)
            class Imposto:
                """
                :ivar ibscbs: Grupo de informações do IBS e CBS
                :ivar pis: Dados do PIS
                :ivar cofins: Dados do COFINS
                :ivar ret_trib: Grupo de informações de retenção de
                    tributos federais
                :ivar tfs: Taxa de Fiscalização de Serviço
                :ivar tfu: Taxa de Fiscalização de Uso
                """

                ibscbs: TtribNfag = field(
                    metadata={
                        "name": "IBSCBS",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                    }
                )
                pis: None | Tnfag.InfNfag.Det.Imposto.Pis = field(
                    default=None,
                    metadata={
                        "name": "PIS",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                    },
                )
                cofins: None | Tnfag.InfNfag.Det.Imposto.Cofins = field(
                    default=None,
                    metadata={
                        "name": "COFINS",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                    },
                )
                ret_trib: None | Tnfag.InfNfag.Det.Imposto.RetTrib = field(
                    default=None,
                    metadata={
                        "name": "retTrib",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                    },
                )
                tfs: None | Tnfag.InfNfag.Det.Imposto.Tfs = field(
                    default=None,
                    metadata={
                        "name": "TFS",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                    },
                )
                tfu: None | Tnfag.InfNfag.Det.Imposto.Tfu = field(
                    default=None,
                    metadata={
                        "name": "TFU",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                    },
                )

                @dataclass(kw_only=True)
                class Pis:
                    """
                    :ivar cst: classificação Tributária do PIS 01 –
                        Tributável com alíquota básica 02 – Tributável
                        com alíquota diferenciada 06 – Tributável com
                        alíquota erro 07 – Operação isenta de
                        contribuição 08 – Operação sem incidência da
                        contribuição 09 – Operação com suspensão da
                        contribuição 49 – Outras operações de saída
                    :ivar v_bc: Valor da BC do PIS
                    :ivar p_pis: Alíquota do PIS (em percentual)
                    :ivar v_pis: Valor do PIS
                    """

                    cst: PisCst = field(
                        metadata={
                            "name": "CST",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfag",
                            "white_space": "preserve",
                        }
                    )
                    v_bc: str = field(
                        metadata={
                            "name": "vBC",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfag",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    p_pis: str = field(
                        metadata={
                            "name": "pPIS",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfag",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                        }
                    )
                    v_pis: str = field(
                        metadata={
                            "name": "vPIS",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfag",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )

                @dataclass(kw_only=True)
                class Cofins:
                    """
                    :ivar cst: classificação Tributária do COFINS 01 –
                        Tributável com alíquota básica 02 – Tributável
                        com alíquota diferenciada 06 – Tributável com
                        alíquota erro 07 – Operação isenta de
                        contribuição 08 – Operação sem incidência da
                        contribuição 09 – Operação com suspensão da
                        contribuição 49 – Outras operações de saída
                    :ivar v_bc: Valor da BC do COFINS
                    :ivar p_cofins: Alíquota do COFINS (em percentual)
                    :ivar v_cofins: Valor do COFINS
                    """

                    cst: CofinsCst = field(
                        metadata={
                            "name": "CST",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfag",
                            "white_space": "preserve",
                        }
                    )
                    v_bc: str = field(
                        metadata={
                            "name": "vBC",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfag",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    p_cofins: str = field(
                        metadata={
                            "name": "pCOFINS",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfag",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                        }
                    )
                    v_cofins: str = field(
                        metadata={
                            "name": "vCOFINS",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfag",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )

                @dataclass(kw_only=True)
                class RetTrib:
                    """
                    :ivar v_ret_pis: Valor do PIS retido
                    :ivar v_ret_cofins: Valor do COFNS retido
                    :ivar v_ret_csll: Valor da CSLL retida
                    :ivar v_irrf: Valor do IRRF retido
                    """

                    v_ret_pis: str = field(
                        metadata={
                            "name": "vRetPIS",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfag",
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1,13}(\.[0-9]{2,8})?",
                        }
                    )
                    v_ret_cofins: str = field(
                        metadata={
                            "name": "vRetCofins",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfag",
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1,13}(\.[0-9]{2,8})?",
                        }
                    )
                    v_ret_csll: str = field(
                        metadata={
                            "name": "vRetCSLL",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfag",
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1,13}(\.[0-9]{2,8})?",
                        }
                    )
                    v_irrf: str = field(
                        metadata={
                            "name": "vIRRF",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfag",
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1,13}(\.[0-9]{2,8})?",
                        }
                    )

                @dataclass(kw_only=True)
                class Tfs:
                    """
                    :ivar v_bctfs: Valor BC TFS
                    :ivar p_tfs: Alíquota do TFS
                    :ivar v_tfs: Valor TFS
                    """

                    v_bctfs: str = field(
                        metadata={
                            "name": "vBCTFS",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfag",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    p_tfs: str = field(
                        metadata={
                            "name": "pTFS",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfag",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                        }
                    )
                    v_tfs: str = field(
                        metadata={
                            "name": "vTFS",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfag",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )

                @dataclass(kw_only=True)
                class Tfu:
                    """
                    :ivar v_bctfu: Valor BC TFU
                    :ivar p_tfu: Alíquota do TFU
                    :ivar v_tfu: Valor TFU
                    """

                    v_bctfu: str = field(
                        metadata={
                            "name": "vBCTFU",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfag",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    p_tfu: str = field(
                        metadata={
                            "name": "pTFU",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfag",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                        }
                    )
                    v_tfu: str = field(
                        metadata={
                            "name": "vTFU",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfag",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )

            @dataclass(kw_only=True)
            class GProcRef:
                """
                :ivar v_item: Valor unitário do item Informar o valor
                    sem a influência da decisão judicial/administrativa.
                :ivar q_faturada: Quantidade Faturada Informar a
                    quantidade de comercialização do produto .
                :ivar v_prod: Valor total do item
                :ivar ind_devolucao: Indicador de devolução do valor do
                    item 1 – Devolução do valor do item
                :ivar g_proc: Grupo identificador do Processo
                """

                v_item: str = field(
                    metadata={
                        "name": "vItem",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{1,13}(\.[0-9]{2,10})?",
                    }
                )
                q_faturada: str = field(
                    metadata={
                        "name": "qFaturada",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{1,11}(\.[0-9]{2,4})?",
                    }
                )
                v_prod: str = field(
                    metadata={
                        "name": "vProd",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{1,13}(\.[0-9]{2,10})?",
                    }
                )
                ind_devolucao: None | GProcRefIndDevolucao = field(
                    default=None,
                    metadata={
                        "name": "indDevolucao",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                        "white_space": "preserve",
                    },
                )
                g_proc: list[Tnfag.InfNfag.Det.GProcRef.GProc] = field(
                    default_factory=list,
                    metadata={
                        "name": "gProc",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                        "min_occurs": 1,
                        "max_occurs": 10,
                    },
                )

                @dataclass(kw_only=True)
                class GProc:
                    """
                    :ivar tp_proc: Tipo de Processo 0 - Processo Adm
                        Estadual; 1 - Justiça Federal; 2 - Justiça
                        Estadual; 3 - Processo Adm Municipal; 4 -
                        Processo Adm Federal; 5 - Procon
                    :ivar n_processo: Número do Processo
                    """

                    tp_proc: TprocessoAg = field(
                        metadata={
                            "name": "tpProc",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfag",
                        }
                    )
                    n_processo: str = field(
                        metadata={
                            "name": "nProcesso",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfag",
                            "min_length": 1,
                            "max_length": 60,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )

        @dataclass(kw_only=True)
        class Total:
            """
            :ivar v_prod: Valor Total dos produtos e serviços
            :ivar v_ret_trib_tot: Total da retenção de tributos federais
            :ivar v_cofins: Valor do COFINS
            :ivar v_pis: Valor do PIS
            :ivar v_tfs: Valor TFS
            :ivar v_tfu: Valor TFU
            :ivar v_nf: Valor Total da NF-e
            :ivar ibscbstot: Totais de IBS e CBS
            :ivar v_tot_dfe: Valor total do documento fiscal (vNF +
                total do IBS + total da CBS)
            """

            v_prod: str = field(
                metadata={
                    "name": "vProd",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            v_ret_trib_tot: Tnfag.InfNfag.Total.VRetTribTot = field(
                metadata={
                    "name": "vRetTribTot",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                }
            )
            v_cofins: str = field(
                metadata={
                    "name": "vCOFINS",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            v_pis: str = field(
                metadata={
                    "name": "vPIS",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            v_tfs: str = field(
                metadata={
                    "name": "vTFS",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            v_tfu: str = field(
                metadata={
                    "name": "vTFU",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            v_nf: str = field(
                metadata={
                    "name": "vNF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            ibscbstot: Tibscbstot = field(
                metadata={
                    "name": "IBSCBSTot",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                }
            )
            v_tot_dfe: str = field(
                metadata={
                    "name": "vTotDFe",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )

            @dataclass(kw_only=True)
            class VRetTribTot:
                """
                :ivar v_ret_pis: Valor do PIS retido
                :ivar v_ret_cofins: Valor do COFNS retido
                :ivar v_ret_csll: Valor da CSLL retida
                :ivar v_irrf: Valor do IRRF retido
                """

                v_ret_pis: str = field(
                    metadata={
                        "name": "vRetPIS",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_ret_cofins: str = field(
                    metadata={
                        "name": "vRetCofins",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_ret_csll: str = field(
                    metadata={
                        "name": "vRetCSLL",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_irrf: str = field(
                    metadata={
                        "name": "vIRRF",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )

        @dataclass(kw_only=True)
        class GFat:
            """
            :ivar compet_fat: Ano e mês referência do faturamento
                (AAAAMM)
            :ivar d_venc_fat: Data de vencimento da fatura Formato AAAA-
                MM-DD
            :ivar d_apres_fat: Data de apresentação da fatura Formato
                AAAA-MM-DD Não obrigatória, conforme item 2.3.2 da Seção
                11.1 do Módulo 11 do PRODIST.
            :ivar d_prox_leitura: Data prevista próxima leitura Formato
                AAAA-MM-DD
            :ivar n_fat: Número da Fatura
            :ivar cod_barras: Linha digitável do código de barras
            :ivar cod_deb_auto: Código de autorização débito em conta
            :ivar cod_banco: Número do banco para débito em conta
            :ivar cod_agencia: Número da agência bancária para débito em
                conta
            :ivar ender_corresp: Endereço de entrega da fatura. Informar
                se diferente do endereço do destinatário
            :ivar g_pix: Grupo de informações do PIX
            """

            compet_fat: str = field(
                metadata={
                    "name": "CompetFat",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "min_length": 6,
                    "max_length": 6,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{1,6}",
                }
            )
            d_venc_fat: str = field(
                metadata={
                    "name": "dVencFat",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"((((20|19|18)(([02468][048])|([13579][26]))-02-29))|((20|19|18)[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                }
            )
            d_apres_fat: None | str = field(
                default=None,
                metadata={
                    "name": "dApresFat",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"((((20|19|18)(([02468][048])|([13579][26]))-02-29))|((20|19|18)[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                },
            )
            d_prox_leitura: str = field(
                metadata={
                    "name": "dProxLeitura",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"((((20|19|18)(([02468][048])|([13579][26]))-02-29))|((20|19|18)[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                }
            )
            n_fat: None | str = field(
                default=None,
                metadata={
                    "name": "nFat",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{1,20}",
                },
            )
            cod_barras: str = field(
                metadata={
                    "name": "codBarras",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "min_length": 1,
                    "max_length": 48,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{1,48}",
                }
            )
            cod_deb_auto: None | str = field(
                default=None,
                metadata={
                    "name": "codDebAuto",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{1,20}",
                },
            )
            cod_banco: None | str = field(
                default=None,
                metadata={
                    "name": "codBanco",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "min_length": 3,
                    "max_length": 5,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                },
            )
            cod_agencia: None | str = field(
                default=None,
                metadata={
                    "name": "codAgencia",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "min_length": 1,
                    "max_length": 10,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                },
            )
            ender_corresp: None | TendeEmi = field(
                default=None,
                metadata={
                    "name": "enderCorresp",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                },
            )
            g_pix: None | Tnfag.InfNfag.GFat.GPix = field(
                default=None,
                metadata={
                    "name": "gPIX",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                },
            )

            @dataclass(kw_only=True)
            class GPix:
                """
                :ivar url_qrcode_pix: URL do QRCode do PIX que será
                    apresentado na fatura
                """

                url_qrcode_pix: str = field(
                    metadata={
                        "name": "urlQRCodePIX",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                        "min_length": 2,
                        "max_length": 2000,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )

        @dataclass(kw_only=True)
        class GAgencia:
            """
            :ivar econ: Demonstrativo de economia de agua
            :ivar econ_acumulada: Demonstrativo de economia de agua
                acumulada no período
            :ivar s_prestador: Selo de segurança do prestador
            :ivar d_emiss_selo: Data de emissão do Selo de segurança do
                prestador
            :ivar s_regulador: Selo de segurança do Regulador
            :ivar n_agencia_atend: Agencia responsável pelo atendimento
            :ivar ender_agencia_atend: Endereço da Agencia responsável
                pelo atendimento
            :ivar g_hist_cons: Histórico de Consumo
            """

            econ: None | str = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "min_length": 2,
                    "max_length": 10,
                },
            )
            econ_acumulada: None | str = field(
                default=None,
                metadata={
                    "name": "econAcumulada",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "min_length": 2,
                    "max_length": 10,
                },
            )
            s_prestador: None | str = field(
                default=None,
                metadata={
                    "name": "sPrestador",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "min_length": 2,
                    "max_length": 10,
                },
            )
            d_emiss_selo: None | str = field(
                default=None,
                metadata={
                    "name": "dEmissSelo",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"((((20|19|18)(([02468][048])|([13579][26]))-02-29))|((20|19|18)[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                },
            )
            s_regulador: None | str = field(
                default=None,
                metadata={
                    "name": "sRegulador",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "min_length": 2,
                    "max_length": 10,
                },
            )
            n_agencia_atend: str = field(
                metadata={
                    "name": "nAgenciaAtend",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "min_length": 2,
                    "max_length": 20,
                }
            )
            ender_agencia_atend: str = field(
                metadata={
                    "name": "enderAgenciaAtend",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "min_length": 2,
                    "max_length": 200,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            g_hist_cons: list[Tnfag.InfNfag.GAgencia.GHistCons] = field(
                default_factory=list,
                metadata={
                    "name": "gHistCons",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "min_occurs": 1,
                    "max_occurs": 5,
                },
            )

            @dataclass(kw_only=True)
            class GHistCons:
                """
                :ivar x_historico: Nome do histórico para
                    exibição/apresentação Exemplo: Consumo Meses
                    Anteriores
                :ivar g_cons: Consumo
                :ivar med_mensal: Média Mensal de consumo
                """

                x_historico: str = field(
                    metadata={
                        "name": "xHistorico",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                        "min_length": 2,
                        "max_length": 60,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                g_cons: list[Tnfag.InfNfag.GAgencia.GHistCons.GCons] = field(
                    default_factory=list,
                    metadata={
                        "name": "gCons",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                        "min_occurs": 1,
                        "max_occurs": 13,
                    },
                )
                med_mensal: str = field(
                    metadata={
                        "name": "medMensal",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{1,13}(\.[0-9]{2,4})?",
                    }
                )

                @dataclass(kw_only=True)
                class GCons:
                    """
                    :ivar compet_fat: Ano e mês referência do
                        faturamento (AAAAMM)
                    :ivar u_med: Unidade Básica de Medida 1 - m3 e 2 -
                        litro
                    :ivar qtd_dias: Quantidade de dias de medição
                    :ivar med_diaria: Média Diária de consumo
                    :ivar consumo: Consumo no mês
                    :ivar vol_fat: Volume Faturado
                    """

                    compet_fat: str = field(
                        metadata={
                            "name": "CompetFat",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfag",
                            "min_length": 6,
                            "max_length": 6,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1,6}",
                        }
                    )
                    u_med: TumedAg = field(
                        metadata={
                            "name": "uMed",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfag",
                        }
                    )
                    qtd_dias: str = field(
                        metadata={
                            "name": "qtdDias",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfag",
                            "white_space": "preserve",
                            "pattern": r"[0-9]{5}",
                        }
                    )
                    med_diaria: None | str = field(
                        default=None,
                        metadata={
                            "name": "medDiaria",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfag",
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1,13}(\.[0-9]{2,4})?",
                        },
                    )
                    consumo: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfag",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        },
                    )
                    vol_fat: str = field(
                        metadata={
                            "name": "volFat",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfag",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )

        @dataclass(kw_only=True)
        class GQualiAgua:
            """
            :ivar compet_analise: Ano e mês referência da analise
                (AAAAMM)
            :ivar g_analise: Grupo de informações da Análise
            :ivar conclusao: Conclusão da Análise
            :ivar c_processo: Legislação aplicada
            :ivar sistema_abast: Nome do Sistema de abastecimento
            """

            compet_analise: str = field(
                metadata={
                    "name": "CompetAnalise",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "min_length": 6,
                    "max_length": 6,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{1,6}",
                }
            )
            g_analise: list[Tnfag.InfNfag.GQualiAgua.GAnalise] = field(
                default_factory=list,
                metadata={
                    "name": "gAnalise",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "min_occurs": 1,
                    "max_occurs": 10,
                },
            )
            conclusao: None | str = field(
                default=None,
                metadata={
                    "name": "Conclusao",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "min_length": 2,
                    "max_length": 50,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                },
            )
            c_processo: None | str = field(
                default=None,
                metadata={
                    "name": "cProcesso",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "min_length": 2,
                    "max_length": 50,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                },
            )
            sistema_abast: None | str = field(
                default=None,
                metadata={
                    "name": "SistemaAbast",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "min_length": 2,
                    "max_length": 50,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                },
            )

            @dataclass(kw_only=True)
            class GAnalise:
                """
                :ivar x_item_analisado: Nome do item analisado
                :ivar n_amostra_minima: Número de amostra minima
                :ivar n_amostra_analisada: Número de amostra analisada
                :ivar n_amostra_fpadrao: Número de amostra fora do
                    padrão
                :ivar n_amostra_dpadrao: Número de amostra dentro do
                    padrão
                :ivar n_media_mensal: Media mensal dos valores da
                    analise
                :ivar x_valor_referencia: Valor de referência
                """

                x_item_analisado: str = field(
                    metadata={
                        "name": "xItemAnalisado",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                        "min_length": 2,
                        "max_length": 60,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                n_amostra_minima: None | str = field(
                    default=None,
                    metadata={
                        "name": "nAmostraMinima",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                        "max_length": 4,
                        "pattern": r"[0-9]{4}",
                    },
                )
                n_amostra_analisada: None | str = field(
                    default=None,
                    metadata={
                        "name": "nAmostraAnalisada",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                        "max_length": 4,
                        "pattern": r"[0-9]{4}",
                    },
                )
                n_amostra_fpadrao: None | str = field(
                    default=None,
                    metadata={
                        "name": "nAmostraFPadrao",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                        "max_length": 4,
                        "pattern": r"[0-9]{4}",
                    },
                )
                n_amostra_dpadrao: None | str = field(
                    default=None,
                    metadata={
                        "name": "nAmostraDPadrao",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                        "max_length": 4,
                        "pattern": r"[0-9]{4}",
                    },
                )
                n_media_mensal: None | str = field(
                    default=None,
                    metadata={
                        "name": "nMediaMensal",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                        "min_length": 2,
                        "max_length": 60,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    },
                )
                x_valor_referencia: None | str = field(
                    default=None,
                    metadata={
                        "name": "xValorReferencia",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfag",
                        "min_length": 2,
                        "max_length": 60,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    },
                )

        @dataclass(kw_only=True)
        class AutXml:
            """
            :ivar cnpj: CNPJ do autorizado Informar zeros não
                significativos
            :ivar cpf: CPF do autorizado Informar zeros não
                significativos
            """

            cnpj: None | str = field(
                default=None,
                metadata={
                    "name": "CNPJ",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"[A-Z0-9]{12}[0-9]{2}",
                },
            )
            cpf: None | str = field(
                default=None,
                metadata={
                    "name": "CPF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                },
            )

        @dataclass(kw_only=True)
        class InfAdic:
            """
            :ivar inf_ad_fisco: Informações adicionais de interesse do
                Fisco Norma referenciada, informações complementares,
                etc
            :ivar inf_cpl: Informações complementares de interesse do
                Contribuinte
            """

            inf_ad_fisco: None | str = field(
                default=None,
                metadata={
                    "name": "infAdFisco",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "min_length": 1,
                    "max_length": 2000,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                },
            )
            inf_cpl: list[str] = field(
                default_factory=list,
                metadata={
                    "name": "infCpl",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "max_occurs": 5,
                    "min_length": 1,
                    "max_length": 3000,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                },
            )

        @dataclass(kw_only=True)
        class InfPaa:
            """
            :ivar cnpjpaa: CNPJ do Provedor de Assinatura e Autorização
                CNPJ da empresa que emitirá a nota do tipo faturamento 1
                em nome de outra empresa
            """

            cnpjpaa: str = field(
                metadata={
                    "name": "CNPJPAA",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"[A-Z0-9]{12}[0-9]{2}",
                }
            )

    @dataclass(kw_only=True)
    class InfNfagSupl:
        """
        :ivar qr_cod_nfag: Texto com o QR-Code para consulta da NFAg
        """

        qr_cod_nfag: str = field(
            metadata={
                "name": "qrCodNFAg",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "min_length": 50,
                "max_length": 1000,
                "white_space": "preserve",
                "pattern": r"((HTTPS?|https?)://.*\?chNFAg=[0-9]{6}[A-Z0-9]{12}[0-9]{26}&tpAmb=[1-2](&sign=[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1})?)",
            }
        )


@dataclass(kw_only=True)
class TretNfag:
    """
    Tipo Retorno do Pedido de Autorização de NFAg.

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
        Homologação
    :ivar c_uf: Identificação da UF
    :ivar ver_aplic: Versão do Aplicativo que processou a NFAg
    :ivar c_stat: código do status do retorno da consulta.
    :ivar x_motivo: Descrição literal do status do do retorno da
        consulta.
    :ivar prot_nfag: Reposta ao processamento da NFAg
    :ivar versao:
    """

    class Meta:
        name = "TRetNFAg"

    tp_amb: Tamb = field(
        metadata={
            "name": "tpAmb",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        }
    )
    c_uf: TcodUfIbge = field(
        metadata={
            "name": "cUF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        }
    )
    ver_aplic: str = field(
        metadata={
            "name": "verAplic",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "min_length": 1,
            "max_length": 20,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    c_stat: str = field(
        metadata={
            "name": "cStat",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"[0-9]{3,4}",
        }
    )
    x_motivo: str = field(
        metadata={
            "name": "xMotivo",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    prot_nfag: None | TprotNfag = field(
        default=None,
        metadata={
            "name": "protNFAg",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    versao: str = field(
        metadata={
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"1\.00",
        }
    )
