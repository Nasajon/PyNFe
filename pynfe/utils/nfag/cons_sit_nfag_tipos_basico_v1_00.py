from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from pynfe_nasajon.pynfe.utils.nfag.tipos_geral_nfag_v1_00 import (
    Tamb,
    TcodUfIbge,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfag"


class ProcEventoNfagVersao(Enum):
    VALUE_1_00 = "1.00"


class ProtNfagVersao(Enum):
    VALUE_1_00 = "1.00"


@dataclass(kw_only=True)
class TconsSitNfag:
    """
    Tipo Pedido de Consulta da Situação Atual da NFAg.

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção; 2 -
        Homologação;
    :ivar x_serv: Serviço Solicitado
    :ivar ch_nfag: Chaves de acesso da NFAg
    :ivar versao:
    """

    class Meta:
        name = "TConsSitNFAg"

    tp_amb: Tamb = field(
        metadata={
            "name": "tpAmb",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        }
    )
    x_serv: str = field(
        init=False,
        default="CONSULTAR",
        metadata={
            "name": "xServ",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        },
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
    versao: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"1\.00",
        }
    )


@dataclass(kw_only=True)
class TretConsSitNfag:
    """
    Tipo Retorno de Pedido de Consulta da Situação Atual de NFAg.

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
        Homologação
    :ivar ver_aplic: Versão do Aplicativo que processou o NF-3e
    :ivar c_stat: Código do status da mensagem enviada.
    :ivar x_motivo: Descrição literal do status do serviço solicitado.
    :ivar c_uf: código da UF de atendimento
    :ivar prot_nfag:
    :ivar proc_evento_nfag:
    :ivar versao:
    """

    class Meta:
        name = "TRetConsSitNFAg"

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
    prot_nfag: None | TretConsSitNfag.ProtNfag = field(
        default=None,
        metadata={
            "name": "protNFAg",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    proc_evento_nfag: list[TretConsSitNfag.ProcEventoNfag] = field(
        default_factory=list,
        metadata={
            "name": "procEventoNFAg",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    versao: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"1\.00",
        }
    )

    @dataclass(kw_only=True)
    class ProtNfag:
        """
        :ivar any_element: Retornar protNF3e da versão correspondente da
            NFAg autorizada
        :ivar versao:
        """

        any_element: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "process_contents": "skip",
            },
        )
        versao: ProtNfagVersao = field(
            metadata={
                "type": "Attribute",
                "white_space": "preserve",
            }
        )

    @dataclass(kw_only=True)
    class ProcEventoNfag:
        """
        :ivar any_element: Retornar procEventoNFAg da versão
            correspondente do evento NFAg autorizado
        :ivar versao:
        """

        any_element: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "process_contents": "skip",
            },
        )
        versao: ProcEventoNfagVersao = field(
            metadata={
                "type": "Attribute",
                "white_space": "preserve",
            }
        )
