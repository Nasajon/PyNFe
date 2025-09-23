# /app/output/tiposSimples_v1_00.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:c27cf6a1980499753073c1afd72a5bfd80976ec9
# Generated 2025-09-22 19:54:31.369935 by PyXB version 1.2.6 using Python 3.12.11.final.0
# Namespace http://www.sped.fazenda.gov.br/nfse

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:d5c1ea7a-47e4-41f3-9b53-a4f568b545a4')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.sped.fazenda.gov.br/nfse', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, fallback_namespace=None, location_base=None, default_namespace=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword fallback_namespace An absent L{pyxb.Namespace} instance
    to use for unqualified names when there is no default namespace in
    scope.  If unspecified or C{None}, the namespace of the module
    containing this function will be used, if it is an absent
    namespace.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.

    @keyword default_namespace An alias for @c fallback_namespace used
    in PyXB 1.1.4 through 1.2.6.  It behaved like a default namespace
    only for absent namespaces.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if fallback_namespace is None:
        fallback_namespace = default_namespace
    if fallback_namespace is None:
        fallback_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=fallback_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, fallback_namespace=None, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if fallback_namespace is None:
        fallback_namespace = default_namespace
    if fallback_namespace is None:
        fallback_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, fallback_namespace)


# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TVerNFSe
class TVerNFSe (pyxb.binding.datatypes.string):

    """Tipo Versão da NF-e - 1.00"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TVerNFSe')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 3, 2)
    _Documentation = 'Tipo Versão da NF-e - 1.00'
TVerNFSe._CF_pattern = pyxb.binding.facets.CF_pattern()
TVerNFSe._CF_pattern.addPattern(pattern='1\\.00')
TVerNFSe._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TVerNFSe._InitializeFacetMap(TVerNFSe._CF_pattern,
   TVerNFSe._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TVerNFSe', TVerNFSe)
_module_typeBindings.TVerNFSe = TVerNFSe

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSString
class TSString (pyxb.binding.datatypes.string):

    """Tipo string genérico"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSString')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 12, 2)
    _Documentation = 'Tipo string genérico'
