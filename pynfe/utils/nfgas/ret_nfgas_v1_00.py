from __future__ import annotations

from dataclasses import dataclass

from pynfe_nasajon.pynfe.utils.nfgas.nfgas_tipos_basico_v1_00 import TretNfgas

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfgas"


@dataclass(kw_only=True)
class RetNfgas(TretNfgas):
    """
    Schema XML de validação do retorno da NFGas.
    """

    class Meta:
        name = "retNFGas"
        namespace = "http://www.portalfiscal.inf.br/nfgas"
