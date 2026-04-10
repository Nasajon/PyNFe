from __future__ import annotations

from dataclasses import dataclass

from pynfe_nasajon.pynfe.utils.nfag.evento_nfag_tipos_basico_v1_00 import (
    TretEvento,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfag"


@dataclass(kw_only=True)
class RetEventoNfag(TretEvento):
    """
    Schema XML de validação do retorno Pedido de Evento da NFAg.
    """

    class Meta:
        name = "retEventoNFAg"
        namespace = "http://www.portalfiscal.inf.br/nfag"
