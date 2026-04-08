from __future__ import annotations

from dataclasses import dataclass

from pynfe_nasajon.pynfe.utils.nfgas.evento_nfgas_tipos_basico_v1_00 import (
    TprocEvento,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfgas"


@dataclass(kw_only=True)
class ProcEventoNfgas(TprocEvento):
    """
    Pedido de Registro de Evento de NFGas processado.
    """

    class Meta:
        name = "procEventoNFGas"
        namespace = "http://www.portalfiscal.inf.br/nfgas"
