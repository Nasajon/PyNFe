from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfag"


class Tamb(Enum):
    """
    Tipo Ambiente.
    """

    VALUE_1 = "1"
    VALUE_2 = "2"


class TcorgaoIbge(Enum):
    """
    Tipo Código de orgão (UF da tabela do IBGE + 90 SUFRAMA + 91 RFB + 92
    BRId).
    """

    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_17 = "17"
    VALUE_21 = "21"
    VALUE_22 = "22"
    VALUE_23 = "23"
    VALUE_24 = "24"
    VALUE_25 = "25"
    VALUE_26 = "26"
    VALUE_27 = "27"
    VALUE_28 = "28"
    VALUE_29 = "29"
    VALUE_31 = "31"
    VALUE_32 = "32"
    VALUE_33 = "33"
    VALUE_35 = "35"
    VALUE_41 = "41"
    VALUE_42 = "42"
    VALUE_43 = "43"
    VALUE_50 = "50"
    VALUE_51 = "51"
    VALUE_52 = "52"
    VALUE_53 = "53"
    VALUE_90 = "90"
    VALUE_91 = "91"
    VALUE_92 = "92"
    VALUE_93 = "93"


@dataclass(kw_only=True)
class TchDfe:
    """
    Tipo Chave de Documento Fiscal Eletrônico.
    """

    class Meta:
        name = "TChDFe"

    value: str = field(
        default="",
        metadata={
            "max_length": 44,
            "white_space": "preserve",
            "pattern": r"[0-9]{6}[A-Z0-9]{12}[0-9]{26}",
        },
    )


@dataclass(kw_only=True)
class Tcnpj:
    """
    Tipo Número do CNPJ.
    """

    class Meta:
        name = "TCnpj"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"[A-Z0-9]{12}[0-9]{2}",
        },
    )


@dataclass(kw_only=True)
class TcnpjOpc:
    """
    Tipo Número do CNPJ Opcional.
    """

    class Meta:
        name = "TCnpjOpc"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"[0-9]{0}|[A-Z0-9]{12}[0-9]{2}",
        },
    )


@dataclass(kw_only=True)
class TcodMunIbge:
    """
    Tipo Código do Município da tabela do IBGE.
    """

    class Meta:
        name = "TCodMunIBGE"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        },
    )


class TcodUfIbge(Enum):
    """
    Tipo Código da UF da tabela do IBGE.
    """

    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_17 = "17"
    VALUE_21 = "21"
    VALUE_22 = "22"
    VALUE_23 = "23"
    VALUE_24 = "24"
    VALUE_25 = "25"
    VALUE_26 = "26"
    VALUE_27 = "27"
    VALUE_28 = "28"
    VALUE_29 = "29"
    VALUE_31 = "31"
    VALUE_32 = "32"
    VALUE_33 = "33"
    VALUE_35 = "35"
    VALUE_41 = "41"
    VALUE_42 = "42"
    VALUE_43 = "43"
    VALUE_50 = "50"
    VALUE_51 = "51"
    VALUE_52 = "52"
    VALUE_53 = "53"


class TcodUfIbgeEx(Enum):
    """
    Tipo Código da UF da tabela do IBGE + 99 para Exterior.
    """

    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_17 = "17"
    VALUE_21 = "21"
    VALUE_22 = "22"
    VALUE_23 = "23"
    VALUE_24 = "24"
    VALUE_25 = "25"
    VALUE_26 = "26"
    VALUE_27 = "27"
    VALUE_28 = "28"
    VALUE_29 = "29"
    VALUE_31 = "31"
    VALUE_32 = "32"
    VALUE_33 = "33"
    VALUE_35 = "35"
    VALUE_41 = "41"
    VALUE_42 = "42"
    VALUE_43 = "43"
    VALUE_50 = "50"
    VALUE_51 = "51"
    VALUE_52 = "52"
    VALUE_53 = "53"
    VALUE_99 = "99"


@dataclass(kw_only=True)
class Tcpf:
    """
    Tipo Número do CPF.
    """

    class Meta:
        name = "TCpf"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"[0-9]{11}",
        },
    )


