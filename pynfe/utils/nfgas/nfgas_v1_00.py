from __future__ import annotations

from dataclasses import dataclass

from pynfe_nasajon.pynfe.utils.nfgas.nfgas_tipos_basico_v1_00 import Tnfgas

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfgas"


@dataclass(kw_only=True)
class Nfgas(Tnfgas):
    """
    Nota Fiscal Eletrônica da Agua.
    """

    class Meta:
        name = "NFGas"
        namespace = "http://www.portalfiscal.inf.br/nfgas"
