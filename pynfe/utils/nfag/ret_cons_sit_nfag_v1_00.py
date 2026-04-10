from __future__ import annotations

from dataclasses import dataclass

from pynfe_nasajon.pynfe.utils.nfag.cons_sit_nfag_tipos_basico_v1_00 import (
    TretConsSitNfag,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfag"


@dataclass(kw_only=True)
class RetConsSitNfag(TretConsSitNfag):
    """
    Schema XML de validação do retorno da consulta da situação atual da
    NFAg.
    """

    class Meta:
        name = "retConsSitNFAg"
        namespace = "http://www.portalfiscal.inf.br/nfag"
