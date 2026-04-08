from __future__ import annotations

from dataclasses import dataclass

from pynfe_nasajon.pynfe.utils.nfgas.evento_nfgas_tipos_basico_v1_00 import (
    Tevento,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfgas"


@dataclass(kw_only=True)
class EventoNfgas(Tevento):
    """
    Schema XML de validação do Pedido de Registro de Evento da NFGas.
    """

    class Meta:
        name = "eventoNFGas"
        namespace = "http://www.portalfiscal.inf.br/nfgas"
