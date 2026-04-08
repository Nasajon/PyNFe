from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from pynfe_nasajon.pynfe.utils.nfgas.tipos_geral_nfgas_v1_00 import (
    Tamb,
    TcodUfIbge,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfgas"


class ProcEventoNfgasVersao(Enum):
    VALUE_1_00 = "1.00"


class ProtNfgasVersao(Enum):
    VALUE_1_00 = "1.00"


@dataclass(kw_only=True)
class TconsSitNfgas:
    """
    Tipo Pedido de Consulta da Situação Atual da NFGas.

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção; 2 -
        Homologação;
    :ivar x_serv: Serviço Solicitado
    :ivar ch_nfgas: Chaves de acesso da NFGas
    :ivar versao:
    """

    class Meta:
        name = "TConsSitNFGas"

    tp_amb: Tamb = field(
        metadata={
            "name": "tpAmb",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
        }
    )
    x_serv: str = field(
        init=False,
        default="CONSULTAR",
        metadata={
            "name": "xServ",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        },
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
    versao: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"1\.00",
        }
    )


@dataclass(kw_only=True)
class TretConsSitNfgas:
    """
    Tipo Retorno de Pedido de Consulta da Situação Atual de NFGas.

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
        Homologação
    :ivar ver_aplic: Versão do Aplicativo que processou o NF-3e
    :ivar c_stat: Código do status da mensagem enviada.
    :ivar x_motivo: Descrição literal do status do serviço solicitado.
    :ivar c_uf: código da UF de atendimento
    :ivar prot_nfgas:
    :ivar proc_evento_nfgas:
    :ivar versao:
    """

    class Meta:
        name = "TRetConsSitNFGas"

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
    c_uf: TcodUfIbge = field(
        metadata={
            "name": "cUF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
        }
    )
    prot_nfgas: None | TretConsSitNfgas.ProtNfgas = field(
        default=None,
        metadata={
            "name": "protNFGas",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
        },
    )
    proc_evento_nfgas: list[TretConsSitNfgas.ProcEventoNfgas] = field(
        default_factory=list,
        metadata={
            "name": "procEventoNFGas",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfgas",
        },
    )
    versao: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"1\.00",
        }
    )

    @dataclass(kw_only=True)
    class ProtNfgas:
        """
        :ivar any_element: Retornar protNF3e da versão correspondente da
            NFGas autorizada
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
        versao: ProtNfgasVersao = field(
            metadata={
                "type": "Attribute",
                "white_space": "preserve",
            }
        )

    @dataclass(kw_only=True)
    class ProcEventoNfgas:
        """
        :ivar any_element: Retornar procEventoNFGas da versão
            correspondente do evento NFGas autorizado
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
        versao: ProcEventoNfgasVersao = field(
            metadata={
                "type": "Attribute",
                "white_space": "preserve",
            }
        )
