from __future__ import annotations

from dataclasses import dataclass

from pynfe_nasajon.pynfe.utils.nfgas.cons_stat_serv_nfgas_tipos_basico_v1_00 import (
    TconsStatServ,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfgas"


@dataclass(kw_only=True)
class ConsStatServNfgas(TconsStatServ):
    """
    Schema XML de validação do Pedido de Consulta do Status do Serviço
    NFGas.
    """

    class Meta:
        name = "consStatServNFGas"
        namespace = "http://www.portalfiscal.inf.br/nfgas"
