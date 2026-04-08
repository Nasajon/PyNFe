from __future__ import annotations

from dataclasses import dataclass

from pynfe_nasajon.pynfe.utils.nfgas.cons_sit_nfgas_tipos_basico_v1_00 import (
    TconsSitNfgas,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfgas"


@dataclass(kw_only=True)
class ConsSitNfgas(TconsSitNfgas):
    """
    Schema de validação XML dp Pedido de Consulta da Situação Atual da
    NFGas.
    """

    class Meta:
        name = "consSitNFGas"
        namespace = "http://www.portalfiscal.inf.br/nfgas"
