from __future__ import annotations

from dataclasses import dataclass

from pynfe_nasajon.pynfe.utils.nfgas.evento_nfgas_tipos_basico_v1_00 import (
    TretEvento,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfgas"


@dataclass(kw_only=True)
class RetEventoNfgas(TretEvento):
    """
    Schema XML de validação do retorno Pedido de Evento da NFGas.
    """

    class Meta:
        name = "retEventoNFGas"
        namespace = "http://www.portalfiscal.inf.br/nfgas"