@dataclass(kw_only=True)
class TcpfVar:
    """
    Tipo Número do CPF de tamanho variável (3-11).
    """

    class Meta:
        name = "TCpfVar"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"[0-9]{3,11}",
        },
    )


@dataclass(kw_only=True)
class Tdata:
    """
    Tipo data AAAA-MM-DD.
    """

    class Meta:
        name = "TData"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"((((20|19|18)(([02468][048])|([13579][26]))-02-29))|((20|19|18)[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
        },
    )


@dataclass(kw_only=True)
class TdateTimeUtc:
    """
    Data e Hora, formato UTC (AAAA-MM-DDThh:mm:ssTZD, onde TZD = +hh:mm ou
    -hh:mm).
    """

    class Meta:
        name = "TDateTimeUTC"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
        },
    )


@dataclass(kw_only=True)
class Tdec0302:
    """
    Tipo Decimal com 5 dígitos, sendo 3 inteiros e 2 decimais.
    """

    class Meta:
        name = "TDec_0302"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        },
    )


@dataclass(kw_only=True)
class Tdec0302Opc:
    """
    Tipo Decimal com 5 dígitos, sendo 3 inteiros e 2 decimais, utilizado em
    tags opcionais.
    """

    class Meta:
        name = "TDec_0302Opc"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        },
    )


@dataclass(kw_only=True)
class Tdec03020303:
    """
    Tipo Decimal com 6 ou 5 dígitos, sendo 3 inteiros e 3 ou 2 decimais.
    """

    class Meta:
        name = "TDec_0302_0303"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"[0-9]{1,3}(\.[0-9]{2,3})?",
        },
    )


@dataclass(kw_only=True)
class Tdec0302A04:
    """
    Tipo Decimal com até 3 dígitos inteiros, podendo ter de 2 até 4
    decimais.
    """

    class Meta:
        name = "TDec_0302a04"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
        },
    )


@dataclass(kw_only=True)
class Tdec0302A04Max100:
    """
    Tipo Decimal com 3 inteiros (no máximo 100), com até 4 decimais.
    """

    class Meta:
        name = "TDec_0302a04Max100"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"0(\.[0-9]{2,4})?|[1-9]{1}[0-9]{0,1}(\.[0-9]{2,4})?|100(\.0{2,4})?",
        },
    )


@dataclass(kw_only=True)
class Tdec0302A04Opc:
    """
    Tipo Decimal com até 3 dígitos inteiros e 2 até 4 decimais.

    Utilizados em TAGs opcionais, não aceita valor zero.
    """

    class Meta:
        name = "TDec_0302a04Opc"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
        },
    )


@dataclass(kw_only=True)
class Tdec0303:
    """
    Tipo Decimal com 6 dígitos, sendo 3 inteiros e 3 decimais.
    """

    class Meta:
        name = "TDec_0303"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{3}|[1-9]{1}[0-9]{0,2}(\.[0-9]{3})?",
        },
    )


@dataclass(kw_only=True)
class Tdec0303Opc:
    """
    Tipo Decimal com 6 dígitos, sendo 3 inteiros e 3 decimais usado em tags
    opcionais.
    """

    class Meta:
        name = "TDec_0303Opc"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"0\.[0-9]{3}|[1-9]{1}[0-9]{0,2}(\.[0-9]{3})?",
        },
    )


@dataclass(kw_only=True)
class Tdec04020408:
    """
    Tipo Decimal com 4 dígitos inteiros e 2 a 8 casas decimais.
    """

    class Meta:
        name = "TDec_0402_0408"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"[0-9]{1,4}(\.[0-9]{2,8})?",
        },
    )


@dataclass(kw_only=True)
class Tdec0503:
    """
    Tipo Decimal com 8 dígitos, sendo 5 inteiros e 3 decimais.
    """

    class Meta:
        name = "TDec_0503"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{3}|[1-9]{1}[0-9]{0,4}(\.[0-9]{3})?",
        },
    )


@dataclass(kw_only=True)
class Tdec0803:
    """
    Tipo Decimal com 11 dígitos, sendo 8 inteiros e 3 decimais.
    """

    class Meta:
        name = "TDec_0803"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{3}|[1-9]{1}[0-9]{0,7}(\.[0-9]{3})?",
        },
    )


