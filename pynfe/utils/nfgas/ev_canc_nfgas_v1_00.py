from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfgas"


class EvCancNfgasDescEvento(Enum):
    CANCELAMENTO = "Cancelamento"


@dataclass(kw_only=True)
class EvCancNfgas:
    """
    Schema XML de validação do evento do cancelamento 110111.

    :ivar desc_evento: Descrição do Evento - “Cancelamento”
    :ivar n_prot: Número do Protocolo de Status da NFGas.
    :ivar x_just: Justificativa do Cancelamento
    """

    class Meta:
        name = "evCancNFGas"
        namespace = "http://www.portalfiscal.inf.br/nfgas"

    desc_evento: EvCancNfgasDescEvento = field(
        metadata={
            "name": "descEvento",
            "type": "Element",
            "white_space": "preserve",
        }
    )
    n_prot: str = field(
        metadata={
            "name": "nProt",
            "type": "Element",
            "white_space": "preserve",
            "pattern": r"[0-9]{16}",
        }
    )
    x_just: str = field(
        metadata={
            "name": "xJust",
            "type": "Element",
            "min_length": 15,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
