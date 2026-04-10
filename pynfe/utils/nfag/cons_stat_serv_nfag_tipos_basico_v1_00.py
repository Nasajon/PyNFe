from __future__ import annotations

from dataclasses import dataclass, field

from pynfe_nasajon.pynfe.utils.nfag.tipos_geral_nfag_v1_00 import (
    Tamb,
    TcodUfIbge,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfag"


@dataclass(kw_only=True)
class TconsStatServ:
    """
    Tipo Pedido de Consulta do Status do Serviço NFAg.

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
        Homologação
    :ivar x_serv: Serviço Solicitado
    :ivar versao:
    """

    class Meta:
        name = "TConsStatServ"

    tp_amb: Tamb = field(
        metadata={
            "name": "tpAmb",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        }
    )
    x_serv: str = field(
        init=False,
        default="STATUS",
        metadata={
            "name": "xServ",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        },
    )
    versao: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"1\.00",
        }
    )


@dataclass(kw_only=True)
class TretConsStatServ:
    """
    Tipo Resultado da Consulta do Status do Serviço NFAg.

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
        Homologação
    :ivar ver_aplic: Versão do Aplicativo que processou a NFAg
    :ivar c_stat: Código do status da mensagem enviada.
    :ivar x_motivo: Descrição literal do status do serviço solicitado.
    :ivar c_uf: Código da UF responsável pelo serviço
    :ivar dh_recbto: AAAA-MM-DDTHH:MM:SS TZD
    :ivar t_med: Tempo médio de resposta do serviço (em segundos) dos
        últimos 5 minutos
    :ivar dh_retorno: AAAA-MM-DDTHH:MM:SS TZD. Deve ser preenchida com
        data e hora previstas para o retorno dos serviços prestados.
    :ivar x_obs: Campo observação utilizado para incluir informações ao
        contribuinte
    :ivar versao:
    """

    class Meta:
        name = "TRetConsStatServ"

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
            "white_space": "collapse",
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
    c_uf: TcodUfIbge = field(
        metadata={
            "name": "cUF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
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
    t_med: None | str = field(
        default=None,
        metadata={
            "name": "tMed",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "pattern": r"[0-9]{1,4}",
        },
    )
    dh_retorno: None | str = field(
        default=None,
        metadata={
            "name": "dhRetorno",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
        },
    )
    x_obs: None | str = field(
        default=None,
        metadata={
            "name": "xObs",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        },
    )
    versao: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"1\.00",
        }
    )
