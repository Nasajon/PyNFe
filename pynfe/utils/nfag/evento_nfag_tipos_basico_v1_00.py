from __future__ import annotations

from dataclasses import dataclass, field

from pynfe_nasajon.pynfe.utils.nfag.tipos_geral_nfag_v1_00 import (
    Tamb,
    TcorgaoIbge,
)
from pynfe_nasajon.pynfe.utils.nfag.xmldsig_core_schema_v1_01 import Signature

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfag"


@dataclass(kw_only=True)
class Tevento:
    """
    Tipo Evento.
    """

    class Meta:
        name = "TEvento"

    inf_evento: Tevento.InfEvento = field(
        metadata={
            "name": "infEvento",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        }
    )
    signature: Signature = field(
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    versao: str = field(
        metadata={
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"1\.00",
        }
    )

    @dataclass(kw_only=True)
    class InfEvento:
        """
        :ivar c_orgao: Código do órgão de recepção do Evento.
        :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
            Homologação
        :ivar cnpj: CNPJ do emissor do evento
        :ivar ch_nfag: Chave de Acesso da NFAg vinculada ao evento
        :ivar dh_evento: Data e Hora do Evento, formato UTC (AAAA-MM-
            DDThh:mm:ssTZD)
        :ivar tp_evento: Tipo do Evento
        :ivar n_seq_evento: Seqüencial do evento para o mesmo tipo de
            evento.  Para maioria dos eventos será 1, nos casos em que
            possa existir mais de um evento o autor do evento deve
            numerar de forma seqüencial.
        :ivar det_evento: Detalhamento do evento específico
        :ivar inf_paa: Grupo de Informação do Provedor de Assinatura e
            Autorização
        :ivar id: Identificador da TAG a ser assinada, a regra de
            formação do Id é: “ID” + tpEvento +  chave da NFAg +
            nSeqEvento
        """

        c_orgao: TcorgaoIbge = field(
            metadata={
                "name": "cOrgao",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
            }
        )
        tp_amb: Tamb = field(
            metadata={
                "name": "tpAmb",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
            }
        )
        cnpj: str = field(
            metadata={
                "name": "CNPJ",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"[A-Z0-9]{12}[0-9]{2}",
            }
        )
        ch_nfag: str = field(
            metadata={
                "name": "chNFAg",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "max_length": 44,
                "white_space": "preserve",
                "pattern": r"[0-9]{6}[A-Z0-9]{12}[0-9]{26}",
            }
        )
        dh_evento: str = field(
            metadata={
                "name": "dhEvento",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
            }
        )
        tp_evento: str = field(
            metadata={
                "name": "tpEvento",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"[0-9]{6}",
            }
        )
        n_seq_evento: str = field(
            metadata={
                "name": "nSeqEvento",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"[0-9]{1,3}",
            }
        )
        det_evento: Tevento.InfEvento.DetEvento = field(
            metadata={
                "name": "detEvento",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
            }
        )
        inf_paa: None | Tevento.InfEvento.InfPaa = field(
            default=None,
            metadata={
                "name": "infPAA",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
            },
        )
        id: str = field(
            metadata={
                "name": "Id",
                "type": "Attribute",
                "pattern": r"ID[0-9]{12}[A-Z0-9]{12}[0-9]{28}|ID[0-9]{12}[A-Z0-9]{12}[0-9]{29}",
            }
        )

        @dataclass(kw_only=True)
        class DetEvento:
            """
            :ivar any_element: XML do evento Insira neste local o XML
                específico do tipo de evento (cancelamento,
                encerramento, registro de passagem).
            :ivar versao_evento:
            """

            any_element: None | object = field(
                default=None,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                    "process_contents": "skip",
                },
            )
            versao_evento: str = field(
                metadata={
                    "name": "versaoEvento",
                    "type": "Attribute",
                    "white_space": "preserve",
                    "pattern": r"1\.(0[0-9]|[1-9][0-9])",
                }
            )

        @dataclass(kw_only=True)
        class InfPaa:
            """
            :ivar cnpjpaa: CNPJ da empresa que emitirá evento em nome de
                outra no caso do faturamento conjunto
            """

            cnpjpaa: str = field(
                metadata={
                    "name": "CNPJPAA",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfag",
                    "white_space": "preserve",
                    "pattern": r"[A-Z0-9]{12}[0-9]{2}",
                }
            )


