from __future__ import annotations

from dataclasses import dataclass

from pynfe_nasajon.pynfe.utils.nfag.evento_nfag_tipos_basico_v1_00 import (
    Tevento,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfag"


@dataclass(kw_only=True)
class EventoNfag(Tevento):
    """
    Schema XML de validação do Pedido de Registro de Evento da NFAg.
    """

    class Meta:
        name = "eventoNFAg"
        namespace = "http://www.portalfiscal.inf.br/nfag"
