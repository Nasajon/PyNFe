from __future__ import annotations

from dataclasses import dataclass

from pynfe_nasajon.pynfe.utils.nfag.evento_nfag_tipos_basico_v1_00 import (
    TprocEvento,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfag"


@dataclass(kw_only=True)
class ProcEventoNfag(TprocEvento):
    """
    Pedido de Registro de Evento de NFAg processado.
    """

    class Meta:
        name = "procEventoNFAg"
        namespace = "http://www.portalfiscal.inf.br/nfag"