@dataclass(kw_only=True)
class TretEvento:
    """
    Tipo retorno do Evento.
    """

    class Meta:
        name = "TRetEvento"

    inf_evento: TretEvento.InfEvento = field(
        metadata={
            "name": "infEvento",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        }
    )
    signature: None | Signature = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )
    versao: str = field(
        metadata={
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"1\.00",
        }
    )

    @dataclass(kw_only=True)
    class InfEvento:
        """
        :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
            Homologação
        :ivar ver_aplic: Versão do Aplicativo que recebeu o Evento
        :ivar c_orgao: Código do órgão de recepção do Evento. Utilizar a
            Tabela do IBGE extendida, utilizar 90 para identificar
            SUFRAMA
        :ivar c_stat: Código do status da registro do Evento
        :ivar x_motivo: Descrição literal do status do registro do
            Evento
        :ivar ch_nfag: Chave de Acesso NFAg vinculada
        :ivar tp_evento: Tipo do Evento vinculado
        :ivar x_evento: Descrição do Evento
        :ivar n_seq_evento: Seqüencial do evento
        :ivar dh_reg_evento: Data e Hora de do recebimento do evento ou
            do registro do evento formato AAAA-MM-DDThh:mm:ssTZD
        :ivar n_prot: Número do protocolo de registro do evento
        :ivar id:
        """

        tp_amb: Tamb = field(
            metadata={
                "name": "tpAmb",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
            }
        )
        ver_aplic: str = field(
            metadata={
                "name": "verAplic",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        c_orgao: TcorgaoIbge = field(
            metadata={
                "name": "cOrgao",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
            }
        )
        c_stat: str = field(
            metadata={
                "name": "cStat",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"[0-9]{3,4}",
            }
        )
        x_motivo: str = field(
            metadata={
                "name": "xMotivo",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "min_length": 1,
                "max_length": 255,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        ch_nfag: None | str = field(
            default=None,
            metadata={
                "name": "chNFAg",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "max_length": 44,
                "white_space": "preserve",
                "pattern": r"[0-9]{6}[A-Z0-9]{12}[0-9]{26}",
            },
        )
        tp_evento: None | str = field(
            default=None,
            metadata={
                "name": "tpEvento",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"[0-9]{6}",
            },
        )
        x_evento: None | str = field(
            default=None,
            metadata={
                "name": "xEvento",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "min_length": 4,
                "max_length": 60,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            },
        )
        n_seq_evento: None | str = field(
            default=None,
            metadata={
                "name": "nSeqEvento",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"[0-9]{1,3}",
            },
        )
        dh_reg_evento: None | str = field(
            default=None,
            metadata={
                "name": "dhRegEvento",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
            },
        )
        n_prot: None | str = field(
            default=None,
            metadata={
                "name": "nProt",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfag",
                "white_space": "preserve",
                "pattern": r"[0-9]{16}",
            },
        )
        id: None | str = field(
            default=None,
            metadata={
                "name": "Id",
                "type": "Attribute",
                "pattern": r"ID[0-9]{16}",
            },
        )


@dataclass(kw_only=True)
class TprocEvento:
    """
    Tipo procEvento.

    :ivar evento_nfag:
    :ivar ret_evento_nfag:
    :ivar versao:
    :ivar ip_transmissor: IP do transmissor do documento fiscal para o
        ambiente autorizador
    :ivar n_porta_con: Porta de origem utilizada na conexão (De 0 a
        65535)
    :ivar dh_conexao: Data e Hora da Conexão de Origem
    """

    class Meta:
        name = "TProcEvento"

    evento_nfag: Tevento = field(
        metadata={
            "name": "eventoNFAg",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        }
    )
    ret_evento_nfag: TretEvento = field(
        metadata={
            "name": "retEventoNFAg",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfag",
        }
    )
    versao: str = field(
        metadata={
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"1\.00",
        }
    )
    ip_transmissor: None | str = field(
        default=None,
        metadata={
            "name": "ipTransmissor",
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])",
        },
    )
    n_porta_con: None | str = field(
        default=None,
        metadata={
            "name": "nPortaCon",
            "type": "Attribute",
            "pattern": r"[0-9]{1,5}",
        },
    )
    dh_conexao: None | str = field(
        default=None,
        metadata={
            "name": "dhConexao",
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
        },
    )
