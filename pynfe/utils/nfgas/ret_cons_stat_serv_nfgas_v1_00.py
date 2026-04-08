from __future__ import annotations

from dataclasses import dataclass

from pynfe_nasajon.pynfe.utils.nfgas.cons_stat_serv_nfgas_tipos_basico_v1_00 import (
    TretConsStatServ,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfgas"


@dataclass(kw_only=True)
class RetConsStatServNfgas(TretConsStatServ):
    """
    Schema XML de validação do Resultado da Consulta do Status do Serviço
    de NFGas.
    """

    class Meta:
        name = "retConsStatServNFGas"
        namespace = "http://www.portalfiscal.inf.br/nfgas"
