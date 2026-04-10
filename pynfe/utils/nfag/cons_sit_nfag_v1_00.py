from __future__ import annotations

from dataclasses import dataclass

from pynfe_nasajon.pynfe.utils.nfag.cons_sit_nfag_tipos_basico_v1_00 import (
    TconsSitNfag,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfag"


@dataclass(kw_only=True)
class ConsSitNfag(TconsSitNfag):
    """
    Schema de validação XML dp Pedido de Consulta da Situação Atual da
    NFAg.
    """

    class Meta:
        name = "consSitNFAg"
        namespace = "http://www.portalfiscal.inf.br/nfag"