TSString._CF_pattern = pyxb.binding.facets.CF_pattern()
TSString._CF_pattern.addPattern(pattern='[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}')
TSString._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSString._InitializeFacetMap(TSString._CF_pattern,
   TSString._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSString', TSString)
_module_typeBindings.TSString = TSString

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSStringComQuebraDeLinha
class TSStringComQuebraDeLinha (pyxb.binding.datatypes.string):

    """Tipo string genérico"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSStringComQuebraDeLinha')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 21, 2)
    _Documentation = 'Tipo string genérico'
TSStringComQuebraDeLinha._CF_pattern = pyxb.binding.facets.CF_pattern()
TSStringComQuebraDeLinha._CF_pattern.addPattern(pattern='[\\s\\S!-ÿ]{1}[\\s\\S -ÿ]{0,}[\\s\\S!-ÿ]{1}|[\\s\\S!-ÿ]{1}')
TSStringComQuebraDeLinha._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSStringComQuebraDeLinha._InitializeFacetMap(TSStringComQuebraDeLinha._CF_pattern,
   TSStringComQuebraDeLinha._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSStringComQuebraDeLinha', TSStringComQuebraDeLinha)
_module_typeBindings.TSStringComQuebraDeLinha = TSStringComQuebraDeLinha

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSIdNFSe
class TSIdNFSe (pyxb.binding.datatypes.string):

    """
	    Informar o identificador precedido do literal ‘NFS’. A regra de formação do identificador de 53 posições da NFS-e é:
        "NFS" + Cód.Mun.(7) + Amb.Ger.(1) + Tipo de Inscrição Federal(1) + Inscrição Federal(14) + No.NFS-e(13) + AnoMes Emis.(4) + Cód.Num.(9) + DV(1)
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSIdNFSe')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 30, 2)
    _Documentation = '\n\t    Informar o identificador precedido do literal ‘NFS’. A regra de formação do identificador de 53 posições da NFS-e é:\n        "NFS" + Cód.Mun.(7) + Amb.Ger.(1) + Tipo de Inscrição Federal(1) + Inscrição Federal(14) + No.NFS-e(13) + AnoMes Emis.(4) + Cód.Num.(9) + DV(1)\n      '
TSIdNFSe._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(53))
TSIdNFSe._CF_pattern = pyxb.binding.facets.CF_pattern()
TSIdNFSe._CF_pattern.addPattern(pattern='NFS[0-9]{50}')
TSIdNFSe._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSIdNFSe._InitializeFacetMap(TSIdNFSe._CF_maxLength,
   TSIdNFSe._CF_pattern,
   TSIdNFSe._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSIdNFSe', TSIdNFSe)
_module_typeBindings.TSIdNFSe = TSIdNFSe

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSIdDPS
class TSIdDPS (pyxb.binding.datatypes.string):

    """
        Informar o identificador precedido do literal ‘DPS’. A regra de formação do identificador de 45 posições da DPS é:
        "DPS" + Cód.Mun (7) + Tipo de Inscrição Federal (1) + Inscrição Federal (14 - CPF completar com 000 à esquerda) + Série DPS (5)+ Núm. DPS (15)
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSIdDPS')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 43, 2)
    _Documentation = '\n        Informar o identificador precedido do literal ‘DPS’. A regra de formação do identificador de 45 posições da DPS é:\n        "DPS" + Cód.Mun (7) + Tipo de Inscrição Federal (1) + Inscrição Federal (14 - CPF completar com 000 à esquerda) + Série DPS (5)+ Núm. DPS (15)\n      '
TSIdDPS._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(45))
TSIdDPS._CF_pattern = pyxb.binding.facets.CF_pattern()
TSIdDPS._CF_pattern.addPattern(pattern='DPS[0-9]{42}')
TSIdDPS._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSIdDPS._InitializeFacetMap(TSIdDPS._CF_maxLength,
   TSIdDPS._CF_pattern,
   TSIdDPS._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSIdDPS', TSIdDPS)
_module_typeBindings.TSIdDPS = TSIdDPS

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSTipoAmbiente
class TSTipoAmbiente (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
		  Tipos de ambiente do Sistema Nacional NFS-e: 1 - Produção; 2 - Homologação;
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSTipoAmbiente')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 56, 2)
    _Documentation = '\n\t\t  Tipos de ambiente do Sistema Nacional NFS-e: 1 - Produção; 2 - Homologação;\n      '
TSTipoAmbiente._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSTipoAmbiente)
TSTipoAmbiente.n1 = TSTipoAmbiente._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
TSTipoAmbiente.n2 = TSTipoAmbiente._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
TSTipoAmbiente._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSTipoAmbiente._InitializeFacetMap(TSTipoAmbiente._CF_enumeration,
   TSTipoAmbiente._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSTipoAmbiente', TSTipoAmbiente)
_module_typeBindings.TSTipoAmbiente = TSTipoAmbiente

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSAmbGeradorNFSe
class TSAmbGeradorNFSe (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
	    Tipo Ambiente Gerador de NFS-e:
        1 - Prefeitura;
        2 - Sistema Nacional da NFS-e;
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSAmbGeradorNFSe')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 68, 2)
    _Documentation = '\n\t    Tipo Ambiente Gerador de NFS-e:\n        1 - Prefeitura;\n        2 - Sistema Nacional da NFS-e;\n      '
TSAmbGeradorNFSe._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSAmbGeradorNFSe)
TSAmbGeradorNFSe.n1 = TSAmbGeradorNFSe._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
TSAmbGeradorNFSe.n2 = TSAmbGeradorNFSe._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
TSAmbGeradorNFSe._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSAmbGeradorNFSe._InitializeFacetMap(TSAmbGeradorNFSe._CF_enumeration,
   TSAmbGeradorNFSe._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSAmbGeradorNFSe', TSAmbGeradorNFSe)
_module_typeBindings.TSAmbGeradorNFSe = TSAmbGeradorNFSe

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSAmbGeradorEvt
class TSAmbGeradorEvt (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
	    Tipo Ambiente gerador do evento:
        1- Prefeitura;
        2- Sefin Nacional;
        3- Ambiente Nacional.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSAmbGeradorEvt')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 82, 2)
    _Documentation = '\n\t    Tipo Ambiente gerador do evento:\n        1- Prefeitura;\n        2- Sefin Nacional;\n        3- Ambiente Nacional.\n      '
TSAmbGeradorEvt._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSAmbGeradorEvt)
TSAmbGeradorEvt.n1 = TSAmbGeradorEvt._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
TSAmbGeradorEvt.n2 = TSAmbGeradorEvt._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
TSAmbGeradorEvt.n3 = TSAmbGeradorEvt._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
TSAmbGeradorEvt._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSAmbGeradorEvt._InitializeFacetMap(TSAmbGeradorEvt._CF_enumeration,
   TSAmbGeradorEvt._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSAmbGeradorEvt', TSAmbGeradorEvt)
_module_typeBindings.TSAmbGeradorEvt = TSAmbGeradorEvt

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSTipoEmissao
class TSTipoEmissao (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
	    Tipo de emissão da NFS-e:
        1 - Emissão normal no modelo da NFS-e Nacional;
        2 - Emissão original em leiaute próprio do município com transcrição para o modelo da NFS-e Nacional.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSTipoEmissao')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 98, 2)
    _Documentation = '\n\t    Tipo de emissão da NFS-e:\n        1 - Emissão normal no modelo da NFS-e Nacional;\n        2 - Emissão original em leiaute próprio do município com transcrição para o modelo da NFS-e Nacional.\n      '
TSTipoEmissao._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSTipoEmissao)
TSTipoEmissao.n1 = TSTipoEmissao._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
TSTipoEmissao.n2 = TSTipoEmissao._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
TSTipoEmissao._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSTipoEmissao._InitializeFacetMap(TSTipoEmissao._CF_enumeration,
   TSTipoEmissao._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSTipoEmissao', TSTipoEmissao)
_module_typeBindings.TSTipoEmissao = TSTipoEmissao

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSProcEmissao
class TSProcEmissao (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        Processo de Emissão da DPS:
        1 - Emissão com aplicativo do contribuinte (via Web Service);
        2 - Emissão com aplicativo disponibilizado pelo fisco (Web);
        3 - Emissão com aplicativo disponibilizado pelo fisco (App);
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSProcEmissao')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 112, 2)
    _Documentation = '\n        Processo de Emissão da DPS:\n        1 - Emissão com aplicativo do contribuinte (via Web Service);\n        2 - Emissão com aplicativo disponibilizado pelo fisco (Web);\n        3 - Emissão com aplicativo disponibilizado pelo fisco (App);\n      '
TSProcEmissao._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSProcEmissao)
TSProcEmissao.n1 = TSProcEmissao._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
TSProcEmissao.n2 = TSProcEmissao._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
TSProcEmissao.n3 = TSProcEmissao._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
TSProcEmissao._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSProcEmissao._InitializeFacetMap(TSProcEmissao._CF_enumeration,
   TSProcEmissao._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSProcEmissao', TSProcEmissao)
_module_typeBindings.TSProcEmissao = TSProcEmissao

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSData
class TSData (pyxb.binding.datatypes.string):

    """Tipo data no formato AAAA-MM-DD"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSData')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 128, 2)
    _Documentation = 'Tipo data no formato AAAA-MM-DD'
TSData._CF_pattern = pyxb.binding.facets.CF_pattern()
TSData._CF_pattern.addPattern(pattern='(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))')
TSData._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSData._InitializeFacetMap(TSData._CF_pattern,
   TSData._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSData', TSData)
_module_typeBindings.TSData = TSData

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSDateTimeUTC
class TSDateTimeUTC (pyxb.binding.datatypes.string):

    """Data e Hora, formato UTC (AAAA-MM-DDThh:mm:ssTZD, onde TZD = +hh:mm ou -hh:mm)"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSDateTimeUTC')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 137, 2)
    _Documentation = 'Data e Hora, formato UTC (AAAA-MM-DDThh:mm:ssTZD, onde TZD = +hh:mm ou -hh:mm)'
TSDateTimeUTC._CF_pattern = pyxb.binding.facets.CF_pattern()
TSDateTimeUTC._CF_pattern.addPattern(pattern='(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\\d):[0-5]\\d:[0-5]\\d([\\-,\\+](0[0-9]|10|11):00|([\\+](12):00))')
TSDateTimeUTC._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSDateTimeUTC._InitializeFacetMap(TSDateTimeUTC._CF_pattern,
   TSDateTimeUTC._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSDateTimeUTC', TSDateTimeUTC)
_module_typeBindings.TSDateTimeUTC = TSDateTimeUTC

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSSerieDPS
class TSSerieDPS (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSSerieDPS')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 155, 2)
    _Documentation = None
TSSerieDPS._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(5))
TSSerieDPS._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSSerieDPS._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSSerieDPS._InitializeFacetMap(TSSerieDPS._CF_maxLength,
   TSSerieDPS._CF_minLength,
   TSSerieDPS._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSSerieDPS', TSSerieDPS)
_module_typeBindings.TSSerieDPS = TSSerieDPS

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSEmitenteDPS
class TSEmitenteDPS (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        Emitente da DPS:
        1 - Prestador
        2 - Tomador
        3 - Intermediário
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSEmitenteDPS')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 162, 2)
    _Documentation = '\n        Emitente da DPS:\n        1 - Prestador\n        2 - Tomador\n        3 - Intermediário\n      '
TSEmitenteDPS._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSEmitenteDPS)
TSEmitenteDPS.n1 = TSEmitenteDPS._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
TSEmitenteDPS.n2 = TSEmitenteDPS._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
TSEmitenteDPS.n3 = TSEmitenteDPS._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
TSEmitenteDPS._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSEmitenteDPS._InitializeFacetMap(TSEmitenteDPS._CF_enumeration,
   TSEmitenteDPS._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSEmitenteDPS', TSEmitenteDPS)
_module_typeBindings.TSEmitenteDPS = TSEmitenteDPS

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSMotivoEmisTI
class TSMotivoEmisTI (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        Motivo da Emissão da DPS pelo Tomador/Intermediário:
        1 - Importação de Serviço;
        2 - Tomador/Intermediário obrigado a emitir NFS-e por legislação municipal;
        3 - Tomador/Intermediário emitindo NFS-e por recusa de emissão pelo prestador;
        4 - Tomador/Intermediário emitindo por rejeitar a NFS-e emitida pelo prestador;
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSMotivoEmisTI')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 178, 2)
    _Documentation = '\n        Motivo da Emissão da DPS pelo Tomador/Intermediário:\n        1 - Importação de Serviço;\n        2 - Tomador/Intermediário obrigado a emitir NFS-e por legislação municipal;\n        3 - Tomador/Intermediário emitindo NFS-e por recusa de emissão pelo prestador;\n        4 - Tomador/Intermediário emitindo por rejeitar a NFS-e emitida pelo prestador;\n      '
TSMotivoEmisTI._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSMotivoEmisTI)
TSMotivoEmisTI.n1 = TSMotivoEmisTI._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
TSMotivoEmisTI.n2 = TSMotivoEmisTI._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
TSMotivoEmisTI.n3 = TSMotivoEmisTI._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
TSMotivoEmisTI.n4 = TSMotivoEmisTI._CF_enumeration.addEnumeration(unicode_value='4', tag='n4')
TSMotivoEmisTI._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSMotivoEmisTI._InitializeFacetMap(TSMotivoEmisTI._CF_enumeration,
   TSMotivoEmisTI._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSMotivoEmisTI', TSMotivoEmisTI)
_module_typeBindings.TSMotivoEmisTI = TSMotivoEmisTI

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSChaveNFSe
class TSChaveNFSe (pyxb.binding.datatypes.string):

    """Tipo Chave da Nota Fiscal de Serviço Eletrônica"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSChaveNFSe')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 196, 2)
    _Documentation = 'Tipo Chave da Nota Fiscal de Serviço Eletrônica'
TSChaveNFSe._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50))
TSChaveNFSe._CF_pattern = pyxb.binding.facets.CF_pattern()
TSChaveNFSe._CF_pattern.addPattern(pattern='[0-9]{50}')
TSChaveNFSe._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSChaveNFSe._InitializeFacetMap(TSChaveNFSe._CF_maxLength,
   TSChaveNFSe._CF_pattern,
   TSChaveNFSe._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSChaveNFSe', TSChaveNFSe)
_module_typeBindings.TSChaveNFSe = TSChaveNFSe

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSChaveNFe
class TSChaveNFe (pyxb.binding.datatypes.string):

    """Tipo Chave da Nota Fiscal Eletrônica - NF-e"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSChaveNFe')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 206, 2)
    _Documentation = 'Tipo Chave da Nota Fiscal Eletrônica - NF-e'
TSChaveNFe._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(44))
TSChaveNFe._CF_pattern = pyxb.binding.facets.CF_pattern()
TSChaveNFe._CF_pattern.addPattern(pattern='[0-9]{44}')
TSChaveNFe._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSChaveNFe._InitializeFacetMap(TSChaveNFe._CF_maxLength,
   TSChaveNFe._CF_pattern,
   TSChaveNFe._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSChaveNFe', TSChaveNFe)
_module_typeBindings.TSChaveNFe = TSChaveNFe

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSCodJustCanc
class TSCodJustCanc (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        Código de justificativa de cancelamento:
        1 - Erro na Emissão;
        2 - Serviço não Prestado;
        9 - Outros;
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSCodJustCanc')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 216, 2)
    _Documentation = '\n        Código de justificativa de cancelamento:\n        1 - Erro na Emissão;\n        2 - Serviço não Prestado;\n        9 - Outros;\n      '
TSCodJustCanc._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSCodJustCanc)
TSCodJustCanc.n1 = TSCodJustCanc._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
TSCodJustCanc.n2 = TSCodJustCanc._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
TSCodJustCanc.n9 = TSCodJustCanc._CF_enumeration.addEnumeration(unicode_value='9', tag='n9')
TSCodJustCanc._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSCodJustCanc._InitializeFacetMap(TSCodJustCanc._CF_enumeration,
   TSCodJustCanc._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSCodJustCanc', TSCodJustCanc)
_module_typeBindings.TSCodJustCanc = TSCodJustCanc

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSCodJustSubst
class TSCodJustSubst (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        Código de justificativa para substituição de NFS-e:
        01 - Desenquadramento de NFS-e do Simples Nacional;
        02 - Enquadramento de NFS-e no Simples Nacional;
        03 - Inclusão Retroativa de Imunidade/Isenção para NFS-e;
        04 - Exclusão Retroativa de Imunidade/Isenção para NFS-e;
        05 - Rejeição de NFS-e pelo tomador ou pelo intermediário se responsável pelo recolhimento do tributo;
        99 - Outros;
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSCodJustSubst')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 232, 2)
    _Documentation = '\n        Código de justificativa para substituição de NFS-e:\n        01 - Desenquadramento de NFS-e do Simples Nacional;\n        02 - Enquadramento de NFS-e no Simples Nacional;\n        03 - Inclusão Retroativa de Imunidade/Isenção para NFS-e;\n        04 - Exclusão Retroativa de Imunidade/Isenção para NFS-e;\n        05 - Rejeição de NFS-e pelo tomador ou pelo intermediário se responsável pelo recolhimento do tributo;\n        99 - Outros;\n      '
TSCodJustSubst._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSCodJustSubst)
TSCodJustSubst.n01 = TSCodJustSubst._CF_enumeration.addEnumeration(unicode_value='01', tag='n01')
TSCodJustSubst.n02 = TSCodJustSubst._CF_enumeration.addEnumeration(unicode_value='02', tag='n02')
TSCodJustSubst.n03 = TSCodJustSubst._CF_enumeration.addEnumeration(unicode_value='03', tag='n03')
TSCodJustSubst.n04 = TSCodJustSubst._CF_enumeration.addEnumeration(unicode_value='04', tag='n04')
TSCodJustSubst.n05 = TSCodJustSubst._CF_enumeration.addEnumeration(unicode_value='05', tag='n05')
TSCodJustSubst.n99 = TSCodJustSubst._CF_enumeration.addEnumeration(unicode_value='99', tag='n99')
TSCodJustSubst._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSCodJustSubst._InitializeFacetMap(TSCodJustSubst._CF_enumeration,
   TSCodJustSubst._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSCodJustSubst', TSCodJustSubst)
_module_typeBindings.TSCodJustSubst = TSCodJustSubst

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSCodJustAnaliseFiscalCanc
class TSCodJustAnaliseFiscalCanc (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        Código do motivo da solicitação de análise fiscal para cancelamento de NFS-e:
        1 - Erro na Emissão;
        2 - Serviço não Prestado;
        3 - Outros.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSCodJustAnaliseFiscalCanc')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 254, 2)
    _Documentation = '\n        Código do motivo da solicitação de análise fiscal para cancelamento de NFS-e:\n        1 - Erro na Emissão;\n        2 - Serviço não Prestado;\n        3 - Outros.\n      '
TSCodJustAnaliseFiscalCanc._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSCodJustAnaliseFiscalCanc)
TSCodJustAnaliseFiscalCanc.n1 = TSCodJustAnaliseFiscalCanc._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
TSCodJustAnaliseFiscalCanc.n2 = TSCodJustAnaliseFiscalCanc._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
TSCodJustAnaliseFiscalCanc.n9 = TSCodJustAnaliseFiscalCanc._CF_enumeration.addEnumeration(unicode_value='9', tag='n9')
TSCodJustAnaliseFiscalCanc._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSCodJustAnaliseFiscalCanc._InitializeFacetMap(TSCodJustAnaliseFiscalCanc._CF_enumeration,
   TSCodJustAnaliseFiscalCanc._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSCodJustAnaliseFiscalCanc', TSCodJustAnaliseFiscalCanc)
_module_typeBindings.TSCodJustAnaliseFiscalCanc = TSCodJustAnaliseFiscalCanc

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSCodMotivoRejeicao
class TSCodMotivoRejeicao (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        Motivo da Rejeição da NFS-e:
        1 - NFS-e em duplicidade;
        2 - NFS-e já emitida pelo tomador;
        3 - Não ocorrência do fato gerador;
        4 - Erro quanto a responsabilidade tributária;
        5 - Erro quanto ao valor do serviço, valor das deduções ou serviço prestado ou data do fato gerador;
        9 - Outros;
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSCodMotivoRejeicao')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 270, 2)
    _Documentation = '\n        Motivo da Rejeição da NFS-e:\n        1 - NFS-e em duplicidade;\n        2 - NFS-e já emitida pelo tomador;\n        3 - Não ocorrência do fato gerador;\n        4 - Erro quanto a responsabilidade tributária;\n        5 - Erro quanto ao valor do serviço, valor das deduções ou serviço prestado ou data do fato gerador;\n        9 - Outros;\n      '
TSCodMotivoRejeicao._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSCodMotivoRejeicao)
TSCodMotivoRejeicao.n1 = TSCodMotivoRejeicao._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
TSCodMotivoRejeicao.n2 = TSCodMotivoRejeicao._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
TSCodMotivoRejeicao.n3 = TSCodMotivoRejeicao._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
TSCodMotivoRejeicao.n4 = TSCodMotivoRejeicao._CF_enumeration.addEnumeration(unicode_value='4', tag='n4')
TSCodMotivoRejeicao.n5 = TSCodMotivoRejeicao._CF_enumeration.addEnumeration(unicode_value='5', tag='n5')
TSCodMotivoRejeicao.n9 = TSCodMotivoRejeicao._CF_enumeration.addEnumeration(unicode_value='9', tag='n9')
TSCodMotivoRejeicao._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSCodMotivoRejeicao._InitializeFacetMap(TSCodMotivoRejeicao._CF_enumeration,
   TSCodMotivoRejeicao._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSCodMotivoRejeicao', TSCodMotivoRejeicao)
_module_typeBindings.TSCodMotivoRejeicao = TSCodMotivoRejeicao

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSCodJustAnaliseFiscalCancDef
class TSCodJustAnaliseFiscalCancDef (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        Resposta da análise da solicitação do cancelamento extemporâneo de NFS-e:
        1 - Cancelamento Extemporâneo Deferido.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSCodJustAnaliseFiscalCancDef')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 292, 2)
    _Documentation = '\n        Resposta da análise da solicitação do cancelamento extemporâneo de NFS-e:\n        1 - Cancelamento Extemporâneo Deferido.\n      '
TSCodJustAnaliseFiscalCancDef._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSCodJustAnaliseFiscalCancDef)
TSCodJustAnaliseFiscalCancDef.n1 = TSCodJustAnaliseFiscalCancDef._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
TSCodJustAnaliseFiscalCancDef._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSCodJustAnaliseFiscalCancDef._InitializeFacetMap(TSCodJustAnaliseFiscalCancDef._CF_enumeration,
   TSCodJustAnaliseFiscalCancDef._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSCodJustAnaliseFiscalCancDef', TSCodJustAnaliseFiscalCancDef)
_module_typeBindings.TSCodJustAnaliseFiscalCancDef = TSCodJustAnaliseFiscalCancDef

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSCodJustAnaliseFiscalCancIndef
class TSCodJustAnaliseFiscalCancIndef (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        Resposta da análise da solicitação do cancelamento extemporâneo de NFS-e:
        1 - Cancelamento Extemporâneo Indeferido;
        2 - Cancelamento Extemporâneo Indeferido Sem Análise de Mérito.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSCodJustAnaliseFiscalCancIndef')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 304, 2)
    _Documentation = '\n        Resposta da análise da solicitação do cancelamento extemporâneo de NFS-e:\n        1 - Cancelamento Extemporâneo Indeferido;\n        2 - Cancelamento Extemporâneo Indeferido Sem Análise de Mérito.\n      '
TSCodJustAnaliseFiscalCancIndef._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSCodJustAnaliseFiscalCancIndef)
TSCodJustAnaliseFiscalCancIndef.n1 = TSCodJustAnaliseFiscalCancIndef._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
TSCodJustAnaliseFiscalCancIndef.n2 = TSCodJustAnaliseFiscalCancIndef._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
TSCodJustAnaliseFiscalCancIndef._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSCodJustAnaliseFiscalCancIndef._InitializeFacetMap(TSCodJustAnaliseFiscalCancIndef._CF_enumeration,
   TSCodJustAnaliseFiscalCancIndef._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSCodJustAnaliseFiscalCancIndef', TSCodJustAnaliseFiscalCancIndef)
_module_typeBindings.TSCodJustAnaliseFiscalCancIndef = TSCodJustAnaliseFiscalCancIndef

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSNumProcAdmAnaliseFiscalCanc
class TSNumProcAdmAnaliseFiscalCanc (pyxb.binding.datatypes.string):

    """Número do processo administrativo municipal vinculado à solicitação de cancelamento extemporâneo de NFS-e."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSNumProcAdmAnaliseFiscalCanc')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 318, 2)
    _Documentation = 'Número do processo administrativo municipal vinculado à solicitação de cancelamento extemporâneo de NFS-e.'
TSNumProcAdmAnaliseFiscalCanc._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
TSNumProcAdmAnaliseFiscalCanc._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSNumProcAdmAnaliseFiscalCanc._CF_pattern = pyxb.binding.facets.CF_pattern()
TSNumProcAdmAnaliseFiscalCanc._CF_pattern.addPattern(pattern='[0-9]{1,30}')
TSNumProcAdmAnaliseFiscalCanc._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSNumProcAdmAnaliseFiscalCanc._InitializeFacetMap(TSNumProcAdmAnaliseFiscalCanc._CF_maxLength,
   TSNumProcAdmAnaliseFiscalCanc._CF_minLength,
   TSNumProcAdmAnaliseFiscalCanc._CF_pattern,
   TSNumProcAdmAnaliseFiscalCanc._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSNumProcAdmAnaliseFiscalCanc', TSNumProcAdmAnaliseFiscalCanc)
_module_typeBindings.TSNumProcAdmAnaliseFiscalCanc = TSNumProcAdmAnaliseFiscalCanc

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSCodAutorManifestacao
class TSCodAutorManifestacao (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        Tipo do autor da manifestação da NFS-e:
        1 - Prestador;
        2 - Tomador;
        3 - Intermediário.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSCodAutorManifestacao')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 329, 2)
    _Documentation = '\n        Tipo do autor da manifestação da NFS-e:\n        1 - Prestador;\n        2 - Tomador;\n        3 - Intermediário.\n      '
TSCodAutorManifestacao._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSCodAutorManifestacao)
TSCodAutorManifestacao.n1 = TSCodAutorManifestacao._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
TSCodAutorManifestacao.n2 = TSCodAutorManifestacao._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
TSCodAutorManifestacao.n3 = TSCodAutorManifestacao._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
TSCodAutorManifestacao._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSCodAutorManifestacao._InitializeFacetMap(TSCodAutorManifestacao._CF_enumeration,
   TSCodAutorManifestacao._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSCodAutorManifestacao', TSCodAutorManifestacao)
_module_typeBindings.TSCodAutorManifestacao = TSCodAutorManifestacao

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSCNPJ
class TSCNPJ (pyxb.binding.datatypes.string):

    """Tipo Número do CNPJ"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSCNPJ')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 354, 2)
    _Documentation = 'Tipo Número do CNPJ'
TSCNPJ._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(14))
TSCNPJ._CF_pattern = pyxb.binding.facets.CF_pattern()
TSCNPJ._CF_pattern.addPattern(pattern='[0-9]{14}')
TSCNPJ._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSCNPJ._InitializeFacetMap(TSCNPJ._CF_maxLength,
   TSCNPJ._CF_pattern,
   TSCNPJ._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSCNPJ', TSCNPJ)
_module_typeBindings.TSCNPJ = TSCNPJ

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSCPF
class TSCPF (pyxb.binding.datatypes.string):

    """Tipo Número do CPF"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSCPF')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 364, 2)
    _Documentation = 'Tipo Número do CPF'
TSCPF._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(11))
TSCPF._CF_pattern = pyxb.binding.facets.CF_pattern()
TSCPF._CF_pattern.addPattern(pattern='[0-9]{11}')
TSCPF._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSCPF._InitializeFacetMap(TSCPF._CF_maxLength,
   TSCPF._CF_pattern,
   TSCPF._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSCPF', TSCPF)
_module_typeBindings.TSCPF = TSCPF

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSCAEPF
class TSCAEPF (pyxb.binding.datatypes.string):

    """Tipo Número do CAEPF"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSCAEPF')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 374, 2)
    _Documentation = 'Tipo Número do CAEPF'
TSCAEPF._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(14))
TSCAEPF._CF_pattern = pyxb.binding.facets.CF_pattern()
TSCAEPF._CF_pattern.addPattern(pattern='[0-9]{14}')
TSCAEPF._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSCAEPF._InitializeFacetMap(TSCAEPF._CF_maxLength,
   TSCAEPF._CF_pattern,
   TSCAEPF._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSCAEPF', TSCAEPF)
_module_typeBindings.TSCAEPF = TSCAEPF

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSNIF
class TSNIF (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSNIF')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 384, 2)
    _Documentation = None
TSNIF._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(40))
TSNIF._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSNIF._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSNIF._InitializeFacetMap(TSNIF._CF_maxLength,
   TSNIF._CF_minLength,
   TSNIF._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSNIF', TSNIF)
_module_typeBindings.TSNIF = TSNIF

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSCodNaoNIF
class TSCodNaoNIF (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        Motivo para não informação do NIF:
        0 - Não informado na nota de origem;
        1 - Dispensado do NIF;
        2 - Não exigência do NIF;
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSCodNaoNIF')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 391, 2)
    _Documentation = '\n        Motivo para não informação do NIF:\n        0 - Não informado na nota de origem;\n        1 - Dispensado do NIF;\n        2 - Não exigência do NIF;\n      '
TSCodNaoNIF._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSCodNaoNIF)
TSCodNaoNIF.n0 = TSCodNaoNIF._CF_enumeration.addEnumeration(unicode_value='0', tag='n0')
TSCodNaoNIF.n1 = TSCodNaoNIF._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
TSCodNaoNIF.n2 = TSCodNaoNIF._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
TSCodNaoNIF._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSCodNaoNIF._InitializeFacetMap(TSCodNaoNIF._CF_enumeration,
   TSCodNaoNIF._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSCodNaoNIF', TSCodNaoNIF)
_module_typeBindings.TSCodNaoNIF = TSCodNaoNIF

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSInscMun
class TSInscMun (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSInscMun')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 407, 2)
    _Documentation = None
TSInscMun._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(15))
TSInscMun._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSInscMun._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSInscMun._InitializeFacetMap(TSInscMun._CF_maxLength,
   TSInscMun._CF_minLength,
   TSInscMun._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSInscMun', TSInscMun)
_module_typeBindings.TSInscMun = TSInscMun

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSNomeRazaoSocial
class TSNomeRazaoSocial (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSNomeRazaoSocial')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 414, 2)
    _Documentation = None
TSNomeRazaoSocial._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(300))
TSNomeRazaoSocial._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSNomeRazaoSocial._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSNomeRazaoSocial._InitializeFacetMap(TSNomeRazaoSocial._CF_maxLength,
   TSNomeRazaoSocial._CF_minLength,
   TSNomeRazaoSocial._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSNomeRazaoSocial', TSNomeRazaoSocial)
_module_typeBindings.TSNomeRazaoSocial = TSNomeRazaoSocial

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSNomeFantasia
class TSNomeFantasia (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSNomeFantasia')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 421, 2)
    _Documentation = None
TSNomeFantasia._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(150))
TSNomeFantasia._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSNomeFantasia._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSNomeFantasia._InitializeFacetMap(TSNomeFantasia._CF_maxLength,
   TSNomeFantasia._CF_minLength,
   TSNomeFantasia._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSNomeFantasia', TSNomeFantasia)
_module_typeBindings.TSNomeFantasia = TSNomeFantasia

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSUF
class TSUF (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """Tipo Sigla da UF"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSUF')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 464, 2)
    _Documentation = 'Tipo Sigla da UF'
TSUF._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSUF)
TSUF.AC = TSUF._CF_enumeration.addEnumeration(unicode_value='AC', tag='AC')
TSUF.AL = TSUF._CF_enumeration.addEnumeration(unicode_value='AL', tag='AL')
TSUF.AM = TSUF._CF_enumeration.addEnumeration(unicode_value='AM', tag='AM')
TSUF.AP = TSUF._CF_enumeration.addEnumeration(unicode_value='AP', tag='AP')
TSUF.BA = TSUF._CF_enumeration.addEnumeration(unicode_value='BA', tag='BA')
TSUF.CE = TSUF._CF_enumeration.addEnumeration(unicode_value='CE', tag='CE')
TSUF.DF = TSUF._CF_enumeration.addEnumeration(unicode_value='DF', tag='DF')
TSUF.ES = TSUF._CF_enumeration.addEnumeration(unicode_value='ES', tag='ES')
TSUF.GO = TSUF._CF_enumeration.addEnumeration(unicode_value='GO', tag='GO')
TSUF.MA = TSUF._CF_enumeration.addEnumeration(unicode_value='MA', tag='MA')
TSUF.MG = TSUF._CF_enumeration.addEnumeration(unicode_value='MG', tag='MG')
TSUF.MS = TSUF._CF_enumeration.addEnumeration(unicode_value='MS', tag='MS')
TSUF.MT = TSUF._CF_enumeration.addEnumeration(unicode_value='MT', tag='MT')
TSUF.PA = TSUF._CF_enumeration.addEnumeration(unicode_value='PA', tag='PA')
TSUF.PB = TSUF._CF_enumeration.addEnumeration(unicode_value='PB', tag='PB')
TSUF.PE = TSUF._CF_enumeration.addEnumeration(unicode_value='PE', tag='PE')
TSUF.PI = TSUF._CF_enumeration.addEnumeration(unicode_value='PI', tag='PI')
TSUF.PR = TSUF._CF_enumeration.addEnumeration(unicode_value='PR', tag='PR')
TSUF.RJ = TSUF._CF_enumeration.addEnumeration(unicode_value='RJ', tag='RJ')
TSUF.RN = TSUF._CF_enumeration.addEnumeration(unicode_value='RN', tag='RN')
TSUF.RO = TSUF._CF_enumeration.addEnumeration(unicode_value='RO', tag='RO')
TSUF.RR = TSUF._CF_enumeration.addEnumeration(unicode_value='RR', tag='RR')
TSUF.RS = TSUF._CF_enumeration.addEnumeration(unicode_value='RS', tag='RS')
TSUF.SC = TSUF._CF_enumeration.addEnumeration(unicode_value='SC', tag='SC')
TSUF.SE = TSUF._CF_enumeration.addEnumeration(unicode_value='SE', tag='SE')
TSUF.SP = TSUF._CF_enumeration.addEnumeration(unicode_value='SP', tag='SP')
TSUF.TO = TSUF._CF_enumeration.addEnumeration(unicode_value='TO', tag='TO')
TSUF._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSUF._InitializeFacetMap(TSUF._CF_enumeration,
   TSUF._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSUF', TSUF)
_module_typeBindings.TSUF = TSUF

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSCEP
class TSCEP (pyxb.binding.datatypes.string):

    """CEP"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSCEP')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 499, 2)
    _Documentation = 'CEP'
TSCEP._CF_pattern = pyxb.binding.facets.CF_pattern()
TSCEP._CF_pattern.addPattern(pattern='[0-9]{8}')
TSCEP._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSCEP._InitializeFacetMap(TSCEP._CF_pattern,
   TSCEP._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSCEP', TSCEP)
_module_typeBindings.TSCEP = TSCEP

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSCodigoEndPostal
class TSCodigoEndPostal (pyxb.binding.datatypes.string):

    """Código de enderaçamento postal"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSCodigoEndPostal')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 508, 2)
    _Documentation = 'Código de enderaçamento postal'
TSCodigoEndPostal._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(11))
TSCodigoEndPostal._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSCodigoEndPostal._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSCodigoEndPostal._InitializeFacetMap(TSCodigoEndPostal._CF_maxLength,
   TSCodigoEndPostal._CF_minLength,
   TSCodigoEndPostal._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSCodigoEndPostal', TSCodigoEndPostal)
_module_typeBindings.TSCodigoEndPostal = TSCodigoEndPostal

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSCidade
class TSCidade (pyxb.binding.datatypes.string):

    """Cidade"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSCidade')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 518, 2)
    _Documentation = 'Cidade'
TSCidade._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60))
TSCidade._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSCidade._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSCidade._InitializeFacetMap(TSCidade._CF_maxLength,
   TSCidade._CF_minLength,
   TSCidade._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSCidade', TSCidade)
_module_typeBindings.TSCidade = TSCidade

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSEstadoProvRegiao
class TSEstadoProvRegiao (pyxb.binding.datatypes.string):

    """Estado, província ou região"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSEstadoProvRegiao')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 528, 2)
    _Documentation = 'Estado, província ou região'
TSEstadoProvRegiao._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60))
TSEstadoProvRegiao._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSEstadoProvRegiao._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSEstadoProvRegiao._InitializeFacetMap(TSEstadoProvRegiao._CF_maxLength,
   TSEstadoProvRegiao._CF_minLength,
   TSEstadoProvRegiao._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSEstadoProvRegiao', TSEstadoProvRegiao)
_module_typeBindings.TSEstadoProvRegiao = TSEstadoProvRegiao

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSTelefone
class TSTelefone (pyxb.binding.datatypes.string):

    """
        Número do telefone do prestador:
        Preencher com o Código DDD + número do telefone.
        Nas operações com exterior é permitido informar o código do país + código da localidade + número do telefone
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSTelefone')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 545, 2)
    _Documentation = '\n        Número do telefone do prestador:\n        Preencher com o Código DDD + número do telefone.\n        Nas operações com exterior é permitido informar o código do país + código da localidade + número do telefone\n      '
TSTelefone._CF_pattern = pyxb.binding.facets.CF_pattern()
TSTelefone._CF_pattern.addPattern(pattern='[0-9]{6,20}')
TSTelefone._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSTelefone._InitializeFacetMap(TSTelefone._CF_pattern,
   TSTelefone._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSTelefone', TSTelefone)
_module_typeBindings.TSTelefone = TSTelefone

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TCCodTribMun
class TCCodTribMun (pyxb.binding.datatypes.string):

    """Código de tributação municipal do ISSQN"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCCodTribMun')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 565, 2)
    _Documentation = 'Código de tributação municipal do ISSQN'
TCCodTribMun._CF_pattern = pyxb.binding.facets.CF_pattern()
TCCodTribMun._CF_pattern.addPattern(pattern='[0-9]{3}')
TCCodTribMun._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TCCodTribMun._InitializeFacetMap(TCCodTribMun._CF_pattern,
   TCCodTribMun._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TCCodTribMun', TCCodTribMun)
_module_typeBindings.TCCodTribMun = TCCodTribMun

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSCodMoeda
class TSCodMoeda (pyxb.binding.datatypes.string):

    """Tipo com código que identifica a moeda conforme tabela do BACEN"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSCodMoeda')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 574, 2)
    _Documentation = 'Tipo com código que identifica a moeda conforme tabela do BACEN'
TSCodMoeda._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(3))
TSCodMoeda._CF_pattern = pyxb.binding.facets.CF_pattern()
TSCodMoeda._CF_pattern.addPattern(pattern='[0-9]{3}')
TSCodMoeda._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSCodMoeda._InitializeFacetMap(TSCodMoeda._CF_maxLength,
   TSCodMoeda._CF_pattern,
   TSCodMoeda._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSCodMoeda', TSCodMoeda)
_module_typeBindings.TSCodMoeda = TSCodMoeda

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSModoPrestacao
class TSModoPrestacao (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
	    Modo de Prestação:
        0 - Desconhecido (tipo não informado na nota de origem);
        1 - Transfronteiriço;
        2 - Consumo no Brasil;
        3 - Presença Comercial no Exterior;
        4 - Movimento Temporário de Pessoas Físicas;
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSModoPrestacao')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 584, 2)
    _Documentation = '\n\t    Modo de Prestação:\n        0 - Desconhecido (tipo não informado na nota de origem);\n        1 - Transfronteiriço;\n        2 - Consumo no Brasil;\n        3 - Presença Comercial no Exterior;\n        4 - Movimento Temporário de Pessoas Físicas;\n      '
TSModoPrestacao._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSModoPrestacao)
TSModoPrestacao.n0 = TSModoPrestacao._CF_enumeration.addEnumeration(unicode_value='0', tag='n0')
TSModoPrestacao.n1 = TSModoPrestacao._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
TSModoPrestacao.n2 = TSModoPrestacao._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
TSModoPrestacao.n3 = TSModoPrestacao._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
TSModoPrestacao.n4 = TSModoPrestacao._CF_enumeration.addEnumeration(unicode_value='4', tag='n4')
TSModoPrestacao._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSModoPrestacao._InitializeFacetMap(TSModoPrestacao._CF_enumeration,
   TSModoPrestacao._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSModoPrestacao', TSModoPrestacao)
_module_typeBindings.TSModoPrestacao = TSModoPrestacao

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSVincPrest
class TSVincPrest (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        Vínculo entre as partes no negócio:
        0 - Sem vínculo com o Tomador/Prestador
        1 - Controlada;
        2 - Controladora;
        3 - Coligada;
        4 - Matriz;
        5 - Filial ou sucursal;
        6 - Outro vínculo;
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSVincPrest')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 604, 2)
    _Documentation = '\n        Vínculo entre as partes no negócio:\n        0 - Sem vínculo com o Tomador/Prestador\n        1 - Controlada;\n        2 - Controladora;\n        3 - Coligada;\n        4 - Matriz;\n        5 - Filial ou sucursal;\n        6 - Outro vínculo;\n      '
TSVincPrest._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSVincPrest)
TSVincPrest.n0 = TSVincPrest._CF_enumeration.addEnumeration(unicode_value='0', tag='n0')
TSVincPrest.n1 = TSVincPrest._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
TSVincPrest.n2 = TSVincPrest._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
TSVincPrest.n3 = TSVincPrest._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
TSVincPrest.n4 = TSVincPrest._CF_enumeration.addEnumeration(unicode_value='4', tag='n4')
TSVincPrest.n5 = TSVincPrest._CF_enumeration.addEnumeration(unicode_value='5', tag='n5')
TSVincPrest.n6 = TSVincPrest._CF_enumeration.addEnumeration(unicode_value='6', tag='n6')
TSVincPrest._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSVincPrest._InitializeFacetMap(TSVincPrest._CF_enumeration,
   TSVincPrest._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSVincPrest', TSVincPrest)
_module_typeBindings.TSVincPrest = TSVincPrest

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSMecAFComExPrest
class TSMecAFComExPrest (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        Mecanismo de apoio/fomento ao Comércio Exterior utilizado pelo prestador do serviço:
        00 - Desconhecido (tipo não informado na nota de origem);
        01 - Nenhum;
        02 - ACC - Adiantamento sobre Contrato de Câmbio – Redução a Zero do IR e do IOF;
        03 - ACE – Adiantamento sobre Cambiais Entregues - Redução a Zero do IR e do IOF;
        04 - BNDES-Exim Pós-Embarque – Serviços;
        05 - BNDES-Exim Pré-Embarque - Serviços;
        06 - FGE - Fundo de Garantia à Exportação;
        07 - PROEX - EQUALIZAÇÃO
        08 - PROEX - Financiamento;
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSMecAFComExPrest')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 628, 2)
    _Documentation = '\n        Mecanismo de apoio/fomento ao Comércio Exterior utilizado pelo prestador do serviço:\n        00 - Desconhecido (tipo não informado na nota de origem);\n        01 - Nenhum;\n        02 - ACC - Adiantamento sobre Contrato de Câmbio – Redução a Zero do IR e do IOF;\n        03 - ACE – Adiantamento sobre Cambiais Entregues - Redução a Zero do IR e do IOF;\n        04 - BNDES-Exim Pós-Embarque – Serviços;\n        05 - BNDES-Exim Pré-Embarque - Serviços;\n        06 - FGE - Fundo de Garantia à Exportação;\n        07 - PROEX - EQUALIZAÇÃO\n        08 - PROEX - Financiamento;\n      '
TSMecAFComExPrest._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSMecAFComExPrest)
TSMecAFComExPrest.n00 = TSMecAFComExPrest._CF_enumeration.addEnumeration(unicode_value='00', tag='n00')
TSMecAFComExPrest.n01 = TSMecAFComExPrest._CF_enumeration.addEnumeration(unicode_value='01', tag='n01')
TSMecAFComExPrest.n02 = TSMecAFComExPrest._CF_enumeration.addEnumeration(unicode_value='02', tag='n02')
TSMecAFComExPrest.n03 = TSMecAFComExPrest._CF_enumeration.addEnumeration(unicode_value='03', tag='n03')
TSMecAFComExPrest.n04 = TSMecAFComExPrest._CF_enumeration.addEnumeration(unicode_value='04', tag='n04')
TSMecAFComExPrest.n05 = TSMecAFComExPrest._CF_enumeration.addEnumeration(unicode_value='05', tag='n05')
TSMecAFComExPrest.n06 = TSMecAFComExPrest._CF_enumeration.addEnumeration(unicode_value='06', tag='n06')
TSMecAFComExPrest.n07 = TSMecAFComExPrest._CF_enumeration.addEnumeration(unicode_value='07', tag='n07')
TSMecAFComExPrest.n08 = TSMecAFComExPrest._CF_enumeration.addEnumeration(unicode_value='08', tag='n08')
TSMecAFComExPrest._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSMecAFComExPrest._InitializeFacetMap(TSMecAFComExPrest._CF_enumeration,
   TSMecAFComExPrest._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSMecAFComExPrest', TSMecAFComExPrest)
_module_typeBindings.TSMecAFComExPrest = TSMecAFComExPrest

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSMecAFComExToma
class TSMecAFComExToma (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        Mecanismo de apoio/fomento ao Comércio Exterior utilizado pelo tomador do serviço:
        00 - Desconhecido (tipo não informado na nota de origem);
        01 - Nenhum;
        02 - Adm. Pública e Repr. Internacional;
        03 - Alugueis e Arrend. Mercantil de maquinas, equip., embarc. e aeronaves;
        04 - Arrendamento Mercantil de aeronave para empresa de transporte aéreo público;
        05 - Comissão a agentes externos na exportação;
        06 - Despesas de armazenagem, mov. e transporte de carga no exterior;
        07 - Eventos FIFA (subsidiária);
        08 - Eventos FIFA;
        09 - Fretes, arrendamentos de embarcações ou aeronaves e outros;
        10 - Material Aeronáutico;
        11 - Promoção de Bens no Exterior;
        12 - Promoção de Dest. Turísticos Brasileiros;
        13 - Promoção do Brasil no Exterior;
        14 - Promoção Serviços no Exterior;
        15 - RECINE;
        16 - RECOPA;
        17 - Registro e Manutenção de marcas, patentes e cultivares;
        18 - REICOMP;
        19 - REIDI;
        20 - REPENEC;
        21 - REPES;
        22 - RETAERO; 
        23 - RETID;
        24 - Royalties, Assistência Técnica, Científica e Assemelhados;
        25 - Serviços de avaliação da conformidade vinculados aos Acordos da OMC;
        26 - ZPE;
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSMecAFComExToma')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 656, 2)
    _Documentation = '\n        Mecanismo de apoio/fomento ao Comércio Exterior utilizado pelo tomador do serviço:\n        00 - Desconhecido (tipo não informado na nota de origem);\n        01 - Nenhum;\n        02 - Adm. Pública e Repr. Internacional;\n        03 - Alugueis e Arrend. Mercantil de maquinas, equip., embarc. e aeronaves;\n        04 - Arrendamento Mercantil de aeronave para empresa de transporte aéreo público;\n        05 - Comissão a agentes externos na exportação;\n        06 - Despesas de armazenagem, mov. e transporte de carga no exterior;\n        07 - Eventos FIFA (subsidiária);\n        08 - Eventos FIFA;\n        09 - Fretes, arrendamentos de embarcações ou aeronaves e outros;\n        10 - Material Aeronáutico;\n        11 - Promoção de Bens no Exterior;\n        12 - Promoção de Dest. Turísticos Brasileiros;\n        13 - Promoção do Brasil no Exterior;\n        14 - Promoção Serviços no Exterior;\n        15 - RECINE;\n        16 - RECOPA;\n        17 - Registro e Manutenção de marcas, patentes e cultivares;\n        18 - REICOMP;\n        19 - REIDI;\n        20 - REPENEC;\n        21 - REPES;\n        22 - RETAERO; \n        23 - RETID;\n        24 - Royalties, Assistência Técnica, Científica e Assemelhados;\n        25 - Serviços de avaliação da conformidade vinculados aos Acordos da OMC;\n        26 - ZPE;\n      '
TSMecAFComExToma._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSMecAFComExToma)
TSMecAFComExToma.n00 = TSMecAFComExToma._CF_enumeration.addEnumeration(unicode_value='00', tag='n00')
TSMecAFComExToma.n01 = TSMecAFComExToma._CF_enumeration.addEnumeration(unicode_value='01', tag='n01')
TSMecAFComExToma.n02 = TSMecAFComExToma._CF_enumeration.addEnumeration(unicode_value='02', tag='n02')
TSMecAFComExToma.n03 = TSMecAFComExToma._CF_enumeration.addEnumeration(unicode_value='03', tag='n03')
TSMecAFComExToma.n04 = TSMecAFComExToma._CF_enumeration.addEnumeration(unicode_value='04', tag='n04')
TSMecAFComExToma.n05 = TSMecAFComExToma._CF_enumeration.addEnumeration(unicode_value='05', tag='n05')
TSMecAFComExToma.n06 = TSMecAFComExToma._CF_enumeration.addEnumeration(unicode_value='06', tag='n06')
TSMecAFComExToma.n07 = TSMecAFComExToma._CF_enumeration.addEnumeration(unicode_value='07', tag='n07')
TSMecAFComExToma.n08 = TSMecAFComExToma._CF_enumeration.addEnumeration(unicode_value='08', tag='n08')
TSMecAFComExToma.n09 = TSMecAFComExToma._CF_enumeration.addEnumeration(unicode_value='09', tag='n09')
TSMecAFComExToma.n10 = TSMecAFComExToma._CF_enumeration.addEnumeration(unicode_value='10', tag='n10')
TSMecAFComExToma.n11 = TSMecAFComExToma._CF_enumeration.addEnumeration(unicode_value='11', tag='n11')
TSMecAFComExToma.n12 = TSMecAFComExToma._CF_enumeration.addEnumeration(unicode_value='12', tag='n12')
TSMecAFComExToma.n13 = TSMecAFComExToma._CF_enumeration.addEnumeration(unicode_value='13', tag='n13')
TSMecAFComExToma.n14 = TSMecAFComExToma._CF_enumeration.addEnumeration(unicode_value='14', tag='n14')
TSMecAFComExToma.n15 = TSMecAFComExToma._CF_enumeration.addEnumeration(unicode_value='15', tag='n15')
TSMecAFComExToma.n16 = TSMecAFComExToma._CF_enumeration.addEnumeration(unicode_value='16', tag='n16')
TSMecAFComExToma.n17 = TSMecAFComExToma._CF_enumeration.addEnumeration(unicode_value='17', tag='n17')
TSMecAFComExToma.n18 = TSMecAFComExToma._CF_enumeration.addEnumeration(unicode_value='18', tag='n18')
TSMecAFComExToma.n19 = TSMecAFComExToma._CF_enumeration.addEnumeration(unicode_value='19', tag='n19')
TSMecAFComExToma.n20 = TSMecAFComExToma._CF_enumeration.addEnumeration(unicode_value='20', tag='n20')
TSMecAFComExToma.n21 = TSMecAFComExToma._CF_enumeration.addEnumeration(unicode_value='21', tag='n21')
TSMecAFComExToma.n22 = TSMecAFComExToma._CF_enumeration.addEnumeration(unicode_value='22', tag='n22')
TSMecAFComExToma.n23 = TSMecAFComExToma._CF_enumeration.addEnumeration(unicode_value='23', tag='n23')
TSMecAFComExToma.n24 = TSMecAFComExToma._CF_enumeration.addEnumeration(unicode_value='24', tag='n24')
TSMecAFComExToma.n25 = TSMecAFComExToma._CF_enumeration.addEnumeration(unicode_value='25', tag='n25')
TSMecAFComExToma.n26 = TSMecAFComExToma._CF_enumeration.addEnumeration(unicode_value='26', tag='n26')
TSMecAFComExToma._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSMecAFComExToma._InitializeFacetMap(TSMecAFComExToma._CF_enumeration,
   TSMecAFComExToma._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSMecAFComExToma', TSMecAFComExToma)
_module_typeBindings.TSMecAFComExToma = TSMecAFComExToma

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSMovTempBens
class TSMovTempBens (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        Vínculo da Operação à Movimentação Temporária de Bens:
        0 - Desconhecido (tipo não informado na nota de origem);
        1 - Não;
        2 - Vinculada - Declaração de Importação;
        3 - Vinculada - Declaração de Exportação;
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSMovTempBens')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 720, 2)
    _Documentation = '\n        Vínculo da Operação à Movimentação Temporária de Bens:\n        0 - Desconhecido (tipo não informado na nota de origem);\n        1 - Não;\n        2 - Vinculada - Declaração de Importação;\n        3 - Vinculada - Declaração de Exportação;\n      '
TSMovTempBens._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSMovTempBens)
TSMovTempBens.n0 = TSMovTempBens._CF_enumeration.addEnumeration(unicode_value='0', tag='n0')
TSMovTempBens.n1 = TSMovTempBens._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
TSMovTempBens.n2 = TSMovTempBens._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
TSMovTempBens.n3 = TSMovTempBens._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
TSMovTempBens._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSMovTempBens._InitializeFacetMap(TSMovTempBens._CF_enumeration,
   TSMovTempBens._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSMovTempBens', TSMovTempBens)
_module_typeBindings.TSMovTempBens = TSMovTempBens

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSCategVeic
class TSCategVeic (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        Categorias de veículos para cobrança:
        00 - Categoria de veículos (tipo não informado na nota de origem)
        01 - Automóvel, caminhonete e furgão;
        02 - Caminhão leve, ônibus, caminhão trator e furgão;
        03 - Automóvel e caminhonete com semireboque;
        04 - Caminhão, caminhão-trator, caminhão-trator com semi-reboque e ônibus;
        05 - Automóvel e caminhonete com reboque;
        06 - Caminhão com reboque;
        07 - Caminhão trator com semi-reboque;
        08 - Motocicletas, motonetas e bicicletas motorizadas;
        09 - Veículo especial;
        10 - Veículo Isento;
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSCategVeic')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 738, 2)
    _Documentation = '\n        Categorias de veículos para cobrança:\n        00 - Categoria de veículos (tipo não informado na nota de origem)\n        01 - Automóvel, caminhonete e furgão;\n        02 - Caminhão leve, ônibus, caminhão trator e furgão;\n        03 - Automóvel e caminhonete com semireboque;\n        04 - Caminhão, caminhão-trator, caminhão-trator com semi-reboque e ônibus;\n        05 - Automóvel e caminhonete com reboque;\n        06 - Caminhão com reboque;\n        07 - Caminhão trator com semi-reboque;\n        08 - Motocicletas, motonetas e bicicletas motorizadas;\n        09 - Veículo especial;\n        10 - Veículo Isento;\n      '
TSCategVeic._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSCategVeic)
TSCategVeic.n00 = TSCategVeic._CF_enumeration.addEnumeration(unicode_value='00', tag='n00')
TSCategVeic.n01 = TSCategVeic._CF_enumeration.addEnumeration(unicode_value='01', tag='n01')
TSCategVeic.n02 = TSCategVeic._CF_enumeration.addEnumeration(unicode_value='02', tag='n02')
TSCategVeic.n03 = TSCategVeic._CF_enumeration.addEnumeration(unicode_value='03', tag='n03')
TSCategVeic.n04 = TSCategVeic._CF_enumeration.addEnumeration(unicode_value='04', tag='n04')
TSCategVeic.n05 = TSCategVeic._CF_enumeration.addEnumeration(unicode_value='05', tag='n05')
TSCategVeic.n06 = TSCategVeic._CF_enumeration.addEnumeration(unicode_value='06', tag='n06')
TSCategVeic.n07 = TSCategVeic._CF_enumeration.addEnumeration(unicode_value='07', tag='n07')
TSCategVeic.n08 = TSCategVeic._CF_enumeration.addEnumeration(unicode_value='08', tag='n08')
TSCategVeic.n09 = TSCategVeic._CF_enumeration.addEnumeration(unicode_value='09', tag='n09')
TSCategVeic.n10 = TSCategVeic._CF_enumeration.addEnumeration(unicode_value='10', tag='n10')
TSCategVeic._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSCategVeic._InitializeFacetMap(TSCategVeic._CF_enumeration,
   TSCategVeic._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSCategVeic', TSCategVeic)
_module_typeBindings.TSCategVeic = TSCategVeic

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSEnvMDIC
class TSEnvMDIC (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
		Compartilhar as informações da NFS-e gerada a partir desta DPS com a Secretaria de Comércio Exterior:
        0 - Não enviar para o MDIC;
        1 - Enviar para o MDIC;
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSEnvMDIC')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 788, 2)
    _Documentation = '\n\t\tCompartilhar as informações da NFS-e gerada a partir desta DPS com a Secretaria de Comércio Exterior:\n        0 - Não enviar para o MDIC;\n        1 - Enviar para o MDIC;\n      '
TSEnvMDIC._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSEnvMDIC)
TSEnvMDIC.n0 = TSEnvMDIC._CF_enumeration.addEnumeration(unicode_value='0', tag='n0')
TSEnvMDIC.n1 = TSEnvMDIC._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
TSEnvMDIC._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSEnvMDIC._InitializeFacetMap(TSEnvMDIC._CF_enumeration,
   TSEnvMDIC._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSEnvMDIC', TSEnvMDIC)
_module_typeBindings.TSEnvMDIC = TSEnvMDIC

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSPlaca
class TSPlaca (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSPlaca')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 802, 2)
    _Documentation = None
TSPlaca._CF_pattern = pyxb.binding.facets.CF_pattern()
TSPlaca._CF_pattern.addPattern(pattern='[A-Z]{2,3}[0-9]{4}|[A-Z]{3,4}[0-9]{3}')
TSPlaca._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSPlaca._InitializeFacetMap(TSPlaca._CF_pattern,
   TSPlaca._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSPlaca', TSPlaca)
_module_typeBindings.TSPlaca = TSPlaca

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSCodAcessoPed
class TSCodAcessoPed (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSCodAcessoPed')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 808, 2)
    _Documentation = None
TSCodAcessoPed._CF_pattern = pyxb.binding.facets.CF_pattern()
TSCodAcessoPed._CF_pattern.addPattern(pattern='[a-zA-Z0-9]{10}')
TSCodAcessoPed._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSCodAcessoPed._InitializeFacetMap(TSCodAcessoPed._CF_pattern,
   TSCodAcessoPed._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSCodAcessoPed', TSCodAcessoPed)
_module_typeBindings.TSCodAcessoPed = TSCodAcessoPed

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSCodContrato
class TSCodContrato (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSCodContrato')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 814, 2)
    _Documentation = None
TSCodContrato._CF_pattern = pyxb.binding.facets.CF_pattern()
TSCodContrato._CF_pattern.addPattern(pattern='[a-zA-Z0-9]{4}')
TSCodContrato._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSCodContrato._InitializeFacetMap(TSCodContrato._CF_pattern,
   TSCodContrato._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSCodContrato', TSCodContrato)
_module_typeBindings.TSCodContrato = TSCodContrato

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSNumEixos
class TSNumEixos (pyxb.binding.datatypes.string):

    """Número de eixos para fins de cobrança"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSNumEixos')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 820, 2)
    _Documentation = 'Número de eixos para fins de cobrança'
TSNumEixos._CF_pattern = pyxb.binding.facets.CF_pattern()
TSNumEixos._CF_pattern.addPattern(pattern='[0-9]{1,2}')
TSNumEixos._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSNumEixos._InitializeFacetMap(TSNumEixos._CF_pattern,
   TSNumEixos._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSNumEixos', TSNumEixos)
_module_typeBindings.TSNumEixos = TSNumEixos

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSRodagem
class TSRodagem (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
		Tipo de rodagem:
        1 - Simples;
        2 - Dupla;
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSRodagem')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 829, 2)
    _Documentation = '\n\t\tTipo de rodagem:\n        1 - Simples;\n        2 - Dupla;\n      '
TSRodagem._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSRodagem)
TSRodagem.n1 = TSRodagem._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
TSRodagem.n2 = TSRodagem._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
TSRodagem._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSRodagem._InitializeFacetMap(TSRodagem._CF_enumeration,
   TSRodagem._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSRodagem', TSRodagem)
_module_typeBindings.TSRodagem = TSRodagem

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSSentido
class TSSentido (pyxb.binding.datatypes.string):

    """Orientação de passagem do veículo: ângulo em graus a partir do norte geográfico em sentido horário, número inteiro de 0 a 359, onde 0º seria o norte, 90º o leste, 180º o sul, 270º o oeste. Precisão mínima de 10"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSSentido')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 843, 2)
    _Documentation = 'Orientação de passagem do veículo: ângulo em graus a partir do norte geográfico em sentido horário, número inteiro de 0 a 359, onde 0º seria o norte, 90º o leste, 180º o sul, 270º o oeste. Precisão mínima de 10'
TSSentido._CF_pattern = pyxb.binding.facets.CF_pattern()
TSSentido._CF_pattern.addPattern(pattern='[0-9]{1,3}')
TSSentido._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSSentido._InitializeFacetMap(TSSentido._CF_pattern,
   TSSentido._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSSentido', TSSentido)
_module_typeBindings.TSSentido = TSSentido

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSIdeEvento
class TSIdeEvento (pyxb.binding.datatypes.string):

    """Identificação da Atividade de Evento (código identificador de evento determinado pela Administração Tributária Municipal)"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSIdeEvento')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 852, 2)
    _Documentation = 'Identificação da Atividade de Evento (código identificador de evento determinado pela Administração Tributária Municipal)'
TSIdeEvento._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
TSIdeEvento._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSIdeEvento._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSIdeEvento._InitializeFacetMap(TSIdeEvento._CF_maxLength,
   TSIdeEvento._CF_minLength,
   TSIdeEvento._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSIdeEvento', TSIdeEvento)
_module_typeBindings.TSIdeEvento = TSIdeEvento

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSCodObra
class TSCodObra (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSCodObra')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 862, 2)
    _Documentation = None
TSCodObra._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
TSCodObra._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSCodObra._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSCodObra._InitializeFacetMap(TSCodObra._CF_maxLength,
   TSCodObra._CF_minLength,
   TSCodObra._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSCodObra', TSCodObra)
_module_typeBindings.TSCodObra = TSCodObra

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSInscImobFisc
class TSInscImobFisc (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSInscImobFisc')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 869, 2)
    _Documentation = None
TSInscImobFisc._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
TSInscImobFisc._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSInscImobFisc._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSInscImobFisc._InitializeFacetMap(TSInscImobFisc._CF_maxLength,
   TSInscImobFisc._CF_minLength,
   TSInscImobFisc._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSInscImobFisc', TSInscImobFisc)
_module_typeBindings.TSInscImobFisc = TSInscImobFisc

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSDRT
class TSDRT (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSDRT')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 876, 2)
    _Documentation = None
TSDRT._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(40))
TSDRT._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSDRT._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSDRT._InitializeFacetMap(TSDRT._CF_maxLength,
   TSDRT._CF_minLength,
   TSDRT._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSDRT', TSDRT)
_module_typeBindings.TSDRT = TSDRT

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSCodVerificacao
class TSCodVerificacao (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSCodVerificacao')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 890, 2)
    _Documentation = None
TSCodVerificacao._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(9))
TSCodVerificacao._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSCodVerificacao._CF_pattern = pyxb.binding.facets.CF_pattern()
TSCodVerificacao._CF_pattern.addPattern(pattern='[a-zA-Z0-9]{1,9}')
TSCodVerificacao._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSCodVerificacao._InitializeFacetMap(TSCodVerificacao._CF_maxLength,
   TSCodVerificacao._CF_minLength,
   TSCodVerificacao._CF_pattern,
   TSCodVerificacao._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSCodVerificacao', TSCodVerificacao)
_module_typeBindings.TSCodVerificacao = TSCodVerificacao

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSSerieNFNFS
class TSSerieNFNFS (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSSerieNFNFS')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 898, 2)
    _Documentation = None
TSSerieNFNFS._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(15))
TSSerieNFNFS._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSSerieNFNFS._CF_pattern = pyxb.binding.facets.CF_pattern()
TSSerieNFNFS._CF_pattern.addPattern(pattern='[a-zA-Z0-9]{1,15}')
TSSerieNFNFS._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSSerieNFNFS._InitializeFacetMap(TSSerieNFNFS._CF_maxLength,
   TSSerieNFNFS._CF_minLength,
   TSSerieNFNFS._CF_pattern,
   TSSerieNFNFS._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSSerieNFNFS', TSSerieNFNFS)
_module_typeBindings.TSSerieNFNFS = TSSerieNFNFS

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSIdeDedRed
class TSIdeDedRed (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
		Identificação da Dedução/Redução:
        1 – Alimentação e bebidas/frigobar;
        2 – Materiais;
        3 – Produção externa;
        4 – Reembolso de despesas;
        5 – Repasse consorciado;
        6 – Repasse plano de saúde;
        7 – Serviços;
        8 – Subempreitada de mão de obra;
        99 – Outras deduções;
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSIdeDedRed')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 906, 2)
    _Documentation = '\n\t\tIdentificação da Dedução/Redução:\n        1 – Alimentação e bebidas/frigobar;\n        2 – Materiais;\n        3 – Produção externa;\n        4 – Reembolso de despesas;\n        5 – Repasse consorciado;\n        6 – Repasse plano de saúde;\n        7 – Serviços;\n        8 – Subempreitada de mão de obra;\n        99 – Outras deduções;\n      '
TSIdeDedRed._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSIdeDedRed)
TSIdeDedRed.n1 = TSIdeDedRed._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
TSIdeDedRed.n2 = TSIdeDedRed._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
TSIdeDedRed.n3 = TSIdeDedRed._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
TSIdeDedRed.n4 = TSIdeDedRed._CF_enumeration.addEnumeration(unicode_value='4', tag='n4')
TSIdeDedRed.n5 = TSIdeDedRed._CF_enumeration.addEnumeration(unicode_value='5', tag='n5')
TSIdeDedRed.n6 = TSIdeDedRed._CF_enumeration.addEnumeration(unicode_value='6', tag='n6')
TSIdeDedRed.n7 = TSIdeDedRed._CF_enumeration.addEnumeration(unicode_value='7', tag='n7')
TSIdeDedRed.n8 = TSIdeDedRed._CF_enumeration.addEnumeration(unicode_value='8', tag='n8')
TSIdeDedRed.n99 = TSIdeDedRed._CF_enumeration.addEnumeration(unicode_value='99', tag='n99')
TSIdeDedRed._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSIdeDedRed._InitializeFacetMap(TSIdeDedRed._CF_enumeration,
   TSIdeDedRed._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSIdeDedRed', TSIdeDedRed)
_module_typeBindings.TSIdeDedRed = TSIdeDedRed

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSNumBeneficioMunicipal
class TSNumBeneficioMunicipal (pyxb.binding.datatypes.string):

    """
        Identificador do benefício parametrizado pelo município.

        Trata-se de um identificador único que foi gerado pelo Sistema Nacional no momento em que o município de incidência do ISSQN incluiu o benefício no sistema.
        
        Critério de formação do número de identificação de parâmetros municipais:   
        7 dígitos - posição 1 a 7: número identificador do Município, conforme código IBGE;
        2 dígitos - posições 8 e 9 : número identificador do tipo de parametrização (01-legislação, 02-regimes especiais, 03-retenções, 04-outros benefícios);
        5 dígitos - posição 10 a 14 : número sequencial definido pelo sistema quando do registro específico do parâmetro dentro do tipo de parametrização no sistema;
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSNumBeneficioMunicipal')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 944, 2)
    _Documentation = '\n        Identificador do benefício parametrizado pelo município.\n\n        Trata-se de um identificador único que foi gerado pelo Sistema Nacional no momento em que o município de incidência do ISSQN incluiu o benefício no sistema.\n        \n        Critério de formação do número de identificação de parâmetros municipais:   \n        7 dígitos - posição 1 a 7: número identificador do Município, conforme código IBGE;\n        2 dígitos - posições 8 e 9 : número identificador do tipo de parametrização (01-legislação, 02-regimes especiais, 03-retenções, 04-outros benefícios);\n        5 dígitos - posição 10 a 14 : número sequencial definido pelo sistema quando do registro específico do parâmetro dentro do tipo de parametrização no sistema;\n      '
TSNumBeneficioMunicipal._CF_pattern = pyxb.binding.facets.CF_pattern()
TSNumBeneficioMunicipal._CF_pattern.addPattern(pattern='[0-9]{14}')
TSNumBeneficioMunicipal._InitializeFacetMap(TSNumBeneficioMunicipal._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'TSNumBeneficioMunicipal', TSNumBeneficioMunicipal)
_module_typeBindings.TSNumBeneficioMunicipal = TSNumBeneficioMunicipal

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSOpExigSuspensa
class TSOpExigSuspensa (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
	    Opção para Exigibilidade Suspensa:
        1 - Exigibilidade Suspensa por Decisão Judicial;
        2 - Exigibilidade Suspensa por Processo Administrativo;
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSOpExigSuspensa')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 961, 2)
    _Documentation = '\n\t    Opção para Exigibilidade Suspensa:\n        1 - Exigibilidade Suspensa por Decisão Judicial;\n        2 - Exigibilidade Suspensa por Processo Administrativo;\n      '
TSOpExigSuspensa._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSOpExigSuspensa)
TSOpExigSuspensa.n1 = TSOpExigSuspensa._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
TSOpExigSuspensa.n2 = TSOpExigSuspensa._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
TSOpExigSuspensa._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSOpExigSuspensa._InitializeFacetMap(TSOpExigSuspensa._CF_enumeration,
   TSOpExigSuspensa._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSOpExigSuspensa', TSOpExigSuspensa)
_module_typeBindings.TSOpExigSuspensa = TSOpExigSuspensa

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSNumProcExigSuspensa
class TSNumProcExigSuspensa (pyxb.binding.datatypes.string):

    """Número do processo judicial ou administrativo de suspensão da exigibilidade"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSNumProcExigSuspensa')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 975, 2)
    _Documentation = 'Número do processo judicial ou administrativo de suspensão da exigibilidade'
TSNumProcExigSuspensa._CF_pattern = pyxb.binding.facets.CF_pattern()
TSNumProcExigSuspensa._CF_pattern.addPattern(pattern='[0-9]{30}')
TSNumProcExigSuspensa._InitializeFacetMap(TSNumProcExigSuspensa._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'TSNumProcExigSuspensa', TSNumProcExigSuspensa)
_module_typeBindings.TSNumProcExigSuspensa = TSNumProcExigSuspensa

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSOpSimpNac
class TSOpSimpNac (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
	    Situação perante o Simples Nacional:
        1 - Não Optante;
        2 - Optante - Microempreendedor Individual (MEI);
        3 - Optante - Microempresa ou Empresa de Pequeno Porte (ME/EPP);
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSOpSimpNac')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 983, 2)
    _Documentation = '\n\t    Situação perante o Simples Nacional:\n        1 - Não Optante;\n        2 - Optante - Microempreendedor Individual (MEI);\n        3 - Optante - Microempresa ou Empresa de Pequeno Porte (ME/EPP);\n      '
TSOpSimpNac._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSOpSimpNac)
TSOpSimpNac.n1 = TSOpSimpNac._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
TSOpSimpNac.n2 = TSOpSimpNac._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
TSOpSimpNac.n3 = TSOpSimpNac._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
TSOpSimpNac._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSOpSimpNac._InitializeFacetMap(TSOpSimpNac._CF_enumeration,
   TSOpSimpNac._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSOpSimpNac', TSOpSimpNac)
_module_typeBindings.TSOpSimpNac = TSOpSimpNac

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSRegimeApuracaoSimpNac
class TSRegimeApuracaoSimpNac (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        Opção para que o contribuinte optante pelo Simples Nacional ME/EPP (opSimpNac = 3) possa indicar, ao emitir o documento fiscal, em qual regime de apuração os tributos federais e municipal estão inseridos, caso tenha ultrapassado algum sublimite ou limite definido para o Simples Nacional.
        1 – Regime de apuração dos tributos federais e municipal pelo SN;
        2 – Regime de apuração dos tributos federais pelo SN e ISSQN  por fora do SN conforme respectiva legislação municipal do tributo;
        3 – Regime de apuração dos tributos federais e municipal por fora do SN conforme respectivas legilações federal e municipal de cada tributo;
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSRegimeApuracaoSimpNac')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 999, 2)
    _Documentation = '\n        Opção para que o contribuinte optante pelo Simples Nacional ME/EPP (opSimpNac = 3) possa indicar, ao emitir o documento fiscal, em qual regime de apuração os tributos federais e municipal estão inseridos, caso tenha ultrapassado algum sublimite ou limite definido para o Simples Nacional.\n        1 – Regime de apuração dos tributos federais e municipal pelo SN;\n        2 – Regime de apuração dos tributos federais pelo SN e ISSQN  por fora do SN conforme respectiva legislação municipal do tributo;\n        3 – Regime de apuração dos tributos federais e municipal por fora do SN conforme respectivas legilações federal e municipal de cada tributo;\n      '
TSRegimeApuracaoSimpNac._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSRegimeApuracaoSimpNac)
TSRegimeApuracaoSimpNac.n1 = TSRegimeApuracaoSimpNac._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
TSRegimeApuracaoSimpNac.n2 = TSRegimeApuracaoSimpNac._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
TSRegimeApuracaoSimpNac.n3 = TSRegimeApuracaoSimpNac._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
TSRegimeApuracaoSimpNac._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSRegimeApuracaoSimpNac._InitializeFacetMap(TSRegimeApuracaoSimpNac._CF_enumeration,
   TSRegimeApuracaoSimpNac._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSRegimeApuracaoSimpNac', TSRegimeApuracaoSimpNac)
_module_typeBindings.TSRegimeApuracaoSimpNac = TSRegimeApuracaoSimpNac

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSOpSNLimUltrap
class TSOpSNLimUltrap (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
	    Opção que indica se o limite do Simples Nacional foi ultrapassado:
        0 - Não ultrapassado;
        1 - Ultrapassado;
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSOpSNLimUltrap')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1015, 2)
    _Documentation = '\n\t    Opção que indica se o limite do Simples Nacional foi ultrapassado:\n        0 - Não ultrapassado;\n        1 - Ultrapassado;\n      '
TSOpSNLimUltrap._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSOpSNLimUltrap)
TSOpSNLimUltrap.n0 = TSOpSNLimUltrap._CF_enumeration.addEnumeration(unicode_value='0', tag='n0')
TSOpSNLimUltrap.n1 = TSOpSNLimUltrap._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
TSOpSNLimUltrap._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSOpSNLimUltrap._InitializeFacetMap(TSOpSNLimUltrap._CF_enumeration,
   TSOpSNLimUltrap._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSOpSNLimUltrap', TSOpSNLimUltrap)
_module_typeBindings.TSOpSNLimUltrap = TSOpSNLimUltrap

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSRegEspTrib
class TSRegEspTrib (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
	    Tipos de Regimes Especiais de Tributação:
        0 - Nenhum;
        1 - Ato Cooperado (Cooperativa);
        2 - Estimativa;
        3 - Microempresa Municipal;
        4 - Notário ou Registrador;
        5 - Profissional Autônomo;
        6 - Sociedade de Profissionais;
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSRegEspTrib')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1029, 2)
    _Documentation = '\n\t    Tipos de Regimes Especiais de Tributação:\n        0 - Nenhum;\n        1 - Ato Cooperado (Cooperativa);\n        2 - Estimativa;\n        3 - Microempresa Municipal;\n        4 - Notário ou Registrador;\n        5 - Profissional Autônomo;\n        6 - Sociedade de Profissionais;\n      '
TSRegEspTrib._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSRegEspTrib)
TSRegEspTrib.n0 = TSRegEspTrib._CF_enumeration.addEnumeration(unicode_value='0', tag='n0')
TSRegEspTrib.n1 = TSRegEspTrib._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
TSRegEspTrib.n2 = TSRegEspTrib._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
TSRegEspTrib.n3 = TSRegEspTrib._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
TSRegEspTrib.n4 = TSRegEspTrib._CF_enumeration.addEnumeration(unicode_value='4', tag='n4')
TSRegEspTrib.n5 = TSRegEspTrib._CF_enumeration.addEnumeration(unicode_value='5', tag='n5')
TSRegEspTrib.n6 = TSRegEspTrib._CF_enumeration.addEnumeration(unicode_value='6', tag='n6')
TSRegEspTrib._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSRegEspTrib._InitializeFacetMap(TSRegEspTrib._CF_enumeration,
   TSRegEspTrib._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSRegEspTrib', TSRegEspTrib)
_module_typeBindings.TSRegEspTrib = TSRegEspTrib

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSTribISSQN
class TSTribISSQN (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
	    Tributação do ISSQN sobre o serviço prestado:
        1 - Operação tributável;
        2 - Imunidade;
        3 - Exportação de serviço;
        4 - Não Incidência;
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSTribISSQN')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1053, 2)
    _Documentation = '\n\t    Tributação do ISSQN sobre o serviço prestado:\n        1 - Operação tributável;\n        2 - Imunidade;\n        3 - Exportação de serviço;\n        4 - Não Incidência;\n      '
TSTribISSQN._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSTribISSQN)
TSTribISSQN.n1 = TSTribISSQN._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
TSTribISSQN.n2 = TSTribISSQN._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
TSTribISSQN.n3 = TSTribISSQN._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
TSTribISSQN.n4 = TSTribISSQN._CF_enumeration.addEnumeration(unicode_value='4', tag='n4')
TSTribISSQN._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSTribISSQN._InitializeFacetMap(TSTribISSQN._CF_enumeration,
   TSTribISSQN._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSTribISSQN', TSTribISSQN)
_module_typeBindings.TSTribISSQN = TSTribISSQN

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSTipoImunidadeISSQN
class TSTipoImunidadeISSQN (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
            Identificação da Imunidade do ISSQN – somente para o caso de Imunidade.

            Tipos de Imunidades:
            
            0 - Imunidade (tipo não informado na nota de origem);
            1 - Patrimônio, renda ou serviços, uns dos outros (CF88, Art 150, VI, a);
            2 - Templos de qualquer culto (CF88, Art 150, VI, b);
            3 - Patrimônio, renda ou serviços dos partidos políticos, inclusive suas fundações, das entidades sindicais dos trabalhadores, das instituições de educação e de assistência social, sem fins lucrativos, atendidos os requisitos da lei (CF88, Art 150, VI, c);
            4 - Livros, jornais, periódicos e o papel destinado a sua impressão (CF88, Art 150, VI, d);
            5 - Fonogramas e videofonogramas musicais produzidos no Brasil contendo obras musicais ou literomusicais de autores brasileiros e/ou obras em geral interpretadas por artistas brasileiros bem como os suportes materiais ou arquivos digitais que os contenham, salvo na etapa de replicação industrial de mídias ópticas de leitura a laser.   (CF88, Art 150, VI, e);
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSTipoImunidadeISSQN')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1083, 2)
    _Documentation = '\n            Identificação da Imunidade do ISSQN – somente para o caso de Imunidade.\n\n            Tipos de Imunidades:\n            \n            0 - Imunidade (tipo não informado na nota de origem);\n            1 - Patrimônio, renda ou serviços, uns dos outros (CF88, Art 150, VI, a);\n            2 - Templos de qualquer culto (CF88, Art 150, VI, b);\n            3 - Patrimônio, renda ou serviços dos partidos políticos, inclusive suas fundações, das entidades sindicais dos trabalhadores, das instituições de educação e de assistência social, sem fins lucrativos, atendidos os requisitos da lei (CF88, Art 150, VI, c);\n            4 - Livros, jornais, periódicos e o papel destinado a sua impressão (CF88, Art 150, VI, d);\n            5 - Fonogramas e videofonogramas musicais produzidos no Brasil contendo obras musicais ou literomusicais de autores brasileiros e/ou obras em geral interpretadas por artistas brasileiros bem como os suportes materiais ou arquivos digitais que os contenham, salvo na etapa de replicação industrial de mídias ópticas de leitura a laser.   (CF88, Art 150, VI, e);\n      '
TSTipoImunidadeISSQN._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSTipoImunidadeISSQN)
TSTipoImunidadeISSQN.n0 = TSTipoImunidadeISSQN._CF_enumeration.addEnumeration(unicode_value='0', tag='n0')
TSTipoImunidadeISSQN.n1 = TSTipoImunidadeISSQN._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
TSTipoImunidadeISSQN.n2 = TSTipoImunidadeISSQN._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
TSTipoImunidadeISSQN.n3 = TSTipoImunidadeISSQN._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
TSTipoImunidadeISSQN.n4 = TSTipoImunidadeISSQN._CF_enumeration.addEnumeration(unicode_value='4', tag='n4')
TSTipoImunidadeISSQN.n5 = TSTipoImunidadeISSQN._CF_enumeration.addEnumeration(unicode_value='5', tag='n5')
TSTipoImunidadeISSQN._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSTipoImunidadeISSQN._InitializeFacetMap(TSTipoImunidadeISSQN._CF_enumeration,
   TSTipoImunidadeISSQN._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSTipoImunidadeISSQN', TSTipoImunidadeISSQN)
_module_typeBindings.TSTipoImunidadeISSQN = TSTipoImunidadeISSQN

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSTipoRetISSQN
class TSTipoRetISSQN (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        Tipo de retencao do ISSQN:
        1 - Não Retido;
        2 - Retido pelo Tomador;
        3 - Retido pelo Intermediario;
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSTipoRetISSQN')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1108, 2)
    _Documentation = '\n        Tipo de retencao do ISSQN:\n        1 - Não Retido;\n        2 - Retido pelo Tomador;\n        3 - Retido pelo Intermediario;\n      '
TSTipoRetISSQN._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSTipoRetISSQN)
TSTipoRetISSQN.n1 = TSTipoRetISSQN._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
TSTipoRetISSQN.n2 = TSTipoRetISSQN._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
TSTipoRetISSQN.n3 = TSTipoRetISSQN._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
TSTipoRetISSQN._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSTipoRetISSQN._InitializeFacetMap(TSTipoRetISSQN._CF_enumeration,
   TSTipoRetISSQN._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSTipoRetISSQN', TSTipoRetISSQN)
_module_typeBindings.TSTipoRetISSQN = TSTipoRetISSQN

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSTipoCST
class TSTipoCST (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        Código de Situação Tributária do PIS/COFINS (CST):
        00 - Nenhum;      
        01 - Operação Tributável com Alíquota Básica;
        02 - Operação Tributável com Alíquota Diferenciada;
        03 - Operação Tributável com Alíquota por Unidade de Medida de Produto;
        04 - Operação Tributável monofásica - Revenda a Alíquota Zero;
        05 - Operação Tributável por Substituição Tributária;
        06 - Operação Tributável a Alíquota Zero;
        07 - Operação Tributável da Contribuição;
        08 - Operação sem Incidência da Contribuição;
        09 - Operação com Suspensão da Contribuição;
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSTipoCST')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1124, 2)
    _Documentation = '\n        Código de Situação Tributária do PIS/COFINS (CST):\n        00 - Nenhum;      \n        01 - Operação Tributável com Alíquota Básica;\n        02 - Operação Tributável com Alíquota Diferenciada;\n        03 - Operação Tributável com Alíquota por Unidade de Medida de Produto;\n        04 - Operação Tributável monofásica - Revenda a Alíquota Zero;\n        05 - Operação Tributável por Substituição Tributária;\n        06 - Operação Tributável a Alíquota Zero;\n        07 - Operação Tributável da Contribuição;\n        08 - Operação sem Incidência da Contribuição;\n        09 - Operação com Suspensão da Contribuição;\n      '
TSTipoCST._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSTipoCST)
TSTipoCST.n00 = TSTipoCST._CF_enumeration.addEnumeration(unicode_value='00', tag='n00')
TSTipoCST.n01 = TSTipoCST._CF_enumeration.addEnumeration(unicode_value='01', tag='n01')
TSTipoCST.n02 = TSTipoCST._CF_enumeration.addEnumeration(unicode_value='02', tag='n02')
TSTipoCST.n03 = TSTipoCST._CF_enumeration.addEnumeration(unicode_value='03', tag='n03')
TSTipoCST.n04 = TSTipoCST._CF_enumeration.addEnumeration(unicode_value='04', tag='n04')
TSTipoCST.n05 = TSTipoCST._CF_enumeration.addEnumeration(unicode_value='05', tag='n05')
TSTipoCST.n06 = TSTipoCST._CF_enumeration.addEnumeration(unicode_value='06', tag='n06')
TSTipoCST.n07 = TSTipoCST._CF_enumeration.addEnumeration(unicode_value='07', tag='n07')
TSTipoCST.n08 = TSTipoCST._CF_enumeration.addEnumeration(unicode_value='08', tag='n08')
TSTipoCST.n09 = TSTipoCST._CF_enumeration.addEnumeration(unicode_value='09', tag='n09')
TSTipoCST._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSTipoCST._InitializeFacetMap(TSTipoCST._CF_enumeration,
   TSTipoCST._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSTipoCST', TSTipoCST)
_module_typeBindings.TSTipoCST = TSTipoCST

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSOpConsumServ
class TSOpConsumServ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        Opção para que o emitente informe onde ocorreu o consumo do serviço prestado.
        0 - Consumo do serviço prestado ocorrido no município do local da prestação;
        1 - Consumo do serviço prestado ocorrido ocorrido no exterior ;
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSOpConsumServ')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1154, 2)
    _Documentation = '\n        Opção para que o emitente informe onde ocorreu o consumo do serviço prestado.\n        0 - Consumo do serviço prestado ocorrido no município do local da prestação;\n        1 - Consumo do serviço prestado ocorrido ocorrido no exterior ;\n      '
TSOpConsumServ._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSOpConsumServ)
TSOpConsumServ.n0 = TSOpConsumServ._CF_enumeration.addEnumeration(unicode_value='0', tag='n0')
TSOpConsumServ.n1 = TSOpConsumServ._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
TSOpConsumServ._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSOpConsumServ._InitializeFacetMap(TSOpConsumServ._CF_enumeration,
   TSOpConsumServ._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSOpConsumServ', TSOpConsumServ)
_module_typeBindings.TSOpConsumServ = TSOpConsumServ

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSTipoRetPISCofins
class TSTipoRetPISCofins (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
	    Tipo de retencao do Pis/Cofins:
        1 - Retido;
        2 - Não Retido;
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSTipoRetPISCofins')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1168, 2)
    _Documentation = '\n\t    Tipo de retencao do Pis/Cofins:\n        1 - Retido;\n        2 - Não Retido;\n      '
TSTipoRetPISCofins._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSTipoRetPISCofins)
TSTipoRetPISCofins.n1 = TSTipoRetPISCofins._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
TSTipoRetPISCofins.n2 = TSTipoRetPISCofins._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
TSTipoRetPISCofins._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSTipoRetPISCofins._InitializeFacetMap(TSTipoRetPISCofins._CF_enumeration,
   TSTipoRetPISCofins._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSTipoRetPISCofins', TSTipoRetPISCofins)
_module_typeBindings.TSTipoRetPISCofins = TSTipoRetPISCofins

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSTipoIndTotTrib
class TSTipoIndTotTrib (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
	    Indicador de informação de valor total de tributos. Possui valor fixo igual a zero (indTotTrib=0).
        Não informar nenhum valor estimado para os Tributos (Decreto 8.264/2014).
        0 - Não;
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSTipoIndTotTrib')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1182, 2)
    _Documentation = '\n\t    Indicador de informação de valor total de tributos. Possui valor fixo igual a zero (indTotTrib=0).\n        Não informar nenhum valor estimado para os Tributos (Decreto 8.264/2014).\n        0 - Não;\n      '
TSTipoIndTotTrib._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSTipoIndTotTrib)
TSTipoIndTotTrib.n0 = TSTipoIndTotTrib._CF_enumeration.addEnumeration(unicode_value='0', tag='n0')
TSTipoIndTotTrib._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSTipoIndTotTrib._InitializeFacetMap(TSTipoIndTotTrib._CF_enumeration,
   TSTipoIndTotTrib._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSTipoIndTotTrib', TSTipoIndTotTrib)
_module_typeBindings.TSTipoIndTotTrib = TSTipoIndTotTrib

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TBMISSQN
class TBMISSQN (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
		  Tipo Benefício Municipal (BM):

		  1) Isenção;
		  2) Redução da BC em 'ppBM' %;
		  3) Redução da BC em R$ 'vInfoBM';
		  4) Alíquota Diferenciada de 'aliqDifBM' %;
	  """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TBMISSQN')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1195, 2)
    _Documentation = "\n\t\t  Tipo Benefício Municipal (BM):\n\n\t\t  1) Isenção;\n\t\t  2) Redução da BC em 'ppBM' %;\n\t\t  3) Redução da BC em R$ 'vInfoBM';\n\t\t  4) Alíquota Diferenciada de 'aliqDifBM' %;\n\t  "
TBMISSQN._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TBMISSQN)
TBMISSQN.n1 = TBMISSQN._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
TBMISSQN.n2 = TBMISSQN._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
TBMISSQN.n3 = TBMISSQN._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
TBMISSQN.n4 = TBMISSQN._CF_enumeration.addEnumeration(unicode_value='4', tag='n4')
TBMISSQN._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TBMISSQN._InitializeFacetMap(TBMISSQN._CF_enumeration,
   TBMISSQN._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TBMISSQN', TBMISSQN)
_module_typeBindings.TBMISSQN = TBMISSQN

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TStat
class TStat (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
	    100 - NFS-e Gerada;
        101 - NFS-e de Substituição Gerada;
        102 - NFS-e de Decisão Judicial;
        103 - NFS-e Avulsa;"
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TStat')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1214, 2)
    _Documentation = '\n\t    100 - NFS-e Gerada;\n        101 - NFS-e de Substituição Gerada;\n        102 - NFS-e de Decisão Judicial;\n        103 - NFS-e Avulsa;"\n      '
TStat._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TStat)
TStat.n100 = TStat._CF_enumeration.addEnumeration(unicode_value='100', tag='n100')
TStat.n101 = TStat._CF_enumeration.addEnumeration(unicode_value='101', tag='n101')
TStat.n102 = TStat._CF_enumeration.addEnumeration(unicode_value='102', tag='n102')
TStat.n103 = TStat._CF_enumeration.addEnumeration(unicode_value='103', tag='n103')
TStat._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TStat._InitializeFacetMap(TStat._CF_enumeration,
   TStat._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TStat', TStat)
_module_typeBindings.TStat = TStat

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSNumDPS
class TSNumDPS (pyxb.binding.datatypes.string):

    """Tipo Número do DPS"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSNumDPS')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1231, 2)
    _Documentation = 'Tipo Número do DPS'
TSNumDPS._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(15))
TSNumDPS._CF_pattern = pyxb.binding.facets.CF_pattern()
TSNumDPS._CF_pattern.addPattern(pattern='[1-9]{1}[0-9]{0,14}')
TSNumDPS._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSNumDPS._InitializeFacetMap(TSNumDPS._CF_maxLength,
   TSNumDPS._CF_pattern,
   TSNumDPS._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSNumDPS', TSNumDPS)
_module_typeBindings.TSNumDPS = TSNumDPS

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSNNFSe
class TSNNFSe (pyxb.binding.datatypes.string):

    """Tipo Número sequencial do documento"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSNNFSe')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1241, 2)
    _Documentation = 'Tipo Número sequencial do documento'
TSNNFSe._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(13))
TSNNFSe._CF_pattern = pyxb.binding.facets.CF_pattern()
TSNNFSe._CF_pattern.addPattern(pattern='[1-9]{1}[0-9]{0,12}')
TSNNFSe._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSNNFSe._InitializeFacetMap(TSNNFSe._CF_maxLength,
   TSNNFSe._CF_pattern,
   TSNNFSe._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSNNFSe', TSNNFSe)
_module_typeBindings.TSNNFSe = TSNNFSe

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSNDFSe
class TSNDFSe (pyxb.binding.datatypes.string):

    """Tipo Número do DFS-e"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSNDFSe')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1251, 2)
    _Documentation = 'Tipo Número do DFS-e'
TSNDFSe._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(13))
TSNDFSe._CF_pattern = pyxb.binding.facets.CF_pattern()
TSNDFSe._CF_pattern.addPattern(pattern='[1-9]{1}[0-9]{0,12}')
TSNDFSe._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSNDFSe._InitializeFacetMap(TSNDFSe._CF_maxLength,
   TSNDFSe._CF_pattern,
   TSNDFSe._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSNDFSe', TSNDFSe)
_module_typeBindings.TSNDFSe = TSNDFSe

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSCodMunIBGE
class TSCodMunIBGE (pyxb.binding.datatypes.string):

    """Tipo Código do Município segundo tabela IBGE"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSCodMunIBGE')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1261, 2)
    _Documentation = 'Tipo Código do Município segundo tabela IBGE'
TSCodMunIBGE._CF_pattern = pyxb.binding.facets.CF_pattern()
TSCodMunIBGE._CF_pattern.addPattern(pattern='[0-9]{7}')
TSCodMunIBGE._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSCodMunIBGE._InitializeFacetMap(TSCodMunIBGE._CF_pattern,
   TSCodMunIBGE._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSCodMunIBGE', TSCodMunIBGE)
_module_typeBindings.TSCodMunIBGE = TSCodMunIBGE

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSCodPaisISO
class TSCodPaisISO (pyxb.binding.datatypes.string):

    """Tipo Código do País segundo tabela ISO"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSCodPaisISO')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1270, 2)
    _Documentation = 'Tipo Código do País segundo tabela ISO'
TSCodPaisISO._CF_pattern = pyxb.binding.facets.CF_pattern()
TSCodPaisISO._CF_pattern.addPattern(pattern='[A-Z]{2}')
TSCodPaisISO._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSCodPaisISO._InitializeFacetMap(TSCodPaisISO._CF_pattern,
   TSCodPaisISO._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSCodPaisISO', TSCodPaisISO)
_module_typeBindings.TSCodPaisISO = TSCodPaisISO

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSCodTribNac
class TSCodTribNac (pyxb.binding.datatypes.string):

    """Código de tributação nacional do ISSQN:
        Regra de formação - 6 dígitos numéricos sendo: 2 para Item (LC 116/2003), 2 para Subitem (LC 116/2003) e 2 para Desdobro Nacional
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSCodTribNac')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1279, 2)
    _Documentation = 'Código de tributação nacional do ISSQN:\n        Regra de formação - 6 dígitos numéricos sendo: 2 para Item (LC 116/2003), 2 para Subitem (LC 116/2003) e 2 para Desdobro Nacional\n      '
TSCodTribNac._CF_pattern = pyxb.binding.facets.CF_pattern()
TSCodTribNac._CF_pattern.addPattern(pattern='[0-9]{6}')
TSCodTribNac._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSCodTribNac._InitializeFacetMap(TSCodTribNac._CF_pattern,
   TSCodTribNac._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSCodTribNac', TSCodTribNac)
_module_typeBindings.TSCodTribNac = TSCodTribNac

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSCodNBS
class TSCodNBS (pyxb.binding.datatypes.string):

    """
        Código da lista de Nomenclatura Brasileira de Serviços (NBS)
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSCodNBS')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1290, 2)
    _Documentation = '\n        Código da lista de Nomenclatura Brasileira de Serviços (NBS)\n      '
TSCodNBS._CF_pattern = pyxb.binding.facets.CF_pattern()
TSCodNBS._CF_pattern.addPattern(pattern='[0-9]{9}')
TSCodNBS._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSCodNBS._InitializeFacetMap(TSCodNBS._CF_pattern,
   TSCodNBS._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSCodNBS', TSCodNBS)
_module_typeBindings.TSCodNBS = TSCodNBS

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSDec15V2
class TSDec15V2 (pyxb.binding.datatypes.string):

    """Valor decimal com 1 a 15 dígitos mais 2 casas decimais"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSDec15V2')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1346, 2)
    _Documentation = 'Valor decimal com 1 a 15 dígitos mais 2 casas decimais'
TSDec15V2._CF_pattern = pyxb.binding.facets.CF_pattern()
TSDec15V2._CF_pattern.addPattern(pattern='0|0\\.[0-9]{2}|[1-9]{1}[0-9]{0,14}(\\.[0-9]{2})?')
TSDec15V2._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSDec15V2._InitializeFacetMap(TSDec15V2._CF_pattern,
   TSDec15V2._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSDec15V2', TSDec15V2)
_module_typeBindings.TSDec15V2 = TSDec15V2

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSDec1V2
class TSDec1V2 (pyxb.binding.datatypes.string):

    """Valor decimal com 1 dígito mais 2 casas decimais"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSDec1V2')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1355, 2)
    _Documentation = 'Valor decimal com 1 dígito mais 2 casas decimais'
TSDec1V2._CF_pattern = pyxb.binding.facets.CF_pattern()
TSDec1V2._CF_pattern.addPattern(pattern='0|[0-9]{1}(\\.[0-9]{2})?')
TSDec1V2._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSDec1V2._InitializeFacetMap(TSDec1V2._CF_pattern,
   TSDec1V2._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSDec1V2', TSDec1V2)
_module_typeBindings.TSDec1V2 = TSDec1V2

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSDec2V2
class TSDec2V2 (pyxb.binding.datatypes.string):

    """Valor decimal com 1 ou 2 dígitos mais 2 casas decimais"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSDec2V2')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1364, 2)
    _Documentation = 'Valor decimal com 1 ou 2 dígitos mais 2 casas decimais'
TSDec2V2._CF_pattern = pyxb.binding.facets.CF_pattern()
TSDec2V2._CF_pattern.addPattern(pattern='0|0\\.[0-9]{2}|[1-9]{1}[0-9]{0,1}(\\.[0-9]{2})?')
TSDec2V2._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSDec2V2._InitializeFacetMap(TSDec2V2._CF_pattern,
   TSDec2V2._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSDec2V2', TSDec2V2)
_module_typeBindings.TSDec2V2 = TSDec2V2

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSDec3V2
class TSDec3V2 (pyxb.binding.datatypes.string):

    """Valor decimal com 1 a 3 dígitos mais 2 casas decimais"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSDec3V2')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1373, 2)
    _Documentation = 'Valor decimal com 1 a 3 dígitos mais 2 casas decimais'
TSDec3V2._CF_pattern = pyxb.binding.facets.CF_pattern()
TSDec3V2._CF_pattern.addPattern(pattern='0|0\\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\\.[0-9]{2})?')
TSDec3V2._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSDec3V2._InitializeFacetMap(TSDec3V2._CF_pattern,
   TSDec3V2._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSDec3V2', TSDec3V2)
_module_typeBindings.TSDec3V2 = TSDec3V2

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSNum3Dig
class TSNum3Dig (pyxb.binding.datatypes.string):

    """Número com 3 dígitos"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSNum3Dig')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1382, 2)
    _Documentation = 'Número com 3 dígitos'
TSNum3Dig._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(3))
TSNum3Dig._CF_pattern = pyxb.binding.facets.CF_pattern()
TSNum3Dig._CF_pattern.addPattern(pattern='[0-9]{1}[0-9]{0,2}')
TSNum3Dig._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSNum3Dig._InitializeFacetMap(TSNum3Dig._CF_maxLength,
   TSNum3Dig._CF_pattern,
   TSNum3Dig._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSNum3Dig', TSNum3Dig)
_module_typeBindings.TSNum3Dig = TSNum3Dig

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSNum7Dig
class TSNum7Dig (pyxb.binding.datatypes.string):

    """Número com 7 dígitos"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSNum7Dig')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1392, 2)
    _Documentation = 'Número com 7 dígitos'
TSNum7Dig._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(7))
TSNum7Dig._CF_pattern = pyxb.binding.facets.CF_pattern()
TSNum7Dig._CF_pattern.addPattern(pattern='[0-9]{7}')
TSNum7Dig._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSNum7Dig._InitializeFacetMap(TSNum7Dig._CF_maxLength,
   TSNum7Dig._CF_pattern,
   TSNum7Dig._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSNum7Dig', TSNum7Dig)
_module_typeBindings.TSNum7Dig = TSNum7Dig

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSNum14Dig
class TSNum14Dig (pyxb.binding.datatypes.string):

    """Número com 14 dígitos"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSNum14Dig')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1402, 2)
    _Documentation = 'Número com 14 dígitos'
TSNum14Dig._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(14))
TSNum14Dig._CF_pattern = pyxb.binding.facets.CF_pattern()
TSNum14Dig._CF_pattern.addPattern(pattern='[0-9]{14}')
TSNum14Dig._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSNum14Dig._InitializeFacetMap(TSNum14Dig._CF_maxLength,
   TSNum14Dig._CF_pattern,
   TSNum14Dig._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSNum14Dig', TSNum14Dig)
_module_typeBindings.TSNum14Dig = TSNum14Dig

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSNum15Dig
class TSNum15Dig (pyxb.binding.datatypes.string):

    """Número com 15 dígitos"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSNum15Dig')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1412, 2)
    _Documentation = 'Número com 15 dígitos'
TSNum15Dig._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(15))
TSNum15Dig._CF_pattern = pyxb.binding.facets.CF_pattern()
TSNum15Dig._CF_pattern.addPattern(pattern='[0-9]{15}')
TSNum15Dig._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSNum15Dig._InitializeFacetMap(TSNum15Dig._CF_maxLength,
   TSNum15Dig._CF_pattern,
   TSNum15Dig._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSNum15Dig', TSNum15Dig)
_module_typeBindings.TSNum15Dig = TSNum15Dig

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSIdPedRefEvt
class TSIdPedRefEvt (pyxb.binding.datatypes.string):

    """
        O identificador do pedido de registro do evento é formado conforme a concatenação dos seguintes campos:
        "PRE" + Chave de Acesso NFS-e + Tipo do evento + Número do Pedido de Registro do Evento (nPedRegEvento)
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSIdPedRefEvt')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1422, 2)
    _Documentation = '\n        O identificador do pedido de registro do evento é formado conforme a concatenação dos seguintes campos:\n        "PRE" + Chave de Acesso NFS-e + Tipo do evento + Número do Pedido de Registro do Evento (nPedRegEvento)\n      '
TSIdPedRefEvt._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(62))
TSIdPedRefEvt._CF_pattern = pyxb.binding.facets.CF_pattern()
TSIdPedRefEvt._CF_pattern.addPattern(pattern='PRE[0-9]{59}')
TSIdPedRefEvt._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSIdPedRefEvt._InitializeFacetMap(TSIdPedRefEvt._CF_maxLength,
   TSIdPedRefEvt._CF_pattern,
   TSIdPedRefEvt._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSIdPedRefEvt', TSIdPedRefEvt)
_module_typeBindings.TSIdPedRefEvt = TSIdPedRefEvt

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSIdEvento
class TSIdEvento (pyxb.binding.datatypes.string):

    """
		  Identificador do evento: "EVT" + Chave de acesso(50) Tipo do evento (6) + Pedido de Registro do Evento(3) (nPedRegEvento)
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSIdEvento')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1435, 2)
    _Documentation = '\n\t\t  Identificador do evento: "EVT" + Chave de acesso(50) Tipo do evento (6) + Pedido de Registro do Evento(3) (nPedRegEvento)\n      '
TSIdEvento._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(62))
TSIdEvento._CF_pattern = pyxb.binding.facets.CF_pattern()
TSIdEvento._CF_pattern.addPattern(pattern='EVT[0-9]{59}')
TSIdEvento._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSIdEvento._InitializeFacetMap(TSIdEvento._CF_maxLength,
   TSIdEvento._CF_pattern,
   TSIdEvento._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSIdEvento', TSIdEvento)
_module_typeBindings.TSIdEvento = TSIdEvento

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSCodigoEventoNFSe
class TSCodigoEventoNFSe (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
		  Código de evento da NFS-e
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSCodigoEventoNFSe')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1447, 2)
    _Documentation = '\n\t\t  Código de evento da NFS-e\n      '
TSCodigoEventoNFSe._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSCodigoEventoNFSe)
TSCodigoEventoNFSe.e101101 = TSCodigoEventoNFSe._CF_enumeration.addEnumeration(unicode_value='e101101', tag='e101101')
TSCodigoEventoNFSe.e105102 = TSCodigoEventoNFSe._CF_enumeration.addEnumeration(unicode_value='e105102', tag='e105102')
TSCodigoEventoNFSe.e105104 = TSCodigoEventoNFSe._CF_enumeration.addEnumeration(unicode_value='e105104', tag='e105104')
TSCodigoEventoNFSe.e105105 = TSCodigoEventoNFSe._CF_enumeration.addEnumeration(unicode_value='e105105', tag='e105105')
TSCodigoEventoNFSe.e305101 = TSCodigoEventoNFSe._CF_enumeration.addEnumeration(unicode_value='e305101', tag='e305101')
TSCodigoEventoNFSe.e907202 = TSCodigoEventoNFSe._CF_enumeration.addEnumeration(unicode_value='e907202', tag='e907202')
TSCodigoEventoNFSe.e967203 = TSCodigoEventoNFSe._CF_enumeration.addEnumeration(unicode_value='e967203', tag='e967203')
TSCodigoEventoNFSe._InitializeFacetMap(TSCodigoEventoNFSe._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'TSCodigoEventoNFSe', TSCodigoEventoNFSe)
_module_typeBindings.TSCodigoEventoNFSe = TSCodigoEventoNFSe

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSIdNumEvento
class TSIdNumEvento (pyxb.binding.datatypes.string):

    """
		  Referência ao Id "Manifestação de rejeição da NFS-e" que originou o presente evento de anulação.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSIdNumEvento')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1463, 2)
    _Documentation = '\n\t\t  Referência ao Id "Manifestação de rejeição da NFS-e" que originou o presente evento de anulação.\n      '
TSIdNumEvento._CF_pattern = pyxb.binding.facets.CF_pattern()
TSIdNumEvento._CF_pattern.addPattern(pattern='[0-9]{59}')
TSIdNumEvento._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSIdNumEvento._InitializeFacetMap(TSIdNumEvento._CF_pattern,
   TSIdNumEvento._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSIdNumEvento', TSIdNumEvento)
_module_typeBindings.TSIdNumEvento = TSIdNumEvento

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSNumDFe
class TSNumDFe (pyxb.binding.datatypes.string):

    """
		  Número sequencial do documento gerado por ambiente gerador de DFe do município.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSNumDFe')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1474, 2)
    _Documentation = '\n\t\t  Número sequencial do documento gerado por ambiente gerador de DFe do município.\n      '
TSNumDFe._CF_pattern = pyxb.binding.facets.CF_pattern()
TSNumDFe._CF_pattern.addPattern(pattern='[0-9]{1,13}')
TSNumDFe._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSNumDFe._InitializeFacetMap(TSNumDFe._CF_pattern,
   TSNumDFe._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSNumDFe', TSNumDFe)
_module_typeBindings.TSNumDFe = TSNumDFe

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSSituacaoEmissaoNFSE
class TSSituacaoEmissaoNFSE (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
		  Situação Emissão NFS-e:
        0 - Não Habilitado;
        1 - Habilitado;
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSSituacaoEmissaoNFSE')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1502, 2)
    _Documentation = '\n\t\t  Situação Emissão NFS-e:\n        0 - Não Habilitado;\n        1 - Habilitado;\n      '
TSSituacaoEmissaoNFSE._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSSituacaoEmissaoNFSE)
TSSituacaoEmissaoNFSE.n0 = TSSituacaoEmissaoNFSE._CF_enumeration.addEnumeration(unicode_value='0', tag='n0')
TSSituacaoEmissaoNFSE.n1 = TSSituacaoEmissaoNFSE._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
TSSituacaoEmissaoNFSE._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSSituacaoEmissaoNFSE._InitializeFacetMap(TSSituacaoEmissaoNFSE._CF_enumeration,
   TSSituacaoEmissaoNFSE._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSSituacaoEmissaoNFSE', TSSituacaoEmissaoNFSE)
_module_typeBindings.TSSituacaoEmissaoNFSE = TSSituacaoEmissaoNFSE

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSCategoriaServico
class TSCategoriaServico (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
		  Categorias do serviço:
        1 - Locação;
        2 - Sublocação;
        3 - Arrendamento;
        4 - Direito de passagem;
        5 - Permissão de uso;
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSCategoriaServico')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1516, 2)
    _Documentation = '\n\t\t  Categorias do serviço:\n        1 - Locação;\n        2 - Sublocação;\n        3 - Arrendamento;\n        4 - Direito de passagem;\n        5 - Permissão de uso;\n      '
TSCategoriaServico._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TSCategoriaServico)
TSCategoriaServico.n1 = TSCategoriaServico._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
TSCategoriaServico.n2 = TSCategoriaServico._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
TSCategoriaServico.n3 = TSCategoriaServico._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
TSCategoriaServico.n4 = TSCategoriaServico._CF_enumeration.addEnumeration(unicode_value='4', tag='n4')
TSCategoriaServico.n5 = TSCategoriaServico._CF_enumeration.addEnumeration(unicode_value='5', tag='n5')
TSCategoriaServico._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSCategoriaServico._InitializeFacetMap(TSCategoriaServico._CF_enumeration,
   TSCategoriaServico._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSCategoriaServico', TSCategoriaServico)
_module_typeBindings.TSCategoriaServico = TSCategoriaServico

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TCObjetoLocacao
class TCObjetoLocacao (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        Tipo de objetos da locação, sublocação, arrendamento, direito de passagem ou permissão de uso:
        1 - Ferrovia;
        2 - Rodovia;
        3 - Postes;
        4 - Cabos;
        5 - Dutos;
        6 - Condutos de qualquer natureza;
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCObjetoLocacao')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1536, 2)
    _Documentation = '\n        Tipo de objetos da locação, sublocação, arrendamento, direito de passagem ou permissão de uso:\n        1 - Ferrovia;\n        2 - Rodovia;\n        3 - Postes;\n        4 - Cabos;\n        5 - Dutos;\n        6 - Condutos de qualquer natureza;\n      '
TCObjetoLocacao._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=TCObjetoLocacao)
TCObjetoLocacao.n1 = TCObjetoLocacao._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
TCObjetoLocacao.n2 = TCObjetoLocacao._CF_enumeration.addEnumeration(unicode_value='2', tag='n2')
TCObjetoLocacao.n3 = TCObjetoLocacao._CF_enumeration.addEnumeration(unicode_value='3', tag='n3')
TCObjetoLocacao.n4 = TCObjetoLocacao._CF_enumeration.addEnumeration(unicode_value='4', tag='n4')
TCObjetoLocacao.n5 = TCObjetoLocacao._CF_enumeration.addEnumeration(unicode_value='5', tag='n5')
TCObjetoLocacao.n6 = TCObjetoLocacao._CF_enumeration.addEnumeration(unicode_value='6', tag='n6')
TCObjetoLocacao._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TCObjetoLocacao._InitializeFacetMap(TCObjetoLocacao._CF_enumeration,
   TCObjetoLocacao._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TCObjetoLocacao', TCObjetoLocacao)
_module_typeBindings.TCObjetoLocacao = TCObjetoLocacao

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSVerAplic
class TSVerAplic (TSString):

    """Tipo Versão do Aplicativo que gerou o documento fiscal"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSVerAplic')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 146, 2)
    _Documentation = 'Tipo Versão do Aplicativo que gerou o documento fiscal'
TSVerAplic._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20))
TSVerAplic._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSVerAplic._InitializeFacetMap(TSVerAplic._CF_maxLength,
   TSVerAplic._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'TSVerAplic', TSVerAplic)
_module_typeBindings.TSVerAplic = TSVerAplic

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSMotivo
class TSMotivo (TSString):

    """Descrição do motivo da substituição da NFS-e"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSMotivo')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 345, 2)
    _Documentation = 'Descrição do motivo da substituição da NFS-e'
TSMotivo._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(255))
TSMotivo._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(15))
TSMotivo._InitializeFacetMap(TSMotivo._CF_maxLength,
   TSMotivo._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'TSMotivo', TSMotivo)
_module_typeBindings.TSMotivo = TSMotivo

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSLogradouro
class TSLogradouro (TSString):

    """Logradouro"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSLogradouro')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 428, 2)
    _Documentation = 'Logradouro'
TSLogradouro._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(255))
TSLogradouro._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSLogradouro._InitializeFacetMap(TSLogradouro._CF_maxLength,
   TSLogradouro._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'TSLogradouro', TSLogradouro)
_module_typeBindings.TSLogradouro = TSLogradouro

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSNumeroEndereco
class TSNumeroEndereco (TSString):

    """Número"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSNumeroEndereco')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 437, 2)
    _Documentation = 'Número'
TSNumeroEndereco._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60))
TSNumeroEndereco._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSNumeroEndereco._InitializeFacetMap(TSNumeroEndereco._CF_maxLength,
   TSNumeroEndereco._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'TSNumeroEndereco', TSNumeroEndereco)
_module_typeBindings.TSNumeroEndereco = TSNumeroEndereco

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSComplementoEndereco
class TSComplementoEndereco (TSString):

    """Complemento"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSComplementoEndereco')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 446, 2)
    _Documentation = 'Complemento'
TSComplementoEndereco._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(156))
TSComplementoEndereco._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSComplementoEndereco._InitializeFacetMap(TSComplementoEndereco._CF_maxLength,
   TSComplementoEndereco._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'TSComplementoEndereco', TSComplementoEndereco)
_module_typeBindings.TSComplementoEndereco = TSComplementoEndereco

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSBairro
class TSBairro (TSString):

    """Bairro"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSBairro')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 455, 2)
    _Documentation = 'Bairro'
TSBairro._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60))
TSBairro._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSBairro._InitializeFacetMap(TSBairro._CF_maxLength,
   TSBairro._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'TSBairro', TSBairro)
_module_typeBindings.TSBairro = TSBairro

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSEnderCompletoExt
class TSEnderCompletoExt (TSString):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSEnderCompletoExt')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 538, 2)
    _Documentation = None
TSEnderCompletoExt._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(255))
TSEnderCompletoExt._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSEnderCompletoExt._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSEnderCompletoExt._InitializeFacetMap(TSEnderCompletoExt._CF_maxLength,
   TSEnderCompletoExt._CF_minLength,
   TSEnderCompletoExt._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSEnderCompletoExt', TSEnderCompletoExt)
_module_typeBindings.TSEnderCompletoExt = TSEnderCompletoExt

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSEmail
class TSEmail (TSString):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSEmail')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 558, 2)
    _Documentation = None
TSEmail._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(80))
TSEmail._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSEmail._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSEmail._InitializeFacetMap(TSEmail._CF_maxLength,
   TSEmail._CF_minLength,
   TSEmail._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSEmail', TSEmail)
_module_typeBindings.TSEmail = TSEmail

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSNumDocImport
class TSNumDocImport (TSString):

    """Número da Declaração de Importação (DI/DSI/DA/DRI-E) averbado"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSNumDocImport')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 770, 2)
    _Documentation = 'Número da Declaração de Importação (DI/DSI/DA/DRI-E) averbado'
TSNumDocImport._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(12))
TSNumDocImport._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSNumDocImport._InitializeFacetMap(TSNumDocImport._CF_maxLength,
   TSNumDocImport._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'TSNumDocImport', TSNumDocImport)
_module_typeBindings.TSNumDocImport = TSNumDocImport

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSNumRegExport
class TSNumRegExport (TSString):

    """Número do Registro de Exportação (RE) averbado"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSNumRegExport')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 779, 2)
    _Documentation = 'Número do Registro de Exportação (RE) averbado'
TSNumRegExport._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(12))
TSNumRegExport._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSNumRegExport._InitializeFacetMap(TSNumRegExport._CF_maxLength,
   TSNumRegExport._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'TSNumRegExport', TSNumRegExport)
_module_typeBindings.TSNumRegExport = TSNumRegExport

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSDescInfCompl
class TSDescInfCompl (TSString):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSDescInfCompl')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 883, 2)
    _Documentation = None
TSDescInfCompl._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2000))
TSDescInfCompl._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSDescInfCompl._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSDescInfCompl._InitializeFacetMap(TSDescInfCompl._CF_maxLength,
   TSDescInfCompl._CF_minLength,
   TSDescInfCompl._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSDescInfCompl', TSDescInfCompl)
_module_typeBindings.TSDescInfCompl = TSDescInfCompl

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSDescOutDedRed
class TSDescOutDedRed (TSString):

    """Descrição da Dedução/Redução quando a opção é "99 – Outras Deduções" """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSDescOutDedRed')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 934, 2)
    _Documentation = 'Descrição da Dedução/Redução quando a opção é "99 – Outras Deduções"'
TSDescOutDedRed._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(150))
TSDescOutDedRed._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSDescOutDedRed._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSDescOutDedRed._InitializeFacetMap(TSDescOutDedRed._CF_maxLength,
   TSDescOutDedRed._CF_minLength,
   TSDescOutDedRed._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSDescOutDedRed', TSDescOutDedRed)
_module_typeBindings.TSDescOutDedRed = TSDescOutDedRed

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSNumProcesso
class TSNumProcesso (TSString):

    """
        Número do processo judicial ou administrativo de suspensão da exigibilidade.
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSNumProcesso')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1071, 2)
    _Documentation = '\n        Número do processo judicial ou administrativo de suspensão da exigibilidade.\n      '
TSNumProcesso._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
TSNumProcesso._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSNumProcesso._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSNumProcesso._InitializeFacetMap(TSNumProcesso._CF_maxLength,
   TSNumProcesso._CF_minLength,
   TSNumProcesso._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSNumProcesso', TSNumProcesso)
_module_typeBindings.TSNumProcesso = TSNumProcesso

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSCodigoInternoContribuinte
class TSCodigoInternoContribuinte (TSString):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSCodigoInternoContribuinte')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1301, 2)
    _Documentation = None
TSCodigoInternoContribuinte._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20))
TSCodigoInternoContribuinte._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSCodigoInternoContribuinte._CF_pattern = pyxb.binding.facets.CF_pattern()
TSCodigoInternoContribuinte._CF_pattern.addPattern(pattern='[a-zA-Z0-9]{1,20}')
TSCodigoInternoContribuinte._InitializeFacetMap(TSCodigoInternoContribuinte._CF_maxLength,
   TSCodigoInternoContribuinte._CF_minLength,
   TSCodigoInternoContribuinte._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'TSCodigoInternoContribuinte', TSCodigoInternoContribuinte)
_module_typeBindings.TSCodigoInternoContribuinte = TSCodigoInternoContribuinte

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSDesc40
class TSDesc40 (TSString):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSDesc40')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1308, 2)
    _Documentation = None
TSDesc40._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(40))
TSDesc40._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSDesc40._InitializeFacetMap(TSDesc40._CF_maxLength,
   TSDesc40._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'TSDesc40', TSDesc40)
_module_typeBindings.TSDesc40 = TSDesc40

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSDesc150
class TSDesc150 (TSString):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSDesc150')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1314, 2)
    _Documentation = None
TSDesc150._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(150))
TSDesc150._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSDesc150._InitializeFacetMap(TSDesc150._CF_maxLength,
   TSDesc150._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'TSDesc150', TSDesc150)
_module_typeBindings.TSDesc150 = TSDesc150

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSDesc255
class TSDesc255 (TSString):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSDesc255')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1320, 2)
    _Documentation = None
TSDesc255._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(255))
TSDesc255._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSDesc255._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSDesc255._InitializeFacetMap(TSDesc255._CF_maxLength,
   TSDesc255._CF_minLength,
   TSDesc255._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSDesc255', TSDesc255)
_module_typeBindings.TSDesc255 = TSDesc255

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSDesc600
class TSDesc600 (TSString):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSDesc600')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1327, 2)
    _Documentation = None
TSDesc600._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(600))
TSDesc600._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSDesc600._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
TSDesc600._InitializeFacetMap(TSDesc600._CF_maxLength,
   TSDesc600._CF_minLength,
   TSDesc600._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', 'TSDesc600', TSDesc600)
_module_typeBindings.TSDesc600 = TSDesc600

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSDesc1000
class TSDesc1000 (TSString):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSDesc1000')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1334, 2)
    _Documentation = None
TSDesc1000._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(1000))
TSDesc1000._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSDesc1000._InitializeFacetMap(TSDesc1000._CF_maxLength,
   TSDesc1000._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'TSDesc1000', TSDesc1000)
_module_typeBindings.TSDesc1000 = TSDesc1000

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSDesc2000
class TSDesc2000 (TSStringComQuebraDeLinha):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSDesc2000')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1340, 2)
    _Documentation = None
TSDesc2000._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2000))
TSDesc2000._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSDesc2000._InitializeFacetMap(TSDesc2000._CF_maxLength,
   TSDesc2000._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'TSDesc2000', TSDesc2000)
_module_typeBindings.TSDesc2000 = TSDesc2000

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSSituacaoCadastroContribuinte
class TSSituacaoCadastroContribuinte (TSString):

    """Identificação da situação do cadastro do contribuinte"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSSituacaoCadastroContribuinte')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1485, 2)
    _Documentation = 'Identificação da situação do cadastro do contribuinte'
TSSituacaoCadastroContribuinte._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(150))
TSSituacaoCadastroContribuinte._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSSituacaoCadastroContribuinte._InitializeFacetMap(TSSituacaoCadastroContribuinte._CF_maxLength,
   TSSituacaoCadastroContribuinte._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'TSSituacaoCadastroContribuinte', TSSituacaoCadastroContribuinte)
_module_typeBindings.TSSituacaoCadastroContribuinte = TSSituacaoCadastroContribuinte

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSMotivoSituacaoCadastroContribuinte
class TSMotivoSituacaoCadastroContribuinte (TSString):

    """Motivo pelo qual o contribuinte se enquadra na situação informada"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSMotivoSituacaoCadastroContribuinte')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1494, 2)
    _Documentation = 'Motivo pelo qual o contribuinte se enquadra na situação informada'
TSMotivoSituacaoCadastroContribuinte._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSMotivoSituacaoCadastroContribuinte._InitializeFacetMap(TSMotivoSituacaoCadastroContribuinte._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'TSMotivoSituacaoCadastroContribuinte', TSMotivoSituacaoCadastroContribuinte)
_module_typeBindings.TSMotivoSituacaoCadastroContribuinte = TSMotivoSituacaoCadastroContribuinte

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSExtensaoTotal
class TSExtensaoTotal (TSString):

    """Extensão total da ferrovia, rodovia, cabos, dutos ou condutos"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSExtensaoTotal')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1558, 2)
    _Documentation = 'Extensão total da ferrovia, rodovia, cabos, dutos ou condutos'
TSExtensaoTotal._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(5))
TSExtensaoTotal._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSExtensaoTotal._CF_pattern = pyxb.binding.facets.CF_pattern()
TSExtensaoTotal._CF_pattern.addPattern(pattern='[0-9]{1,5}')
TSExtensaoTotal._InitializeFacetMap(TSExtensaoTotal._CF_maxLength,
   TSExtensaoTotal._CF_minLength,
   TSExtensaoTotal._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'TSExtensaoTotal', TSExtensaoTotal)
_module_typeBindings.TSExtensaoTotal = TSExtensaoTotal

# Atomic simple type: {http://www.sped.fazenda.gov.br/nfse}TSNumeroPostes
class TSNumeroPostes (TSString):

    """Número total de postes"""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TSNumeroPostes')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposSimples_v1.00.xsd', 1568, 2)
    _Documentation = 'Número total de postes'
TSNumeroPostes._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(6))
TSNumeroPostes._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
TSNumeroPostes._CF_pattern = pyxb.binding.facets.CF_pattern()
TSNumeroPostes._CF_pattern.addPattern(pattern='[0-9]{1,6}')
TSNumeroPostes._InitializeFacetMap(TSNumeroPostes._CF_maxLength,
   TSNumeroPostes._CF_minLength,
   TSNumeroPostes._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'TSNumeroPostes', TSNumeroPostes)
_module_typeBindings.TSNumeroPostes = TSNumeroPostes
