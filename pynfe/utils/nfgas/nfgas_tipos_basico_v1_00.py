from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from pynfe_nasajon.pynfe.utils.nfgas.dfe_tipos_basicos_v1_00 import (
    TcompraGovReduzido,
    Tibscbstot,
    TtribNfgas,
)
from pynfe_nasajon.pynfe.utils.nfgas.tipos_geral_nfgas_v1_00 import (
    Tamb,
    TcodUfIbge,
    TmodNf,
    Tuf,
    TufSemEx,
)
from pynfe_nasajon.pynfe.utils.nfgas.xmldsig_core_schema_v1_01 import Signature

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfgas"


class CofinsCst(Enum):
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_49 = "49"


class Icms00Cst(Enum):
    VALUE_00 = "00"


class Icms10Cst(Enum):
    VALUE_10 = "10"


class Icms20Cst(Enum):
    VALUE_20 = "20"


class Icms40Cst(Enum):
    VALUE_40 = "40"
    VALUE_41 = "41"


class Icms51Cst(Enum):
    VALUE_51 = "51"


class Icms60Cst(Enum):
    VALUE_60 = "60"


class Icms70Cst(Enum):
    VALUE_70 = "70"


class Icms70IndDeduzDeson(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"


class Icms70ModBc(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class Icms70ModBcst(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"


class Icms70MotDesIcms(Enum):
    VALUE_3 = "3"
    VALUE_9 = "9"
    VALUE_12 = "12"


class Icms70MotDesIcmsst(Enum):
    VALUE_3 = "3"
    VALUE_9 = "9"
    VALUE_12 = "12"


class Icms90Cst(Enum):
    VALUE_90 = "90"


class PisCst(Enum):
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_49 = "49"


class Tclasse(Enum):
    """
    Tipo de Classe.
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
    VALUE_10 = "10"
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
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
            "white_space": "preserve",
            "pattern": r"[A-Z0-9]{12}[0-9]{2}",
        },
    )
    cpf: None | str = field(
        default=None,
        metadata={
            "name": "CPF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
            "white_space": "preserve",
            "pattern": r"[0-9]{11}",
        },
    )
    x_contato: str = field(
        metadata={
            "name": "xContato",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
            "min_length": 2,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    email: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[^@]+@[^\.]+\..+",
        }
    )
    fone: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
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


class TfatNf(Enum):
    """
    Tipo de Faturamento da NFGas.
    """

    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class TfinNf(Enum):
    """
    Finalidade da NFGas.
    """

    VALUE_0 = "0"
    VALUE_3 = "3"


class TgrContrat(Enum):
    """
    Tipo Grandeza Contratada.
    """

    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"


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


class TmotSub(Enum):
    """
    Tipo Motivo Substituição.
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"


class TorigemQtd(Enum):
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


class Tprocesso(Enum):
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
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
            "white_space": "preserve",
            "pattern": r"[A-Z0-9]{12}[0-9]{2}",
        }
    )
    x_contato: str = field(
        metadata={
            "name": "xContato",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
            "min_length": 2,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    email: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[^@]+@[^\.]+\..+",
        }
    )
    fone: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
            "white_space": "preserve",
            "pattern": r"[0-9]{7,12}",
        }
    )
    id_csrt: None | str = field(
        default=None,
        metadata={
            "name": "idCSRT",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
            "pattern": r"[0-9]{3}",
        },
    )
    hash_csrt: None | bytes = field(
        default=None,
        metadata={
            "name": "hashCSRT",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
            "length": 20,
            "format": "base64",
        },
    )


class Tumed(Enum):
    """
    Tipo da unidade básica de medida.
    """

    VALUE_1 = "1"


class TumedItem(Enum):
    """
    Tipo da unidade básica de medida.
    """

    VALUE_1 = "1"
    VALUE_2 = "2"


class TtpEmis(Enum):
    """
    Tipo de emissão da NFGas.
    """

    VALUE_1 = "1"
    VALUE_2 = "2"


class GMedTpEqp(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"


class GMedTpMedidor(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"


class GProcRefIndDevolucao(Enum):
    VALUE_1 = "1"


class ImpostoIndSemCst(Enum):
    VALUE_1 = "1"


class ImpostoOrig(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"
    VALUE_7 = "7"
    VALUE_8 = "8"


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
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
            "min_length": 2,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    nro: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    x_mun: str = field(
        metadata={
            "name": "xMun",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )
    uf: TufSemEx = field(
        metadata={
            "name": "UF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
        }
    )
    fone: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
            "white_space": "preserve",
            "pattern": r"[0-9]{7,12}",
        },
    )
    email: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    nro: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    x_mun: str = field(
        metadata={
            "name": "xMun",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        },
    )
    uf: Tuf = field(
        metadata={
            "name": "UF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
        }
    )
    c_pais: None | str = field(
        default=None,
        metadata={
            "name": "cPais",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
            "white_space": "preserve",
            "pattern": r"[0-9]{1,4}",
        },
    )
    x_pais: None | str = field(
        default=None,
        metadata={
            "name": "xPais",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
            "white_space": "preserve",
            "pattern": r"[0-9]{7,12}",
        },
    )
    email: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[^@]+@[^\.]+\..+",
        },
    )


@dataclass(kw_only=True)
class Tmedida:
    """
    Tipo de dados de medida.

    :ivar u_med: Unidade Básica de Medida 1 –m3
    :ivar v_med: Valor da medição (vMedAtu – vMedAnt)
    """

    class Meta:
        name = "TMedida"

    u_med: Tumed = field(
        metadata={
            "name": "uMed",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
        }
    )
    v_med: str = field(
        metadata={
            "name": "vMed",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
            "white_space": "preserve",
            "pattern": r"[0-9]{1,13}(\.[0-9]{2,4})?",
        }
    )


