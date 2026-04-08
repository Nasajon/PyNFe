from __future__ import annotations

from dataclasses import dataclass

from pynfe_nasajon.pynfe.utils.nfgas.cons_sit_nfgas_tipos_basico_v1_00 import (
    TretConsSitNfgas,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfgas"


@dataclass(kw_only=True)
class RetConsSitNfgas(TretConsSitNfgas):
    """
    Schema XML de validação do retorno da consulta da situação atual da
    NFGas.
    """

    class Meta:
        name = "retConsSitNFGas"
        namespace = "http://www.portalfiscal.inf.br/nfgas"