@dataclass(kw_only=True)
class Tdec0803Opc:
    """
    Tipo Decimal com 11 dígitos, sendo 8 inteiros e 3 decimais utilizado em
    tags opcionais.
    """

    class Meta:
        name = "TDec_0803Opc"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"0\.[0-9]{3}|[1-9]{1}[0-9]{0,7}(\.[0-9]{3})?",
        },
    )


@dataclass(kw_only=True)
class Tdec0804:
    """
    Tipo Decimal com 12 dígitos, sendo 8 inteiros e 4 decimais.
    """

    class Meta:
        name = "TDec_0804"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,7}(\.[0-9]{4})?",
        },
    )


@dataclass(kw_only=True)
class Tdec0804Opc:
    """
    Tipo Decimal com 12 dígitos, sendo 8 inteiros e 4 decimais, utilizado
    em tags opcionais.
    """

    class Meta:
        name = "TDec_0804Opc"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"0\.[0-9]{4}|[1-9]{1}[0-9]{0,7}(\.[0-9]{4})?",
        },
    )


@dataclass(kw_only=True)
class Tdec0906:
    """
    Tipo Decimal com 15 dígitos, sendo 9 inteiros e 6 decimais.
    """

    class Meta:
        name = "TDec_0906"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{6}|[1-9]{1}[0-9]{0,8}(\.[0-9]{6})?",
        },
    )


@dataclass(kw_only=True)
class Tdec0906Opc:
    """
    Tipo Decimal com 15 dígitos, sendo 9 inteiros e 6 decimais, utilizado
    em tags opcionais.
    """

    class Meta:
        name = "TDec_0906Opc"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"0\.[0-9]{6}|[1-9]{1}[0-9]{0,8}(\.[0-9]{6})?",
        },
    )


@dataclass(kw_only=True)
class Tdec0908:
    """
    Tipo Decimal com 15 dígitos, sendo 9 inteiros e 8 decimais.
    """

    class Meta:
        name = "TDec_0908"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{8}|[1-9]{1}[0-9]{0,8}(\.[0-9]{8})?",
        },
    )


@dataclass(kw_only=True)
class Tdec0908Opc:
    """
    Tipo Decimal com 15 dígitos, sendo 9 inteiros e 8 decimais, utilizado
    em tags opcionais.
    """

    class Meta:
        name = "TDec_0908Opc"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"0\.[0-9]{8}|[1-9]{1}[0-9]{0,8}(\.[0-9]{8})?",
        },
    )


@dataclass(kw_only=True)
class Tdec11001104:
    """
    Tipo Decimal com 11 dígitos inteiros e 0 a 4 casas decimais.
    """

    class Meta:
        name = "TDec_1100_1104"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"[0-9]{1,11}(\.[0-9]{2,4})?",
        },
    )


@dataclass(kw_only=True)
class Tdec1104:
    """
    Tipo Decimal com 15 dígitos, sendo 11 inteiros e 4 decimais.
    """

    class Meta:
        name = "TDec_1104"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})?",
        },
    )


@dataclass(kw_only=True)
class Tdec1104Opc:
    """
    Tipo Decimal com 15 dígitos, sendo 11 inteiros e 4 decimais, utilizado
    em tags opcionais.
    """

    class Meta:
        name = "TDec_1104Opc"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"0\.[0-9]{4}|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})?",
        },
    )


@dataclass(kw_only=True)
class Tdec1203:
    """
    Tipo Decimal com 15 dígitos, sendo 12 inteiros e 3 decimais.
    """

    class Meta:
        name = "TDec_1203"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{3}|[1-9]{1}[0-9]{0,11}(\.[0-9]{3})?",
        },
    )


@dataclass(kw_only=True)
class Tdec1203Opc:
    """
    Tipo Decimal com 15 dígitos, sendo 12 inteiros e 3 decimais, utilizado
    em tags opcionais.
    """

    class Meta:
        name = "TDec_1203Opc"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"0\.[0-9]{3}|[1-9]{1}[0-9]{0,11}(\.[0-9]{3})?",
        },
    )