@dataclass(kw_only=True)
class TprotNfgas:
    """
    Tipo Protocolo de status resultado do processamento da NFGas.

    :ivar inf_prot: Dados do protocolo de status
    :ivar inf_fisco: Mensagem do Fisco
    :ivar signature:
    :ivar versao:
    """

    class Meta:
        name = "TProtNFGas"

    inf_prot: TprotNfgas.InfProt = field(
        metadata={
            "name": "infProt",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
        }
    )
    inf_fisco: None | TprotNfgas.InfFisco = field(
        default=None,
        metadata={
            "name": "infFisco",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
        :ivar ver_aplic: Versão do Aplicativo que processou a NFGas
        :ivar ch_nfgas: Chave de acesso da NFGas
        :ivar dh_recbto: Data e hora de processamento, no formato AAAA-
            MM-DDTHH:MM:SS TZD.
        :ivar n_prot: Número do Protocolo de Status da NFGas.
        :ivar dig_val: Digest Value da NFGas processado. Utilizado para
            conferir a integridade da NFGas original.
        :ivar c_stat: Código do status da NFGas
        :ivar x_motivo: Descrição literal do status da NFGas
        :ivar id:
        """

        tp_amb: Tamb = field(
            metadata={
                "name": "tpAmb",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfgas",
            }
        )
        ver_aplic: str = field(
            metadata={
                "name": "verAplic",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        ch_nfgas: str = field(
            metadata={
                "name": "chNFGas",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                "max_length": 44,
                "white_space": "preserve",
                "pattern": r"[0-9]{6}[A-Z0-9]{12}[0-9]{26}",
            }
        )
        dh_recbto: str = field(
            metadata={
                "name": "dhRecbto",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                "white_space": "preserve",
                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
            }
        )
        n_prot: None | str = field(
            default=None,
            metadata={
                "name": "nProt",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                "white_space": "preserve",
                "pattern": r"[0-9]{16}",
            },
        )
        dig_val: None | bytes = field(
            default=None,
            metadata={
                "name": "digVal",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                "format": "base64",
            },
        )
        c_stat: str = field(
            metadata={
                "name": "cStat",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                "white_space": "preserve",
                "pattern": r"[0-9]{3,4}",
            }
        )
        x_motivo: str = field(
            metadata={
                "name": "xMotivo",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                "white_space": "preserve",
                "pattern": r"[0-9]{3,4}",
            }
        )
        x_msg: str = field(
            metadata={
                "name": "xMsg",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                "min_length": 1,
                "max_length": 255,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )


@dataclass(kw_only=True)
class Tnfgas:
    """
    Tipo Nota Fiscal de Gas.

    :ivar inf_nfgas: Informações da NFGas
    :ivar inf_nfgas_supl: Informações suplementares da NFGas
    :ivar signature:
    """

    class Meta:
        name = "TNFGas"

    inf_nfgas: Tnfgas.InfNfgas = field(
        metadata={
            "name": "infNFGas",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
        }
    )
    inf_nfgas_supl: Tnfgas.InfNfgasSupl = field(
        metadata={
            "name": "infNFGasSupl",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
    class InfNfgas:
        """
        :ivar ide: Identificação da NFGas
        :ivar emit: Identificação do Emitente do documento fiscal
        :ivar dest: Identificação do destinatário
        :ivar instalacao: Dados da Instalação OPCIONAL para TpFat=3
        :ivar g_sub: Grupo de informações da substituição
        :ivar g_vol_contrat: Grupo de informações das volumes
            contratados
        :ivar g_med: Grupo de informações dos Equipamentos de Medição
        :ivar det: Detalhamento de Produtos e Serviços
        :ivar total: Dados dos totais da NFGas Para Tipo de Faturamento
            Agregador (tpFat=3) todos os totalizadores devem ser zero,
            exceto vNF e vTotDFe que devem ser a soma do vTotDFe das
            notas anteriores informadas no grupo gAgregadora
        :ivar g_fat: Grupo de informações de controle da Fatura
            Obrigatorio para tpFat 1 e 3 (normal e agregador) Vedado
            para tpFat 2 (agregado)
        :ivar g_agencia: Grupo de informações da Agência reguladora
            Obrigatorio para tpFat 1 e 2 (normal e agregada) Vedado para
            tpFat 3 (agregadora)
        :ivar aut_xml: Autorizados para download do XML do DF-e Informar
            CNPJ ou CPF. Preencher os zeros não significativos.
        :ivar inf_adic: Informações Adicionais
        :ivar g_resp_tec: Informações do Responsável Técnico pela
            emissão do DF-e
        :ivar versao: Versão do leiaute
        :ivar id: Identificador da tag a ser assinada Informar a chave
            de acesso da NFGas e precedida do literal "NFGas"
        """

        ide: Tnfgas.InfNfgas.Ide = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfgas",
            }
        )
        emit: Tnfgas.InfNfgas.Emit = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfgas",
            }
        )
        dest: Tnfgas.InfNfgas.Dest = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfgas",
            }
        )
        instalacao: None | Tnfgas.InfNfgas.Instalacao = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfgas",
            },
        )
        g_sub: None | Tnfgas.InfNfgas.GSub = field(
            default=None,
            metadata={
                "name": "gSub",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfgas",
            },
        )
        g_vol_contrat: list[Tnfgas.InfNfgas.GVolContrat] = field(
            default_factory=list,
            metadata={
                "name": "gVolContrat",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                "max_occurs": 20,
            },
        )
        g_med: list[Tnfgas.InfNfgas.GMed] = field(
            default_factory=list,
            metadata={
                "name": "gMed",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                "max_occurs": 99,
            },
        )
        det: list[Tnfgas.InfNfgas.Det] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                "min_occurs": 1,
                "max_occurs": 990,
            },
        )
        total: Tnfgas.InfNfgas.Total = field(
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfgas",
            }
        )
        g_fat: None | Tnfgas.InfNfgas.GFat = field(
            default=None,
            metadata={
                "name": "gFat",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfgas",
            },
        )
        g_agencia: None | Tnfgas.InfNfgas.GAgencia = field(
            default=None,
            metadata={
                "name": "gAgencia",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfgas",
            },
        )
        aut_xml: list[Tnfgas.InfNfgas.AutXml] = field(
            default_factory=list,
            metadata={
                "name": "autXML",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                "max_occurs": 10,
            },
        )
        inf_adic: None | Tnfgas.InfNfgas.InfAdic = field(
            default=None,
            metadata={
                "name": "infAdic",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfgas",
            },
        )
        g_resp_tec: None | TrespTec = field(
            default=None,
            metadata={
                "name": "gRespTec",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
                "pattern": r"NFGas[0-9]{6}[A-Z0-9]{12}[0-9]{26}",
            }
        )

        @dataclass(kw_only=True)
        class Ide:
            """
            :ivar c_uf: Código da UF do emitente da NFGas Código da UF
                do emitente do Documento Fiscal. Utilizar a Tabela do
                IBGE de código de unidades da federação.
            :ivar tp_amb: Tipo do Ambiente 1 - Produção; 2 - Homologação
            :ivar mod: Modelo da NFGas Utilizar o código 76 para
                identificação da NFGas
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
                Autorizador de recepção da NFGas Se o autorizador da
                NFGas possuir apenas um site deverá ser informado com
                Zero (0), em caso de Autorizador trabalhar com múltiplos
                sites indicar o número do site para qual foi endereçada
                a NFGas (1 a 9). Observação: O ambiente autorizador que
                trabalhar com mais de um Site deverá divulgar para cada
                endereço de site qual número correspondente de
                nSiteAutoriz o contribuinte pode usar
            :ivar c_mun_fg: Código do município de ocorrência do fato
                gerador do IBS/CBS
            :ivar fin_nfgas: Finalidade de emissão da NFGas 0 - NFGas
                normal; 3 - NFGas substituição;
            :ivar tp_fat: Tipo de Faturamento da NFGas 1 - Faturamento
                Normal; 2 - Faturamento Agregado; 3 - Faturamento
                Agregador
            :ivar ver_proc: Versão do processo de emissão Informar a
                versão do aplicativo emissor de NFGas
            :ivar dh_cont: Data e Hora da entrada em contingência
                Informar a data e hora no formato AAAA-MM-DDTHH:MM:SS
            :ivar x_just: Justificativa da entrada em contingência
            :ivar g_compra_gov: Grupo de Compras Governamentais
            """

            c_uf: TcodUfIbge = field(
                metadata={
                    "name": "cUF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                }
            )
            tp_amb: Tamb = field(
                metadata={
                    "name": "tpAmb",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                }
            )
            mod: TmodNf = field(
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                }
            )
            serie: str = field(
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "white_space": "preserve",
                    "pattern": r"0|[1-9]{1}[0-9]{0,2}",
                }
            )
            n_nf: str = field(
                metadata={
                    "name": "nNF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "white_space": "preserve",
                    "pattern": r"[1-9]{1}[0-9]{0,8}",
                }
            )
            c_nf: str = field(
                metadata={
                    "name": "cNF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{7}",
                }
            )
            c_dv: str = field(
                metadata={
                    "name": "cDV",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{1}",
                }
            )
            dh_emi: str = field(
                metadata={
                    "name": "dhEmi",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            tp_emis: TtpEmis = field(
                metadata={
                    "name": "tpEmis",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                }
            )
            n_site_autoriz: str = field(
                metadata={
                    "name": "nSiteAutoriz",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{1}",
                }
            )
            c_mun_fg: str = field(
                metadata={
                    "name": "cMunFG",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{7}",
                }
            )
            fin_nfgas: TfinNf = field(
                metadata={
                    "name": "finNFGas",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                }
            )
            tp_fat: TfatNf = field(
                metadata={
                    "name": "tpFat",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                }
            )
            ver_proc: str = field(
                metadata={
                    "name": "verProc",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                },
            )
            x_just: None | str = field(
                default=None,
                metadata={
                    "name": "xJust",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "white_space": "preserve",
                    "pattern": r"[A-Z0-9]{12}[0-9]{2}",
                }
            )
            ie: str = field(
                metadata={
                    "name": "IE",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}",
                }
            )
            x_nome: str = field(
                metadata={
                    "name": "xNome",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                }
            )

        @dataclass(kw_only=True)
        class Dest:
            """
            :ivar x_nome: Razão social ou Nome do destinatário
            :ivar cnpj: Número do CNPJ Em caso de empresa não
                estabelecida no Brasil, será informado o CNPJ com zeros.
                Informar os zeros não significativos.
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
            :ivar ender_dest: Endereço do destinatário
            """

            x_nome: str = field(
                metadata={
                    "name": "xNome",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0}|[A-Z0-9]{12}[0-9]{2}",
                },
            )
            cpf: None | str = field(
                default=None,
                metadata={
                    "name": "CPF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                },
            )
            id_outros: None | str = field(
                default=None,
                metadata={
                    "name": "idOutros",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0,14}|ISENTO",
                },
            )
            im: None | str = field(
                default=None,
                metadata={
                    "name": "IM",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                }
            )

        @dataclass(kw_only=True)
        class Instalacao:
            """
            :ivar id_instalacao: Código único de Identificação da
                Instalação
            :ivar id_cod_cliente: Código de Identificação do Cliente
                para empresa emitente
            :ivar tp_instalacao: Tipo de Instalação 1 - Cativo 2 - Livre
                3 - Parcialmente Livre
            :ivar n_contrato: Número do Contrato
            :ivar tp_classe: Classe de Consumo da Instalação 01 -
                Comercial 02 - Industrial 03 - Residencial 04 - Térmico
                05 - Veicular Posto 06 - Veicular Frota 07 - GNC 08 -
                GNL 09 - Cogeração 10 - Refinaria 99 - Outros
            :ivar x_classe: Detalhamento da Classe quando informado
                Outros
            :ivar lat_gps: Latitude do ponto geográfico da localização
                da captura
            :ivar long_gps: Longitude do ponto geográfico da localização
                da captura
            :ivar cod_roteiro_leitura: Roteiro da Leitura para uso
                operacional
            """

            id_instalacao: str = field(
                metadata={
                    "name": "idInstalacao",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "min_length": 1,
                    "max_length": 15,
                    "white_space": "preserve",
                    "pattern": r"([!-ÿ]{0}|[!-ÿ]{1,15})?",
                }
            )
            id_cod_cliente: None | str = field(
                default=None,
                metadata={
                    "name": "idCodCliente",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "min_length": 2,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"([!-ÿ]{0}|[!-ÿ]{2,20})?",
                },
            )
            tp_instalacao: Tligacao = field(
                metadata={
                    "name": "tpInstalacao",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                }
            )
            n_contrato: None | str = field(
                default=None,
                metadata={
                    "name": "nContrato",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"([!-ÿ]{0}|[!-ÿ]{1,20})?",
                },
            )
            tp_classe: Tclasse = field(
                metadata={
                    "name": "tpClasse",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                }
            )
            x_classe: None | str = field(
                default=None,
                metadata={
                    "name": "xClasse",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "min_length": 1,
                    "max_length": 200,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                },
            )
            lat_gps: None | str = field(
                default=None,
                metadata={
                    "name": "latGPS",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "white_space": "preserve",
                    "pattern": r"[0-9]\.[0-9]{6}|[1-8][0-9]\.[0-9]{6}|90\.[0-9]{6}|-[0-9]\.[0-9]{6}|-[1-8][0-9]\.[0-9]{6}|-90\.[0-9]{6}",
                },
            )
            long_gps: None | str = field(
                default=None,
                metadata={
                    "name": "longGPS",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "white_space": "preserve",
                    "pattern": r"[0-9]\.[0-9]{6}|[1-9][0-9]\.[0-9]{6}|1[0-7][0-9]\.[0-9]{6}|180\.[0-9]{6}|-[0-9]\.[0-9]{6}|-[1-9][0-9]\.[0-9]{6}|-1[0-7][0-9]\.[0-9]{6}|-180\.[0-9]{6}",
                },
            )
            cod_roteiro_leitura: None | str = field(
                default=None,
                metadata={
                    "name": "codRoteiroLeitura",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "min_length": 2,
                    "max_length": 100,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                },
            )

        @dataclass(kw_only=True)
        class GSub:
            """
            :ivar ch_nfgas: Chave de acesso da NFGas referenciada
            :ivar g_nf: Informação da NF em papel referenciada
            :ivar mot_sub: Motivo da substituição 01 – Erro de Leitura
                02 – Erro de Preço ou Erro de Tarifa; 03 – Decisão
                Judicial 04 – Erro Cadastral; 05 - Erro de Tributação 06
                - Decisão da Reguladora;
            """

            ch_nfgas: None | str = field(
                default=None,
                metadata={
                    "name": "chNFGas",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "max_length": 44,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{6}[A-Z0-9]{12}[0-9]{26}",
                },
            )
            g_nf: None | Tnfgas.InfNfgas.GSub.GNf = field(
                default=None,
                metadata={
                    "name": "gNF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                },
            )
            mot_sub: TmotSub = field(
                metadata={
                    "name": "motSub",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                }
            )

            @dataclass(kw_only=True)
            class GNf:
                """
                :ivar cnpj: CNPJ do Emitente Informar o CNPJ do emitente
                    do Documento Fiscal
                :ivar serie: Serie do documento fiscal
                :ivar n_nf: Número do documento fiscal
                :ivar compet_emis: Ano e mês da emissão da NF papel
                    (AAAAMM)
                :ivar compet_apur: Ano e mês de apuração (AAAAMM)
                :ivar hash115: Hash do registro no arquivo do convênio
                    115
                """

                cnpj: str = field(
                    metadata={
                        "name": "CNPJ",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        "white_space": "preserve",
                        "pattern": r"[A-Z0-9]{12}[0-9]{2}",
                    }
                )
                serie: str = field(
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        "min_length": 1,
                        "max_length": 3,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                n_nf: str = field(
                    metadata={
                        "name": "nNF",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        "white_space": "preserve",
                        "pattern": r"[1-9]{1}[0-9]{0,8}",
                    }
                )
                compet_emis: str = field(
                    metadata={
                        "name": "CompetEmis",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        "min_length": 6,
                        "max_length": 6,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{1,6}",
                    }
                )
                compet_apur: str = field(
                    metadata={
                        "name": "CompetApur",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        "min_length": 6,
                        "max_length": 6,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{1,6}",
                    }
                )
                hash115: None | bytes = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        "min_length": 32,
                        "max_length": 32,
                        "format": "base64",
                    },
                )

        @dataclass(kw_only=True)
        class GVolContrat:
            """
            :ivar tp_vol_contrat: Tipo de volume contratado 1 - Demanda
                mínima; 2 - Montante de Uso do Sistema de Distribuição;
                3 - Encargo de Capacidade; 4 - Volume Contratado
            :ivar q_unid_contrat: Quantidade Contratada em m3
            :ivar n_contrat: Número de referência para informar nos
                produtos a relação com a quantidade contratada
            """

            tp_vol_contrat: TgrContrat = field(
                metadata={
                    "name": "tpVolContrat",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                }
            )
            q_unid_contrat: str = field(
                metadata={
                    "name": "qUnidContrat",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{1,13}(\.[0-9]{2,6})?",
                }
            )
            n_contrat: str = field(
                metadata={
                    "name": "nContrat",
                    "type": "Attribute",
                    "min_length": 2,
                    "max_length": 2,
                    "white_space": "preserve",
                    "pattern": r"(0[1-9]|1[0-9]|20)",
                }
            )

        @dataclass(kw_only=True)
        class GMed:
            """
            :ivar id_eqp: Identificação do equipamento de Medição
            :ivar d_med_ant: Data da leitura anterior Formato AAAA-MM-DD
                Em caso da 1a leitura do equipamento, informar a data de
                instalação do hidrômetro
            :ivar v_med_ant: Valor da medição (leitura) anterior
            :ivar d_med_atu: Data da leitura atual Formato AAAA-MM-DD
            :ivar v_med_atu: Valor da medição (leitura) atual
            :ivar tp_eqp: 1 - Medidor 2 - Conversor
            :ivar tp_medidor: 1 - Turbina 2 - Rotativo 3 - Diafragma 4 -
                Ultrasonico Informado apenas para tpEqp = 1
            :ivar n_med: Número de referência para informar nos produtos
                a relação com a medição
            """

            id_eqp: str = field(
                metadata={
                    "name": "idEqp",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "white_space": "preserve",
                    "pattern": r"((((20|19|18)(([02468][048])|([13579][26]))-02-29))|((20|19|18)[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                }
            )
            v_med_ant: str = field(
                metadata={
                    "name": "vMedAnt",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{1,13}(\.[0-9]{2,4})?",
                }
            )
            d_med_atu: str = field(
                metadata={
                    "name": "dMedAtu",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "white_space": "preserve",
                    "pattern": r"((((20|19|18)(([02468][048])|([13579][26]))-02-29))|((20|19|18)[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                }
            )
            v_med_atu: str = field(
                metadata={
                    "name": "vMedAtu",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{1,13}(\.[0-9]{2,4})?",
                }
            )
            tp_eqp: GMedTpEqp = field(
                metadata={
                    "name": "tpEqp",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "white_space": "preserve",
                }
            )
            tp_medidor: None | GMedTpMedidor = field(
                default=None,
                metadata={
                    "name": "tpMedidor",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "white_space": "preserve",
                },
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
        class Det:
            """
            :ivar g_normal: Informar se faturamento normal (1) ou
                agregado (2)
            :ivar g_agregadora: Informar para faturamento agregador (3)
            :ivar n_item: Número do item da NFGas
            :ivar ch_nfgas_ant: Chave de Acesso da NFGas anterior Usar
                para NFGas quando indicar um item de devolução de nota
                anterior DEVE SER USADA NA NOTA AGREGADORA PARA INDICAR
                AS NOTAS QUE FORAM AGREGADAS Informar chave de acesso de
                referencia anterior TAG OPCIONAL, DEVE SER INFORMADA
                APENAS NOS CASOS PREVISTOS DE NOTA ANTERIOR REFERENCIADA
            :ivar n_item_ant: Número do item da NFGas anterior Informar
                nro do item da chave de acesso de referencia anterior
                TAG OPCIONAL, DEVE SER INFORMADA APENAS NOS CASOS
                PREVISTOS DE NOTA ANTERIOR REFERENCIADA
            """

            g_normal: None | Tnfgas.InfNfgas.Det.GNormal = field(
                default=None,
                metadata={
                    "name": "gNormal",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                },
            )
            g_agregadora: None | Tnfgas.InfNfgas.Det.GAgregadora = field(
                default=None,
                metadata={
                    "name": "gAgregadora",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
            ch_nfgas_ant: None | str = field(
                default=None,
                metadata={
                    "name": "chNFGasAnt",
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
            class GNormal:
                """
                :ivar g_tarif: Grupo de Tarifas por Período
                :ivar prod: Dados do Produto ou Serviço
                :ivar imposto: Tributos incidentes no Produto ou Serviço
                :ivar g_proc_ref: Grupo Processo referenciado Este grupo
                    somente deverá ser preenchido quando houver processo
                    judicial ou administrativo que altere valores.
                :ivar inf_ad_prod: Informações adicionais do produto
                    (norma referenciada, informações complementares,
                    etc)
                """

                g_tarif: list[Tnfgas.InfNfgas.Det.GNormal.GTarif] = field(
                    default_factory=list,
                    metadata={
                        "name": "gTarif",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        "max_occurs": 6,
                    },
                )
                prod: Tnfgas.InfNfgas.Det.GNormal.Prod = field(
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    }
                )
                imposto: Tnfgas.InfNfgas.Det.GNormal.Imposto = field(
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    }
                )
                g_proc_ref: None | Tnfgas.InfNfgas.Det.GNormal.GProcRef = (
                    field(
                        default=None,
                        metadata={
                            "name": "gProcRef",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        },
                    )
                )
                inf_ad_prod: None | str = field(
                    default=None,
                    metadata={
                        "name": "infAdProd",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        "min_length": 1,
                        "max_length": 500,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    },
                )

                @dataclass(kw_only=True)
                class GTarif:
                    """
                    :ivar d_ini_tarif: Data de início da aplicação da
                        tarifa Data de início da aplicação da tarifa no
                        período considerado para o faturamento ( Formato
                        AAAA-MM-DD)
                    :ivar d_fim_tarif: Data de fim da aplicação da
                        tarifa Data de fim da aplicação da tarifa no
                        período considerado para o faturamento (Formato
                        AAAA-MM-DD)
                    :ivar n_ato: Número do Ato
                    :ivar ano_ato: Ano do Ato (AAAA)
                    :ivar tp_faixa_cons: Faixa Prevista de Consumo 1 -
                        Fixa 2 - Média
                    :ivar v_tarif_aplic: Valor da tarifa aplicada
                    """

                    d_ini_tarif: str = field(
                        metadata={
                            "name": "dIniTarif",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                            "white_space": "preserve",
                            "pattern": r"((((20|19|18)(([02468][048])|([13579][26]))-02-29))|((20|19|18)[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                        }
                    )
                    d_fim_tarif: None | str = field(
                        default=None,
                        metadata={
                            "name": "dFimTarif",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                            "white_space": "preserve",
                            "pattern": r"((((20|19|18)(([02468][048])|([13579][26]))-02-29))|((20|19|18)[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                        },
                    )
                    n_ato: str = field(
                        metadata={
                            "name": "nAto",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                            "min_length": 4,
                            "max_length": 4,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{4}",
                        }
                    )
                    tp_faixa_cons: Tfaixa = field(
                        metadata={
                            "name": "tpFaixaCons",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        }
                    )
                    v_tarif_aplic: str = field(
                        metadata={
                            "name": "vTarifAplic",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{8}|[1-9]{1}[0-9]{0,8}(\.[0-9]{8})?",
                        }
                    )

                @dataclass(kw_only=True)
                class Prod:
                    """
                    :ivar ind_origem_qtd: Indicador da origem da
                        quantidade faturada 1 - Media; 2 - Medido; 3 -
                        Contratada; 4 - Residual estimado 5 - Residual
                        medido 6 - Sem quantidade 7 - Por Faixa;
                    :ivar g_medicao: Grupo para referenciar qual medição
                        e medida estão relacionadas ao item Informar
                        para origem qtd = 1 ou 5
                    :ivar c_prod: Código do produto ou serviço.
                    :ivar x_prod: Descrição do produto ou serviço
                    :ivar c_class: Código de classificação Tabela de
                        Classificação de Item da Gas (validar por RV)
                    :ivar cfop: CFOP Utilizar Tabela de CFOP.
                    :ivar u_med: Unidade Básica de Medida 1 - m3; 2 -
                        Unidade
                    :ivar q_faturada: Quantidade Faturada
                    :ivar v_item: Valor unitário do item
                    :ivar fator_pcs: Fator de poder calorifico Deve
                        maior que zero Se informado multipla ao valor do
                        vItem
                    :ivar fator_ptz: Fator de correção Se informado
                        multipla ao valor do vItem Deve maior que zero
                    :ivar fator_p: Fator de correção de pressão
                    :ivar fator_t: Fator de correção de temperatura
                    :ivar v_prod: Valor total do item
                    :ivar ind_devolucao: Indicador de devolução do valor
                        do item 1 – Devolução do valor do item
                    """

                    ind_origem_qtd: TorigemQtd = field(
                        metadata={
                            "name": "indOrigemQtd",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        }
                    )
                    g_medicao: (
                        None | Tnfgas.InfNfgas.Det.GNormal.Prod.GMedicao
                    ) = field(
                        default=None,
                        metadata={
                            "name": "gMedicao",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        },
                    )
                    c_prod: str = field(
                        metadata={
                            "name": "cProd",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                            "min_length": 7,
                            "max_length": 7,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{7}",
                        }
                    )
                    cfop: None | str = field(
                        default=None,
                        metadata={
                            "name": "CFOP",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                            "white_space": "preserve",
                            "pattern": r"[123567][0-9]([0-9][1-9]|[1-9][0-9])",
                        },
                    )
                    u_med: TumedItem = field(
                        metadata={
                            "name": "uMed",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        }
                    )
                    q_faturada: str = field(
                        metadata={
                            "name": "qFaturada",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1,11}(\.[0-9]{2,4})?",
                        }
                    )
                    v_item: str = field(
                        metadata={
                            "name": "vItem",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1,13}(\.[0-9]{2,10})?",
                        }
                    )
                    fator_pcs: None | str = field(
                        default=None,
                        metadata={
                            "name": "fatorPCS",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1,11}(\.[0-9]{2,4})?",
                        },
                    )
                    fator_ptz: None | str = field(
                        default=None,
                        metadata={
                            "name": "fatorPTZ",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1,11}(\.[0-9]{2,4})?",
                        },
                    )
                    fator_p: None | str = field(
                        default=None,
                        metadata={
                            "name": "fatorP",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1,11}(\.[0-9]{2,4})?",
                        },
                    )
                    fator_t: None | str = field(
                        default=None,
                        metadata={
                            "name": "fatorT",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1,11}(\.[0-9]{2,4})?",
                        },
                    )
                    v_prod: str = field(
                        metadata={
                            "name": "vProd",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1,13}(\.[0-9]{2,10})?",
                        }
                    )
                    ind_devolucao: None | ProdIndDevolucao = field(
                        default=None,
                        metadata={
                            "name": "indDevolucao",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                            "white_space": "preserve",
                        },
                    )

                    @dataclass(kw_only=True)
                    class GMedicao:
                        """
                        :ivar n_med: Referência para a medição ao qual
                            se refere o item
                        :ivar n_contrat: Referência para o grupo de
                            demanda contratada ao qual se refere o item
                        :ivar g_medida: Grupo de medida
                        :ivar tp_mot_nao_leitura: Tipo Motivo da não
                            leitura 1 - Consumidor; 2 - Distribuidora; 3
                            - Independente do Consumidor e
                            distribuidora;
                        :ivar x_mot_nao_leitura: Detalhamento do motivo
                            da não leitura
                        """

                        n_med: str = field(
                            metadata={
                                "name": "nMed",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "min_length": 2,
                                "max_length": 2,
                                "white_space": "preserve",
                                "pattern": r"(0[1-9]|1[0-9]|20)",
                            }
                        )
                        n_contrat: None | str = field(
                            default=None,
                            metadata={
                                "name": "nContrat",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "min_length": 2,
                                "max_length": 2,
                                "white_space": "preserve",
                                "pattern": r"(0[1-9]|1[0-9]|20)",
                            },
                        )
                        g_medida: None | Tmedida = field(
                            default=None,
                            metadata={
                                "name": "gMedida",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                            },
                        )
                        tp_mot_nao_leitura: None | TmotNaoLeitura = field(
                            default=None,
                            metadata={
                                "name": "tpMotNaoLeitura",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                            },
                        )
                        x_mot_nao_leitura: None | str = field(
                            default=None,
                            metadata={
                                "name": "xMotNaoLeitura",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "min_length": 1,
                                "max_length": 200,
                                "white_space": "preserve",
                                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                            },
                        )

                @dataclass(kw_only=True)
                class Imposto:
                    """
                    :ivar orig: Origem da mercadoria 0 - Nacional,
                        exceto as indicadas nos códigos 3, 4, 5 e 8 1 -
                        Estrangeira - Importação direta, exceto a
                        indicada no código 6 2 - Estrangeira - Adquirida
                        no mercado interno, exceto a indicada no código
                        7 3 - Nacional, mercadoria ou bem com Conteúdo
                        de Importação superior a 40% e inferior ou igual
                        a 70% 4 - Nacional, cuja produção tenha sido
                        feita em conformidade com os processos
                        produtivos básicos de que tratam as legislações
                        citadas nos Ajustes 5 - Nacional, mercadoria ou
                        bem com Conteúdo de Importação inferior ou igual
                        a 40% 6 - Estrangeira - Importação direta, sem
                        similar nacional, constante em lista da CAMEX e
                        gás natural 7 - Estrangeira - Adquirida no
                        mercado interno, sem similar nacional, constante
                        lista CAMEX e gás natural 8 - Nacional,
                        mercadoria ou bem com Conteúdo de Importação
                        superior a 70%
                    :ivar icms00: Prestação sujeito à tributação normal
                        do ICMS Tributada integralmente
                    :ivar icms10: Tributada e com cobrança do ICMS por
                        substituição tributária
                    :ivar icms20: Prestação sujeito à tributação com
                        redução de BC do ICMS
                    :ivar icms40: Tributação Isenta, Não tributada
                    :ivar icms51: Tributação com Diferimento A exigência
                        do preenchimento das informações do ICMS
                        diferido fica a critério de cada UF
                    :ivar icms60: Tributação pelo ICMS 60 - ICMS cobrado
                        anteriormente por substituição tributária
                    :ivar icms70: Tributação pelo ICMS 70 - Com redução
                        de base de cálculo e cobrança do ICMS por
                        substituição tributária
                    :ivar icms90: ICMS Outros Será usado no caso da
                        subvenção
                    :ivar ind_sem_cst: Sem Situação Tributária para o
                        ICMS Informar para itens que não tenham nenhuma
                        relação com o ICMS. Quando informado o item NÃO
                        PODE ter CFOP informado Se informado esse grupo
                        o schema não permite informar nenhum dos grupos
                        de ICMSXX
                    :ivar ibscbs: Grupo de informações do IBS e CBS
                    :ivar pis: Dados do PIS
                    :ivar cofins: Dados do COFINS
                    :ivar ret_trib: Grupo de informações de retenção de
                        tributos federais
                    :ivar tx_reg: Taxa Regulatória
                    """

                    orig: None | ImpostoOrig = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        },
                    )
                    icms00: (
                        None | Tnfgas.InfNfgas.Det.GNormal.Imposto.Icms00
                    ) = field(
                        default=None,
                        metadata={
                            "name": "ICMS00",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        },
                    )
                    icms10: (
                        None | Tnfgas.InfNfgas.Det.GNormal.Imposto.Icms10
                    ) = field(
                        default=None,
                        metadata={
                            "name": "ICMS10",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        },
                    )
                    icms20: (
                        None | Tnfgas.InfNfgas.Det.GNormal.Imposto.Icms20
                    ) = field(
                        default=None,
                        metadata={
                            "name": "ICMS20",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        },
                    )
                    icms40: (
                        None | Tnfgas.InfNfgas.Det.GNormal.Imposto.Icms40
                    ) = field(
                        default=None,
                        metadata={
                            "name": "ICMS40",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        },
                    )
                    icms51: (
                        None | Tnfgas.InfNfgas.Det.GNormal.Imposto.Icms51
                    ) = field(
                        default=None,
                        metadata={
                            "name": "ICMS51",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        },
                    )
                    icms60: (
                        None | Tnfgas.InfNfgas.Det.GNormal.Imposto.Icms60
                    ) = field(
                        default=None,
                        metadata={
                            "name": "ICMS60",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        },
                    )
                    icms70: (
                        None | Tnfgas.InfNfgas.Det.GNormal.Imposto.Icms70
                    ) = field(
                        default=None,
                        metadata={
                            "name": "ICMS70",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        },
                    )
                    icms90: (
                        None | Tnfgas.InfNfgas.Det.GNormal.Imposto.Icms90
                    ) = field(
                        default=None,
                        metadata={
                            "name": "ICMS90",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        },
                    )
                    ind_sem_cst: None | ImpostoIndSemCst = field(
                        default=None,
                        metadata={
                            "name": "indSemCST",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                            "white_space": "preserve",
                        },
                    )
                    ibscbs: TtribNfgas = field(
                        metadata={
                            "name": "IBSCBS",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        }
                    )
                    pis: None | Tnfgas.InfNfgas.Det.GNormal.Imposto.Pis = (
                        field(
                            default=None,
                            metadata={
                                "name": "PIS",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                            },
                        )
                    )
                    cofins: (
                        None | Tnfgas.InfNfgas.Det.GNormal.Imposto.Cofins
                    ) = field(
                        default=None,
                        metadata={
                            "name": "COFINS",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        },
                    )
                    ret_trib: (
                        None | Tnfgas.InfNfgas.Det.GNormal.Imposto.RetTrib
                    ) = field(
                        default=None,
                        metadata={
                            "name": "retTrib",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        },
                    )
                    tx_reg: (
                        None | Tnfgas.InfNfgas.Det.GNormal.Imposto.TxReg
                    ) = field(
                        default=None,
                        metadata={
                            "name": "TxReg",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        },
                    )

                    @dataclass(kw_only=True)
                    class Pis:
                        """
                        :ivar cst: classificação Tributária do PIS 01 –
                            Tributável com alíquota básica 02 –
                            Tributável com alíquota diferenciada 06 –
                            Tributável com alíquota erro 07 – Operação
                            isenta de contribuição 08 – Operação sem
                            incidência da contribuição 09 – Operação com
                            suspensão da contribuição 49 – Outras
                            operações de saída
                        :ivar v_bc: Valor da BC do PIS
                        :ivar p_pis: Alíquota do PIS (em percentual)
                        :ivar v_pis: Valor do PIS
                        """

                        cst: PisCst = field(
                            metadata={
                                "name": "CST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                            }
                        )
                        v_bc: str = field(
                            metadata={
                                "name": "vBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_pis: str = field(
                            metadata={
                                "name": "pPIS",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_pis: str = field(
                            metadata={
                                "name": "vPIS",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )

                    @dataclass(kw_only=True)
                    class Cofins:
                        """
                        :ivar cst: classificação Tributária do COFINS 01
                            – Tributável com alíquota básica 02 –
                            Tributável com alíquota diferenciada 06 –
                            Tributável com alíquota erro 07 – Operação
                            isenta de contribuição 08 – Operação sem
                            incidência da contribuição 09 – Operação com
                            suspensão da contribuição 49 – Outras
                            operações de saída
                        :ivar v_bc: Valor da BC do COFINS
                        :ivar p_cofins: Alíquota do COFINS (em
                            percentual)
                        :ivar v_cofins: Valor do COFINS
                        """

                        cst: CofinsCst = field(
                            metadata={
                                "name": "CST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                            }
                        )
                        v_bc: str = field(
                            metadata={
                                "name": "vBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_cofins: str = field(
                            metadata={
                                "name": "pCOFINS",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_cofins: str = field(
                            metadata={
                                "name": "vCOFINS",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"[0-9]{1,13}(\.[0-9]{2,8})?",
                            }
                        )
                        v_ret_cofins: str = field(
                            metadata={
                                "name": "vRetCofins",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"[0-9]{1,13}(\.[0-9]{2,8})?",
                            }
                        )
                        v_ret_csll: str = field(
                            metadata={
                                "name": "vRetCSLL",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"[0-9]{1,13}(\.[0-9]{2,8})?",
                            }
                        )
                        v_irrf: str = field(
                            metadata={
                                "name": "vIRRF",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"[0-9]{1,13}(\.[0-9]{2,8})?",
                            }
                        )

                    @dataclass(kw_only=True)
                    class TxReg:
                        """
                        :ivar v_bc: Valor BC
                        :ivar p_taxa: Alíquota
                        :ivar v_taxa: Valor
                        """

                        v_bc: str = field(
                            metadata={
                                "name": "vBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_taxa: str = field(
                            metadata={
                                "name": "pTaxa",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_taxa: str = field(
                            metadata={
                                "name": "vTaxa",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )

                    @dataclass(kw_only=True)
                    class Icms00:
                        """
                        :ivar cst: classificação Tributária do Serviço
                            00 - tributação normal ICMS
                        :ivar v_bc: Valor da BC do ICMS
                        :ivar p_icms: Alíquota do ICMS
                        :ivar v_icms: Valor do ICMS
                        :ivar p_fcp: Percentual de ICMS relativo ao
                            Fundo de Combate à Pobreza (FCP).
                        :ivar v_fcp: Valor do ICMS relativo ao Fundo de
                            Combate à Pobreza (FCP).
                        """

                        cst: Icms00Cst = field(
                            metadata={
                                "name": "CST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                            }
                        )
                        v_bc: str = field(
                            metadata={
                                "name": "vBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_icms: str = field(
                            metadata={
                                "name": "pICMS",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
                            }
                        )
                        v_icms: str = field(
                            metadata={
                                "name": "vICMS",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_fcp: None | str = field(
                            default=None,
                            metadata={
                                "name": "pFCP",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            },
                        )
                        v_fcp: None | str = field(
                            default=None,
                            metadata={
                                "name": "vFCP",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            },
                        )

                    @dataclass(kw_only=True)
                    class Icms10:
                        """
                        :ivar cst: classificação Tributária do Serviço
                            10=Tributada e com cobrança do ICMS por
                            substituição tributária
                        :ivar v_bcst: Valor da BC do ICMS ST
                        :ivar p_icmsst: Alíquota do ICMS ST
                        :ivar v_icmsst: Valor do ICMS ST retido
                        :ivar p_fcpst: Percentual de ICMS relativo ao
                            Fundo de Combate à Pobreza (FCP).
                        :ivar v_fcpst: Valor do ICMS relativo ao Fundo
                            de Combate à Pobreza (FCP).
                        """

                        cst: Icms10Cst = field(
                            metadata={
                                "name": "CST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                            }
                        )
                        v_bcst: str = field(
                            metadata={
                                "name": "vBCST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_icmsst: str = field(
                            metadata={
                                "name": "pICMSST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
                            }
                        )
                        v_icmsst: str = field(
                            metadata={
                                "name": "vICMSST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_fcpst: None | str = field(
                            default=None,
                            metadata={
                                "name": "pFCPST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            },
                        )
                        v_fcpst: None | str = field(
                            default=None,
                            metadata={
                                "name": "vFCPST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            },
                        )

                    @dataclass(kw_only=True)
                    class Icms20:
                        """
                        :ivar cst: Classificação Tributária do serviço
                            20 - tributação com BC reduzida do ICMS
                        :ivar p_red_bc: Percentual de redução da BC
                        :ivar v_bc: Valor da BC do ICMS
                        :ivar p_icms: Alíquota do ICMS
                        :ivar v_icms: Valor do ICMS
                        :ivar v_icmsdeson: Valor do ICMS de desoneração
                        :ivar c_benef: Código de Benefício Fiscal na UF
                            aplicado ao item Código de Benefício Fiscal
                            utilizado pela UF, aplicado ao item.
                        :ivar p_fcp: Percentual de ICMS relativo ao
                            Fundo de Combate à Pobreza (FCP).
                        :ivar v_fcp: Valor do ICMS relativo ao Fundo de
                            Combate à Pobreza (FCP).
                        """

                        cst: Icms20Cst = field(
                            metadata={
                                "name": "CST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                            }
                        )
                        p_red_bc: str = field(
                            metadata={
                                "name": "pRedBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
                            }
                        )
                        v_bc: str = field(
                            metadata={
                                "name": "vBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_icms: str = field(
                            metadata={
                                "name": "pICMS",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
                            }
                        )
                        v_icms: str = field(
                            metadata={
                                "name": "vICMS",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        v_icmsdeson: None | str = field(
                            default=None,
                            metadata={
                                "name": "vICMSDeson",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            },
                        )
                        c_benef: None | str = field(
                            default=None,
                            metadata={
                                "name": "cBenef",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "max_length": 10,
                                "white_space": "preserve",
                            },
                        )
                        p_fcp: None | str = field(
                            default=None,
                            metadata={
                                "name": "pFCP",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            },
                        )
                        v_fcp: None | str = field(
                            default=None,
                            metadata={
                                "name": "vFCP",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            },
                        )

                    @dataclass(kw_only=True)
                    class Icms40:
                        """
                        :ivar cst: Classificação Tributária do serviço
                            40=Isenta; 41=Não tributada;
                        :ivar v_icmsdeson: Valor do ICMS de desoneração
                        :ivar c_benef: Código de Benefício Fiscal na UF
                            aplicado ao item Código de Benefício Fiscal
                            utilizado pela UF, aplicado ao item.
                        """

                        cst: Icms40Cst = field(
                            metadata={
                                "name": "CST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                            }
                        )
                        v_icmsdeson: None | str = field(
                            default=None,
                            metadata={
                                "name": "vICMSDeson",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            },
                        )
                        c_benef: None | str = field(
                            default=None,
                            metadata={
                                "name": "cBenef",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "max_length": 10,
                                "white_space": "preserve",
                            },
                        )

                    @dataclass(kw_only=True)
                    class Icms51:
                        """
                        :ivar cst: Classificação Tributária do serviço
                            Tributação pelo ICMS 51 - Diferimento
                        :ivar v_icmsdeson: Valor do ICMS de desoneração
                        :ivar c_benef: Código de Benefício Fiscal na UF
                            aplicado ao item Código de Benefício Fiscal
                            utilizado pela UF, aplicado ao item.
                        """

                        cst: Icms51Cst = field(
                            metadata={
                                "name": "CST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                            }
                        )
                        v_icmsdeson: None | str = field(
                            default=None,
                            metadata={
                                "name": "vICMSDeson",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            },
                        )
                        c_benef: None | str = field(
                            default=None,
                            metadata={
                                "name": "cBenef",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "max_length": 10,
                                "white_space": "preserve",
                            },
                        )

                    @dataclass(kw_only=True)
                    class Icms60:
                        """
                        :ivar cst: Tributação pelo ICMS 60 - ICMS
                            cobrado anteriormente por substituição
                            tributária
                        :ivar v_bcstret: Valor da BC do ICMS ST retido
                            anteriormente
                        :ivar p_icmsstret: Aliquota suportada pelo
                            consumidor final.
                        :ivar v_icmssubstituto: Valor do ICMS Próprio do
                            Substituto cobrado em operação anterior
                        :ivar v_icmsstret: Valor do ICMS ST retido
                            anteriormente
                        :ivar v_bcfcpstret: Valor da Base de cálculo do
                            FCP retido anteriormente por ST.
                        :ivar p_fcpstret: Percentual de FCP retido
                            anteriormente por substituição tributária.
                        :ivar v_fcpstret: Valor do FCP retido por
                            substituição tributária.
                        :ivar p_red_bcefet: Percentual de redução da
                            base de cálculo efetiva.
                        :ivar v_bcefet: Valor da base de cálculo
                            efetiva.
                        :ivar p_icmsefet: Alíquota do ICMS efetiva.
                        :ivar v_icmsefet: Valor do ICMS efetivo.
                        :ivar v_icmsdeson: Valor do ICMS de desoneração
                        :ivar c_benef: Código de Benefício Fiscal na UF
                            aplicado ao item Código de Benefício Fiscal
                            utilizado pela UF, aplicado ao item.
                        """

                        cst: Icms60Cst = field(
                            metadata={
                                "name": "CST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                            }
                        )
                        v_bcstret: None | str = field(
                            default=None,
                            metadata={
                                "name": "vBCSTRet",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            },
                        )
                        p_icmsstret: None | str = field(
                            default=None,
                            metadata={
                                "name": "pICMSSTRet",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            },
                        )
                        v_icmssubstituto: None | str = field(
                            default=None,
                            metadata={
                                "name": "vICMSSubstituto",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            },
                        )
                        v_icmsstret: None | str = field(
                            default=None,
                            metadata={
                                "name": "vICMSSTRet",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            },
                        )
                        v_bcfcpstret: None | str = field(
                            default=None,
                            metadata={
                                "name": "vBCFCPSTRet",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            },
                        )
                        p_fcpstret: None | str = field(
                            default=None,
                            metadata={
                                "name": "pFCPSTRet",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            },
                        )
                        v_fcpstret: None | str = field(
                            default=None,
                            metadata={
                                "name": "vFCPSTRet",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            },
                        )
                        p_red_bcefet: None | str = field(
                            default=None,
                            metadata={
                                "name": "pRedBCEfet",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            },
                        )
                        v_bcefet: None | str = field(
                            default=None,
                            metadata={
                                "name": "vBCEfet",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            },
                        )
                        p_icmsefet: None | str = field(
                            default=None,
                            metadata={
                                "name": "pICMSEfet",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            },
                        )
                        v_icmsefet: None | str = field(
                            default=None,
                            metadata={
                                "name": "vICMSEfet",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            },
                        )
                        v_icmsdeson: None | str = field(
                            default=None,
                            metadata={
                                "name": "vICMSDeson",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            },
                        )
                        c_benef: None | str = field(
                            default=None,
                            metadata={
                                "name": "cBenef",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "max_length": 10,
                                "white_space": "preserve",
                            },
                        )

                    @dataclass(kw_only=True)
                    class Icms70:
                        """
                        :ivar cst: Tributção pelo ICMS 70 - Com redução
                            de base de cálculo e cobrança do ICMS por
                            substituição tributária
                        :ivar mod_bc: Modalidade de determinação da BC
                            do ICMS: 0 - Margem Valor Agregado (%); 1 -
                            Pauta (valor); 2 - Preço Tabelado Máximo
                            (valor); 3 - Valor da Operação.
                        :ivar p_red_bc: Percentual de redução da BC
                        :ivar v_bc: Valor da BC do ICMS
                        :ivar p_icms: Alíquota do ICMS
                        :ivar v_icms: Valor do ICMS
                        :ivar v_bcfcp: Valor da Base de cálculo do FCP.
                        :ivar p_fcp: Percentual de ICMS relativo ao
                            Fundo de Combate à Pobreza (FCP).
                        :ivar v_fcp: Valor do ICMS relativo ao Fundo de
                            Combate à Pobreza (FCP).
                        :ivar mod_bcst: Modalidade de determinação da BC
                            do ICMS ST: 0 – Preço tabelado ou máximo
                            sugerido; 1 - Lista Negativa (valor); 2 -
                            Lista Positiva (valor); 3 - Lista Neutra
                            (valor); 4 - Margem Valor Agregado (%); 5 -
                            Pauta (valor); 6 - Valor da Operação.
                        :ivar p_mvast: Percentual da Margem de Valor
                            Adicionado ICMS ST
                        :ivar p_red_bcst: Percentual de redução da BC
                            ICMS ST
                        :ivar v_bcst: Valor da BC do ICMS ST
                        :ivar p_icmsst: Alíquota do ICMS ST
                        :ivar v_icmsst: Valor do ICMS ST
                        :ivar v_bcfcpst: Valor da Base de cálculo do FCP
                            retido por substituição tributária.
                        :ivar p_fcpst: Percentual de FCP retido por
                            substituição tributária.
                        :ivar v_fcpst: Valor do FCP retido por
                            substituição tributária.
                        :ivar v_icmsdeson: Valor do ICMS de desoneração
                        :ivar mot_des_icms: Motivo da desoneração do
                            ICMS:3-Uso na
                            agropecuária;9-Outros;12-Fomento
                            agropecuário
                        :ivar ind_deduz_deson: Indica se o valor do ICMS
                            desonerado (vICMSDeson) deduz do valor do
                            item (vProd): 0=Valor do ICMS desonerado
                            (vICMSDeson) não deduz do valor do item
                            (vProd) / total da NF-e; 1=Valor do ICMS
                            desonerado (vICMSDeson) deduz do valor do
                            item (vProd) / total da NF-e.
                        :ivar v_icmsstdeson: Valor do ICMS-ST
                            desonerado.
                        :ivar mot_des_icmsst: Motivo da desoneração do
                            ICMS-ST: 3-Uso na agropecuária; 9-Outros;
                            12-Fomento agropecuário.
                        """

                        cst: Icms70Cst = field(
                            metadata={
                                "name": "CST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                            }
                        )
                        mod_bc: Icms70ModBc = field(
                            metadata={
                                "name": "modBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                            }
                        )
                        p_red_bc: str = field(
                            metadata={
                                "name": "pRedBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_bc: str = field(
                            metadata={
                                "name": "vBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_icms: str = field(
                            metadata={
                                "name": "pICMS",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_icms: str = field(
                            metadata={
                                "name": "vICMS",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        v_bcfcp: None | str = field(
                            default=None,
                            metadata={
                                "name": "vBCFCP",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            },
                        )
                        p_fcp: None | str = field(
                            default=None,
                            metadata={
                                "name": "pFCP",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            },
                        )
                        v_fcp: None | str = field(
                            default=None,
                            metadata={
                                "name": "vFCP",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            },
                        )
                        mod_bcst: Icms70ModBcst = field(
                            metadata={
                                "name": "modBCST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                            }
                        )
                        p_mvast: None | str = field(
                            default=None,
                            metadata={
                                "name": "pMVAST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            },
                        )
                        p_red_bcst: None | str = field(
                            default=None,
                            metadata={
                                "name": "pRedBCST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            },
                        )
                        v_bcst: str = field(
                            metadata={
                                "name": "vBCST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_icmsst: str = field(
                            metadata={
                                "name": "pICMSST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_icmsst: str = field(
                            metadata={
                                "name": "vICMSST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        v_bcfcpst: None | str = field(
                            default=None,
                            metadata={
                                "name": "vBCFCPST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            },
                        )
                        p_fcpst: None | str = field(
                            default=None,
                            metadata={
                                "name": "pFCPST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            },
                        )
                        v_fcpst: None | str = field(
                            default=None,
                            metadata={
                                "name": "vFCPST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            },
                        )
                        v_icmsdeson: None | str = field(
                            default=None,
                            metadata={
                                "name": "vICMSDeson",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            },
                        )
                        mot_des_icms: None | Icms70MotDesIcms = field(
                            default=None,
                            metadata={
                                "name": "motDesICMS",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                            },
                        )
                        ind_deduz_deson: None | Icms70IndDeduzDeson = field(
                            default=None,
                            metadata={
                                "name": "indDeduzDeson",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                            },
                        )
                        v_icmsstdeson: None | str = field(
                            default=None,
                            metadata={
                                "name": "vICMSSTDeson",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            },
                        )
                        mot_des_icmsst: None | Icms70MotDesIcmsst = field(
                            default=None,
                            metadata={
                                "name": "motDesICMSST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                            },
                        )

                    @dataclass(kw_only=True)
                    class Icms90:
                        """
                        :ivar cst: Classificação Tributária do Serviço
                            90 - ICMS outros
                        :ivar v_bc: Valor da BC do ICMS
                        :ivar p_icms: Alíquota do ICMS
                        :ivar v_icms: Valor do ICMS
                        :ivar v_icmsdeson: Valor do ICMS de desoneração
                        :ivar c_benef: Código de Benefício Fiscal na UF
                            aplicado ao item Código de Benefício Fiscal
                            utilizado pela UF, aplicado ao item.
                        :ivar p_fcp: Percentual de ICMS relativo ao
                            Fundo de Combate à Pobreza (FCP).
                        :ivar v_fcp: Valor do ICMS relativo ao Fundo de
                            Combate à Pobreza (FCP).
                        """

                        cst: Icms90Cst = field(
                            metadata={
                                "name": "CST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                            }
                        )
                        v_bc: None | str = field(
                            default=None,
                            metadata={
                                "name": "vBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            },
                        )
                        p_icms: None | str = field(
                            default=None,
                            metadata={
                                "name": "pICMS",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
                            },
                        )
                        v_icms: None | str = field(
                            default=None,
                            metadata={
                                "name": "vICMS",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            },
                        )
                        v_icmsdeson: None | str = field(
                            default=None,
                            metadata={
                                "name": "vICMSDeson",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            },
                        )
                        c_benef: None | str = field(
                            default=None,
                            metadata={
                                "name": "cBenef",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "max_length": 10,
                                "white_space": "preserve",
                            },
                        )
                        p_fcp: None | str = field(
                            default=None,
                            metadata={
                                "name": "pFCP",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            },
                        )
                        v_fcp: None | str = field(
                            default=None,
                            metadata={
                                "name": "vFCP",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            },
                        )

                @dataclass(kw_only=True)
                class GProcRef:
                    """
                    :ivar v_item: Valor unitário do item Informar o
                        valor sem a influência da decisão
                        judicial/administrativa.
                    :ivar q_faturada: Quantidade Faturada Informar a
                        quantidade de comercialização do produto .
                    :ivar v_prod: Valor total do item
                    :ivar ind_devolucao: Indicador de devolução do valor
                        do item 1 – Devolução do valor do item
                    :ivar g_proc: Grupo identificador do Processo
                    """

                    v_item: str = field(
                        metadata={
                            "name": "vItem",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1,13}(\.[0-9]{2,10})?",
                        }
                    )
                    q_faturada: str = field(
                        metadata={
                            "name": "qFaturada",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1,11}(\.[0-9]{2,4})?",
                        }
                    )
                    v_prod: str = field(
                        metadata={
                            "name": "vProd",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1,13}(\.[0-9]{2,10})?",
                        }
                    )
                    ind_devolucao: None | GProcRefIndDevolucao = field(
                        default=None,
                        metadata={
                            "name": "indDevolucao",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                            "white_space": "preserve",
                        },
                    )
                    g_proc: list[
                        Tnfgas.InfNfgas.Det.GNormal.GProcRef.GProc
                    ] = field(
                        default_factory=list,
                        metadata={
                            "name": "gProc",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
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

                        tp_proc: Tprocesso = field(
                            metadata={
                                "name": "tpProc",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                            }
                        )
                        n_processo: str = field(
                            metadata={
                                "name": "nProcesso",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                                "min_length": 1,
                                "max_length": 60,
                                "white_space": "preserve",
                                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                            }
                        )

            @dataclass(kw_only=True)
            class GAgregadora:
                """
                :ivar c_class: Código de classificação Tabela de
                    Classificação de Item da NFGas (validar por RV)
                :ivar v_tot_dfe: Valor total do documento fiscal da nota
                    agregada
                """

                c_class: str = field(
                    metadata={
                        "name": "cClass",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        "min_length": 7,
                        "max_length": 7,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{7}",
                    }
                )
                v_tot_dfe: str = field(
                    metadata={
                        "name": "vTotDFe",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )

        @dataclass(kw_only=True)
        class Total:
            """
            :ivar v_prod: Valor Total dos produtos e serviços
            :ivar icmstot: Totais referentes ao ICMS
            :ivar v_ret_trib_tot: Total da retenção de tributos federais
            :ivar v_cofins: Valor do COFINS
            :ivar v_pis: Valor do PIS
            :ivar v_tx_reg: Valor Taxa Regulatoria
            :ivar v_nf: Valor Total da NFGas
            :ivar ibscbstot: Totais de IBS e CBS
            :ivar v_tot_dfe: Valor total do documento fiscal (vNF +
                total do IBS + total da CBS)
            """

            v_prod: str = field(
                metadata={
                    "name": "vProd",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            icmstot: Tnfgas.InfNfgas.Total.Icmstot = field(
                metadata={
                    "name": "ICMSTot",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                }
            )
            v_ret_trib_tot: Tnfgas.InfNfgas.Total.VRetTribTot = field(
                metadata={
                    "name": "vRetTribTot",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                }
            )
            v_cofins: str = field(
                metadata={
                    "name": "vCOFINS",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            v_pis: str = field(
                metadata={
                    "name": "vPIS",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            v_tx_reg: str = field(
                metadata={
                    "name": "vTxReg",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            v_nf: str = field(
                metadata={
                    "name": "vNF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            ibscbstot: Tibscbstot = field(
                metadata={
                    "name": "IBSCBSTot",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                }
            )
            v_tot_dfe: str = field(
                metadata={
                    "name": "vTotDFe",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )

            @dataclass(kw_only=True)
            class Icmstot:
                """
                :ivar v_bc: BC do ICMS
                :ivar v_icms: Valor Total do ICMS
                :ivar v_icmsdeson: Valor Total do ICMS desonerado
                :ivar v_fcp: Valor Total do FCP (Fundo de Combate à
                    Pobreza).
                :ivar v_bcst: BC do ICMS ST
                :ivar v_st: Valor Total do ICMS ST
                :ivar v_fcpst: Valor Total do FCP (Fundo de Combate à
                    Pobreza) retido por substituição tributária.
                """

                v_bc: str = field(
                    metadata={
                        "name": "vBC",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_icms: str = field(
                    metadata={
                        "name": "vICMS",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_icmsdeson: str = field(
                    metadata={
                        "name": "vICMSDeson",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_fcp: str = field(
                    metadata={
                        "name": "vFCP",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_bcst: str = field(
                    metadata={
                        "name": "vBCST",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_st: str = field(
                    metadata={
                        "name": "vST",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_fcpst: str = field(
                    metadata={
                        "name": "vFCPST",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
                        "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_ret_cofins: str = field(
                    metadata={
                        "name": "vRetCofins",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_ret_csll: str = field(
                    metadata={
                        "name": "vRetCSLL",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_irrf: str = field(
                    metadata={
                        "name": "vIRRF",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
                AAAA-MM-DD
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
            :ivar inf_ad_fat: Informações adicionais de faturamento
            """

            compet_fat: str = field(
                metadata={
                    "name": "CompetFat",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "white_space": "preserve",
                    "pattern": r"((((20|19|18)(([02468][048])|([13579][26]))-02-29))|((20|19|18)[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                }
            )
            d_apres_fat: None | str = field(
                default=None,
                metadata={
                    "name": "dApresFat",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "white_space": "preserve",
                    "pattern": r"((((20|19|18)(([02468][048])|([13579][26]))-02-29))|((20|19|18)[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                },
            )
            d_prox_leitura: str = field(
                metadata={
                    "name": "dProxLeitura",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "white_space": "preserve",
                    "pattern": r"((((20|19|18)(([02468][048])|([13579][26]))-02-29))|((20|19|18)[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                }
            )
            n_fat: None | str = field(
                default=None,
                metadata={
                    "name": "nFat",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                },
            )
            g_pix: None | Tnfgas.InfNfgas.GFat.GPix = field(
                default=None,
                metadata={
                    "name": "gPIX",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                },
            )
            inf_ad_fat: None | str = field(
                default=None,
                metadata={
                    "name": "infAdFat",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "min_length": 1,
                    "max_length": 5000,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
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
                        "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        "min_length": 2,
                        "max_length": 2000,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )

        @dataclass(kw_only=True)
        class GAgencia:
            """
            :ivar nome_agencia_atend: Nome da Agencia responsável pelo
                atendimento
            :ivar ender_agencia_atend: Endereço da Agencia responsável
                pelo atendimento
            :ivar sitio_agencia_atend: Sítio eletrônico da Agencia
            :ivar g_hist_cons: Histórico de Consumo
            :ivar inf_ad_reg: Informações adicionais de interesse das
                agencias reguladoras Norma referenciada, informações
                complementares, etc
            """

            nome_agencia_atend: None | str = field(
                default=None,
                metadata={
                    "name": "nomeAgenciaAtend",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                },
            )
            ender_agencia_atend: None | str = field(
                default=None,
                metadata={
                    "name": "enderAgenciaAtend",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "min_length": 2,
                    "max_length": 200,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                },
            )
            sitio_agencia_atend: None | str = field(
                default=None,
                metadata={
                    "name": "sitioAgenciaAtend",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "min_length": 2,
                    "max_length": 200,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                },
            )
            g_hist_cons: list[Tnfgas.InfNfgas.GAgencia.GHistCons] = field(
                default_factory=list,
                metadata={
                    "name": "gHistCons",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "min_occurs": 1,
                    "max_occurs": 5,
                },
            )
            inf_ad_reg: None | str = field(
                default=None,
                metadata={
                    "name": "infAdReg",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "min_length": 1,
                    "max_length": 5000,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
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
                        "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        "min_length": 2,
                        "max_length": 60,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                g_cons: list[Tnfgas.InfNfgas.GAgencia.GHistCons.GCons] = field(
                    default_factory=list,
                    metadata={
                        "name": "gCons",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        "min_occurs": 1,
                        "max_occurs": 13,
                    },
                )
                med_mensal: str = field(
                    metadata={
                        "name": "medMensal",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{1,13}(\.[0-9]{2,4})?",
                    }
                )

                @dataclass(kw_only=True)
                class GCons:
                    """
                    :ivar compet_fat: Ano e mês referência do
                        faturamento (AAAAMM)
                    :ivar u_med: Unidade Básica de Medida 1 - m3
                    :ivar qtd_dias: Quantidade de dias de medição
                    :ivar med_diaria: Média Diária de consumo
                    :ivar consumo: Consumo no mês
                    :ivar v_fat: Valor Faturado
                    """

                    compet_fat: str = field(
                        metadata={
                            "name": "CompetFat",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                            "min_length": 6,
                            "max_length": 6,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1,6}",
                        }
                    )
                    u_med: Tumed = field(
                        metadata={
                            "name": "uMed",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                        }
                    )
                    qtd_dias: str = field(
                        metadata={
                            "name": "qtdDias",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                            "white_space": "preserve",
                            "pattern": r"[0-9]{2}",
                        }
                    )
                    med_diaria: None | str = field(
                        default=None,
                        metadata={
                            "name": "medDiaria",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1,13}(\.[0-9]{2,4})?",
                        },
                    )
                    consumo: None | str = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1,13}(\.[0-9]{2,4})?",
                        },
                    )
                    v_fat: str = field(
                        metadata={
                            "name": "vFat",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfgas",
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1,13}(\.[0-9]{2,4})?",
                        }
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
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "white_space": "preserve",
                    "pattern": r"[A-Z0-9]{12}[0-9]{2}",
                },
            )
            cpf: None | str = field(
                default=None,
                metadata={
                    "name": "CPF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
                    "namespace": "http://www.portalfiscal.inf.br/nfgas",
                    "max_occurs": 5,
                    "min_length": 1,
                    "max_length": 3000,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                },
            )

    @dataclass(kw_only=True)
    class InfNfgasSupl:
        """
        :ivar qr_cod_nfgas: Texto com o QR-Code para consulta da NFGas
        """

        qr_cod_nfgas: str = field(
            metadata={
                "name": "qrCodNFGas",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfgas",
                "min_length": 50,
                "max_length": 1000,
                "white_space": "preserve",
                "pattern": r"((HTTPS?|https?)://.*\?chNFGas=[0-9]{6}[A-Z0-9]{12}[0-9]{26}&tpAmb=[1-2](&sign=[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1})?)",
            }
        )


@dataclass(kw_only=True)
class TretNfgas:
    """
    Tipo Retorno do Pedido de Autorização de NFGas.

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
        Homologação
    :ivar c_uf: Identificação da UF
    :ivar ver_aplic: Versão do Aplicativo que processou a NFGas
    :ivar c_stat: código do status do retorno da consulta.
    :ivar x_motivo: Descrição literal do status do do retorno da
        consulta.
    :ivar prot_nfgas: Reposta ao processamento da NFGas
    :ivar versao:
    """

    class Meta:
        name = "TRetNFGas"

    tp_amb: Tamb = field(
        metadata={
            "name": "tpAmb",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
        }
    )
    c_uf: TcodUfIbge = field(
        metadata={
            "name": "cUF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
        }
    )
    ver_aplic: str = field(
        metadata={
            "name": "verAplic",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
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
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
            "white_space": "preserve",
            "pattern": r"[0-9]{3,4}",
        }
    )
    x_motivo: str = field(
        metadata={
            "name": "xMotivo",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    prot_nfgas: None | TprotNfgas = field(
        default=None,
        metadata={
            "name": "protNFGas",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
        },
    )
    versao: str = field(
        metadata={
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"1\.00",
        }
    )
