from __future__ import annotations

from dataclasses import dataclass

from pynfe_nasajon.pynfe.utils.nfag.nfag_tipos_basico_v1_00 import Tnfag

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfag"


@dataclass(kw_only=True)
class Nfag(Tnfag):
    """
    Nota Fiscal Eletrônica da Agua.
    """

    class Meta:
        name = "NFAg"
        namespace = "http://www.portalfiscal.inf.br/nfag"