@dataclass(kw_only=True)
class Tdec1204:
    """
    Tipo Decimal com 16 dígitos, sendo 12 de corpo e 4 decimais.
    """

    class Meta:
        name = "TDec_1204"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,11}(\.[0-9]{4})?",
        },
    )


@dataclass(kw_only=True)
class Tdec1204Opc:
    """
    Tipo Decimal com 16 dígitos, sendo 12 inteiros e 4 decimais, utilizado
    em tags opcionais.
    """

    class Meta:
        name = "TDec_1204Opc"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"0\.[0-9]{4}|[1-9]{1}[0-9]{0,11}(\.[0-9]{4})?",
        },
    )


@dataclass(kw_only=True)
class Tdec1302:
    """
    Tipo Decimal com 15 dígitos, sendo 13 inteiros e 2 decimais.
    """

    class Meta:
        name = "TDec_1302"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )


@dataclass(kw_only=True)
class Tdec1302Opc:
    """
    Tipo Decimal com 15 dígitos, sendo 13 inteiros e 2 decimais, utilizado
    em tags opcionais.
    """

    class Meta:
        name = "TDec_1302Opc"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )


@dataclass(kw_only=True)
class Tdec13021304:
    """
    Tipo Decimal com 13 dígitos inteiros e 2 a 4 casas decimais.
    """

    class Meta:
        name = "TDec_1302_1304"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"[0-9]{1,13}(\.[0-9]{2,4})?",
        },
    )


@dataclass(kw_only=True)
class Tdec13021306:
    """
    Tipo Decimal com 13 dígitos inteiros e 2 a 6 casas decimais.
    """

    class Meta:
        name = "TDec_1302_1306"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"[0-9]{1,13}(\.[0-9]{2,6})?",
        },
    )


@dataclass(kw_only=True)
class Tdec13021308:
    """
    Tipo Decimal com 13 dígitos inteiros e 2 a 8 casas decimais.
    """

    class Meta:
        name = "TDec_1302_1308"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"[0-9]{1,13}(\.[0-9]{2,8})?",
        },
    )


@dataclass(kw_only=True)
class Tdec13021310:
    """
    Tipo Decimal com 13 dígitos inteiros e 2 a 10 casas decimais.
    """

    class Meta:
        name = "TDec_1302_1310"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"[0-9]{1,13}(\.[0-9]{2,10})?",
        },
    )


@dataclass(kw_only=True)
class Tipv4:
    """
    Tipo IP versão 4.
    """

    class Meta:
        name = "TIPv4"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])",
        },
    )


@dataclass(kw_only=True)
class Tie:
    """
    Tipo Inscrição Estadual do Emitente.
    """

    class Meta:
        name = "TIe"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"[0-9]{2,14}",
        },
    )


@dataclass(kw_only=True)
class TieDest:
    """
    Tipo Inscrição Estadual do Destinatário.
    """

    class Meta:
        name = "TIeDest"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"[0-9]{0,14}|ISENTO",
        },
    )


@dataclass(kw_only=True)
class Tjust:
    """
    Tipo Justificativa.
    """

    class Meta:
        name = "TJust"

    value: str = field(
        default="",
        metadata={
            "min_length": 15,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        },
    )


@dataclass(kw_only=True)
class Tlatitude:
    """
    Coordenada geográfica Latitude.
    """

    class Meta:
        name = "TLatitude"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"[0-9]\.[0-9]{6}|[1-8][0-9]\.[0-9]{6}|90\.[0-9]{6}|-[0-9]\.[0-9]{6}|-[1-8][0-9]\.[0-9]{6}|-90\.[0-9]{6}",
        },
    )


@dataclass(kw_only=True)
class Tlongitude:
    """
    Coordenada geográfica Longitude.
    """

    class Meta:
        name = "TLongitude"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"[0-9]\.[0-9]{6}|[1-9][0-9]\.[0-9]{6}|1[0-7][0-9]\.[0-9]{6}|180\.[0-9]{6}|-[0-9]\.[0-9]{6}|-[1-9][0-9]\.[0-9]{6}|-1[0-7][0-9]\.[0-9]{6}|-180\.[0-9]{6}",
        },
    )


