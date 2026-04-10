from __future__ import annotations

from dataclasses import dataclass

from pynfe_nasajon.pynfe.utils.nfag.cons_stat_serv_nfag_tipos_basico_v1_00 import (
    TretConsStatServ,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfag"


@dataclass(kw_only=True)
class RetConsStatServNfag(TretConsStatServ):
    """
    Schema XML de validação do Resultado da Consulta do Status do Serviço
    de NFAg.
    """

    class Meta:
        name = "retConsStatServNFAg"
        namespace = "http://www.portalfiscal.inf.br/nfag"
