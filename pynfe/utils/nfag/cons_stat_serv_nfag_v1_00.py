from __future__ import annotations

from dataclasses import dataclass

from pynfe_nasajon.pynfe.utils.nfag.cons_stat_serv_nfag_tipos_basico_v1_00 import (
    TconsStatServ,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfag"


@dataclass(kw_only=True)
class ConsStatServNfag(TconsStatServ):
    """
    Schema XML de validação do Pedido de Consulta do Status do Serviço
    NFAg.
    """

    class Meta:
        name = "consStatServNFAg"
        namespace = "http://www.portalfiscal.inf.br/nfag"
