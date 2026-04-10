from __future__ import annotations

from dataclasses import dataclass

from pynfe_nasajon.pynfe.utils.nfag.nfag_tipos_basico_v1_00 import TretNfag

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfag"


@dataclass(kw_only=True)
class RetNfag(TretNfag):
    """
    Schema XML de validação do retorno da NFAg.
    """

    class Meta:
        name = "retNFAg"
        namespace = "http://www.portalfiscal.inf.br/nfag"