@dataclass(kw_only=True)
class Tmed:
    """
    Tipo temp médio em segundos.
    """

    class Meta:
        name = "TMed"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"[0-9]{1,4}",
        },
    )


class TmodNfag(Enum):
    """
    Tipo Modelo NFAg.
    """

    VALUE_75 = "75"


@dataclass(kw_only=True)
class Tmotivo:
    """
    Tipo Motivo.
    """

    class Meta:
        name = "TMotivo"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        },
    )


@dataclass(kw_only=True)
class Tnf:
    """
    Tipo Número do Documento Fiscal.
    """

    class Meta:
        name = "TNF"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"[1-9]{1}[0-9]{0,8}",
        },
    )


@dataclass(kw_only=True)
class Tnsu:
    """
    Tipo número sequencial único do AN.
    """

    class Meta:
        name = "TNSU"

    value: str = field(
        default="",
        metadata={
            "pattern": r"[0-9]{15}",
        },
    )


@dataclass(kw_only=True)
class Tprot:
    """
    Tipo Número do Protocolo de Status.
    """

    class Meta:
        name = "TProt"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"[0-9]{16}",
        },
    )


@dataclass(kw_only=True)
class Trec:
    """
    Tipo Número do Recibo do envio de lote de DF-e.
    """

    class Meta:
        name = "TRec"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"[0-9]{16}",
        },
    )


@dataclass(kw_only=True)
class TsegCodBarra:
    """
    Tipo Segundo Codigo Barra.
    """

    class Meta:
        name = "TSegCodBarra"

    value: str = field(
        default="",
        metadata={
            "pattern": r"[0-9]{36}",
        },
    )


@dataclass(kw_only=True)
class Tserie:
    """
    Tipo Série do Documento Fiscal.
    """

    class Meta:
        name = "TSerie"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"0|[1-9]{1}[0-9]{0,2}",
        },
    )


@dataclass(kw_only=True)
class Tserv:
    """
    Tipo Serviço solicitado.
    """

    class Meta:
        name = "TServ"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        },
    )


@dataclass(kw_only=True)
class Tstat:
    """
    Tipo Código da Mensagem enviada.
    """

    class Meta:
        name = "TStat"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"[0-9]{3,4}",
        },
    )


@dataclass(kw_only=True)
class Tstring:
    """
    Tipo string genérico.
    """

    class Meta:
        name = "TString"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        },
    )


class Tuf(Enum):
    """
    Tipo Sigla da UF.
    """

    AC = "AC"
    AL = "AL"
    AM = "AM"
    AP = "AP"
    BA = "BA"
    CE = "CE"
    DF = "DF"
    ES = "ES"
    GO = "GO"
    MA = "MA"
    MG = "MG"
    MS = "MS"
    MT = "MT"
    PA = "PA"
    PB = "PB"
    PE = "PE"
    PI = "PI"
    PR = "PR"
    RJ = "RJ"
    RN = "RN"
    RO = "RO"
    RR = "RR"
    RS = "RS"
    SC = "SC"
    SE = "SE"
    SP = "SP"
    TO = "TO"
    EX = "EX"


class TufSemEx(Enum):
    """
    Tipo Sigla da UF - Sem Exterior.
    """

    AC = "AC"
    AL = "AL"
    AM = "AM"
    AP = "AP"
    BA = "BA"
    CE = "CE"
    DF = "DF"
    ES = "ES"
    GO = "GO"
    MA = "MA"
    MG = "MG"
    MS = "MS"
    MT = "MT"
    PA = "PA"
    PB = "PB"
    PE = "PE"
    PI = "PI"
    PR = "PR"
    RJ = "RJ"
    RN = "RN"
    RO = "RO"
    RR = "RR"
    RS = "RS"
    SC = "SC"
    SE = "SE"
    SP = "SP"
    TO = "TO"


@dataclass(kw_only=True)
class TverAplic:
    """
    Tipo Versão do Aplicativo.
    """

    class Meta:
        name = "TVerAplic"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
            "max_length": 20,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        },
    )


@dataclass(kw_only=True)
class Tano:
    """
    Tipo ano.
    """

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"[0-9]{2}",
        },
    )
