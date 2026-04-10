from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlPeriod

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfag"


@dataclass(kw_only=True)
class TajusteCompet:
    """
    Tipo Ajuste de Competência.

    :ivar compet_apur: Ano e mês referência do período de apuração
        (AAAA-MM)
    :ivar v_ibs: Valor do IBS
    :ivar v_cbs: Valor da CBS
    """

    class Meta:
        name = "TAjusteCompet"

    compet_apur: XmlPeriod = field(
        metadata={
            "name": "competApur",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "min_inclusive": XmlPeriod("2025-01"),
        }
    )
    v_ibs: str = field(
        metadata={
            "name": "vIBS",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    v_cbs: str = field(
        metadata={
            "name": "vCBS",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )


@dataclass(kw_only=True)
class TcredPres:
    """
    Tipo Crédito Presumido.

    :ivar p_cred_pres: Percentual do Crédito Presumido
    :ivar v_cred_pres: Valor do Crédito Presumido
    :ivar v_cred_pres_cond_sus: Valor do Crédito Presumido Condição
        Suspensiva, preencher apenas para cCredPres que possui indicação
        de Condição Suspensiva
    """

    class Meta:
        name = "TCredPres"

    p_cred_pres: str = field(
        metadata={
            "name": "pCredPres",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
        }
    )
    v_cred_pres: None | str = field(
        default=None,
        metadata={
            "name": "vCredPres",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    v_cred_pres_cond_sus: None | str = field(
        default=None,
        metadata={
            "name": "vCredPresCondSus",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )


@dataclass(kw_only=True)
class TdevTrib:
    """
    Tipo Devolução Tributo.

    :ivar v_dev_trib: Valor do tributo devolvido. No fornecimento de
        energia elétrica, água, esgoto e gás natural e em outras
        hipóteses definidas no regulamento
    """

    class Meta:
        name = "TDevTrib"

    v_dev_trib: str = field(
        metadata={
            "name": "vDevTrib",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )


@dataclass(kw_only=True)
class Tdif:
    """
    Tipo Diferimento.

    :ivar p_dif: Percentual do diferimento
    :ivar v_dif: Valor do diferimento
    """

    class Meta:
        name = "TDif"

    p_dif: str = field(
        metadata={
            "name": "pDif",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
        }
    )
    v_dif: str = field(
        metadata={
            "name": "vDif",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )


class TenteGov(Enum):
    """
    Tipo de Ente Governamental.
    """

    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"


@dataclass(kw_only=True)
class TestornoCred:
    """
    Tipo Estorno de Crédito.

    :ivar v_ibsest_cred: Valor do IBS a ser estornado
    :ivar v_cbsest_cred: Valor da CBS a ser estornada
    """

    class Meta:
        name = "TEstornoCred"

    v_ibsest_cred: str = field(
        metadata={
            "name": "vIBSEstCred",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    v_cbsest_cred: str = field(
        metadata={
            "name": "vCBSEstCred",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )


@dataclass(kw_only=True)
class TibscbsmonoTot:
    """
    Grupo de informações de totais da CBS/IBS com monofasia.

    :ivar v_bcibscbs: Total Base de Calculo
    :ivar g_ibs: Totalização do IBS
    :ivar g_cbs: Totalização da CBS
    :ivar g_mono: Totais da Monofasia Só deverá ser utilizado para DFe
        modelos 55 e 65
    :ivar g_estorno_cred: Totalização do estorno de crédito
    """

    class Meta:
        name = "TIBSCBSMonoTot"

    v_bcibscbs: str = field(
        metadata={
            "name": "vBCIBSCBS",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    g_ibs: None | TibscbsmonoTot.GIbs = field(
        default=None,
        metadata={
            "name": "gIBS",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    g_cbs: None | TibscbsmonoTot.GCbs = field(
        default=None,
        metadata={
            "name": "gCBS",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    g_mono: None | TibscbsmonoTot.GMono = field(
        default=None,
        metadata={
            "name": "gMono",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    g_estorno_cred: None | TibscbsmonoTot.GEstornoCred = field(
        default=None,
        metadata={
            "name": "gEstornoCred",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )

    @dataclass(kw_only=True)
    class GIbs:
        """
        :ivar g_ibsuf: Totalização do IBS de competência da UF
        :ivar g_ibsmun: Totalização do IBS de competência Municipal
        :ivar v_ibs: Valor total do IBS
        :ivar v_cred_pres: Total do Crédito Presumido
        :ivar v_cred_pres_cond_sus: Total do Crédito Presumido Condição
            Suspensiva
        """

        g_ibsuf: TibscbsmonoTot.GIbs.GIbsuf = field(
            metadata={
                "name": "gIBSUF",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
            }
        )
        g_ibsmun: TibscbsmonoTot.GIbs.GIbsmun = field(
            metadata={
                "name": "gIBSMun",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
            }
        )
        v_ibs: str = field(
            metadata={
                "name": "vIBS",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        v_cred_pres: str = field(
            metadata={
                "name": "vCredPres",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        v_cred_pres_cond_sus: str = field(
            metadata={
                "name": "vCredPresCondSus",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )

        @dataclass(kw_only=True)
        class GIbsuf:
            """
            :ivar v_dif: Total do Diferimento
            :ivar v_dev_trib: Total de devoluções de tributos
            :ivar v_ibsuf: Valor total do IBS Estadual
            """

            v_dif: str = field(
                metadata={
                    "name": "vDif",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            v_dev_trib: str = field(
                metadata={
                    "name": "vDevTrib",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            v_ibsuf: str = field(
                metadata={
                    "name": "vIBSUF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )

        @dataclass(kw_only=True)
        class GIbsmun:
            """
            :ivar v_dif: Total do Diferimento
            :ivar v_dev_trib: Total de devoluções de tributos
            :ivar v_ibsmun: Valor total do IBS Municipal
            """

            v_dif: str = field(
                metadata={
                    "name": "vDif",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            v_dev_trib: str = field(
                metadata={
                    "name": "vDevTrib",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            v_ibsmun: str = field(
                metadata={
                    "name": "vIBSMun",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )

    @dataclass(kw_only=True)
    class GCbs:
        """
        :ivar v_dif: Total do Diferimento
        :ivar v_dev_trib: Total de devoluções de tributos
        :ivar v_cbs: Valor total da CBS
        :ivar v_cred_pres: Total do Crédito Presumido
        :ivar v_cred_pres_cond_sus: Total do Crédito Presumido Condição
            Suspensiva
        """

        v_dif: str = field(
            metadata={
                "name": "vDif",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        v_dev_trib: str = field(
            metadata={
                "name": "vDevTrib",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        v_cbs: str = field(
            metadata={
                "name": "vCBS",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        v_cred_pres: str = field(
            metadata={
                "name": "vCredPres",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        v_cred_pres_cond_sus: str = field(
            metadata={
                "name": "vCredPresCondSus",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )

    @dataclass(kw_only=True)
    class GMono:
        """
        :ivar v_ibsmono: Valor total do IBS monofásico
        :ivar v_cbsmono: Valor total da CBS monofásica
        :ivar v_ibsmono_reten: Valor total do IBS monofásico sujeito a
            retenção
        :ivar v_cbsmono_reten: Valor total da CBS monofásica sujeita a
            retenção
        :ivar v_ibsmono_ret: Valor do IBS monofásico retido
            anteriormente
        :ivar v_cbsmono_ret: Valor da CBS monofásica retida
            anteriormente
        """

        v_ibsmono: str = field(
            metadata={
                "name": "vIBSMono",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        v_cbsmono: str = field(
            metadata={
                "name": "vCBSMono",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        v_ibsmono_reten: str = field(
            metadata={
                "name": "vIBSMonoReten",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        v_cbsmono_reten: str = field(
            metadata={
                "name": "vCBSMonoReten",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        v_ibsmono_ret: str = field(
            metadata={
                "name": "vIBSMonoRet",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        v_cbsmono_ret: str = field(
            metadata={
                "name": "vCBSMonoRet",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )

    @dataclass(kw_only=True)
    class GEstornoCred:
        """
        :ivar v_ibsest_cred: Valor total do IBS estornado
        :ivar v_cbsest_cred: Valor total da CBS estornada
        """

        v_ibsest_cred: str = field(
            metadata={
                "name": "vIBSEstCred",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        v_cbsest_cred: str = field(
            metadata={
                "name": "vCBSEstCred",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )


@dataclass(kw_only=True)
class Tibscbstot:
    """
    Grupo de informações de totais da CBS/IBS.

    :ivar v_bcibscbs: Total Base de Calculo
    :ivar g_ibs: Totalização do IBS
    :ivar g_cbs: Totalização da CBS
    :ivar g_estorno_cred: Totalização do estorno de crédito
    """

    class Meta:
        name = "TIBSCBSTot"

    v_bcibscbs: str = field(
        metadata={
            "name": "vBCIBSCBS",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    g_ibs: Tibscbstot.GIbs = field(
        metadata={
            "name": "gIBS",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        }
    )
    g_cbs: Tibscbstot.GCbs = field(
        metadata={
            "name": "gCBS",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        }
    )
    g_estorno_cred: None | Tibscbstot.GEstornoCred = field(
        default=None,
        metadata={
            "name": "gEstornoCred",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )

    @dataclass(kw_only=True)
    class GIbs:
        """
        :ivar g_ibsuf: Totalização do IBS de competência da UF
        :ivar g_ibsmun: Totalização do IBS de competência Municipal
        :ivar v_ibs: Valor total do IBS
        """

        g_ibsuf: Tibscbstot.GIbs.GIbsuf = field(
            metadata={
                "name": "gIBSUF",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
            }
        )
        g_ibsmun: Tibscbstot.GIbs.GIbsmun = field(
            metadata={
                "name": "gIBSMun",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
            }
        )
        v_ibs: str = field(
            metadata={
                "name": "vIBS",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )

        @dataclass(kw_only=True)
        class GIbsuf:
            """
            :ivar v_dif: Total do Diferimento
            :ivar v_dev_trib: Total de devoluções de tributos
            :ivar v_ibsuf: Valor total do IBS Estadual
            """

            v_dif: str = field(
                metadata={
                    "name": "vDif",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            v_dev_trib: str = field(
                metadata={
                    "name": "vDevTrib",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            v_ibsuf: str = field(
                metadata={
                    "name": "vIBSUF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )

        @dataclass(kw_only=True)
        class GIbsmun:
            """
            :ivar v_dif: Total do Diferimento
            :ivar v_dev_trib: Total de devoluções de tributos
            :ivar v_ibsmun: Valor total do IBS Municipal
            """

            v_dif: str = field(
                metadata={
                    "name": "vDif",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            v_dev_trib: str = field(
                metadata={
                    "name": "vDevTrib",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            v_ibsmun: str = field(
                metadata={
                    "name": "vIBSMun",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )

    @dataclass(kw_only=True)
    class GCbs:
        """
        :ivar v_dif: Total do Diferimento
        :ivar v_dev_trib: Total de devoluções de tributos
        :ivar v_cbs: Valor total da CBS
        """

        v_dif: str = field(
            metadata={
                "name": "vDif",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        v_dev_trib: str = field(
            metadata={
                "name": "vDevTrib",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        v_cbs: str = field(
            metadata={
                "name": "vCBS",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )

    @dataclass(kw_only=True)
    class GEstornoCred:
        """
        :ivar v_ibsest_cred: Valor total do IBS estornado
        :ivar v_cbsest_cred: Valor total da CBS estornada
        """

        v_ibsest_cred: str = field(
            metadata={
                "name": "vIBSEstCred",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        v_cbsest_cred: str = field(
            metadata={
                "name": "vCBSEstCred",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )


@dataclass(kw_only=True)
class Tis:
    """
    Grupo de informações do Imposto Seletivo.

    :ivar cstis: Código Situação Tributária do Imposto Seletivo
    :ivar c_class_trib_is:
    :ivar v_bcis: Valor do BC
    :ivar p_is: Alíquota do Imposto Seletivo (percentual)
    :ivar p_isespec: Alíquota do Imposto Seletivo (por valor)
    :ivar u_trib: Unidade de medida apropriada especificada em Lei
        Ordinaria para fins de apuração do Imposto Seletivo
    :ivar q_trib: Quantidade com abse no campo uTrib informado
    :ivar v_is: Valor do Imposto Seletivo calculado
    """

    class Meta:
        name = "TIS"

    cstis: str = field(
        metadata={
            "name": "CSTIS",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"\d{3}",
        }
    )
    c_class_trib_is: str = field(
        metadata={
            "name": "cClassTribIS",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"\d{6}",
        }
    )
    v_bcis: None | str = field(
        default=None,
        metadata={
            "name": "vBCIS",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )
    p_is: None | str = field(
        default=None,
        metadata={
            "name": "pIS",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
        },
    )
    p_isespec: None | str = field(
        default=None,
        metadata={
            "name": "pISEspec",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
        },
    )
    u_trib: None | str = field(
        default=None,
        metadata={
            "name": "uTrib",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "min_length": 1,
            "max_length": 6,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        },
    )
    q_trib: None | str = field(
        default=None,
        metadata={
            "name": "qTrib",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0\.[1-9]{1}[0-9]{3}|0\.[0-9]{3}[1-9]{1}|0\.[0-9]{2}[1-9]{1}[0-9]{1}|0\.[0-9]{1}[1-9]{1}[0-9]{2}|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})?",
        },
    )
    v_is: None | str = field(
        default=None,
        metadata={
            "name": "vIS",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        },
    )


@dataclass(kw_only=True)
class Tistot:
    """
    Grupo de informações de totais do Imposto Seletivo.

    :ivar v_is: Valor Total do Imposto Seletivo
    """

    class Meta:
        name = "TISTot"

    v_is: str = field(
        metadata={
            "name": "vIS",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )


class TindDoacao(Enum):
    """
    Tipo Indicador de Doação.
    """

    VALUE_1 = "1"


@dataclass(kw_only=True)
class Tmonofasia:
    """
    Tipo Monofasia.

    :ivar g_mono_padrao: Grupo de informações da Tributação Monofásica
        padrão
    :ivar g_mono_reten: Grupo de informações da Tributação Monofásica
        sujeita a retenção
    :ivar g_mono_ret: Grupo de informações da Tributação Monofásica
        retida anteriormente
    :ivar g_mono_dif: Grupo de informações do diferimento da Tributação
        Monofásica
    :ivar v_tot_ibsmono_item: Total de IBS monofásico do item
    :ivar v_tot_cbsmono_item: Total da CBS monofásica do item
    """

    class Meta:
        name = "TMonofasia"

    g_mono_padrao: None | Tmonofasia.GMonoPadrao = field(
        default=None,
        metadata={
            "name": "gMonoPadrao",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    g_mono_reten: None | Tmonofasia.GMonoReten = field(
        default=None,
        metadata={
            "name": "gMonoReten",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    g_mono_ret: None | Tmonofasia.GMonoRet = field(
        default=None,
        metadata={
            "name": "gMonoRet",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    g_mono_dif: None | Tmonofasia.GMonoDif = field(
        default=None,
        metadata={
            "name": "gMonoDif",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    v_tot_ibsmono_item: str = field(
        metadata={
            "name": "vTotIBSMonoItem",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    v_tot_cbsmono_item: str = field(
        metadata={
            "name": "vTotCBSMonoItem",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )

    @dataclass(kw_only=True)
    class GMonoPadrao:
        """
        :ivar q_bcmono: Quantidade tributada na monofasia
        :ivar ad_rem_ibs: Alíquota ad rem do IBS
        :ivar ad_rem_cbs: Alíquota ad rem da CBS
        :ivar v_ibsmono: Valor do IBS monofásico
        :ivar v_cbsmono: Valor da CBS monofásica
        """

        q_bcmono: str = field(
            metadata={
                "name": "qBCMono",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})?",
            }
        )
        ad_rem_ibs: str = field(
            metadata={
                "name": "adRemIBS",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
            }
        )
        ad_rem_cbs: str = field(
            metadata={
                "name": "adRemCBS",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
            }
        )
        v_ibsmono: str = field(
            metadata={
                "name": "vIBSMono",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        v_cbsmono: str = field(
            metadata={
                "name": "vCBSMono",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )

    @dataclass(kw_only=True)
    class GMonoReten:
        """
        :ivar q_bcmono_reten: Quantidade tributada sujeita a retenção.
        :ivar ad_rem_ibsreten: Alíquota ad rem do IBS sujeito a retenção
        :ivar v_ibsmono_reten: Valor do IBS monofásico sujeito a
            retenção
        :ivar ad_rem_cbsreten: Alíquota ad rem da CBS sujeita a retenção
        :ivar v_cbsmono_reten: Valor da CBS monofásica sujeita a
            retenção
        """

        q_bcmono_reten: str = field(
            metadata={
                "name": "qBCMonoReten",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})?",
            }
        )
        ad_rem_ibsreten: str = field(
            metadata={
                "name": "adRemIBSReten",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
            }
        )
        v_ibsmono_reten: str = field(
            metadata={
                "name": "vIBSMonoReten",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        ad_rem_cbsreten: str = field(
            metadata={
                "name": "adRemCBSReten",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
            }
        )
        v_cbsmono_reten: str = field(
            metadata={
                "name": "vCBSMonoReten",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )

    @dataclass(kw_only=True)
    class GMonoRet:
        """
        :ivar q_bcmono_ret: Quantidade tributada retida anteriormente
        :ivar ad_rem_ibsret: Alíquota ad rem do IBS retido anteriormente
        :ivar v_ibsmono_ret: Valor do IBS retido anteriormente
        :ivar ad_rem_cbsret: Alíquota ad rem da CBS retida anteriormente
        :ivar v_cbsmono_ret: Valor da CBS retida anteriormente
        """

        q_bcmono_ret: str = field(
            metadata={
                "name": "qBCMonoRet",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})?",
            }
        )
        ad_rem_ibsret: str = field(
            metadata={
                "name": "adRemIBSRet",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
            }
        )
        v_ibsmono_ret: str = field(
            metadata={
                "name": "vIBSMonoRet",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        ad_rem_cbsret: str = field(
            metadata={
                "name": "adRemCBSRet",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
            }
        )
        v_cbsmono_ret: str = field(
            metadata={
                "name": "vCBSMonoRet",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )

    @dataclass(kw_only=True)
    class GMonoDif:
        """
        :ivar p_dif_ibs: Percentual do diferimento do imposto monofásico
        :ivar v_ibsmono_dif: Valor do IBS monofásico diferido
        :ivar p_dif_cbs: Percentual do diferimento do imposto monofásico
        :ivar v_cbsmono_dif: Valor da CBS monofásica diferida
        """

        p_dif_ibs: str = field(
            metadata={
                "name": "pDifIBS",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
            }
        )
        v_ibsmono_dif: str = field(
            metadata={
                "name": "vIBSMonoDif",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        p_dif_cbs: str = field(
            metadata={
                "name": "pDifCBS",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
            }
        )
        v_cbsmono_dif: str = field(
            metadata={
                "name": "vCBSMonoDif",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )


class ToperCompraGov(Enum):
    """
    Tipo da Operação com Ente Governamental.
    """

    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"


@dataclass(kw_only=True)
class TpagRef:
    """
    Tipo Pagamento que ocorre em DFe emitdo anteriormente Informado para
    abater as parcelas de antecipação de pagamento, conforme art. 10 §4.

    :ivar ref_dfe: Chave de acesso do documento fiscal de antecipação de
        pagamento Obs: esse DFe deverá ter o indAntecipacaoPgto marcado
        no grupo ide
    """

    class Meta:
        name = "TPagRef"

    ref_dfe: list[object] = field(
        default_factory=list,
        metadata={
            "name": "refDFe",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "min_occurs": 1,
            "max_occurs": 99,
        },
    )


@dataclass(kw_only=True)
class TpagamentoRtc:
    """
    Tipo dados do pagamento para o sistema de arrecadação Cada DFe que
    utilizar deverá utilizar esses tipo no grupo ide.

    :ivar tp_meio_pgto: (Meio de pagamento utilizado (ver IT DFe
        2026.001)
    :ivar cnpjreceb: CNPJ do recebedor do pagamento Informar zeros não
        significativos
    :ivar cnpjbase_psp: CNPJ base da instituição financeira Informar
        zeros não significativos
    :ivar n_pag: Número sequencial do pagamento
    :ivar id_transacao: ID específico da transação financeira conforme o
        meio de pagamento
    """

    class Meta:
        name = "TPagamentoRTC"

    tp_meio_pgto: str = field(
        metadata={
            "name": "tpMeioPgto",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"[0-9]{2}",
        }
    )
    cnpjreceb: str = field(
        metadata={
            "name": "CNPJReceb",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"[A-Z0-9]{12}[0-9]{2}",
        }
    )
    cnpjbase_psp: str = field(
        metadata={
            "name": "CNPJBasePSP",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"[A-Z0-9]{8}",
        }
    )
    n_pag: str = field(
        metadata={
            "name": "nPag",
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"[1-9]{1}[0-9]{0,1}|[1-8]{1}[0-9]{2}|[9]{1}[0-8]{1}[0-9]{1}|[9]{1}[9]{1}[0]{1}",
        }
    )
    id_transacao: str = field(
        metadata={
            "name": "idTransacao",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 35,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )


@dataclass(kw_only=True)
class Tred:
    """
    Tipo Redução Base de Cálculo.

    :ivar p_red_aliq: Percentual de redução de aliquota do cClassTrib
    :ivar p_aliq_efet: Aliquota Efetiva que será aplicada a Base de
        Calculo (em percentual)
    """

    class Meta:
        name = "TRed"

    p_red_aliq: str = field(
        metadata={
            "name": "pRedAliq",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
        }
    )
    p_aliq_efet: str = field(
        metadata={
            "name": "pAliqEfet",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
        }
    )


class TtpCredPresIbszfm(Enum):
    """
    Tipo de classificação do Crédito Presumido IBS ZFM.
    """

    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"


@dataclass(kw_only=True)
class TtransfCred:
    """
    Tipo Transferência de Crédito.

    :ivar v_ibs: Valor do IBS a ser transferido
    :ivar v_cbs: Valor da CBS a ser transferida
    """

    class Meta:
        name = "TTransfCred"

    v_ibs: str = field(
        metadata={
            "name": "vIBS",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    v_cbs: str = field(
        metadata={
            "name": "vCBS",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )


@dataclass(kw_only=True)
class TtribCompraGov:
    """
    Tipo Tributação Compra Governamental.

    :ivar p_aliq_ibsuf:
    :ivar v_trib_ibsuf: Valor que seria devido a UF, sem aplicação do
        Art. 473. da LC 214/2025
    :ivar p_aliq_ibsmun:
    :ivar v_trib_ibsmun: Valor que seria devido ao município, sem
        aplicação do Art. 473. da LC 214/2025
    :ivar p_aliq_cbs:
    :ivar v_trib_cbs: Valor que seria devido a CBS, sem aplicação do
        Art. 473. da LC 214/2025
    """

    class Meta:
        name = "TTribCompraGov"

    p_aliq_ibsuf: str = field(
        metadata={
            "name": "pAliqIBSUF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
        }
    )
    v_trib_ibsuf: str = field(
        metadata={
            "name": "vTribIBSUF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    p_aliq_ibsmun: str = field(
        metadata={
            "name": "pAliqIBSMun",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
        }
    )
    v_trib_ibsmun: str = field(
        metadata={
            "name": "vTribIBSMun",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    p_aliq_cbs: str = field(
        metadata={
            "name": "pAliqCBS",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
        }
    )
    v_trib_cbs: str = field(
        metadata={
            "name": "vTribCBS",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )


@dataclass(kw_only=True)
class TtribRegular:
    """
    Tipo Tributação Regular.

    :ivar cstreg: Código da Situação Tributária do IBS e CBS Informar
        qual seria o CST caso não cumprida a condição
        resolutória/suspensiva
    :ivar c_class_trib_reg: Informar qual seria o cClassTrib caso não
        cumprida a condição resolutória/suspensiva
    :ivar p_aliq_efet_reg_ibsuf: Alíquota do IBS da UF Informar como
        seria a Alíquota caso não cumprida a condição
        resolutória/suspensiva
    :ivar v_trib_reg_ibsuf: Valor do IBS da UF Informar como seria o
        valor do Tributo caso não cumprida a condição
        resolutória/suspensiva
    :ivar p_aliq_efet_reg_ibsmun: Alíquota do IBS do Município Informar
        como seria a Alíquota caso não cumprida a condição
        resolutória/suspensiva
    :ivar v_trib_reg_ibsmun: Valor do IBS do Município Informar como
        seria o valor do Tributo caso não cumprida a condição
        resolutória/suspensiva
    :ivar p_aliq_efet_reg_cbs: Alíquota da CBS Informar como seria a
        Alíquota caso não cumprida a condição resolutória/suspensiva
    :ivar v_trib_reg_cbs: Valor da CBS Informar como seria o valor do
        Tributo caso não cumprida a condição resolutória/suspensiva
    """

    class Meta:
        name = "TTribRegular"

    cstreg: str = field(
        metadata={
            "name": "CSTReg",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"\d{3}",
        }
    )
    c_class_trib_reg: str = field(
        metadata={
            "name": "cClassTribReg",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"\d{6}",
        }
    )
    p_aliq_efet_reg_ibsuf: str = field(
        metadata={
            "name": "pAliqEfetRegIBSUF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
        }
    )
    v_trib_reg_ibsuf: str = field(
        metadata={
            "name": "vTribRegIBSUF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    p_aliq_efet_reg_ibsmun: str = field(
        metadata={
            "name": "pAliqEfetRegIBSMun",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
        }
    )
    v_trib_reg_ibsmun: str = field(
        metadata={
            "name": "vTribRegIBSMun",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    p_aliq_efet_reg_cbs: str = field(
        metadata={
            "name": "pAliqEfetRegCBS",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
        }
    )
    v_trib_reg_cbs: str = field(
        metadata={
            "name": "vTribRegCBS",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )


@dataclass(kw_only=True)
class Tcibs:
    """
    Tipo CBS IBS Completo.

    :ivar v_bc: Valor do BC
    :ivar g_ibsuf: Grupo de informações do IBS na UF
    :ivar g_ibsmun: Grupo de Informações do IBS no Município
    :ivar v_ibs: Valor do IBS
    :ivar g_cbs: Grupo de Tributação da CBS
    :ivar g_trib_regular: Grupo de informações da Tributação Regular.
        Informar como seria a tributação caso não cumprida a condição
        resolutória/suspensiva. Exemplo 1: Art. 442, §4. Operações com
        ZFM e ALC. Exemplo 2: Operações com suspensão do tributo.
    :ivar g_trib_compra_gov: Grupo de informações da composição do valor
        do IBS e da CBS em compras governamental
    """

    class Meta:
        name = "TCIBS"

    v_bc: str = field(
        metadata={
            "name": "vBC",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    g_ibsuf: Tcibs.GIbsuf = field(
        metadata={
            "name": "gIBSUF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        }
    )
    g_ibsmun: Tcibs.GIbsmun = field(
        metadata={
            "name": "gIBSMun",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        }
    )
    v_ibs: str = field(
        metadata={
            "name": "vIBS",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    g_cbs: Tcibs.GCbs = field(
        metadata={
            "name": "gCBS",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        }
    )
    g_trib_regular: None | TtribRegular = field(
        default=None,
        metadata={
            "name": "gTribRegular",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    g_trib_compra_gov: None | TtribCompraGov = field(
        default=None,
        metadata={
            "name": "gTribCompraGov",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )

    @dataclass(kw_only=True)
    class GCbs:
        """
        :ivar p_cbs: Aliquota da CBS (em percentual)
        :ivar g_dif: Grupo de campos do Diferimento
        :ivar g_dev_trib: Grupo de Informações da devolução de tributos
        :ivar g_red: Grupo de campos da redução de aliquota
        :ivar v_cbs: Valor da CBS
        """

        p_cbs: str = field(
            metadata={
                "name": "pCBS",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
            }
        )
        g_dif: None | Tdif = field(
            default=None,
            metadata={
                "name": "gDif",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
            },
        )
        g_dev_trib: None | TdevTrib = field(
            default=None,
            metadata={
                "name": "gDevTrib",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
            },
        )
        g_red: None | Tred = field(
            default=None,
            metadata={
                "name": "gRed",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
            },
        )
        v_cbs: str = field(
            metadata={
                "name": "vCBS",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )

    @dataclass(kw_only=True)
    class GIbsuf:
        """
        :ivar p_ibsuf: Aliquota do IBS de competência das UF (em
            percentual)
        :ivar g_dif: Grupo de campos do Diferimento
        :ivar g_dev_trib: Grupo de Informações da devolução de tributos
        :ivar g_red: Grupo de campos da redução de aliquota
        :ivar v_ibsuf: Valor do IBS de competência das UF
        """

        p_ibsuf: str = field(
            metadata={
                "name": "pIBSUF",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
            }
        )
        g_dif: None | Tdif = field(
            default=None,
            metadata={
                "name": "gDif",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
            },
        )
        g_dev_trib: None | TdevTrib = field(
            default=None,
            metadata={
                "name": "gDevTrib",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
            },
        )
        g_red: None | Tred = field(
            default=None,
            metadata={
                "name": "gRed",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
            },
        )
        v_ibsuf: str = field(
            metadata={
                "name": "vIBSUF",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )

    @dataclass(kw_only=True)
    class GIbsmun:
        """
        :ivar p_ibsmun: Aliquota do IBS Municipal (em percentual)
        :ivar g_dif: Grupo de campos do Diferimento
        :ivar g_dev_trib: Grupo de Informações da devolução de tributos
        :ivar g_red: Grupo de campos da redução de aliquota
        :ivar v_ibsmun: Valor do IBS Municipal
        """

        p_ibsmun: str = field(
            metadata={
                "name": "pIBSMun",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
            }
        )
        g_dif: None | Tdif = field(
            default=None,
            metadata={
                "name": "gDif",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
            },
        )
        g_dev_trib: None | TdevTrib = field(
            default=None,
            metadata={
                "name": "gDevTrib",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
            },
        )
        g_red: None | Tred = field(
            default=None,
            metadata={
                "name": "gRed",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
            },
        )
        v_ibsmun: str = field(
            metadata={
                "name": "vIBSMun",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )


@dataclass(kw_only=True)
class TcompraGov:
    """
    Tipo Compras Governamentais Cada DFe que utilizar deverá utilizar esses
    tipo no grupo ide.

    :ivar tp_ente_gov: Para administração pública direta e suas
        autarquias e fundações: 1=União 2=Estados 3=Distrito Federal
        4=Municípios 5=Consórcio Público 6=Comitê Gestor do IBS
    :ivar p_redutor: Percentual de redução de aliquota em compra
        governamental
    :ivar tp_oper_gov: Tipo da operação com ente governamental: 1 –
        Fornecimento com pagamento posterior; 2 - Recebimento do
        pagamento com fornecimento já realizado; 3 – Fornecimento com
        pagamento já realizado; 4 – Recebimento do pagamento com
        fornecimento posterior;
    """

    class Meta:
        name = "TCompraGov"

    tp_ente_gov: TenteGov = field(
        metadata={
            "name": "tpEnteGov",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        }
    )
    p_redutor: str = field(
        metadata={
            "name": "pRedutor",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
        }
    )
    tp_oper_gov: ToperCompraGov = field(
        metadata={
            "name": "tpOperGov",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        }
    )


@dataclass(kw_only=True)
class TcompraGovReduzido:
    """
    Tipo Compras Governamentais Cada DFe que utilizar deverá utilizar esses
    tipo no grupo ide.

    :ivar tp_ente_gov: Para administração pública direta e suas
        autarquias e fundações: 1=União 2=Estados 3=Distrito Federal
        4=Municípios 5=Consórcio Público 6=Comitê Gestor do IBS
    :ivar p_redutor: Percentual de redução de aliquota em compra
        governamental
    :ivar tp_oper_gov: Tipo da operação com ente governamental: 1 –
        Fornecimento com pagamento posterior; 2 - Recebimento do
        pagamento com fornecimento já realizado; 3 – Fornecimento com
        pagamento já realizado; 4 – Recebimento do pagamento com
        fornecimento posterior;
    :ivar ref_dfe_ant: Chave de acesso do documento fiscal anterior.
        Deverá ser informado para tpOperGov 2 e 3 e vedado para os tipos
        1 e 4. No caso do toOperGov 2 aceitará apenas uma chave
        referenciada, no tipo 3 poderá aceitar múltiplas chaves Obs: a
        chave de acesso deverá ser de um emitente com o mesmo CNPJ base
    """

    class Meta:
        name = "TCompraGovReduzido"

    tp_ente_gov: TenteGov = field(
        metadata={
            "name": "tpEnteGov",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        }
    )
    p_redutor: str = field(
        metadata={
            "name": "pRedutor",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
        }
    )
    tp_oper_gov: ToperCompraGov = field(
        metadata={
            "name": "tpOperGov",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        }
    )
    ref_dfe_ant: list[object] = field(
        default_factory=list,
        metadata={
            "name": "refDFeAnt",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )


@dataclass(kw_only=True)
class TcredPresIbszfm:
    """
    Tipo Informações do crédito presumido de IBS para fornecimentos a
    partir da ZFM.

    :ivar compet_apur: Ano e mês referência do período de apuração
        (AAAA-MM)
    :ivar tp_cred_pres_ibszfm: Classificação de acordo com o art. 450, §
        1º, da LC 214/25 para o cálculo do crédito presumido na ZFM 0 -
        Sem crédito presumido; 1 - Bens de consumo final (55%); 2 - Bens
        de capital (75%); 3 - Bens intermediários (90,25%); 4 - Bens de
        informática e outros definidos em legislação (100%). OBS:
        Percentuais definidos no art. 450, § 1º, da LC 214/25 para o
        cálculo do crédito presumido
    :ivar v_cred_pres_ibszfm: Valor do crédito presumido calculado sobre
        o saldo devedor apurado
    """

    class Meta:
        name = "TCredPresIBSZFM"

    compet_apur: XmlPeriod = field(
        metadata={
            "name": "competApur",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "min_inclusive": XmlPeriod("2025-01"),
        }
    )
    tp_cred_pres_ibszfm: TtpCredPresIbszfm = field(
        metadata={
            "name": "tpCredPresIBSZFM",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        }
    )
    v_cred_pres_ibszfm: str = field(
        metadata={
            "name": "vCredPresIBSZFM",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )


@dataclass(kw_only=True)
class TcredPresOper:
    """
    Tipo Crédito Presumido da Operação.

    :ivar v_bccred_pres: Valor da Base de Cálculo do Crédito Presumido
        da Operação
    :ivar c_cred_pres: Código de Classificação do Crédito Presumido do
        IBS e da CBS
    :ivar g_ibscred_pres: Grupo de Informações do Crédito Presumido
        referente ao IBS, quando aproveitado pelo emitente do documento.
    :ivar g_cbscred_pres: Grupo de Informações do Crédito Presumido
        referente a CBS, quando aproveitado pelo emitente do documento.
    """

    class Meta:
        name = "TCredPresOper"

    v_bccred_pres: str = field(
        metadata={
            "name": "vBCCredPres",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    c_cred_pres: str = field(
        metadata={
            "name": "cCredPres",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"\d{2}",
        }
    )
    g_ibscred_pres: None | TcredPres = field(
        default=None,
        metadata={
            "name": "gIBSCredPres",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    g_cbscred_pres: None | TcredPres = field(
        default=None,
        metadata={
            "name": "gCBSCredPres",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )


@dataclass(kw_only=True)
class TtribBpe:
    """
    Grupo de informações da Tributação do BPe.

    :ivar cst: Código Situação Tributária do IBS/CBS
    :ivar c_class_trib:
    :ivar ind_doacao:
    :ivar g_ibscbs:
    :ivar g_estorno_cred: Informado conforme indicador no cClassTrib
    """

    class Meta:
        name = "TTribBPe"

    cst: str = field(
        metadata={
            "name": "CST",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"\d{3}",
        }
    )
    c_class_trib: str = field(
        metadata={
            "name": "cClassTrib",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"\d{6}",
        }
    )
    ind_doacao: None | TindDoacao = field(
        default=None,
        metadata={
            "name": "indDoacao",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    g_ibscbs: None | Tcibs = field(
        default=None,
        metadata={
            "name": "gIBSCBS",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    g_estorno_cred: None | TestornoCred = field(
        default=None,
        metadata={
            "name": "gEstornoCred",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )


@dataclass(kw_only=True)
class TtribCte:
    """
    Grupo de informações da Tributação do CTe.

    :ivar cst: Código Situação Tributária do IBS/CBS
    :ivar c_class_trib:
    :ivar ind_doacao:
    :ivar g_ibscbs:
    :ivar g_estorno_cred: Informado conforme indicador no cClassTrib
    """

    class Meta:
        name = "TTribCTe"

    cst: str = field(
        metadata={
            "name": "CST",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"\d{3}",
        }
    )
    c_class_trib: str = field(
        metadata={
            "name": "cClassTrib",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"\d{6}",
        }
    )
    ind_doacao: None | TindDoacao = field(
        default=None,
        metadata={
            "name": "indDoacao",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    g_ibscbs: None | Tcibs = field(
        default=None,
        metadata={
            "name": "gIBSCBS",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    g_estorno_cred: None | TestornoCred = field(
        default=None,
        metadata={
            "name": "gEstornoCred",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )


@dataclass(kw_only=True)
class TtribNf3E:
    """
    Grupo de informações da Tributação da NF3e.

    :ivar cst: Código Situação Tributária do IBS/CBS
    :ivar c_class_trib:
    :ivar ind_doacao: Indica se a operação é de doação
    :ivar g_ibscbs:
    :ivar g_estorno_cred: Informado conforme indicador no cClassTrib
    """

    class Meta:
        name = "TTribNF3e"

    cst: str = field(
        metadata={
            "name": "CST",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"\d{3}",
        }
    )
    c_class_trib: str = field(
        metadata={
            "name": "cClassTrib",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"\d{6}",
        }
    )
    ind_doacao: None | TindDoacao = field(
        default=None,
        metadata={
            "name": "indDoacao",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    g_ibscbs: None | Tcibs = field(
        default=None,
        metadata={
            "name": "gIBSCBS",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    g_estorno_cred: None | TestornoCred = field(
        default=None,
        metadata={
            "name": "gEstornoCred",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )


@dataclass(kw_only=True)
class TtribNfag:
    """
    Grupo de informações da Tributação da NFAg.

    :ivar cst: Código Situação Tributária do IBS/CBS
    :ivar c_class_trib:
    :ivar ind_doacao:
    :ivar g_ibscbs:
    :ivar g_estorno_cred: Informado conforme indicador no cClassTrib
    """

    class Meta:
        name = "TTribNFAg"

    cst: str = field(
        metadata={
            "name": "CST",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"\d{3}",
        }
    )
    c_class_trib: str = field(
        metadata={
            "name": "cClassTrib",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"\d{6}",
        }
    )
    ind_doacao: None | TindDoacao = field(
        default=None,
        metadata={
            "name": "indDoacao",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    g_ibscbs: None | Tcibs = field(
        default=None,
        metadata={
            "name": "gIBSCBS",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    g_estorno_cred: None | TestornoCred = field(
        default=None,
        metadata={
            "name": "gEstornoCred",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )


@dataclass(kw_only=True)
class TtribNfce:
    """
    Grupo de informações da Tributação da NFCe.

    :ivar cst: Código Situação Tributária do IBS/CBS
    :ivar c_class_trib:
    :ivar ind_doacao: Indica se a operação é de doação
    :ivar g_ibscbs:
    :ivar g_ibscbsmono:
    """

    class Meta:
        name = "TTribNFCe"

    cst: str = field(
        metadata={
            "name": "CST",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"\d{3}",
        }
    )
    c_class_trib: str = field(
        metadata={
            "name": "cClassTrib",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"\d{6}",
        }
    )
    ind_doacao: None | TindDoacao = field(
        default=None,
        metadata={
            "name": "indDoacao",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    g_ibscbs: None | Tcibs = field(
        default=None,
        metadata={
            "name": "gIBSCBS",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    g_ibscbsmono: None | Tmonofasia = field(
        default=None,
        metadata={
            "name": "gIBSCBSMono",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )


@dataclass(kw_only=True)
class TtribNfcom:
    """
    Grupo de informações da Tributação da NFCom.

    :ivar cst: Código Situação Tributária do IBS/CBS
    :ivar c_class_trib:
    :ivar ind_doacao: Indica se a operação é de doação
    :ivar g_ibscbs:
    :ivar g_estorno_cred: Informado conforme indicador no cClassTrib
    """

    class Meta:
        name = "TTribNFCom"

    cst: str = field(
        metadata={
            "name": "CST",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"\d{3}",
        }
    )
    c_class_trib: str = field(
        metadata={
            "name": "cClassTrib",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"\d{6}",
        }
    )
    ind_doacao: None | TindDoacao = field(
        default=None,
        metadata={
            "name": "indDoacao",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    g_ibscbs: None | Tcibs = field(
        default=None,
        metadata={
            "name": "gIBSCBS",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    g_estorno_cred: None | TestornoCred = field(
        default=None,
        metadata={
            "name": "gEstornoCred",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )


@dataclass(kw_only=True)
class TtribNfgas:
    """
    Grupo de informações da Tributação da NFGas.

    :ivar cst: Código Situação Tributária do IBS/CBS
    :ivar c_class_trib:
    :ivar ind_doacao:
    :ivar g_ibscbs:
    :ivar g_ibscbsmono: Informar essa opção da Choice para Monofasia
    :ivar g_estorno_cred: Informado conforme indicador no cClassTrib
    """

    class Meta:
        name = "TTribNFGas"

    cst: str = field(
        metadata={
            "name": "CST",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"\d{3}",
        }
    )
    c_class_trib: str = field(
        metadata={
            "name": "cClassTrib",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"\d{6}",
        }
    )
    ind_doacao: None | TindDoacao = field(
        default=None,
        metadata={
            "name": "indDoacao",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    g_ibscbs: None | Tcibs = field(
        default=None,
        metadata={
            "name": "gIBSCBS",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    g_ibscbsmono: None | Tmonofasia = field(
        default=None,
        metadata={
            "name": "gIBSCBSMono",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    g_estorno_cred: None | TestornoCred = field(
        default=None,
        metadata={
            "name": "gEstornoCred",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )


@dataclass(kw_only=True)
class TtribNfe:
    """
    Grupo de informações da Tributação da NFe.

    :ivar cst: Código Situação Tributária do IBS/CBS
    :ivar c_class_trib:
    :ivar ind_doacao: Indica se a operação é de doação
    :ivar g_ibscbs:
    :ivar g_ibscbsmono: Informar essa opção da Choice para Monofasia
        (CST 620)
    :ivar g_transf_cred: Informar essa opção da Choice para o CST 800
    :ivar g_ajuste_compet: Informar essa opção da Choice para o CST 811
    :ivar g_estorno_cred: Informado conforme indicador no cClassTrib
    :ivar g_cred_pres_oper: Crédito Presumido da Operação. Informado
        conforme indicador no cClassTrib.
    :ivar g_cred_pres_ibszfm: Classificação de acordo com o art. 450, §
        1º, da LC 214/25 para o cálculo do crédito presumido na ZFM.
        Informado conforme indicador no cClassTrib.
    """

    class Meta:
        name = "TTribNFe"

    cst: str = field(
        metadata={
            "name": "CST",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"\d{3}",
        }
    )
    c_class_trib: str = field(
        metadata={
            "name": "cClassTrib",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
            "white_space": "preserve",
            "pattern": r"\d{6}",
        }
    )
    ind_doacao: None | TindDoacao = field(
        default=None,
        metadata={
            "name": "indDoacao",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    g_ibscbs: None | Tcibs = field(
        default=None,
        metadata={
            "name": "gIBSCBS",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    g_ibscbsmono: None | Tmonofasia = field(
        default=None,
        metadata={
            "name": "gIBSCBSMono",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    g_transf_cred: None | TtransfCred = field(
        default=None,
        metadata={
            "name": "gTransfCred",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    g_ajuste_compet: None | TajusteCompet = field(
        default=None,
        metadata={
            "name": "gAjusteCompet",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    g_estorno_cred: None | TestornoCred = field(
        default=None,
        metadata={
            "name": "gEstornoCred",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    g_cred_pres_oper: None | TcredPresOper = field(
        default=None,
        metadata={
            "name": "gCredPresOper",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
    g_cred_pres_ibszfm: None | TcredPresIbszfm = field(
        default=None,
        metadata={
            "name": "gCredPresIBSZFM",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        },
    )
