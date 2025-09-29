# /app/output/pedRegEvento_v1_00.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:c27cf6a1980499753073c1afd72a5bfd80976ec9
# Generated 2025-09-29 12:21:49.635772 by PyXB version 1.2.6 using Python 3.12.11.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:d07989c6-f6fb-4579-8024-b97b0f07310a')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pynfe.utils.nfse.nacional._ds as _ImportedBinding__ds
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.sped.fazenda.gov.br/nfse', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_ds = _ImportedBinding__ds.Namespace
_Namespace_ds.configureCategories(['typeBinding', 'elementBinding'])

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


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 217, 8)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON)
STD_ANON.Cancelamento_de_NFS_e = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Cancelamento de NFS-e', tag='Cancelamento_de_NFS_e')
STD_ANON._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration,
   STD_ANON._CF_whiteSpace)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 246, 8)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_)
STD_ANON_.Cancelamento_de_NFS_e_por_Substituicao = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='Cancelamento de NFS-e por Substituicao', tag='Cancelamento_de_NFS_e_por_Substituicao')
STD_ANON_._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration,
   STD_ANON_._CF_whiteSpace)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 280, 8)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_2)
STD_ANON_2.Solicitacao_de_Analise_Fiscal_para_Cancelamento_de_NFS_e = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='Solicitacao de Analise Fiscal para Cancelamento de NFS-e', tag='Solicitacao_de_Analise_Fiscal_para_Cancelamento_de_NFS_e')
STD_ANON_2._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration,
   STD_ANON_2._CF_whiteSpace)
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 309, 8)
    _Documentation = None
STD_ANON_3._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_3)
STD_ANON_3.Cancelamento_de_NFS_e_Deferido_por_Anlise_Fiscal = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='Cancelamento de NFS-e Deferido por Análise Fiscal', tag='Cancelamento_de_NFS_e_Deferido_por_Anlise_Fiscal')
STD_ANON_3._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_enumeration,
   STD_ANON_3._CF_whiteSpace)
_module_typeBindings.STD_ANON_3 = STD_ANON_3

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 357, 8)
    _Documentation = None
STD_ANON_4._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_4)
STD_ANON_4.Cancelamento_de_NFS_e_Indeferido_por_Anlise_Fiscal = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='Cancelamento de NFS-e Indeferido por Análise Fiscal', tag='Cancelamento_de_NFS_e_Indeferido_por_Anlise_Fiscal')
STD_ANON_4._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_enumeration,
   STD_ANON_4._CF_whiteSpace)
_module_typeBindings.STD_ANON_4 = STD_ANON_4

# Atomic simple type: [anonymous]
class STD_ANON_5 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 404, 8)
    _Documentation = None
STD_ANON_5._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_5)
STD_ANON_5.Confirmao_do_Prestador = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='Confirmação do Prestador', tag='Confirmao_do_Prestador')
STD_ANON_5._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
STD_ANON_5._InitializeFacetMap(STD_ANON_5._CF_enumeration,
   STD_ANON_5._CF_whiteSpace)
_module_typeBindings.STD_ANON_5 = STD_ANON_5

# Atomic simple type: [anonymous]
class STD_ANON_6 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 423, 8)
    _Documentation = None
STD_ANON_6._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_6)
STD_ANON_6.Confirmao_do_Tomador = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='Confirmação do Tomador', tag='Confirmao_do_Tomador')
STD_ANON_6._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
STD_ANON_6._InitializeFacetMap(STD_ANON_6._CF_enumeration,
   STD_ANON_6._CF_whiteSpace)
_module_typeBindings.STD_ANON_6 = STD_ANON_6

# Atomic simple type: [anonymous]
class STD_ANON_7 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 442, 8)
    _Documentation = None
STD_ANON_7._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_7)
STD_ANON_7.Confirmao_do_Intermedirio = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='Confirmação do Intermediário', tag='Confirmao_do_Intermedirio')
STD_ANON_7._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
STD_ANON_7._InitializeFacetMap(STD_ANON_7._CF_enumeration,
   STD_ANON_7._CF_whiteSpace)
_module_typeBindings.STD_ANON_7 = STD_ANON_7

# Atomic simple type: [anonymous]
class STD_ANON_8 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 461, 8)
    _Documentation = None
STD_ANON_8._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_8)
STD_ANON_8.Confirmao_Tcita = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='Confirmação Tácita', tag='Confirmao_Tcita')
STD_ANON_8._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
STD_ANON_8._InitializeFacetMap(STD_ANON_8._CF_enumeration,
   STD_ANON_8._CF_whiteSpace)
_module_typeBindings.STD_ANON_8 = STD_ANON_8

# Atomic simple type: [anonymous]
class STD_ANON_9 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 480, 8)
    _Documentation = None
STD_ANON_9._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_9)
STD_ANON_9.Rejeio_do_Prestador = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value='Rejeição do Prestador', tag='Rejeio_do_Prestador')
STD_ANON_9._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
STD_ANON_9._InitializeFacetMap(STD_ANON_9._CF_enumeration,
   STD_ANON_9._CF_whiteSpace)
_module_typeBindings.STD_ANON_9 = STD_ANON_9

# Atomic simple type: [anonymous]
class STD_ANON_10 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 505, 8)
    _Documentation = None
STD_ANON_10._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_10)
STD_ANON_10.Rejeio_do_Tomador = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value='Rejeição do Tomador', tag='Rejeio_do_Tomador')
STD_ANON_10._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
STD_ANON_10._InitializeFacetMap(STD_ANON_10._CF_enumeration,
   STD_ANON_10._CF_whiteSpace)
_module_typeBindings.STD_ANON_10 = STD_ANON_10

# Atomic simple type: [anonymous]
class STD_ANON_11 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 530, 8)
    _Documentation = None
STD_ANON_11._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_11)
STD_ANON_11.Rejeio_do_Intermedirio = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value='Rejeição do Intermediário', tag='Rejeio_do_Intermedirio')
STD_ANON_11._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
STD_ANON_11._InitializeFacetMap(STD_ANON_11._CF_enumeration,
   STD_ANON_11._CF_whiteSpace)
_module_typeBindings.STD_ANON_11 = STD_ANON_11

# Atomic simple type: [anonymous]
class STD_ANON_12 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 555, 8)
    _Documentation = None
STD_ANON_12._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_12)
STD_ANON_12.Anulao_da_Rejeio = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='Anulação da Rejeição', tag='Anulao_da_Rejeio')
STD_ANON_12._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
STD_ANON_12._InitializeFacetMap(STD_ANON_12._CF_enumeration,
   STD_ANON_12._CF_whiteSpace)
_module_typeBindings.STD_ANON_12 = STD_ANON_12

# Atomic simple type: [anonymous]
class STD_ANON_13 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 580, 8)
    _Documentation = None
STD_ANON_13._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_13)
STD_ANON_13.Cancelamento_de_NFS_e_por_Ofcio = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value='Cancelamento de NFS-e por Ofício', tag='Cancelamento_de_NFS_e_por_Ofcio')
STD_ANON_13._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
STD_ANON_13._InitializeFacetMap(STD_ANON_13._CF_enumeration,
   STD_ANON_13._CF_whiteSpace)
_module_typeBindings.STD_ANON_13 = STD_ANON_13

# Atomic simple type: [anonymous]
class STD_ANON_14 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 620, 8)
    _Documentation = None
STD_ANON_14._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_14)
STD_ANON_14.Bloqueio_de_NFS_e_por_Ofcio = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='Bloqueio de NFS-e por Ofício', tag='Bloqueio_de_NFS_e_por_Ofcio')
STD_ANON_14._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
STD_ANON_14._InitializeFacetMap(STD_ANON_14._CF_enumeration,
   STD_ANON_14._CF_whiteSpace)
_module_typeBindings.STD_ANON_14 = STD_ANON_14

# Atomic simple type: [anonymous]
class STD_ANON_15 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 656, 8)
    _Documentation = None
STD_ANON_15._CF_enumeration = pyxb.binding.facets.CF_enumeration(enum_prefix=None, value_datatype=STD_ANON_15)
STD_ANON_15.Desbloqueio_de_NFS_e_por_Ofcio = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value='Desbloqueio de NFS-e por Ofício', tag='Desbloqueio_de_NFS_e_por_Ofcio')
STD_ANON_15._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.preserve)
STD_ANON_15._InitializeFacetMap(STD_ANON_15._CF_enumeration,
   STD_ANON_15._CF_whiteSpace)
_module_typeBindings.STD_ANON_15 = STD_ANON_15

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

# Complex type {http://www.sped.fazenda.gov.br/nfse}TCEmitente with content type ELEMENT_ONLY
class TCEmitente (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCEmitente with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCEmitente')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 144, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}CNPJ uses Python identifier CNPJ
    __CNPJ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CNPJ'), 'CNPJ', '__httpwww_sped_fazenda_gov_brnfse_TCEmitente_httpwww_sped_fazenda_gov_brnfseCNPJ', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 147, 8), )

    
    CNPJ = property(__CNPJ.value, __CNPJ.set, None, '\n              Número do CNPJ do emitente da NFS-e.\n            ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}CPF uses Python identifier CPF
    __CPF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CPF'), 'CPF', '__httpwww_sped_fazenda_gov_brnfse_TCEmitente_httpwww_sped_fazenda_gov_brnfseCPF', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 154, 8), )

    
    CPF = property(__CPF.value, __CPF.set, None, '\n              Número do CPF do emitente da NFS-e.\n            ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}IM uses Python identifier IM
    __IM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IM'), 'IM', '__httpwww_sped_fazenda_gov_brnfse_TCEmitente_httpwww_sped_fazenda_gov_brnfseIM', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 162, 6), )

    
    IM = property(__IM.value, __IM.set, None, 'Número da inscrição municipal')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xNome uses Python identifier xNome
    __xNome = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xNome'), 'xNome', '__httpwww_sped_fazenda_gov_brnfse_TCEmitente_httpwww_sped_fazenda_gov_brnfsexNome', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 167, 6), )

    
    xNome = property(__xNome.value, __xNome.set, None, '\n            Nome / Razão Social do emitente.\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xFant uses Python identifier xFant
    __xFant = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xFant'), 'xFant', '__httpwww_sped_fazenda_gov_brnfse_TCEmitente_httpwww_sped_fazenda_gov_brnfsexFant', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 174, 6), )

    
    xFant = property(__xFant.value, __xFant.set, None, '\n            Nome / Fantasia do emitente.\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}enderNac uses Python identifier enderNac
    __enderNac = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'enderNac'), 'enderNac', '__httpwww_sped_fazenda_gov_brnfse_TCEmitente_httpwww_sped_fazenda_gov_brnfseenderNac', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 181, 6), )

    
    enderNac = property(__enderNac.value, __enderNac.set, None, 'Grupo de informações do endereço nacional do Emitente da NFS-e')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}fone uses Python identifier fone
    __fone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fone'), 'fone', '__httpwww_sped_fazenda_gov_brnfse_TCEmitente_httpwww_sped_fazenda_gov_brnfsefone', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 186, 6), )

    
    fone = property(__fone.value, __fone.set, None, '\n            Número do telefone do emitente.\n            (Preencher com o Código DDD + número do telefone.\n            Nas operações com exterior é permitido informar o código do país + código da localidade + número do telefone)\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}email uses Python identifier email
    __email = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'email'), 'email', '__httpwww_sped_fazenda_gov_brnfse_TCEmitente_httpwww_sped_fazenda_gov_brnfseemail', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 195, 6), )

    
    email = property(__email.value, __email.set, None, 'E-mail do emitente.')

    _ElementMap.update({
        __CNPJ.name() : __CNPJ,
        __CPF.name() : __CPF,
        __IM.name() : __IM,
        __xNome.name() : __xNome,
        __xFant.name() : __xFant,
        __enderNac.name() : __enderNac,
        __fone.name() : __fone,
        __email.name() : __email
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCEmitente = TCEmitente
Namespace.addCategoryObject('typeBinding', 'TCEmitente', TCEmitente)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCValoresNFSe with content type ELEMENT_ONLY
class TCValoresNFSe (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCValoresNFSe with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCValoresNFSe')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 203, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}vCalcDR uses Python identifier vCalcDR
    __vCalcDR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vCalcDR'), 'vCalcDR', '__httpwww_sped_fazenda_gov_brnfse_TCValoresNFSe_httpwww_sped_fazenda_gov_brnfsevCalcDR', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 205, 6), )

    
    vCalcDR = property(__vCalcDR.value, __vCalcDR.set, None, '\n            Valor monetário (R$) de dedução/redução da base de cálculo (BC) do ISSQN.\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}tpBM uses Python identifier tpBM
    __tpBM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tpBM'), 'tpBM', '__httpwww_sped_fazenda_gov_brnfse_TCValoresNFSe_httpwww_sped_fazenda_gov_brnfsetpBM', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 212, 6), )

    
    tpBM = property(__tpBM.value, __tpBM.set, None, "\n            Tipo Benefício Municipal (BM):\n\n\t\t\t1) Isenção;\n            2) Redução da BC em 'ppBM' %;\n            3) Redução da BC em R$ 'vInfoBM';\n            4) Alíquota Diferenciada de 'aliqDifBM' %;\n          ")

    
    # Element {http://www.sped.fazenda.gov.br/nfse}vCalcBM uses Python identifier vCalcBM
    __vCalcBM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vCalcBM'), 'vCalcBM', '__httpwww_sped_fazenda_gov_brnfse_TCValoresNFSe_httpwww_sped_fazenda_gov_brnfsevCalcBM', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 224, 6), )

    
    vCalcBM = property(__vCalcBM.value, __vCalcBM.set, None, '\n            Valor monetário (R$) do percentual de redução da base de cálculo (BC) do ISSQN devido a um benefício municipal (BM).\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}vBC uses Python identifier vBC
    __vBC = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vBC'), 'vBC', '__httpwww_sped_fazenda_gov_brnfse_TCValoresNFSe_httpwww_sped_fazenda_gov_brnfsevBC', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 231, 6), )

    
    vBC = property(__vBC.value, __vBC.set, None, '\n            Valor monetário (R$) do percentual de redução da base de cálculo (BC) do ISSQN devido a um benefício municipal (BM).\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}pAliqAplic uses Python identifier pAliqAplic
    __pAliqAplic = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'pAliqAplic'), 'pAliqAplic', '__httpwww_sped_fazenda_gov_brnfse_TCValoresNFSe_httpwww_sped_fazenda_gov_brnfsepAliqAplic', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 238, 6), )

    
    pAliqAplic = property(__pAliqAplic.value, __pAliqAplic.set, None, '\n            Alíquota aplicada sobre a base de cálculo para apuração do ISSQN.\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}vISSQN uses Python identifier vISSQN
    __vISSQN = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vISSQN'), 'vISSQN', '__httpwww_sped_fazenda_gov_brnfse_TCValoresNFSe_httpwww_sped_fazenda_gov_brnfsevISSQN', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 245, 6), )

    
    vISSQN = property(__vISSQN.value, __vISSQN.set, None, '\n            Valor do ISSQN (R$) = Valor da Base de Cálculo x Alíquota ISSQN = vBC x pAliqAplic\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}vTotalRet uses Python identifier vTotalRet
    __vTotalRet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vTotalRet'), 'vTotalRet', '__httpwww_sped_fazenda_gov_brnfse_TCValoresNFSe_httpwww_sped_fazenda_gov_brnfsevTotalRet', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 252, 6), )

    
    vTotalRet = property(__vTotalRet.value, __vTotalRet.set, None, '\n            Valor total de retenções = Σ(CP + IRRF + CSLL  + ISSQN* +  (PIS + COFINS)**)\n            vTotalRet (R$) = (vRetCP + vRetIRRF + vRetCSLL) + vISSQN* + (vPIS + vCOFINS)**\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}vLiq uses Python identifier vLiq
    __vLiq = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vLiq'), 'vLiq', '__httpwww_sped_fazenda_gov_brnfse_TCValoresNFSe_httpwww_sped_fazenda_gov_brnfsevLiq', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 260, 6), )

    
    vLiq = property(__vLiq.value, __vLiq.set, None, '\n            Valor líquido = Valor do serviço - Desconto condicionado - Desconto incondicionado - Valores retidos (CP, IRRF, CSLL)* - Valores, se retidos (ISSQN, PIS, COFINS)**\n            Valor Líquido (R$) = vServ – vDescIncond – vDescCond – (vRetCP + vRetIRRF + vRetCSLL)* – (vISSQN - vPIS + vCOFINS)**\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xOutInf uses Python identifier xOutInf
    __xOutInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xOutInf'), 'xOutInf', '__httpwww_sped_fazenda_gov_brnfse_TCValoresNFSe_httpwww_sped_fazenda_gov_brnfsexOutInf', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 268, 6), )

    
    xOutInf = property(__xOutInf.value, __xOutInf.set, None, '\n            Uso da Administração Tributária Municipal.\n          ')

    _ElementMap.update({
        __vCalcDR.name() : __vCalcDR,
        __tpBM.name() : __tpBM,
        __vCalcBM.name() : __vCalcBM,
        __vBC.name() : __vBC,
        __pAliqAplic.name() : __pAliqAplic,
        __vISSQN.name() : __vISSQN,
        __vTotalRet.name() : __vTotalRet,
        __vLiq.name() : __vLiq,
        __xOutInf.name() : __xOutInf
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCValoresNFSe = TCValoresNFSe
Namespace.addCategoryObject('typeBinding', 'TCValoresNFSe', TCValoresNFSe)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCSubstituicao with content type ELEMENT_ONLY
class TCSubstituicao (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCSubstituicao with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCSubstituicao')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 384, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}chSubstda uses Python identifier chSubstda
    __chSubstda = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'chSubstda'), 'chSubstda', '__httpwww_sped_fazenda_gov_brnfse_TCSubstituicao_httpwww_sped_fazenda_gov_brnfsechSubstda', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 386, 6), )

    
    chSubstda = property(__chSubstda.value, __chSubstda.set, None, 'Chave de acesso da NFS-e a ser substituída')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}cMotivo uses Python identifier cMotivo
    __cMotivo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cMotivo'), 'cMotivo', '__httpwww_sped_fazenda_gov_brnfse_TCSubstituicao_httpwww_sped_fazenda_gov_brnfsecMotivo', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 391, 6), )

    
    cMotivo = property(__cMotivo.value, __cMotivo.set, None, '\n            Código de justificativa para substituição de NFS-e:\n            01 - Desenquadramento de NFS-e do Simples Nacional;\n            02 - Enquadramento de NFS-e no Simples Nacional;\n            03 - Inclusão Retroativa de Imunidade/Isenção para NFS-e;\n            04 - Exclusão Retroativa de Imunidade/Isenção para NFS-e;\n            05 - Rejeição de NFS-e pelo tomador ou pelo intermediário se responsável pelo recolhimento do tributo;\n            99 - Outros;\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xMotivo uses Python identifier xMotivo
    __xMotivo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xMotivo'), 'xMotivo', '__httpwww_sped_fazenda_gov_brnfse_TCSubstituicao_httpwww_sped_fazenda_gov_brnfsexMotivo', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 404, 6), )

    
    xMotivo = property(__xMotivo.value, __xMotivo.set, None, 'Descrição do motivo da substituição da NFS-e')

    _ElementMap.update({
        __chSubstda.name() : __chSubstda,
        __cMotivo.name() : __cMotivo,
        __xMotivo.name() : __xMotivo
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCSubstituicao = TCSubstituicao
Namespace.addCategoryObject('typeBinding', 'TCSubstituicao', TCSubstituicao)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCInfoPrestador with content type ELEMENT_ONLY
class TCInfoPrestador (pyxb.binding.basis.complexTypeDefinition):
    """Informações do prestador da NFS-e. Difere das demais pessoas por causa das informações de regimes de tributação"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCInfoPrestador')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 412, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}CNPJ uses Python identifier CNPJ
    __CNPJ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CNPJ'), 'CNPJ', '__httpwww_sped_fazenda_gov_brnfse_TCInfoPrestador_httpwww_sped_fazenda_gov_brnfseCNPJ', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 418, 8), )

    
    CNPJ = property(__CNPJ.value, __CNPJ.set, None, 'Número do CNPJ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}CPF uses Python identifier CPF
    __CPF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CPF'), 'CPF', '__httpwww_sped_fazenda_gov_brnfse_TCInfoPrestador_httpwww_sped_fazenda_gov_brnfseCPF', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 423, 8), )

    
    CPF = property(__CPF.value, __CPF.set, None, 'Número do CPF')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}NIF uses Python identifier NIF
    __NIF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NIF'), 'NIF', '__httpwww_sped_fazenda_gov_brnfse_TCInfoPrestador_httpwww_sped_fazenda_gov_brnfseNIF', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 428, 8), )

    
    NIF = property(__NIF.value, __NIF.set, None, 'Número de Identificação Fiscal fornecido por órgão de administração tributária no exterior')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}cNaoNIF uses Python identifier cNaoNIF
    __cNaoNIF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cNaoNIF'), 'cNaoNIF', '__httpwww_sped_fazenda_gov_brnfse_TCInfoPrestador_httpwww_sped_fazenda_gov_brnfsecNaoNIF', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 433, 8), )

    
    cNaoNIF = property(__cNaoNIF.value, __cNaoNIF.set, None, '\n              Motivo para não informação do NIF:\n              0 - Não informado na nota de origem;\n              1 - Dispensado do NIF;\n              2 - Não exigência do NIF;\n            ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}CAEPF uses Python identifier CAEPF
    __CAEPF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CAEPF'), 'CAEPF', '__httpwww_sped_fazenda_gov_brnfse_TCInfoPrestador_httpwww_sped_fazenda_gov_brnfseCAEPF', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 444, 6), )

    
    CAEPF = property(__CAEPF.value, __CAEPF.set, None, 'Número do Cadastro de Atividade Econômica da Pessoa Física (CAEPF) do prestador do serviço.')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}IM uses Python identifier IM
    __IM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IM'), 'IM', '__httpwww_sped_fazenda_gov_brnfse_TCInfoPrestador_httpwww_sped_fazenda_gov_brnfseIM', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 449, 6), )

    
    IM = property(__IM.value, __IM.set, None, 'Número da inscrição municipal')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xNome uses Python identifier xNome
    __xNome = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xNome'), 'xNome', '__httpwww_sped_fazenda_gov_brnfse_TCInfoPrestador_httpwww_sped_fazenda_gov_brnfsexNome', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 454, 6), )

    
    xNome = property(__xNome.value, __xNome.set, None, 'Nome/Nome Empresarial do prestador')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}end uses Python identifier end
    __end = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'end'), 'end', '__httpwww_sped_fazenda_gov_brnfse_TCInfoPrestador_httpwww_sped_fazenda_gov_brnfseend', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 459, 6), )

    
    end = property(__end.value, __end.set, None, 'Dados de endereço do prestador')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}fone uses Python identifier fone
    __fone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fone'), 'fone', '__httpwww_sped_fazenda_gov_brnfse_TCInfoPrestador_httpwww_sped_fazenda_gov_brnfsefone', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 464, 6), )

    
    fone = property(__fone.value, __fone.set, None, '\n            Número do telefone do prestador:\n            Preencher com o Código DDD + número do telefone.\n            Nas operações com exterior é permitido informar o código do país + código da localidade + número do telefone)\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}email uses Python identifier email
    __email = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'email'), 'email', '__httpwww_sped_fazenda_gov_brnfse_TCInfoPrestador_httpwww_sped_fazenda_gov_brnfseemail', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 473, 6), )

    
    email = property(__email.value, __email.set, None, 'E-mail')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}regTrib uses Python identifier regTrib
    __regTrib = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'regTrib'), 'regTrib', '__httpwww_sped_fazenda_gov_brnfse_TCInfoPrestador_httpwww_sped_fazenda_gov_brnfseregTrib', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 478, 6), )

    
    regTrib = property(__regTrib.value, __regTrib.set, None, '\n            Grupo de informações relativas aos regimes de tributação do prestador de serviços\n          ')

    _ElementMap.update({
        __CNPJ.name() : __CNPJ,
        __CPF.name() : __CPF,
        __NIF.name() : __NIF,
        __cNaoNIF.name() : __cNaoNIF,
        __CAEPF.name() : __CAEPF,
        __IM.name() : __IM,
        __xNome.name() : __xNome,
        __end.name() : __end,
        __fone.name() : __fone,
        __email.name() : __email,
        __regTrib.name() : __regTrib
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCInfoPrestador = TCInfoPrestador
Namespace.addCategoryObject('typeBinding', 'TCInfoPrestador', TCInfoPrestador)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCRegTrib with content type ELEMENT_ONLY
class TCRegTrib (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCRegTrib with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCRegTrib')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 488, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}opSimpNac uses Python identifier opSimpNac
    __opSimpNac = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'opSimpNac'), 'opSimpNac', '__httpwww_sped_fazenda_gov_brnfse_TCRegTrib_httpwww_sped_fazenda_gov_brnfseopSimpNac', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 490, 6), )

    
    opSimpNac = property(__opSimpNac.value, __opSimpNac.set, None, '\n            Situação perante o Simples Nacional:\n            1 - Não Optante;\n            2 - Optante - Microempreendedor Individual (MEI);\n            3 - Optante - Microempresa ou Empresa de Pequeno Porte (ME/EPP);\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}regApTribSN uses Python identifier regApTribSN
    __regApTribSN = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'regApTribSN'), 'regApTribSN', '__httpwww_sped_fazenda_gov_brnfse_TCRegTrib_httpwww_sped_fazenda_gov_brnfseregApTribSN', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 500, 6), )

    
    regApTribSN = property(__regApTribSN.value, __regApTribSN.set, None, '\n            Opção para que o contribuinte optante pelo Simples Nacional ME/EPP (opSimpNac = 3) possa indicar, ao emitir o documento fiscal, em qual regime de apuração os tributos federais e municipal estão inseridos, caso tenha ultrapassado algum sublimite ou limite definido para o Simples Nacional.\n            1 – Regime de apuração dos tributos federais e municipal pelo SN;\n            2 – Regime de apuração dos tributos federais pelo SN e ISSQN  por fora do SN conforme respectiva legislação municipal do tributo;\n            3 – Regime de apuração dos tributos federais e municipal por fora do SN conforme respectivas legilações federal e municipal de cada tributo;\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}regEspTrib uses Python identifier regEspTrib
    __regEspTrib = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'regEspTrib'), 'regEspTrib', '__httpwww_sped_fazenda_gov_brnfse_TCRegTrib_httpwww_sped_fazenda_gov_brnfseregEspTrib', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 510, 6), )

    
    regEspTrib = property(__regEspTrib.value, __regEspTrib.set, None, '\n            Tipos de Regimes Especiais de Tributação:\n            0 - Nenhum;\n            1 - Ato Cooperado (Cooperativa);\n            2 - Estimativa;\n            3 - Microempresa Municipal;\n            4 - Notário ou Registrador;\n            5 - Profissional Autônomo;\n            6 - Sociedade de Profissionais;\n          ')

    _ElementMap.update({
        __opSimpNac.name() : __opSimpNac,
        __regApTribSN.name() : __regApTribSN,
        __regEspTrib.name() : __regEspTrib
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCRegTrib = TCRegTrib
Namespace.addCategoryObject('typeBinding', 'TCRegTrib', TCRegTrib)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCInfoPessoa with content type ELEMENT_ONLY
class TCInfoPessoa (pyxb.binding.basis.complexTypeDefinition):
    """Informações das pessoas envolvidas na NFS-e. Pode ser o tomador, o intermediário ou o fornecedor (dedução/redução)"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCInfoPessoa')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 527, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}CNPJ uses Python identifier CNPJ
    __CNPJ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CNPJ'), 'CNPJ', '__httpwww_sped_fazenda_gov_brnfse_TCInfoPessoa_httpwww_sped_fazenda_gov_brnfseCNPJ', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 533, 8), )

    
    CNPJ = property(__CNPJ.value, __CNPJ.set, None, 'Número do CNPJ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}CPF uses Python identifier CPF
    __CPF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CPF'), 'CPF', '__httpwww_sped_fazenda_gov_brnfse_TCInfoPessoa_httpwww_sped_fazenda_gov_brnfseCPF', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 538, 8), )

    
    CPF = property(__CPF.value, __CPF.set, None, 'Número do CPF')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}NIF uses Python identifier NIF
    __NIF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NIF'), 'NIF', '__httpwww_sped_fazenda_gov_brnfse_TCInfoPessoa_httpwww_sped_fazenda_gov_brnfseNIF', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 543, 8), )

    
    NIF = property(__NIF.value, __NIF.set, None, 'Número de Identificação Fiscal fornecido por órgão de administração tributária no exterior')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}cNaoNIF uses Python identifier cNaoNIF
    __cNaoNIF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cNaoNIF'), 'cNaoNIF', '__httpwww_sped_fazenda_gov_brnfse_TCInfoPessoa_httpwww_sped_fazenda_gov_brnfsecNaoNIF', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 548, 8), )

    
    cNaoNIF = property(__cNaoNIF.value, __cNaoNIF.set, None, '\n              Motivo para não informação do NIF:\n              0 - Não informado na nota de origem;\n              1 - Dispensado do NIF;\n              2 - Não exigência do NIF;\n            ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}CAEPF uses Python identifier CAEPF
    __CAEPF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CAEPF'), 'CAEPF', '__httpwww_sped_fazenda_gov_brnfse_TCInfoPessoa_httpwww_sped_fazenda_gov_brnfseCAEPF', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 559, 6), )

    
    CAEPF = property(__CAEPF.value, __CAEPF.set, None, 'Número do Cadastro de Atividade Econômica da Pessoa Física (CAEPF)')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}IM uses Python identifier IM
    __IM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IM'), 'IM', '__httpwww_sped_fazenda_gov_brnfse_TCInfoPessoa_httpwww_sped_fazenda_gov_brnfseIM', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 564, 6), )

    
    IM = property(__IM.value, __IM.set, None, 'Número da inscrição municipal')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xNome uses Python identifier xNome
    __xNome = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xNome'), 'xNome', '__httpwww_sped_fazenda_gov_brnfse_TCInfoPessoa_httpwww_sped_fazenda_gov_brnfsexNome', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 569, 6), )

    
    xNome = property(__xNome.value, __xNome.set, None, 'Nome/Nome Empresarial')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}end uses Python identifier end
    __end = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'end'), 'end', '__httpwww_sped_fazenda_gov_brnfse_TCInfoPessoa_httpwww_sped_fazenda_gov_brnfseend', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 574, 6), )

    
    end = property(__end.value, __end.set, None, 'Dados de endereço')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}fone uses Python identifier fone
    __fone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fone'), 'fone', '__httpwww_sped_fazenda_gov_brnfse_TCInfoPessoa_httpwww_sped_fazenda_gov_brnfsefone', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 579, 6), )

    
    fone = property(__fone.value, __fone.set, None, '\n            Número do telefone do prestador:\n            Preencher com o Código DDD + número do telefone.\n            Nas operações com exterior é permitido informar o código do país + código da localidade + número do telefone)\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}email uses Python identifier email
    __email = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'email'), 'email', '__httpwww_sped_fazenda_gov_brnfse_TCInfoPessoa_httpwww_sped_fazenda_gov_brnfseemail', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 588, 6), )

    
    email = property(__email.value, __email.set, None, 'E-mail')

    _ElementMap.update({
        __CNPJ.name() : __CNPJ,
        __CPF.name() : __CPF,
        __NIF.name() : __NIF,
        __cNaoNIF.name() : __cNaoNIF,
        __CAEPF.name() : __CAEPF,
        __IM.name() : __IM,
        __xNome.name() : __xNome,
        __end.name() : __end,
        __fone.name() : __fone,
        __email.name() : __email
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCInfoPessoa = TCInfoPessoa
Namespace.addCategoryObject('typeBinding', 'TCInfoPessoa', TCInfoPessoa)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCEndereco with content type ELEMENT_ONLY
class TCEndereco (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCEndereco with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCEndereco')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 596, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}endNac uses Python identifier endNac
    __endNac = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'endNac'), 'endNac', '__httpwww_sped_fazenda_gov_brnfse_TCEndereco_httpwww_sped_fazenda_gov_brnfseendNac', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 599, 8), )

    
    endNac = property(__endNac.value, __endNac.set, None, 'Grupo de informações específicas de endereço nacional')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}endExt uses Python identifier endExt
    __endExt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'endExt'), 'endExt', '__httpwww_sped_fazenda_gov_brnfse_TCEndereco_httpwww_sped_fazenda_gov_brnfseendExt', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 604, 8), )

    
    endExt = property(__endExt.value, __endExt.set, None, 'Grupo de informações específicas de endereço no exterior')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xLgr uses Python identifier xLgr
    __xLgr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xLgr'), 'xLgr', '__httpwww_sped_fazenda_gov_brnfse_TCEndereco_httpwww_sped_fazenda_gov_brnfsexLgr', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 610, 6), )

    
    xLgr = property(__xLgr.value, __xLgr.set, None, 'Tipo e nome do logradouro da localização do imóvel')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}nro uses Python identifier nro
    __nro = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nro'), 'nro', '__httpwww_sped_fazenda_gov_brnfse_TCEndereco_httpwww_sped_fazenda_gov_brnfsenro', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 615, 6), )

    
    nro = property(__nro.value, __nro.set, None, 'Número do imóvel')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xCpl uses Python identifier xCpl
    __xCpl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xCpl'), 'xCpl', '__httpwww_sped_fazenda_gov_brnfse_TCEndereco_httpwww_sped_fazenda_gov_brnfsexCpl', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 620, 6), )

    
    xCpl = property(__xCpl.value, __xCpl.set, None, 'Complemento do endereço')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xBairro uses Python identifier xBairro
    __xBairro = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xBairro'), 'xBairro', '__httpwww_sped_fazenda_gov_brnfse_TCEndereco_httpwww_sped_fazenda_gov_brnfsexBairro', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 625, 6), )

    
    xBairro = property(__xBairro.value, __xBairro.set, None, 'Bairro')

    _ElementMap.update({
        __endNac.name() : __endNac,
        __endExt.name() : __endExt,
        __xLgr.name() : __xLgr,
        __nro.name() : __nro,
        __xCpl.name() : __xCpl,
        __xBairro.name() : __xBairro
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCEndereco = TCEndereco
Namespace.addCategoryObject('typeBinding', 'TCEndereco', TCEndereco)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCEnderecoEmitente with content type ELEMENT_ONLY
class TCEnderecoEmitente (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCEnderecoEmitente with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCEnderecoEmitente')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 633, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}xLgr uses Python identifier xLgr
    __xLgr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xLgr'), 'xLgr', '__httpwww_sped_fazenda_gov_brnfse_TCEnderecoEmitente_httpwww_sped_fazenda_gov_brnfsexLgr', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 635, 6), )

    
    xLgr = property(__xLgr.value, __xLgr.set, None, 'Tipo e nome do logradouro da localização do imóvel')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}nro uses Python identifier nro
    __nro = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nro'), 'nro', '__httpwww_sped_fazenda_gov_brnfse_TCEnderecoEmitente_httpwww_sped_fazenda_gov_brnfsenro', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 640, 6), )

    
    nro = property(__nro.value, __nro.set, None, 'Número do imóvel')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xCpl uses Python identifier xCpl
    __xCpl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xCpl'), 'xCpl', '__httpwww_sped_fazenda_gov_brnfse_TCEnderecoEmitente_httpwww_sped_fazenda_gov_brnfsexCpl', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 645, 6), )

    
    xCpl = property(__xCpl.value, __xCpl.set, None, 'Complemento do endereço')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xBairro uses Python identifier xBairro
    __xBairro = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xBairro'), 'xBairro', '__httpwww_sped_fazenda_gov_brnfse_TCEnderecoEmitente_httpwww_sped_fazenda_gov_brnfsexBairro', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 650, 6), )

    
    xBairro = property(__xBairro.value, __xBairro.set, None, 'Bairro')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}cMun uses Python identifier cMun
    __cMun = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cMun'), 'cMun', '__httpwww_sped_fazenda_gov_brnfse_TCEnderecoEmitente_httpwww_sped_fazenda_gov_brnfsecMun', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 655, 6), )

    
    cMun = property(__cMun.value, __cMun.set, None, 'Código do município, conforme Tabela do IBGE')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}UF uses Python identifier UF
    __UF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UF'), 'UF', '__httpwww_sped_fazenda_gov_brnfse_TCEnderecoEmitente_httpwww_sped_fazenda_gov_brnfseUF', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 660, 6), )

    
    UF = property(__UF.value, __UF.set, None, 'Sigla da unidade da federação do município do endereço do emitente.')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}CEP uses Python identifier CEP
    __CEP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CEP'), 'CEP', '__httpwww_sped_fazenda_gov_brnfse_TCEnderecoEmitente_httpwww_sped_fazenda_gov_brnfseCEP', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 665, 6), )

    
    CEP = property(__CEP.value, __CEP.set, None, 'Número do CEP')

    _ElementMap.update({
        __xLgr.name() : __xLgr,
        __nro.name() : __nro,
        __xCpl.name() : __xCpl,
        __xBairro.name() : __xBairro,
        __cMun.name() : __cMun,
        __UF.name() : __UF,
        __CEP.name() : __CEP
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCEnderecoEmitente = TCEnderecoEmitente
Namespace.addCategoryObject('typeBinding', 'TCEnderecoEmitente', TCEnderecoEmitente)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCEnderecoSimples with content type ELEMENT_ONLY
class TCEnderecoSimples (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCEnderecoSimples with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCEnderecoSimples')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 673, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}CEP uses Python identifier CEP
    __CEP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CEP'), 'CEP', '__httpwww_sped_fazenda_gov_brnfse_TCEnderecoSimples_httpwww_sped_fazenda_gov_brnfseCEP', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 676, 8), )

    
    CEP = property(__CEP.value, __CEP.set, None, 'Número do CEP')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}endExt uses Python identifier endExt
    __endExt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'endExt'), 'endExt', '__httpwww_sped_fazenda_gov_brnfse_TCEnderecoSimples_httpwww_sped_fazenda_gov_brnfseendExt', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 681, 8), )

    
    endExt = property(__endExt.value, __endExt.set, None, 'Grupo de informações específicas de endereço no exterior')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xLgr uses Python identifier xLgr
    __xLgr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xLgr'), 'xLgr', '__httpwww_sped_fazenda_gov_brnfse_TCEnderecoSimples_httpwww_sped_fazenda_gov_brnfsexLgr', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 687, 6), )

    
    xLgr = property(__xLgr.value, __xLgr.set, None, 'Tipo e nome do logradouro da localização do imóvel')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}nro uses Python identifier nro
    __nro = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nro'), 'nro', '__httpwww_sped_fazenda_gov_brnfse_TCEnderecoSimples_httpwww_sped_fazenda_gov_brnfsenro', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 692, 6), )

    
    nro = property(__nro.value, __nro.set, None, 'Número do imóvel')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xCpl uses Python identifier xCpl
    __xCpl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xCpl'), 'xCpl', '__httpwww_sped_fazenda_gov_brnfse_TCEnderecoSimples_httpwww_sped_fazenda_gov_brnfsexCpl', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 697, 6), )

    
    xCpl = property(__xCpl.value, __xCpl.set, None, 'Complemento do endereço')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xBairro uses Python identifier xBairro
    __xBairro = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xBairro'), 'xBairro', '__httpwww_sped_fazenda_gov_brnfse_TCEnderecoSimples_httpwww_sped_fazenda_gov_brnfsexBairro', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 702, 6), )

    
    xBairro = property(__xBairro.value, __xBairro.set, None, 'Bairro')

    _ElementMap.update({
        __CEP.name() : __CEP,
        __endExt.name() : __endExt,
        __xLgr.name() : __xLgr,
        __nro.name() : __nro,
        __xCpl.name() : __xCpl,
        __xBairro.name() : __xBairro
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCEnderecoSimples = TCEnderecoSimples
Namespace.addCategoryObject('typeBinding', 'TCEnderecoSimples', TCEnderecoSimples)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCEnderNac with content type ELEMENT_ONLY
class TCEnderNac (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCEnderNac with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCEnderNac')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 710, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}cMun uses Python identifier cMun
    __cMun = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cMun'), 'cMun', '__httpwww_sped_fazenda_gov_brnfse_TCEnderNac_httpwww_sped_fazenda_gov_brnfsecMun', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 712, 6), )

    
    cMun = property(__cMun.value, __cMun.set, None, 'Código do município, conforme Tabela do IBGE')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}CEP uses Python identifier CEP
    __CEP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CEP'), 'CEP', '__httpwww_sped_fazenda_gov_brnfse_TCEnderNac_httpwww_sped_fazenda_gov_brnfseCEP', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 717, 6), )

    
    CEP = property(__CEP.value, __CEP.set, None, 'Número do CEP')

    _ElementMap.update({
        __cMun.name() : __cMun,
        __CEP.name() : __CEP
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCEnderNac = TCEnderNac
Namespace.addCategoryObject('typeBinding', 'TCEnderNac', TCEnderNac)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCEnderExt with content type ELEMENT_ONLY
class TCEnderExt (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCEnderExt with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCEnderExt')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 725, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}cPais uses Python identifier cPais
    __cPais = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cPais'), 'cPais', '__httpwww_sped_fazenda_gov_brnfse_TCEnderExt_httpwww_sped_fazenda_gov_brnfsecPais', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 727, 6), )

    
    cPais = property(__cPais.value, __cPais.set, None, 'Código do país (Tabela de Países ISO)')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}cEndPost uses Python identifier cEndPost
    __cEndPost = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cEndPost'), 'cEndPost', '__httpwww_sped_fazenda_gov_brnfse_TCEnderExt_httpwww_sped_fazenda_gov_brnfsecEndPost', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 732, 6), )

    
    cEndPost = property(__cEndPost.value, __cEndPost.set, None, 'Código alfanumérico do Endereçamento Postal no exterior do prestador do serviço.')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xCidade uses Python identifier xCidade
    __xCidade = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xCidade'), 'xCidade', '__httpwww_sped_fazenda_gov_brnfse_TCEnderExt_httpwww_sped_fazenda_gov_brnfsexCidade', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 737, 6), )

    
    xCidade = property(__xCidade.value, __xCidade.set, None, 'Nome da cidade no exterior do prestador do serviço.')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xEstProvReg uses Python identifier xEstProvReg
    __xEstProvReg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xEstProvReg'), 'xEstProvReg', '__httpwww_sped_fazenda_gov_brnfse_TCEnderExt_httpwww_sped_fazenda_gov_brnfsexEstProvReg', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 742, 6), )

    
    xEstProvReg = property(__xEstProvReg.value, __xEstProvReg.set, None, 'Estado, província ou região da cidade no exterior do prestador do serviço.')

    _ElementMap.update({
        __cPais.name() : __cPais,
        __cEndPost.name() : __cEndPost,
        __xCidade.name() : __xCidade,
        __xEstProvReg.name() : __xEstProvReg
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCEnderExt = TCEnderExt
Namespace.addCategoryObject('typeBinding', 'TCEnderExt', TCEnderExt)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCEnderExtSimples with content type ELEMENT_ONLY
class TCEnderExtSimples (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCEnderExtSimples with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCEnderExtSimples')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 750, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}cEndPost uses Python identifier cEndPost
    __cEndPost = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cEndPost'), 'cEndPost', '__httpwww_sped_fazenda_gov_brnfse_TCEnderExtSimples_httpwww_sped_fazenda_gov_brnfsecEndPost', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 752, 6), )

    
    cEndPost = property(__cEndPost.value, __cEndPost.set, None, 'Código alfanumérico do Endereçamento Postal no exterior do prestador do serviço.')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xCidade uses Python identifier xCidade
    __xCidade = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xCidade'), 'xCidade', '__httpwww_sped_fazenda_gov_brnfse_TCEnderExtSimples_httpwww_sped_fazenda_gov_brnfsexCidade', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 757, 6), )

    
    xCidade = property(__xCidade.value, __xCidade.set, None, 'Nome da cidade no exterior do prestador do serviço.')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xEstProvReg uses Python identifier xEstProvReg
    __xEstProvReg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xEstProvReg'), 'xEstProvReg', '__httpwww_sped_fazenda_gov_brnfse_TCEnderExtSimples_httpwww_sped_fazenda_gov_brnfsexEstProvReg', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 762, 6), )

    
    xEstProvReg = property(__xEstProvReg.value, __xEstProvReg.set, None, 'Estado, província ou região da cidade no exterior do prestador do serviço.')

    _ElementMap.update({
        __cEndPost.name() : __cEndPost,
        __xCidade.name() : __xCidade,
        __xEstProvReg.name() : __xEstProvReg
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCEnderExtSimples = TCEnderExtSimples
Namespace.addCategoryObject('typeBinding', 'TCEnderExtSimples', TCEnderExtSimples)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCEnderObraEvento with content type ELEMENT_ONLY
class TCEnderObraEvento (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCEnderObraEvento with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCEnderObraEvento')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 770, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}CEP uses Python identifier CEP
    __CEP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CEP'), 'CEP', '__httpwww_sped_fazenda_gov_brnfse_TCEnderObraEvento_httpwww_sped_fazenda_gov_brnfseCEP', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 773, 8), )

    
    CEP = property(__CEP.value, __CEP.set, None, 'Número do CEP')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}endExt uses Python identifier endExt
    __endExt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'endExt'), 'endExt', '__httpwww_sped_fazenda_gov_brnfse_TCEnderObraEvento_httpwww_sped_fazenda_gov_brnfseendExt', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 778, 8), )

    
    endExt = property(__endExt.value, __endExt.set, None, 'Grupo de informações específicas de endereço no exterior')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xLgr uses Python identifier xLgr
    __xLgr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xLgr'), 'xLgr', '__httpwww_sped_fazenda_gov_brnfse_TCEnderObraEvento_httpwww_sped_fazenda_gov_brnfsexLgr', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 784, 6), )

    
    xLgr = property(__xLgr.value, __xLgr.set, None, 'Tipo e nome do logradouro da localização do imóvel')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}nro uses Python identifier nro
    __nro = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nro'), 'nro', '__httpwww_sped_fazenda_gov_brnfse_TCEnderObraEvento_httpwww_sped_fazenda_gov_brnfsenro', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 789, 6), )

    
    nro = property(__nro.value, __nro.set, None, 'Número do imóvel')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xCpl uses Python identifier xCpl
    __xCpl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xCpl'), 'xCpl', '__httpwww_sped_fazenda_gov_brnfse_TCEnderObraEvento_httpwww_sped_fazenda_gov_brnfsexCpl', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 794, 6), )

    
    xCpl = property(__xCpl.value, __xCpl.set, None, 'Complemento do endereço')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xBairro uses Python identifier xBairro
    __xBairro = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xBairro'), 'xBairro', '__httpwww_sped_fazenda_gov_brnfse_TCEnderObraEvento_httpwww_sped_fazenda_gov_brnfsexBairro', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 799, 6), )

    
    xBairro = property(__xBairro.value, __xBairro.set, None, 'Bairro')

    _ElementMap.update({
        __CEP.name() : __CEP,
        __endExt.name() : __endExt,
        __xLgr.name() : __xLgr,
        __nro.name() : __nro,
        __xCpl.name() : __xCpl,
        __xBairro.name() : __xBairro
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCEnderObraEvento = TCEnderObraEvento
Namespace.addCategoryObject('typeBinding', 'TCEnderObraEvento', TCEnderObraEvento)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCServ with content type ELEMENT_ONLY
class TCServ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCServ with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCServ')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 807, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}locPrest uses Python identifier locPrest
    __locPrest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'locPrest'), 'locPrest', '__httpwww_sped_fazenda_gov_brnfse_TCServ_httpwww_sped_fazenda_gov_brnfselocPrest', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 809, 6), )

    
    locPrest = property(__locPrest.value, __locPrest.set, None, '\n            Grupo de informações relativas ao local da prestação do serviço\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}cServ uses Python identifier cServ
    __cServ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cServ'), 'cServ', '__httpwww_sped_fazenda_gov_brnfse_TCServ_httpwww_sped_fazenda_gov_brnfsecServ', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 816, 6), )

    
    cServ = property(__cServ.value, __cServ.set, None, '\n            Grupo de informações relativas ao código do serviço prestado\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}comExt uses Python identifier comExt
    __comExt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'comExt'), 'comExt', '__httpwww_sped_fazenda_gov_brnfse_TCServ_httpwww_sped_fazenda_gov_brnfsecomExt', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 823, 6), )

    
    comExt = property(__comExt.value, __comExt.set, None, 'Grupo de informações relativas à exportação/importação de serviço prestado')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}lsadppu uses Python identifier lsadppu
    __lsadppu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lsadppu'), 'lsadppu', '__httpwww_sped_fazenda_gov_brnfse_TCServ_httpwww_sped_fazenda_gov_brnfselsadppu', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 828, 6), )

    
    lsadppu = property(__lsadppu.value, __lsadppu.set, None, 'Grupo de informações relativas a atividades de Locação, sublocação, arrendamento, direito de passagem ou permissão de uso, compartilhado ou não, de ferrovia, rodovia, postes, cabos, dutos e condutos de qualquer natureza')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}obra uses Python identifier obra
    __obra = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'obra'), 'obra', '__httpwww_sped_fazenda_gov_brnfse_TCServ_httpwww_sped_fazenda_gov_brnfseobra', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 833, 6), )

    
    obra = property(__obra.value, __obra.set, None, 'Grupo de informações do DPS relativas à serviço de obra')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}atvEvento uses Python identifier atvEvento
    __atvEvento = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'atvEvento'), 'atvEvento', '__httpwww_sped_fazenda_gov_brnfse_TCServ_httpwww_sped_fazenda_gov_brnfseatvEvento', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 838, 6), )

    
    atvEvento = property(__atvEvento.value, __atvEvento.set, None, 'Grupo de informações do DPS relativas à Evento')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}explRod uses Python identifier explRod
    __explRod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'explRod'), 'explRod', '__httpwww_sped_fazenda_gov_brnfse_TCServ_httpwww_sped_fazenda_gov_brnfseexplRod', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 843, 6), )

    
    explRod = property(__explRod.value, __explRod.set, None, 'Grupo de informações relativas a pedágio')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}infoCompl uses Python identifier infoCompl
    __infoCompl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'infoCompl'), 'infoCompl', '__httpwww_sped_fazenda_gov_brnfse_TCServ_httpwww_sped_fazenda_gov_brnfseinfoCompl', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 848, 6), )

    
    infoCompl = property(__infoCompl.value, __infoCompl.set, None, '\n            Grupo de informações complementares disponível para todos os serviços prestados\n          ')

    _ElementMap.update({
        __locPrest.name() : __locPrest,
        __cServ.name() : __cServ,
        __comExt.name() : __comExt,
        __lsadppu.name() : __lsadppu,
        __obra.name() : __obra,
        __atvEvento.name() : __atvEvento,
        __explRod.name() : __explRod,
        __infoCompl.name() : __infoCompl
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCServ = TCServ
Namespace.addCategoryObject('typeBinding', 'TCServ', TCServ)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCLocPrest with content type ELEMENT_ONLY
class TCLocPrest (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCLocPrest with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCLocPrest')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 858, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}cLocPrestacao uses Python identifier cLocPrestacao
    __cLocPrestacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cLocPrestacao'), 'cLocPrestacao', '__httpwww_sped_fazenda_gov_brnfse_TCLocPrest_httpwww_sped_fazenda_gov_brnfsecLocPrestacao', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 860, 6), )

    
    cLocPrestacao = property(__cLocPrestacao.value, __cLocPrestacao.set, None, 'Código do município onde o serviço foi prestado (tabela do IBGE)')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}cPaisPrestacao uses Python identifier cPaisPrestacao
    __cPaisPrestacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cPaisPrestacao'), 'cPaisPrestacao', '__httpwww_sped_fazenda_gov_brnfse_TCLocPrest_httpwww_sped_fazenda_gov_brnfsecPaisPrestacao', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 865, 6), )

    
    cPaisPrestacao = property(__cPaisPrestacao.value, __cPaisPrestacao.set, None, 'Código do país onde o serviço foi prestado (Tabela de Países ISO)')

    _ElementMap.update({
        __cLocPrestacao.name() : __cLocPrestacao,
        __cPaisPrestacao.name() : __cPaisPrestacao
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCLocPrest = TCLocPrest
Namespace.addCategoryObject('typeBinding', 'TCLocPrest', TCLocPrest)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCCServ with content type ELEMENT_ONLY
class TCCServ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCCServ with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCCServ')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 873, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}cTribNac uses Python identifier cTribNac
    __cTribNac = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cTribNac'), 'cTribNac', '__httpwww_sped_fazenda_gov_brnfse_TCCServ_httpwww_sped_fazenda_gov_brnfsecTribNac', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 875, 6), )

    
    cTribNac = property(__cTribNac.value, __cTribNac.set, None, '\n            Código de tributação nacional do ISSQN:\n            Regra de formação - 6 dígitos numéricos sendo: 2 para Item (LC 116/2003), 2 para Subitem (LC 116/2003) e 2 para Desdobro Nacional\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}cTribMun uses Python identifier cTribMun
    __cTribMun = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cTribMun'), 'cTribMun', '__httpwww_sped_fazenda_gov_brnfse_TCCServ_httpwww_sped_fazenda_gov_brnfsecTribMun', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 883, 6), )

    
    cTribMun = property(__cTribMun.value, __cTribMun.set, None, 'Código de tributação municipal do ISSQN')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xDescServ uses Python identifier xDescServ
    __xDescServ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xDescServ'), 'xDescServ', '__httpwww_sped_fazenda_gov_brnfse_TCCServ_httpwww_sped_fazenda_gov_brnfsexDescServ', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 888, 6), )

    
    xDescServ = property(__xDescServ.value, __xDescServ.set, None, 'Descrição completa do serviço prestado')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}cNBS uses Python identifier cNBS
    __cNBS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cNBS'), 'cNBS', '__httpwww_sped_fazenda_gov_brnfse_TCCServ_httpwww_sped_fazenda_gov_brnfsecNBS', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 893, 6), )

    
    cNBS = property(__cNBS.value, __cNBS.set, None, 'Código NBS (Nomenclatura Brasileira de Serviços, Intangíveis e outras Operações que produzam Variações no Patrimônio) correspondente ao serviço prestado')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}cIntContrib uses Python identifier cIntContrib
    __cIntContrib = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cIntContrib'), 'cIntContrib', '__httpwww_sped_fazenda_gov_brnfse_TCCServ_httpwww_sped_fazenda_gov_brnfsecIntContrib', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 898, 6), )

    
    cIntContrib = property(__cIntContrib.value, __cIntContrib.set, None, '\n            Código interno do contribuinte\n          ')

    _ElementMap.update({
        __cTribNac.name() : __cTribNac,
        __cTribMun.name() : __cTribMun,
        __xDescServ.name() : __xDescServ,
        __cNBS.name() : __cNBS,
        __cIntContrib.name() : __cIntContrib
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCCServ = TCCServ
Namespace.addCategoryObject('typeBinding', 'TCCServ', TCCServ)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCComExterior with content type ELEMENT_ONLY
class TCComExterior (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCComExterior with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCComExterior')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 908, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}mdPrestacao uses Python identifier mdPrestacao
    __mdPrestacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mdPrestacao'), 'mdPrestacao', '__httpwww_sped_fazenda_gov_brnfse_TCComExterior_httpwww_sped_fazenda_gov_brnfsemdPrestacao', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 910, 6), )

    
    mdPrestacao = property(__mdPrestacao.value, __mdPrestacao.set, None, '\n            Modo de Prestação:\n            0 - Desconhecido (tipo não informado na nota de origem);\n            1 - Transfronteiriço;\n            2 - Consumo no Brasil;\n            3 - Movimento Temporário de Pessoas Físicas;\n            4 - Consumo no Exterior;\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}vincPrest uses Python identifier vincPrest
    __vincPrest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vincPrest'), 'vincPrest', '__httpwww_sped_fazenda_gov_brnfse_TCComExterior_httpwww_sped_fazenda_gov_brnfsevincPrest', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 922, 6), )

    
    vincPrest = property(__vincPrest.value, __vincPrest.set, None, 'Vínculo entre as partes no negócio:\n            0 - Sem vínculo com o Tomador/Prestador\n            1 - Controlada;\n            2 - Controladora;\n            3 - Coligada;\n            4 - Matriz;\n            5 - Filial ou sucursal;\n            6 - Outro vínculo;\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}tpMoeda uses Python identifier tpMoeda
    __tpMoeda = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tpMoeda'), 'tpMoeda', '__httpwww_sped_fazenda_gov_brnfse_TCComExterior_httpwww_sped_fazenda_gov_brnfsetpMoeda', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 935, 6), )

    
    tpMoeda = property(__tpMoeda.value, __tpMoeda.set, None, 'Identifica a moeda da transação comercial')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}vServMoeda uses Python identifier vServMoeda
    __vServMoeda = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vServMoeda'), 'vServMoeda', '__httpwww_sped_fazenda_gov_brnfse_TCComExterior_httpwww_sped_fazenda_gov_brnfsevServMoeda', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 940, 6), )

    
    vServMoeda = property(__vServMoeda.value, __vServMoeda.set, None, 'Valor do serviço prestado expresso em moeda estrangeira especificada em tpmoeda')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}mecAFComexP uses Python identifier mecAFComexP
    __mecAFComexP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mecAFComexP'), 'mecAFComexP', '__httpwww_sped_fazenda_gov_brnfse_TCComExterior_httpwww_sped_fazenda_gov_brnfsemecAFComexP', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 945, 6), )

    
    mecAFComexP = property(__mecAFComexP.value, __mecAFComexP.set, None, '\n            Mecanismo de apoio/fomento ao Comércio Exterior utilizado pelo prestador do serviço:\n            00 - Desconhecido (tipo não informado na nota de origem);\n            01 - Nenhum;\n            02 - ACC - Adiantamento sobre Contrato de Câmbio – Redução a Zero do IR e do IOF;\n            03 - ACE – Adiantamento sobre Cambiais Entregues - Redução a Zero do IR e do IOF;\n            04 - BNDES-Exim Pós-Embarque – Serviços;\n            05 - BNDES-Exim Pré-Embarque - Serviços;\n            06 - FGE - Fundo de Garantia à Exportação;\n            07 - PROEX - EQUALIZAÇÃO\n            08 - PROEX - Financiamento;\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}mecAFComexT uses Python identifier mecAFComexT
    __mecAFComexT = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mecAFComexT'), 'mecAFComexT', '__httpwww_sped_fazenda_gov_brnfse_TCComExterior_httpwww_sped_fazenda_gov_brnfsemecAFComexT', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 961, 6), )

    
    mecAFComexT = property(__mecAFComexT.value, __mecAFComexT.set, None, '\n            Mecanismo de apoio/fomento ao Comércio Exterior utilizado pelo tomador do serviço:\n            00 - Desconhecido (tipo não informado na nota de origem);\n            01 - Nenhum;\n            02 - Adm. Pública e Repr. Internacional;\n            03 - Alugueis e Arrend. Mercantil de maquinas, equip., embarc. e aeronaves;\n            04 - Arrendamento Mercantil de aeronave para empresa de transporte aéreo público;\n            05 - Comissão a agentes externos na exportação;\n            06 - Despesas de armazenagem, mov. e transporte de carga no exterior;\n            07 - Eventos FIFA (subsidiária);\n            08 - Eventos FIFA;\n            09 - Fretes, arrendamentos de embarcações ou aeronaves e outros;\n            10 - Material Aeronáutico;\n            11 - Promoção de Bens no Exterior;\n            12 - Promoção de Dest. Turísticos Brasileiros;\n            13 - Promoção do Brasil no Exterior;\n            14 - Promoção Serviços no Exterior;\n            15 - RECINE;\n            16 - RECOPA;\n            17 - Registro e Manutenção de marcas, patentes e cultivares;\n            18 - REICOMP;\n            19 - REIDI;\n            20 - REPENEC;\n            21 - REPES;\n            22 - RETAERO; \n            23 - RETID;\n            24 - Royalties, Assistência Técnica, Científica e Assemelhados;\n            25 - Serviços de avaliação da conformidade vinculados aos Acordos da OMC;\n            26 - ZPE;\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}movTempBens uses Python identifier movTempBens
    __movTempBens = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'movTempBens'), 'movTempBens', '__httpwww_sped_fazenda_gov_brnfse_TCComExterior_httpwww_sped_fazenda_gov_brnfsemovTempBens', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 995, 6), )

    
    movTempBens = property(__movTempBens.value, __movTempBens.set, None, '\n            Vínculo da Operação à Movimentação Temporária de Bens:\n            0 - Desconhecido (tipo não informado na nota de origem);\n            1 - Não;\n            2 - Vinculada - Declaração de Importação;\n            3 - Vinculada - Declaração de Exportação;\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}nDI uses Python identifier nDI
    __nDI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nDI'), 'nDI', '__httpwww_sped_fazenda_gov_brnfse_TCComExterior_httpwww_sped_fazenda_gov_brnfsenDI', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1006, 6), )

    
    nDI = property(__nDI.value, __nDI.set, None, 'Número da Declaração de Importação (DI/DSI/DA/DRI-E) averbado')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}nRE uses Python identifier nRE
    __nRE = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nRE'), 'nRE', '__httpwww_sped_fazenda_gov_brnfse_TCComExterior_httpwww_sped_fazenda_gov_brnfsenRE', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1011, 6), )

    
    nRE = property(__nRE.value, __nRE.set, None, 'Número do Registro de Exportação (RE) averbado')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}mdic uses Python identifier mdic
    __mdic = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mdic'), 'mdic', '__httpwww_sped_fazenda_gov_brnfse_TCComExterior_httpwww_sped_fazenda_gov_brnfsemdic', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1016, 6), )

    
    mdic = property(__mdic.value, __mdic.set, None, '\n            Compartilhar as informações da NFS-e gerada a partir desta DPS com a Secretaria de Comércio Exterior:\n            0 - Não enviar para o MDIC;\n            1 - Enviar para o MDIC;\n          ')

    _ElementMap.update({
        __mdPrestacao.name() : __mdPrestacao,
        __vincPrest.name() : __vincPrest,
        __tpMoeda.name() : __tpMoeda,
        __vServMoeda.name() : __vServMoeda,
        __mecAFComexP.name() : __mecAFComexP,
        __mecAFComexT.name() : __mecAFComexT,
        __movTempBens.name() : __movTempBens,
        __nDI.name() : __nDI,
        __nRE.name() : __nRE,
        __mdic.name() : __mdic
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCComExterior = TCComExterior
Namespace.addCategoryObject('typeBinding', 'TCComExterior', TCComExterior)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCExploracaoRodoviaria with content type ELEMENT_ONLY
class TCExploracaoRodoviaria (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCExploracaoRodoviaria with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCExploracaoRodoviaria')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1028, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}categVeic uses Python identifier categVeic
    __categVeic = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'categVeic'), 'categVeic', '__httpwww_sped_fazenda_gov_brnfse_TCExploracaoRodoviaria_httpwww_sped_fazenda_gov_brnfsecategVeic', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1030, 6), )

    
    categVeic = property(__categVeic.value, __categVeic.set, None, '\n            Categorias de veículos para cobrança:\n            00 - Categoria de veículos (tipo não informado na nota de origem)\n            01 - Automóvel, caminhonete e furgão;\n            02 - Caminhão leve, ônibus, caminhão trator e furgão;\n            03 - Automóvel e caminhonete com semireboque;\n            04 - Caminhão, caminhão-trator, caminhão-trator com semi-reboque e ônibus;\n            05 - Automóvel e caminhonete com reboque;\n            06 - Caminhão com reboque;\n            07 - Caminhão trator com semi-reboque;\n            08 - Motocicletas, motonetas e bicicletas motorizadas;\n            09 - Veículo especial;\n            10 - Veículo Isento;\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}nEixos uses Python identifier nEixos
    __nEixos = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nEixos'), 'nEixos', '__httpwww_sped_fazenda_gov_brnfse_TCExploracaoRodoviaria_httpwww_sped_fazenda_gov_brnfsenEixos', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1048, 6), )

    
    nEixos = property(__nEixos.value, __nEixos.set, None, 'Número de eixos para fins de cobrança')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}rodagem uses Python identifier rodagem
    __rodagem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'rodagem'), 'rodagem', '__httpwww_sped_fazenda_gov_brnfse_TCExploracaoRodoviaria_httpwww_sped_fazenda_gov_brnfserodagem', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1053, 6), )

    
    rodagem = property(__rodagem.value, __rodagem.set, None, 'Tipo de rodagem')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}sentido uses Python identifier sentido
    __sentido = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'sentido'), 'sentido', '__httpwww_sped_fazenda_gov_brnfse_TCExploracaoRodoviaria_httpwww_sped_fazenda_gov_brnfsesentido', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1058, 6), )

    
    sentido = property(__sentido.value, __sentido.set, None, 'Placa do veículo')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}placa uses Python identifier placa
    __placa = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'placa'), 'placa', '__httpwww_sped_fazenda_gov_brnfse_TCExploracaoRodoviaria_httpwww_sped_fazenda_gov_brnfseplaca', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1063, 6), )

    
    placa = property(__placa.value, __placa.set, None, 'Placa do veículo')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}codAcessoPed uses Python identifier codAcessoPed
    __codAcessoPed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'codAcessoPed'), 'codAcessoPed', '__httpwww_sped_fazenda_gov_brnfse_TCExploracaoRodoviaria_httpwww_sped_fazenda_gov_brnfsecodAcessoPed', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1068, 6), )

    
    codAcessoPed = property(__codAcessoPed.value, __codAcessoPed.set, None, 'Código de acesso gerado automaticamente pelo sistema emissor da concessionária.')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}codContrato uses Python identifier codContrato
    __codContrato = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'codContrato'), 'codContrato', '__httpwww_sped_fazenda_gov_brnfse_TCExploracaoRodoviaria_httpwww_sped_fazenda_gov_brnfsecodContrato', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1073, 6), )

    
    codContrato = property(__codContrato.value, __codContrato.set, None, 'Código de contrato gerado automaticamente pelo sistema nacional no cadastro da concessionária.')

    _ElementMap.update({
        __categVeic.name() : __categVeic,
        __nEixos.name() : __nEixos,
        __rodagem.name() : __rodagem,
        __sentido.name() : __sentido,
        __placa.name() : __placa,
        __codAcessoPed.name() : __codAcessoPed,
        __codContrato.name() : __codContrato
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCExploracaoRodoviaria = TCExploracaoRodoviaria
Namespace.addCategoryObject('typeBinding', 'TCExploracaoRodoviaria', TCExploracaoRodoviaria)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCLocacaoSublocacao with content type ELEMENT_ONLY
class TCLocacaoSublocacao (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCLocacaoSublocacao with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCLocacaoSublocacao')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1081, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}categ uses Python identifier categ
    __categ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'categ'), 'categ', '__httpwww_sped_fazenda_gov_brnfse_TCLocacaoSublocacao_httpwww_sped_fazenda_gov_brnfsecateg', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1083, 6), )

    
    categ = property(__categ.value, __categ.set, None, 'Categoria do serviço')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}objeto uses Python identifier objeto
    __objeto = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'objeto'), 'objeto', '__httpwww_sped_fazenda_gov_brnfse_TCLocacaoSublocacao_httpwww_sped_fazenda_gov_brnfseobjeto', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1088, 6), )

    
    objeto = property(__objeto.value, __objeto.set, None, 'Tipo de objetos da locação, sublocação, arrendamento, direito de passagem ou permissão de uso')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}extensao uses Python identifier extensao
    __extensao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'extensao'), 'extensao', '__httpwww_sped_fazenda_gov_brnfse_TCLocacaoSublocacao_httpwww_sped_fazenda_gov_brnfseextensao', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1093, 6), )

    
    extensao = property(__extensao.value, __extensao.set, None, 'Extensão total da ferrovia, rodovia, cabos, dutos ou condutos')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}nPostes uses Python identifier nPostes
    __nPostes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nPostes'), 'nPostes', '__httpwww_sped_fazenda_gov_brnfse_TCLocacaoSublocacao_httpwww_sped_fazenda_gov_brnfsenPostes', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1098, 6), )

    
    nPostes = property(__nPostes.value, __nPostes.set, None, 'Número total de postes')

    _ElementMap.update({
        __categ.name() : __categ,
        __objeto.name() : __objeto,
        __extensao.name() : __extensao,
        __nPostes.name() : __nPostes
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCLocacaoSublocacao = TCLocacaoSublocacao
Namespace.addCategoryObject('typeBinding', 'TCLocacaoSublocacao', TCLocacaoSublocacao)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCAtvEvento with content type ELEMENT_ONLY
class TCAtvEvento (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCAtvEvento with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCAtvEvento')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1106, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}xNome uses Python identifier xNome
    __xNome = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xNome'), 'xNome', '__httpwww_sped_fazenda_gov_brnfse_TCAtvEvento_httpwww_sped_fazenda_gov_brnfsexNome', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1108, 6), )

    
    xNome = property(__xNome.value, __xNome.set, None, 'Descrição do evento Artístico, Cultural, Esportivo, etc')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}dtIni uses Python identifier dtIni
    __dtIni = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dtIni'), 'dtIni', '__httpwww_sped_fazenda_gov_brnfse_TCAtvEvento_httpwww_sped_fazenda_gov_brnfsedtIni', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1113, 6), )

    
    dtIni = property(__dtIni.value, __dtIni.set, None, 'Data de início da atividade de evento. Ano, Mês e Dia (AAAA-MM-DD)')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}dtFim uses Python identifier dtFim
    __dtFim = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dtFim'), 'dtFim', '__httpwww_sped_fazenda_gov_brnfse_TCAtvEvento_httpwww_sped_fazenda_gov_brnfsedtFim', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1118, 6), )

    
    dtFim = property(__dtFim.value, __dtFim.set, None, 'Data de fim da atividade de evento. Ano, Mês e Dia (AAAA-MM-DD)')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}idAtvEvt uses Python identifier idAtvEvt
    __idAtvEvt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'idAtvEvt'), 'idAtvEvt', '__httpwww_sped_fazenda_gov_brnfse_TCAtvEvento_httpwww_sped_fazenda_gov_brnfseidAtvEvt', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1124, 8), )

    
    idAtvEvt = property(__idAtvEvt.value, __idAtvEvt.set, None, 'Identificação da Atividade de Evento (código identificador de evento determinado pela Administração Tributária Municipal)')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}end uses Python identifier end
    __end = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'end'), 'end', '__httpwww_sped_fazenda_gov_brnfse_TCAtvEvento_httpwww_sped_fazenda_gov_brnfseend', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1129, 8), )

    
    end = property(__end.value, __end.set, None, 'Grupo de informações relativas ao endereço da atividade, evento ou local do serviço prestado')

    _ElementMap.update({
        __xNome.name() : __xNome,
        __dtIni.name() : __dtIni,
        __dtFim.name() : __dtFim,
        __idAtvEvt.name() : __idAtvEvt,
        __end.name() : __end
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCAtvEvento = TCAtvEvento
Namespace.addCategoryObject('typeBinding', 'TCAtvEvento', TCAtvEvento)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCInfoObra with content type ELEMENT_ONLY
class TCInfoObra (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCInfoObra with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCInfoObra')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1138, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}inscImobFisc uses Python identifier inscImobFisc
    __inscImobFisc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inscImobFisc'), 'inscImobFisc', '__httpwww_sped_fazenda_gov_brnfse_TCInfoObra_httpwww_sped_fazenda_gov_brnfseinscImobFisc', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1140, 6), )

    
    inscImobFisc = property(__inscImobFisc.value, __inscImobFisc.set, None, 'Inscrição imobiliária fiscal (código fornecido pela Prefeitura Municipal para a identificação da obra ou para fins de recolhimento do IPTU)')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}cObra uses Python identifier cObra
    __cObra = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cObra'), 'cObra', '__httpwww_sped_fazenda_gov_brnfse_TCInfoObra_httpwww_sped_fazenda_gov_brnfsecObra', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1146, 8), )

    
    cObra = property(__cObra.value, __cObra.set, None, 'Número de identificação da obra.\n              Cadastro Nacional de Obras (CNO) ou Cadastro Específico do INSS (CEI).\n            ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}end uses Python identifier end
    __end = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'end'), 'end', '__httpwww_sped_fazenda_gov_brnfse_TCInfoObra_httpwww_sped_fazenda_gov_brnfseend', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1153, 8), )

    
    end = property(__end.value, __end.set, None, 'Grupo de informações do endereço da obra do serviço prestado\n            ')

    _ElementMap.update({
        __inscImobFisc.name() : __inscImobFisc,
        __cObra.name() : __cObra,
        __end.name() : __end
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCInfoObra = TCInfoObra
Namespace.addCategoryObject('typeBinding', 'TCInfoObra', TCInfoObra)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCInfoCompl with content type ELEMENT_ONLY
class TCInfoCompl (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCInfoCompl with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCInfoCompl')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1163, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}idDocTec uses Python identifier idDocTec
    __idDocTec = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'idDocTec'), 'idDocTec', '__httpwww_sped_fazenda_gov_brnfse_TCInfoCompl_httpwww_sped_fazenda_gov_brnfseidDocTec', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1165, 6), )

    
    idDocTec = property(__idDocTec.value, __idDocTec.set, None, '\n            Identificador de Documento de Responsabilidade Técnica: ART, RRT, DRT, Outros.\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}docRef uses Python identifier docRef
    __docRef = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'docRef'), 'docRef', '__httpwww_sped_fazenda_gov_brnfse_TCInfoCompl_httpwww_sped_fazenda_gov_brnfsedocRef', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1172, 6), )

    
    docRef = property(__docRef.value, __docRef.set, None, '\n            Chave da nota, número identificador da nota, número do contrato ou outro identificador de documento emitido pelo prestador de serviços, que subsidia a emissão dessa nota pelo tomador do serviço ou intermediário (preenchimento obrigatório caso a nota esteja sendo emitida pelo Tomador ou intermediário do serviço).\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xInfComp uses Python identifier xInfComp
    __xInfComp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xInfComp'), 'xInfComp', '__httpwww_sped_fazenda_gov_brnfse_TCInfoCompl_httpwww_sped_fazenda_gov_brnfsexInfComp', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1179, 6), )

    
    xInfComp = property(__xInfComp.value, __xInfComp.set, None, '\n            Informações complementares\n          ')

    _ElementMap.update({
        __idDocTec.name() : __idDocTec,
        __docRef.name() : __docRef,
        __xInfComp.name() : __xInfComp
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCInfoCompl = TCInfoCompl
Namespace.addCategoryObject('typeBinding', 'TCInfoCompl', TCInfoCompl)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCInfoValores with content type ELEMENT_ONLY
class TCInfoValores (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCInfoValores with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCInfoValores')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1189, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}vServPrest uses Python identifier vServPrest
    __vServPrest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vServPrest'), 'vServPrest', '__httpwww_sped_fazenda_gov_brnfse_TCInfoValores_httpwww_sped_fazenda_gov_brnfsevServPrest', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1191, 6), )

    
    vServPrest = property(__vServPrest.value, __vServPrest.set, None, '\n            Grupo de informações relativas aos valores do serviço prestado\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}vDescCondIncond uses Python identifier vDescCondIncond
    __vDescCondIncond = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vDescCondIncond'), 'vDescCondIncond', '__httpwww_sped_fazenda_gov_brnfse_TCInfoValores_httpwww_sped_fazenda_gov_brnfsevDescCondIncond', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1198, 6), )

    
    vDescCondIncond = property(__vDescCondIncond.value, __vDescCondIncond.set, None, '\n            Grupo de informações relativas aos descontos condicionados e incondicionados\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}vDedRed uses Python identifier vDedRed
    __vDedRed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vDedRed'), 'vDedRed', '__httpwww_sped_fazenda_gov_brnfse_TCInfoValores_httpwww_sped_fazenda_gov_brnfsevDedRed', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1205, 6), )

    
    vDedRed = property(__vDedRed.value, __vDedRed.set, None, '\n            Grupo de informações relativas ao valores para dedução/redução do valor da base de cálculo (valor do serviço)\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}trib uses Python identifier trib
    __trib = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'trib'), 'trib', '__httpwww_sped_fazenda_gov_brnfse_TCInfoValores_httpwww_sped_fazenda_gov_brnfsetrib', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1212, 6), )

    
    trib = property(__trib.value, __trib.set, None, '\n            Grupo de informações relacionados aos tributos relacionados ao serviço prestado\n          ')

    _ElementMap.update({
        __vServPrest.name() : __vServPrest,
        __vDescCondIncond.name() : __vDescCondIncond,
        __vDedRed.name() : __vDedRed,
        __trib.name() : __trib
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCInfoValores = TCInfoValores
Namespace.addCategoryObject('typeBinding', 'TCInfoValores', TCInfoValores)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCInfoTributacao with content type ELEMENT_ONLY
class TCInfoTributacao (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCInfoTributacao with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCInfoTributacao')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1222, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}tribMun uses Python identifier tribMun
    __tribMun = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tribMun'), 'tribMun', '__httpwww_sped_fazenda_gov_brnfse_TCInfoTributacao_httpwww_sped_fazenda_gov_brnfsetribMun', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1224, 6), )

    
    tribMun = property(__tribMun.value, __tribMun.set, None, '\n            Grupo de informações relacionados ao Imposto Sobre Serviços de Qualquer Natureza - ISSQN\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}tribFed uses Python identifier tribFed
    __tribFed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tribFed'), 'tribFed', '__httpwww_sped_fazenda_gov_brnfse_TCInfoTributacao_httpwww_sped_fazenda_gov_brnfsetribFed', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1231, 6), )

    
    tribFed = property(__tribFed.value, __tribFed.set, None, '\n            Grupo de informações de outros tributos relacionados ao serviço prestado\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}totTrib uses Python identifier totTrib
    __totTrib = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'totTrib'), 'totTrib', '__httpwww_sped_fazenda_gov_brnfse_TCInfoTributacao_httpwww_sped_fazenda_gov_brnfsetotTrib', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1238, 6), )

    
    totTrib = property(__totTrib.value, __totTrib.set, None, '\n            Grupo de informações para totais aproximados dos tributos relacionados ao serviço prestado\n          ')

    _ElementMap.update({
        __tribMun.name() : __tribMun,
        __tribFed.name() : __tribFed,
        __totTrib.name() : __totTrib
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCInfoTributacao = TCInfoTributacao
Namespace.addCategoryObject('typeBinding', 'TCInfoTributacao', TCInfoTributacao)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCVServPrest with content type ELEMENT_ONLY
class TCVServPrest (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCVServPrest with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCVServPrest')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1248, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}vReceb uses Python identifier vReceb
    __vReceb = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vReceb'), 'vReceb', '__httpwww_sped_fazenda_gov_brnfse_TCVServPrest_httpwww_sped_fazenda_gov_brnfsevReceb', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1250, 6), )

    
    vReceb = property(__vReceb.value, __vReceb.set, None, 'Valor monetário recebido pelo intermediário do serviço (R$)')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}vServ uses Python identifier vServ
    __vServ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vServ'), 'vServ', '__httpwww_sped_fazenda_gov_brnfse_TCVServPrest_httpwww_sped_fazenda_gov_brnfsevServ', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1255, 6), )

    
    vServ = property(__vServ.value, __vServ.set, None, 'Valor dos serviços em R$')

    _ElementMap.update({
        __vReceb.name() : __vReceb,
        __vServ.name() : __vServ
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCVServPrest = TCVServPrest
Namespace.addCategoryObject('typeBinding', 'TCVServPrest', TCVServPrest)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCVDescCondIncond with content type ELEMENT_ONLY
class TCVDescCondIncond (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCVDescCondIncond with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCVDescCondIncond')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1263, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}vDescIncond uses Python identifier vDescIncond
    __vDescIncond = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vDescIncond'), 'vDescIncond', '__httpwww_sped_fazenda_gov_brnfse_TCVDescCondIncond_httpwww_sped_fazenda_gov_brnfsevDescIncond', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1265, 6), )

    
    vDescIncond = property(__vDescIncond.value, __vDescIncond.set, None, 'Valor monetário do desconto incondicionado (R$)')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}vDescCond uses Python identifier vDescCond
    __vDescCond = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vDescCond'), 'vDescCond', '__httpwww_sped_fazenda_gov_brnfse_TCVDescCondIncond_httpwww_sped_fazenda_gov_brnfsevDescCond', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1270, 6), )

    
    vDescCond = property(__vDescCond.value, __vDescCond.set, None, 'Valor monetário do desconto condicionado (R$)')

    _ElementMap.update({
        __vDescIncond.name() : __vDescIncond,
        __vDescCond.name() : __vDescCond
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCVDescCondIncond = TCVDescCondIncond
Namespace.addCategoryObject('typeBinding', 'TCVDescCondIncond', TCVDescCondIncond)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCInfoDedRed with content type ELEMENT_ONLY
class TCInfoDedRed (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCInfoDedRed with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCInfoDedRed')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1278, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}pDR uses Python identifier pDR
    __pDR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'pDR'), 'pDR', '__httpwww_sped_fazenda_gov_brnfse_TCInfoDedRed_httpwww_sped_fazenda_gov_brnfsepDR', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1281, 8), )

    
    pDR = property(__pDR.value, __pDR.set, None, '\n              Valor percentual padrão para dedução/redução do valor do serviço\n            ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}vDR uses Python identifier vDR
    __vDR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vDR'), 'vDR', '__httpwww_sped_fazenda_gov_brnfse_TCInfoDedRed_httpwww_sped_fazenda_gov_brnfsevDR', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1288, 8), )

    
    vDR = property(__vDR.value, __vDR.set, None, '\n              Valor monetário padrão para dedução/redução do valor do serviço\n            ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}documentos uses Python identifier documentos
    __documentos = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'documentos'), 'documentos', '__httpwww_sped_fazenda_gov_brnfse_TCInfoDedRed_httpwww_sped_fazenda_gov_brnfsedocumentos', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1295, 8), )

    
    documentos = property(__documentos.value, __documentos.set, None, '\n              Grupo de informações de documento utilizado para Dedução/Redução do valor do serviço\n            ')

    _ElementMap.update({
        __pDR.name() : __pDR,
        __vDR.name() : __vDR,
        __documentos.name() : __documentos
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCInfoDedRed = TCInfoDedRed
Namespace.addCategoryObject('typeBinding', 'TCInfoDedRed', TCInfoDedRed)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCListaDocDedRed with content type ELEMENT_ONLY
class TCListaDocDedRed (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCListaDocDedRed with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCListaDocDedRed')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1306, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}docDedRed uses Python identifier docDedRed
    __docDedRed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'docDedRed'), 'docDedRed', '__httpwww_sped_fazenda_gov_brnfse_TCListaDocDedRed_httpwww_sped_fazenda_gov_brnfsedocDedRed', True, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1308, 6), )

    
    docDedRed = property(__docDedRed.value, __docDedRed.set, None, '\n            Grupo de informações de documento utilizado para Dedução/Redução do valor do serviço\n          ')

    _ElementMap.update({
        __docDedRed.name() : __docDedRed
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCListaDocDedRed = TCListaDocDedRed
Namespace.addCategoryObject('typeBinding', 'TCListaDocDedRed', TCListaDocDedRed)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCDocDedRed with content type ELEMENT_ONLY
class TCDocDedRed (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCDocDedRed with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCDocDedRed')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1318, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}chNFSe uses Python identifier chNFSe
    __chNFSe = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'chNFSe'), 'chNFSe', '__httpwww_sped_fazenda_gov_brnfse_TCDocDedRed_httpwww_sped_fazenda_gov_brnfsechNFSe', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1321, 8), )

    
    chNFSe = property(__chNFSe.value, __chNFSe.set, None, 'Chave de Acesso da NFS-e (Padrão Nacional)')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}chNFe uses Python identifier chNFe
    __chNFe = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'chNFe'), 'chNFe', '__httpwww_sped_fazenda_gov_brnfse_TCDocDedRed_httpwww_sped_fazenda_gov_brnfsechNFe', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1326, 8), )

    
    chNFe = property(__chNFe.value, __chNFe.set, None, 'Chave de Acesso da NF-e')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}NFSeMun uses Python identifier NFSeMun
    __NFSeMun = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NFSeMun'), 'NFSeMun', '__httpwww_sped_fazenda_gov_brnfse_TCDocDedRed_httpwww_sped_fazenda_gov_brnfseNFSeMun', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1331, 8), )

    
    NFSeMun = property(__NFSeMun.value, __NFSeMun.set, None, 'Grupo de informações de Outras NFS-e (Padrão anterior de NFS-e)')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}NFNFS uses Python identifier NFNFS
    __NFNFS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NFNFS'), 'NFNFS', '__httpwww_sped_fazenda_gov_brnfse_TCDocDedRed_httpwww_sped_fazenda_gov_brnfseNFNFS', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1336, 8), )

    
    NFNFS = property(__NFNFS.value, __NFNFS.set, None, 'Grupo de informações de NF ou NFS (Modelo não eletrônico)')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}nDocFisc uses Python identifier nDocFisc
    __nDocFisc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nDocFisc'), 'nDocFisc', '__httpwww_sped_fazenda_gov_brnfse_TCDocDedRed_httpwww_sped_fazenda_gov_brnfsenDocFisc', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1341, 8), )

    
    nDocFisc = property(__nDocFisc.value, __nDocFisc.set, None, 'Número de documento fiscal')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}nDoc uses Python identifier nDoc
    __nDoc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nDoc'), 'nDoc', '__httpwww_sped_fazenda_gov_brnfse_TCDocDedRed_httpwww_sped_fazenda_gov_brnfsenDoc', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1346, 8), )

    
    nDoc = property(__nDoc.value, __nDoc.set, None, 'Número de documento não fiscal')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}tpDedRed uses Python identifier tpDedRed
    __tpDedRed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tpDedRed'), 'tpDedRed', '__httpwww_sped_fazenda_gov_brnfse_TCDocDedRed_httpwww_sped_fazenda_gov_brnfsetpDedRed', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1352, 6), )

    
    tpDedRed = property(__tpDedRed.value, __tpDedRed.set, None, '\n            Identificação da Dedução/Redução:\n            1 – Alimentação e bebidas/frigobar;\n            2 – Materiais;\n            3 – Produção externa;\n            4 – Reembolso de despesas;\n            5 – Repasse consorciado;\n            6 – Repasse plano de saúde;\n            7 – Serviços;\n            8 – Subempreitada de mão de obra;\n            99 – Outras deduções;\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xDescOutDed uses Python identifier xDescOutDed
    __xDescOutDed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xDescOutDed'), 'xDescOutDed', '__httpwww_sped_fazenda_gov_brnfse_TCDocDedRed_httpwww_sped_fazenda_gov_brnfsexDescOutDed', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1368, 6), )

    
    xDescOutDed = property(__xDescOutDed.value, __xDescOutDed.set, None, 'Descrição da Dedução/Redução quando a opção é "99 – Outras Deduções"')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}dtEmiDoc uses Python identifier dtEmiDoc
    __dtEmiDoc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dtEmiDoc'), 'dtEmiDoc', '__httpwww_sped_fazenda_gov_brnfse_TCDocDedRed_httpwww_sped_fazenda_gov_brnfsedtEmiDoc', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1373, 6), )

    
    dtEmiDoc = property(__dtEmiDoc.value, __dtEmiDoc.set, None, 'Data da emissão do documento dedutível. Ano, mês e dia (AAAA-MM-DD)')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}vDedutivelRedutivel uses Python identifier vDedutivelRedutivel
    __vDedutivelRedutivel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vDedutivelRedutivel'), 'vDedutivelRedutivel', '__httpwww_sped_fazenda_gov_brnfse_TCDocDedRed_httpwww_sped_fazenda_gov_brnfsevDedutivelRedutivel', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1378, 6), )

    
    vDedutivelRedutivel = property(__vDedutivelRedutivel.value, __vDedutivelRedutivel.set, None, '\n            Valor monetário total dedutível/redutível no documento informado (R$).\n            Este é o valor total no documento informado que é passível de dedução/redução.\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}vDeducaoReducao uses Python identifier vDeducaoReducao
    __vDeducaoReducao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vDeducaoReducao'), 'vDeducaoReducao', '__httpwww_sped_fazenda_gov_brnfse_TCDocDedRed_httpwww_sped_fazenda_gov_brnfsevDeducaoReducao', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1386, 6), )

    
    vDeducaoReducao = property(__vDeducaoReducao.value, __vDeducaoReducao.set, None, '\n            Valor monetário utilizado para dedução/redução do valor do serviço da NFS-e que está sendo emitida (R$).\n            Deve ser menor ou igual ao valor deduzível/redutível (vDedutivelRedutivel).\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}fornec uses Python identifier fornec
    __fornec = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'fornec'), 'fornec', '__httpwww_sped_fazenda_gov_brnfse_TCDocDedRed_httpwww_sped_fazenda_gov_brnfsefornec', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1394, 6), )

    
    fornec = property(__fornec.value, __fornec.set, None, 'Grupo de informações do Fornecedor em Deduções de Serviços')

    _ElementMap.update({
        __chNFSe.name() : __chNFSe,
        __chNFe.name() : __chNFe,
        __NFSeMun.name() : __NFSeMun,
        __NFNFS.name() : __NFNFS,
        __nDocFisc.name() : __nDocFisc,
        __nDoc.name() : __nDoc,
        __tpDedRed.name() : __tpDedRed,
        __xDescOutDed.name() : __xDescOutDed,
        __dtEmiDoc.name() : __dtEmiDoc,
        __vDedutivelRedutivel.name() : __vDedutivelRedutivel,
        __vDeducaoReducao.name() : __vDeducaoReducao,
        __fornec.name() : __fornec
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCDocDedRed = TCDocDedRed
Namespace.addCategoryObject('typeBinding', 'TCDocDedRed', TCDocDedRed)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCDocOutNFSe with content type ELEMENT_ONLY
class TCDocOutNFSe (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCDocOutNFSe with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCDocOutNFSe')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1402, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}cMunNFSeMun uses Python identifier cMunNFSeMun
    __cMunNFSeMun = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cMunNFSeMun'), 'cMunNFSeMun', '__httpwww_sped_fazenda_gov_brnfse_TCDocOutNFSe_httpwww_sped_fazenda_gov_brnfsecMunNFSeMun', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1404, 6), )

    
    cMunNFSeMun = property(__cMunNFSeMun.value, __cMunNFSeMun.set, None, 'Código Município emissor da nota eletrônica municipal (Tabela do IBGE)')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}nNFSeMun uses Python identifier nNFSeMun
    __nNFSeMun = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nNFSeMun'), 'nNFSeMun', '__httpwww_sped_fazenda_gov_brnfse_TCDocOutNFSe_httpwww_sped_fazenda_gov_brnfsenNFSeMun', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1409, 6), )

    
    nNFSeMun = property(__nNFSeMun.value, __nNFSeMun.set, None, 'Número da nota eletrônica municipal')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}cVerifNFSeMun uses Python identifier cVerifNFSeMun
    __cVerifNFSeMun = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cVerifNFSeMun'), 'cVerifNFSeMun', '__httpwww_sped_fazenda_gov_brnfse_TCDocOutNFSe_httpwww_sped_fazenda_gov_brnfsecVerifNFSeMun', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1414, 6), )

    
    cVerifNFSeMun = property(__cVerifNFSeMun.value, __cVerifNFSeMun.set, None, 'Código de Verificação da nota eletrônica municipal')

    _ElementMap.update({
        __cMunNFSeMun.name() : __cMunNFSeMun,
        __nNFSeMun.name() : __nNFSeMun,
        __cVerifNFSeMun.name() : __cVerifNFSeMun
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCDocOutNFSe = TCDocOutNFSe
Namespace.addCategoryObject('typeBinding', 'TCDocOutNFSe', TCDocOutNFSe)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCDocNFNFS with content type ELEMENT_ONLY
class TCDocNFNFS (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCDocNFNFS with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCDocNFNFS')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1422, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}nNFS uses Python identifier nNFS
    __nNFS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nNFS'), 'nNFS', '__httpwww_sped_fazenda_gov_brnfse_TCDocNFNFS_httpwww_sped_fazenda_gov_brnfsenNFS', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1424, 6), )

    
    nNFS = property(__nNFS.value, __nNFS.set, None, 'Número da Nota Fiscal NF ou NFS')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}modNFS uses Python identifier modNFS
    __modNFS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'modNFS'), 'modNFS', '__httpwww_sped_fazenda_gov_brnfse_TCDocNFNFS_httpwww_sped_fazenda_gov_brnfsemodNFS', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1429, 6), )

    
    modNFS = property(__modNFS.value, __modNFS.set, None, 'Modelo da Nota Fiscal NF ou NFS')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}serieNFS uses Python identifier serieNFS
    __serieNFS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'serieNFS'), 'serieNFS', '__httpwww_sped_fazenda_gov_brnfse_TCDocNFNFS_httpwww_sped_fazenda_gov_brnfseserieNFS', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1434, 6), )

    
    serieNFS = property(__serieNFS.value, __serieNFS.set, None, 'Série Nota Fiscal NF ou NFS')

    _ElementMap.update({
        __nNFS.name() : __nNFS,
        __modNFS.name() : __modNFS,
        __serieNFS.name() : __serieNFS
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCDocNFNFS = TCDocNFNFS
Namespace.addCategoryObject('typeBinding', 'TCDocNFNFS', TCDocNFNFS)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCTribMunicipal with content type ELEMENT_ONLY
class TCTribMunicipal (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCTribMunicipal with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCTribMunicipal')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1442, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}tribISSQN uses Python identifier tribISSQN
    __tribISSQN = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tribISSQN'), 'tribISSQN', '__httpwww_sped_fazenda_gov_brnfse_TCTribMunicipal_httpwww_sped_fazenda_gov_brnfsetribISSQN', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1444, 6), )

    
    tribISSQN = property(__tribISSQN.value, __tribISSQN.set, None, '\n            Tributação do ISSQN sobre o serviço prestado:\n            1 - Operação tributável;\n            2 - Imunidade;\n            3 - Exportação de serviço;\n            4 - Não Incidência;\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}cPaisResult uses Python identifier cPaisResult
    __cPaisResult = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cPaisResult'), 'cPaisResult', '__httpwww_sped_fazenda_gov_brnfse_TCTribMunicipal_httpwww_sped_fazenda_gov_brnfsecPaisResult', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1455, 6), )

    
    cPaisResult = property(__cPaisResult.value, __cPaisResult.set, None, '\n            Código do país onde se verficou o resultado da prestação do serviço para o caso de Exportação de Serviço.(Tabela de Países ISO)\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}tpImunidade uses Python identifier tpImunidade
    __tpImunidade = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tpImunidade'), 'tpImunidade', '__httpwww_sped_fazenda_gov_brnfse_TCTribMunicipal_httpwww_sped_fazenda_gov_brnfsetpImunidade', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1462, 6), )

    
    tpImunidade = property(__tpImunidade.value, __tpImunidade.set, None, '\n            Identificação da Imunidade do ISSQN – somente para o caso de Imunidade.\n            Tipos de Imunidades:            \n            0 - Imunidade (tipo não informado na nota de origem);\n            1 - Patrimônio, renda ou serviços, uns dos outros (CF88, Art 150, VI, a);\n            2 - Templos de qualquer culto (CF88, Art 150, VI, b);\n            3 - Patrimônio, renda ou serviços dos partidos políticos, inclusive suas fundações, das entidades sindicais dos trabalhadores, das instituições de educação e de assistência social, sem fins lucrativos, atendidos os requisitos da lei (CF88, Art 150, VI, c);\n            4 - Livros, jornais, periódicos e o papel destinado a sua impressão (CF88, Art 150, VI, d);\n            5 - Fonogramas e videofonogramas musicais produzidos no Brasil contendo obras musicais ou literomusicais de autores brasileiros e/ou obras em geral interpretadas por artistas brasileiros bem como os suportes materiais ou arquivos digitais que os contenham, salvo na etapa de replicação industrial de mídias ópticas de leitura a laser.   (CF88, Art 150, VI, e);\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}exigSusp uses Python identifier exigSusp
    __exigSusp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'exigSusp'), 'exigSusp', '__httpwww_sped_fazenda_gov_brnfse_TCTribMunicipal_httpwww_sped_fazenda_gov_brnfseexigSusp', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1476, 6), )

    
    exigSusp = property(__exigSusp.value, __exigSusp.set, None, '\n            Informações para a suspensão da Exigibilidade do ISSQN\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}BM uses Python identifier BM
    __BM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BM'), 'BM', '__httpwww_sped_fazenda_gov_brnfse_TCTribMunicipal_httpwww_sped_fazenda_gov_brnfseBM', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1483, 6), )

    
    BM = property(__BM.value, __BM.set, None, '\n            Tributação do ISSQN sobre o serviço prestado:\n            1 - Operação tributável;\n            2 - Exportação de serviço;\n            3 - Não Incidência;\n            4 - Imunidade;\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}tpRetISSQN uses Python identifier tpRetISSQN
    __tpRetISSQN = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tpRetISSQN'), 'tpRetISSQN', '__httpwww_sped_fazenda_gov_brnfse_TCTribMunicipal_httpwww_sped_fazenda_gov_brnfsetpRetISSQN', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1494, 6), )

    
    tpRetISSQN = property(__tpRetISSQN.value, __tpRetISSQN.set, None, '\n            Tipo de retencao do ISSQN:\n            1 - Não Retido;\n            2 - Retido pelo Tomador;\n            3 - Retido pelo Intermediario;\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}pAliq uses Python identifier pAliq
    __pAliq = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'pAliq'), 'pAliq', '__httpwww_sped_fazenda_gov_brnfse_TCTribMunicipal_httpwww_sped_fazenda_gov_brnfsepAliq', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1504, 6), )

    
    pAliq = property(__pAliq.value, __pAliq.set, None, '\n            Valor da alíquota (%) do serviço prestado relativo ao município sujeito ativo (município de incidência) do ISSQN.\n            Se o município de incidência pertence ao Sistema Nacional NFS-e a alíquota estará parametrizada e, portanto, será fornecida pelo sistema.\n            Se o município de incidência não pertence ao Sistema Nacional NFS-e a alíquota não estará parametrizada e, por isso, deverá ser fornecida pelo emitente.\n          ')

    _ElementMap.update({
        __tribISSQN.name() : __tribISSQN,
        __cPaisResult.name() : __cPaisResult,
        __tpImunidade.name() : __tpImunidade,
        __exigSusp.name() : __exigSusp,
        __BM.name() : __BM,
        __tpRetISSQN.name() : __tpRetISSQN,
        __pAliq.name() : __pAliq
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCTribMunicipal = TCTribMunicipal
Namespace.addCategoryObject('typeBinding', 'TCTribMunicipal', TCTribMunicipal)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCBeneficioMunicipal with content type ELEMENT_ONLY
class TCBeneficioMunicipal (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCBeneficioMunicipal with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCBeneficioMunicipal')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1516, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}nBM uses Python identifier nBM
    __nBM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nBM'), 'nBM', '__httpwww_sped_fazenda_gov_brnfse_TCBeneficioMunicipal_httpwww_sped_fazenda_gov_brnfsenBM', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1518, 6), )

    
    nBM = property(__nBM.value, __nBM.set, None, '\n            Identificador do benefício parametrizado pelo município.\n\n            Trata-se de um identificador único que foi gerado pelo Sistema Nacional no momento em que o município de incidência do ISSQN incluiu o benefício no sistema.\n            \n            Critério de formação do número de identificação de parâmetros municipais:\n            7 dígitos - posição 1 a 7: número identificador do Município, conforme código IBGE;\n            2 dígitos - posições 8 e 9 : número identificador do tipo de parametrização (01-legislação, 02-regimes especiais, 03-retenções, 04-outros benefícios);\n            5 dígitos - posição 10 a 14 : número sequencial definido pelo sistema quando do registro específico do parâmetro dentro do tipo de parametrização no sistema;\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}vRedBCBM uses Python identifier vRedBCBM
    __vRedBCBM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vRedBCBM'), 'vRedBCBM', '__httpwww_sped_fazenda_gov_brnfse_TCBeneficioMunicipal_httpwww_sped_fazenda_gov_brnfsevRedBCBM', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1533, 8), )

    
    vRedBCBM = property(__vRedBCBM.value, __vRedBCBM.set, None, '\n              Valor monetário informado pelo emitente para redução da base de cálculo (BC) do ISSQN devido a um Benefício Municipal (BM).\n            ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}pRedBCBM uses Python identifier pRedBCBM
    __pRedBCBM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'pRedBCBM'), 'pRedBCBM', '__httpwww_sped_fazenda_gov_brnfse_TCBeneficioMunicipal_httpwww_sped_fazenda_gov_brnfsepRedBCBM', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1540, 8), )

    
    pRedBCBM = property(__pRedBCBM.value, __pRedBCBM.set, None, '\n              Valor percentual informado pelo emitente para redução da base de cálculo (BC) do ISSQN devido a um Benefício Municipal (BM).\n            ')

    _ElementMap.update({
        __nBM.name() : __nBM,
        __vRedBCBM.name() : __vRedBCBM,
        __pRedBCBM.name() : __pRedBCBM
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCBeneficioMunicipal = TCBeneficioMunicipal
Namespace.addCategoryObject('typeBinding', 'TCBeneficioMunicipal', TCBeneficioMunicipal)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCExigSuspensa with content type ELEMENT_ONLY
class TCExigSuspensa (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCExigSuspensa with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCExigSuspensa')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1551, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}tpSusp uses Python identifier tpSusp
    __tpSusp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tpSusp'), 'tpSusp', '__httpwww_sped_fazenda_gov_brnfse_TCExigSuspensa_httpwww_sped_fazenda_gov_brnfsetpSusp', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1553, 6), )

    
    tpSusp = property(__tpSusp.value, __tpSusp.set, None, '\n            Opção para Exigibilidade Suspensa:\n            1 - Exigibilidade Suspensa por Decisão Judicial;\n            2 - Exigibilidade Suspensa por Processo Administrativo;\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}nProcesso uses Python identifier nProcesso
    __nProcesso = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nProcesso'), 'nProcesso', '__httpwww_sped_fazenda_gov_brnfse_TCExigSuspensa_httpwww_sped_fazenda_gov_brnfsenProcesso', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1562, 6), )

    
    nProcesso = property(__nProcesso.value, __nProcesso.set, None, '\n            Número do processo judicial ou administrativo de suspensão da exigibilidade\n          ')

    _ElementMap.update({
        __tpSusp.name() : __tpSusp,
        __nProcesso.name() : __nProcesso
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCExigSuspensa = TCExigSuspensa
Namespace.addCategoryObject('typeBinding', 'TCExigSuspensa', TCExigSuspensa)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCTribFederal with content type ELEMENT_ONLY
class TCTribFederal (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCTribFederal with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCTribFederal')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1572, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}piscofins uses Python identifier piscofins
    __piscofins = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'piscofins'), 'piscofins', '__httpwww_sped_fazenda_gov_brnfse_TCTribFederal_httpwww_sped_fazenda_gov_brnfsepiscofins', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1574, 6), )

    
    piscofins = property(__piscofins.value, __piscofins.set, None, '\n            Grupo de informações dos tributos PIS/COFINS\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}vRetCP uses Python identifier vRetCP
    __vRetCP = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vRetCP'), 'vRetCP', '__httpwww_sped_fazenda_gov_brnfse_TCTribFederal_httpwww_sped_fazenda_gov_brnfsevRetCP', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1581, 6), )

    
    vRetCP = property(__vRetCP.value, __vRetCP.set, None, '\n            Valor monetário do CP(R$).\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}vRetIRRF uses Python identifier vRetIRRF
    __vRetIRRF = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vRetIRRF'), 'vRetIRRF', '__httpwww_sped_fazenda_gov_brnfse_TCTribFederal_httpwww_sped_fazenda_gov_brnfsevRetIRRF', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1588, 6), )

    
    vRetIRRF = property(__vRetIRRF.value, __vRetIRRF.set, None, '\n            Valor monetário do IRRF (R$).\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}vRetCSLL uses Python identifier vRetCSLL
    __vRetCSLL = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vRetCSLL'), 'vRetCSLL', '__httpwww_sped_fazenda_gov_brnfse_TCTribFederal_httpwww_sped_fazenda_gov_brnfsevRetCSLL', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1595, 6), )

    
    vRetCSLL = property(__vRetCSLL.value, __vRetCSLL.set, None, '\n            Valor monetário do CSLL (R$).\n          ')

    _ElementMap.update({
        __piscofins.name() : __piscofins,
        __vRetCP.name() : __vRetCP,
        __vRetIRRF.name() : __vRetIRRF,
        __vRetCSLL.name() : __vRetCSLL
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCTribFederal = TCTribFederal
Namespace.addCategoryObject('typeBinding', 'TCTribFederal', TCTribFederal)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCTribOutrosPisCofins with content type ELEMENT_ONLY
class TCTribOutrosPisCofins (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCTribOutrosPisCofins with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCTribOutrosPisCofins')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1605, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}CST uses Python identifier CST
    __CST = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CST'), 'CST', '__httpwww_sped_fazenda_gov_brnfse_TCTribOutrosPisCofins_httpwww_sped_fazenda_gov_brnfseCST', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1607, 6), )

    
    CST = property(__CST.value, __CST.set, None, '\n            Código de Situação Tributária do PIS/COFINS (CST):\n            00 - Nenhum;      \n            01 - Operação Tributável com Alíquota Básica;\n            02 - Operação Tributável com Alíquota Diferenciada;\n            03 - Operação Tributável com Alíquota por Unidade de Medida de Produto;\n            04 - Operação Tributável monofásica - Revenda a Alíquota Zero;\n            05 - Operação Tributável por Substituição Tributária;\n            06 - Operação Tributável a Alíquota Zero;\n            07 - Operação Tributável da Contribuição;\n            08 - Operação sem Incidência da Contribuição;\n            09 - Operação com Suspensão da Contribuição;\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}vBCPisCofins uses Python identifier vBCPisCofins
    __vBCPisCofins = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vBCPisCofins'), 'vBCPisCofins', '__httpwww_sped_fazenda_gov_brnfse_TCTribOutrosPisCofins_httpwww_sped_fazenda_gov_brnfsevBCPisCofins', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1624, 6), )

    
    vBCPisCofins = property(__vBCPisCofins.value, __vBCPisCofins.set, None, '\n            Valor da Base de Cálculo do PIS/COFINS (R$).\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}pAliqPis uses Python identifier pAliqPis
    __pAliqPis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'pAliqPis'), 'pAliqPis', '__httpwww_sped_fazenda_gov_brnfse_TCTribOutrosPisCofins_httpwww_sped_fazenda_gov_brnfsepAliqPis', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1631, 6), )

    
    pAliqPis = property(__pAliqPis.value, __pAliqPis.set, None, '\n            Valor da Alíquota do PIS (%).\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}pAliqCofins uses Python identifier pAliqCofins
    __pAliqCofins = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'pAliqCofins'), 'pAliqCofins', '__httpwww_sped_fazenda_gov_brnfse_TCTribOutrosPisCofins_httpwww_sped_fazenda_gov_brnfsepAliqCofins', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1638, 6), )

    
    pAliqCofins = property(__pAliqCofins.value, __pAliqCofins.set, None, '\n            Valor da Alíquota da COFINS (%).\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}vPis uses Python identifier vPis
    __vPis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vPis'), 'vPis', '__httpwww_sped_fazenda_gov_brnfse_TCTribOutrosPisCofins_httpwww_sped_fazenda_gov_brnfsevPis', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1645, 6), )

    
    vPis = property(__vPis.value, __vPis.set, None, '\n            Valor monetário do PIS (R$).\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}vCofins uses Python identifier vCofins
    __vCofins = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vCofins'), 'vCofins', '__httpwww_sped_fazenda_gov_brnfse_TCTribOutrosPisCofins_httpwww_sped_fazenda_gov_brnfsevCofins', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1652, 6), )

    
    vCofins = property(__vCofins.value, __vCofins.set, None, '\n            Valor monetário do COFINS (R$).\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}tpRetPisCofins uses Python identifier tpRetPisCofins
    __tpRetPisCofins = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tpRetPisCofins'), 'tpRetPisCofins', '__httpwww_sped_fazenda_gov_brnfse_TCTribOutrosPisCofins_httpwww_sped_fazenda_gov_brnfsetpRetPisCofins', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1659, 6), )

    
    tpRetPisCofins = property(__tpRetPisCofins.value, __tpRetPisCofins.set, None, '\n            Tipo de retencao do Pis/Cofins:\n            1 - Retido;\n            2 - Não Retido;\n          ')

    _ElementMap.update({
        __CST.name() : __CST,
        __vBCPisCofins.name() : __vBCPisCofins,
        __pAliqPis.name() : __pAliqPis,
        __pAliqCofins.name() : __pAliqCofins,
        __vPis.name() : __vPis,
        __vCofins.name() : __vCofins,
        __tpRetPisCofins.name() : __tpRetPisCofins
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCTribOutrosPisCofins = TCTribOutrosPisCofins
Namespace.addCategoryObject('typeBinding', 'TCTribOutrosPisCofins', TCTribOutrosPisCofins)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCTribTotal with content type ELEMENT_ONLY
class TCTribTotal (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCTribTotal with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCTribTotal')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1671, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}vTotTrib uses Python identifier vTotTrib
    __vTotTrib = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vTotTrib'), 'vTotTrib', '__httpwww_sped_fazenda_gov_brnfse_TCTribTotal_httpwww_sped_fazenda_gov_brnfsevTotTrib', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1674, 8), )

    
    vTotTrib = property(__vTotTrib.value, __vTotTrib.set, None, '\n              Valor monetário total aproximado dos tributos, em conformidade com o artigo 1o da Lei no 12.741/2012\n            ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}pTotTrib uses Python identifier pTotTrib
    __pTotTrib = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'pTotTrib'), 'pTotTrib', '__httpwww_sped_fazenda_gov_brnfse_TCTribTotal_httpwww_sped_fazenda_gov_brnfsepTotTrib', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1681, 8), )

    
    pTotTrib = property(__pTotTrib.value, __pTotTrib.set, None, '\n              Valor percentual total aproximado dos tributos, em conformidade com o artigo 1o da Lei no 12.741/2012\n            ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}indTotTrib uses Python identifier indTotTrib
    __indTotTrib = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'indTotTrib'), 'indTotTrib', '__httpwww_sped_fazenda_gov_brnfse_TCTribTotal_httpwww_sped_fazenda_gov_brnfseindTotTrib', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1688, 8), )

    
    indTotTrib = property(__indTotTrib.value, __indTotTrib.set, None, '\n              Indicador de informação de valor total de tributos. Possui valor fixo igual a zero (indTotTrib=0).\n              Não informar nenhum valor estimado para os Tributos (Decreto 8.264/2014).\n              0 - Não;\n            ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}pTotTribSN uses Python identifier pTotTribSN
    __pTotTribSN = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'pTotTribSN'), 'pTotTribSN', '__httpwww_sped_fazenda_gov_brnfse_TCTribTotal_httpwww_sped_fazenda_gov_brnfsepTotTribSN', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1697, 8), )

    
    pTotTribSN = property(__pTotTribSN.value, __pTotTribSN.set, None, '\n              Valor percentual aproximado do total dos tributos da alíquota do Simples Nacional (%)\n            ')

    _ElementMap.update({
        __vTotTrib.name() : __vTotTrib,
        __pTotTrib.name() : __pTotTrib,
        __indTotTrib.name() : __indTotTrib,
        __pTotTribSN.name() : __pTotTribSN
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCTribTotal = TCTribTotal
Namespace.addCategoryObject('typeBinding', 'TCTribTotal', TCTribTotal)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCTribTotalMonet with content type ELEMENT_ONLY
class TCTribTotalMonet (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCTribTotalMonet with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCTribTotalMonet')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1708, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}vTotTribFed uses Python identifier vTotTribFed
    __vTotTribFed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vTotTribFed'), 'vTotTribFed', '__httpwww_sped_fazenda_gov_brnfse_TCTribTotalMonet_httpwww_sped_fazenda_gov_brnfsevTotTribFed', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1710, 6), )

    
    vTotTribFed = property(__vTotTribFed.value, __vTotTribFed.set, None, '\n            Valor monetário total aproximado dos tributos federais (R$).\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}vTotTribEst uses Python identifier vTotTribEst
    __vTotTribEst = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vTotTribEst'), 'vTotTribEst', '__httpwww_sped_fazenda_gov_brnfse_TCTribTotalMonet_httpwww_sped_fazenda_gov_brnfsevTotTribEst', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1717, 6), )

    
    vTotTribEst = property(__vTotTribEst.value, __vTotTribEst.set, None, '\n            Valor monetário total aproximado dos tributos estaduais (R$).\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}vTotTribMun uses Python identifier vTotTribMun
    __vTotTribMun = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'vTotTribMun'), 'vTotTribMun', '__httpwww_sped_fazenda_gov_brnfse_TCTribTotalMonet_httpwww_sped_fazenda_gov_brnfsevTotTribMun', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1724, 6), )

    
    vTotTribMun = property(__vTotTribMun.value, __vTotTribMun.set, None, '\n            Valor monetário total aproximado dos tributos municipais (R$).\n          ')

    _ElementMap.update({
        __vTotTribFed.name() : __vTotTribFed,
        __vTotTribEst.name() : __vTotTribEst,
        __vTotTribMun.name() : __vTotTribMun
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCTribTotalMonet = TCTribTotalMonet
Namespace.addCategoryObject('typeBinding', 'TCTribTotalMonet', TCTribTotalMonet)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCTribTotalPercent with content type ELEMENT_ONLY
class TCTribTotalPercent (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCTribTotalPercent with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCTribTotalPercent')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1734, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}pTotTribFed uses Python identifier pTotTribFed
    __pTotTribFed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'pTotTribFed'), 'pTotTribFed', '__httpwww_sped_fazenda_gov_brnfse_TCTribTotalPercent_httpwww_sped_fazenda_gov_brnfsepTotTribFed', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1736, 6), )

    
    pTotTribFed = property(__pTotTribFed.value, __pTotTribFed.set, None, '\n            Valor percentual total aproximado dos tributos federais (%).\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}pTotTribEst uses Python identifier pTotTribEst
    __pTotTribEst = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'pTotTribEst'), 'pTotTribEst', '__httpwww_sped_fazenda_gov_brnfse_TCTribTotalPercent_httpwww_sped_fazenda_gov_brnfsepTotTribEst', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1743, 6), )

    
    pTotTribEst = property(__pTotTribEst.value, __pTotTribEst.set, None, '\n            Valor percentual total aproximado dos tributos estaduais (%).\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}pTotTribMun uses Python identifier pTotTribMun
    __pTotTribMun = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'pTotTribMun'), 'pTotTribMun', '__httpwww_sped_fazenda_gov_brnfse_TCTribTotalPercent_httpwww_sped_fazenda_gov_brnfsepTotTribMun', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1750, 6), )

    
    pTotTribMun = property(__pTotTribMun.value, __pTotTribMun.set, None, '\n            Valor percentual total aproximado dos tributos municipais (%).\n          ')

    _ElementMap.update({
        __pTotTribFed.name() : __pTotTribFed,
        __pTotTribEst.name() : __pTotTribEst,
        __pTotTribMun.name() : __pTotTribMun
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCTribTotalPercent = TCTribTotalPercent
Namespace.addCategoryObject('typeBinding', 'TCTribTotalPercent', TCTribTotalPercent)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TE101101 with content type ELEMENT_ONLY
class TE101101 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TE101101 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TE101101')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 209, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}xDesc uses Python identifier xDesc
    __xDesc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xDesc'), 'xDesc', '__httpwww_sped_fazenda_gov_brnfse_TE101101_httpwww_sped_fazenda_gov_brnfsexDesc', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 211, 6), )

    
    xDesc = property(__xDesc.value, __xDesc.set, None, '\n            Descrição do Evento: Descrição do evento: "Cancelamento de NFS-e".\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}cMotivo uses Python identifier cMotivo
    __cMotivo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cMotivo'), 'cMotivo', '__httpwww_sped_fazenda_gov_brnfse_TE101101_httpwww_sped_fazenda_gov_brnfsecMotivo', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 224, 6), )

    
    cMotivo = property(__cMotivo.value, __cMotivo.set, None, 'Código de justificativa de cancelamento')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xMotivo uses Python identifier xMotivo
    __xMotivo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xMotivo'), 'xMotivo', '__httpwww_sped_fazenda_gov_brnfse_TE101101_httpwww_sped_fazenda_gov_brnfsexMotivo', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 229, 6), )

    
    xMotivo = property(__xMotivo.value, __xMotivo.set, None, 'Descrição para explicitar o motivo indicado neste evento')

    _ElementMap.update({
        __xDesc.name() : __xDesc,
        __cMotivo.name() : __cMotivo,
        __xMotivo.name() : __xMotivo
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TE101101 = TE101101
Namespace.addCategoryObject('typeBinding', 'TE101101', TE101101)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TE105102 with content type ELEMENT_ONLY
class TE105102 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TE105102 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TE105102')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 238, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}xDesc uses Python identifier xDesc
    __xDesc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xDesc'), 'xDesc', '__httpwww_sped_fazenda_gov_brnfse_TE105102_httpwww_sped_fazenda_gov_brnfsexDesc', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 240, 6), )

    
    xDesc = property(__xDesc.value, __xDesc.set, None, '\n            Descrição do Evento: Descrição do evento: "Cancelamento de NFS-e por Substituição".\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}cMotivo uses Python identifier cMotivo
    __cMotivo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cMotivo'), 'cMotivo', '__httpwww_sped_fazenda_gov_brnfse_TE105102_httpwww_sped_fazenda_gov_brnfsecMotivo', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 253, 6), )

    
    cMotivo = property(__cMotivo.value, __cMotivo.set, None, 'Código de justificativa de cancelamento substituição')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xMotivo uses Python identifier xMotivo
    __xMotivo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xMotivo'), 'xMotivo', '__httpwww_sped_fazenda_gov_brnfse_TE105102_httpwww_sped_fazenda_gov_brnfsexMotivo', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 258, 6), )

    
    xMotivo = property(__xMotivo.value, __xMotivo.set, None, 'Descrição para explicitar o motivo indicado neste evento')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}chSubstituta uses Python identifier chSubstituta
    __chSubstituta = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'chSubstituta'), 'chSubstituta', '__httpwww_sped_fazenda_gov_brnfse_TE105102_httpwww_sped_fazenda_gov_brnfsechSubstituta', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 263, 6), )

    
    chSubstituta = property(__chSubstituta.value, __chSubstituta.set, None, 'Chave de Acesso da NFS-e substituta.')

    _ElementMap.update({
        __xDesc.name() : __xDesc,
        __cMotivo.name() : __cMotivo,
        __xMotivo.name() : __xMotivo,
        __chSubstituta.name() : __chSubstituta
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TE105102 = TE105102
Namespace.addCategoryObject('typeBinding', 'TE105102', TE105102)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TE101103 with content type ELEMENT_ONLY
class TE101103 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TE101103 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TE101103')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 272, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}xDesc uses Python identifier xDesc
    __xDesc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xDesc'), 'xDesc', '__httpwww_sped_fazenda_gov_brnfse_TE101103_httpwww_sped_fazenda_gov_brnfsexDesc', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 274, 6), )

    
    xDesc = property(__xDesc.value, __xDesc.set, None, '\n            Descrição do evento: "Solicitação de Análise Fiscal para Cancelamento de NFS-e"\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}cMotivo uses Python identifier cMotivo
    __cMotivo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cMotivo'), 'cMotivo', '__httpwww_sped_fazenda_gov_brnfse_TE101103_httpwww_sped_fazenda_gov_brnfsecMotivo', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 287, 6), )

    
    cMotivo = property(__cMotivo.value, __cMotivo.set, None, 'Código do motivo da solicitação de análise fiscal para cancelamento de NFS-e:')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xMotivo uses Python identifier xMotivo
    __xMotivo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xMotivo'), 'xMotivo', '__httpwww_sped_fazenda_gov_brnfse_TE101103_httpwww_sped_fazenda_gov_brnfsexMotivo', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 292, 6), )

    
    xMotivo = property(__xMotivo.value, __xMotivo.set, None, 'Descrição para explicitar o motivo indicado neste evento')

    _ElementMap.update({
        __xDesc.name() : __xDesc,
        __cMotivo.name() : __cMotivo,
        __xMotivo.name() : __xMotivo
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TE101103 = TE101103
Namespace.addCategoryObject('typeBinding', 'TE101103', TE101103)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TE105104 with content type ELEMENT_ONLY
class TE105104 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TE105104 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TE105104')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 301, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}xDesc uses Python identifier xDesc
    __xDesc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xDesc'), 'xDesc', '__httpwww_sped_fazenda_gov_brnfse_TE105104_httpwww_sped_fazenda_gov_brnfsexDesc', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 303, 6), )

    
    xDesc = property(__xDesc.value, __xDesc.set, None, '\n            Descrição do evento: "Cancelamento de NFS-e Deferido por Análise Fiscal"\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}CPFAgTrib uses Python identifier CPFAgTrib
    __CPFAgTrib = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CPFAgTrib'), 'CPFAgTrib', '__httpwww_sped_fazenda_gov_brnfse_TE105104_httpwww_sped_fazenda_gov_brnfseCPFAgTrib', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 316, 6), )

    
    CPFAgTrib = property(__CPFAgTrib.value, __CPFAgTrib.set, None, '\n            CPF do agente da administração tributária municipal que efetuou o deferimento da  solicitação de análise fiscal para cancelamento de NFS-e.\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}nProcAdm uses Python identifier nProcAdm
    __nProcAdm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nProcAdm'), 'nProcAdm', '__httpwww_sped_fazenda_gov_brnfse_TE105104_httpwww_sped_fazenda_gov_brnfsenProcAdm', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 323, 6), )

    
    nProcAdm = property(__nProcAdm.value, __nProcAdm.set, None, '\n            Número do processo administrativo municipal vinculado à solicitação de análise fiscal para cancelamento de NFS-e.\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}cMotivo uses Python identifier cMotivo
    __cMotivo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cMotivo'), 'cMotivo', '__httpwww_sped_fazenda_gov_brnfse_TE105104_httpwww_sped_fazenda_gov_brnfsecMotivo', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 330, 6), )

    
    cMotivo = property(__cMotivo.value, __cMotivo.set, None, '\n            Resposta da solicitação de análise fiscal para cancelamento de NFS-e:\n            1 - Cancelamento de NFS-e Deferido.\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xMotivo uses Python identifier xMotivo
    __xMotivo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xMotivo'), 'xMotivo', '__httpwww_sped_fazenda_gov_brnfse_TE105104_httpwww_sped_fazenda_gov_brnfsexMotivo', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 338, 6), )

    
    xMotivo = property(__xMotivo.value, __xMotivo.set, None, '\n            Descrição para explicitar o motivo indicado neste evento\n          ')

    _ElementMap.update({
        __xDesc.name() : __xDesc,
        __CPFAgTrib.name() : __CPFAgTrib,
        __nProcAdm.name() : __nProcAdm,
        __cMotivo.name() : __cMotivo,
        __xMotivo.name() : __xMotivo
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TE105104 = TE105104
Namespace.addCategoryObject('typeBinding', 'TE105104', TE105104)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TE105105 with content type ELEMENT_ONLY
class TE105105 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TE105105 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TE105105')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 349, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}xDesc uses Python identifier xDesc
    __xDesc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xDesc'), 'xDesc', '__httpwww_sped_fazenda_gov_brnfse_TE105105_httpwww_sped_fazenda_gov_brnfsexDesc', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 351, 6), )

    
    xDesc = property(__xDesc.value, __xDesc.set, None, '\n            Descrição do evento: "Cancelamento de NFS-e Indeferido por Análise Fiscal".\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}CPFAgTrib uses Python identifier CPFAgTrib
    __CPFAgTrib = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CPFAgTrib'), 'CPFAgTrib', '__httpwww_sped_fazenda_gov_brnfse_TE105105_httpwww_sped_fazenda_gov_brnfseCPFAgTrib', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 364, 6), )

    
    CPFAgTrib = property(__CPFAgTrib.value, __CPFAgTrib.set, None, '\n            CPF do agente da administração tributária municipal que efetuou o indeferimento da solicitação de análise fiscal para cancelamento de NFS-e.\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}nProcAdm uses Python identifier nProcAdm
    __nProcAdm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nProcAdm'), 'nProcAdm', '__httpwww_sped_fazenda_gov_brnfse_TE105105_httpwww_sped_fazenda_gov_brnfsenProcAdm', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 371, 6), )

    
    nProcAdm = property(__nProcAdm.value, __nProcAdm.set, None, '\n            Número do processo administrativo municipal vinculado à solicitação de análise fiscal para cancelamento de NFS-e.\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}cMotivo uses Python identifier cMotivo
    __cMotivo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cMotivo'), 'cMotivo', '__httpwww_sped_fazenda_gov_brnfse_TE105105_httpwww_sped_fazenda_gov_brnfsecMotivo', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 378, 6), )

    
    cMotivo = property(__cMotivo.value, __cMotivo.set, None, '\n            Resposta da solicitação de análise fiscal para cancelamento de NFS-e:\n            1 - Cancelamento de NFS-e Indeferido;\n            2 - Cancelamento de NFS-e Indeferido Sem Análise de Mérito.\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xMotivo uses Python identifier xMotivo
    __xMotivo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xMotivo'), 'xMotivo', '__httpwww_sped_fazenda_gov_brnfse_TE105105_httpwww_sped_fazenda_gov_brnfsexMotivo', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 387, 6), )

    
    xMotivo = property(__xMotivo.value, __xMotivo.set, None, 'Descrição para explicitar o motivo indicado neste evento')

    _ElementMap.update({
        __xDesc.name() : __xDesc,
        __CPFAgTrib.name() : __CPFAgTrib,
        __nProcAdm.name() : __nProcAdm,
        __cMotivo.name() : __cMotivo,
        __xMotivo.name() : __xMotivo
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TE105105 = TE105105
Namespace.addCategoryObject('typeBinding', 'TE105105', TE105105)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TE202201 with content type ELEMENT_ONLY
class TE202201 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TE202201 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TE202201')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 396, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}xDesc uses Python identifier xDesc
    __xDesc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xDesc'), 'xDesc', '__httpwww_sped_fazenda_gov_brnfse_TE202201_httpwww_sped_fazenda_gov_brnfsexDesc', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 398, 6), )

    
    xDesc = property(__xDesc.value, __xDesc.set, None, '\n            Descrição do evento: "Confirmação do Prestador".\n          ')

    _ElementMap.update({
        __xDesc.name() : __xDesc
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TE202201 = TE202201
Namespace.addCategoryObject('typeBinding', 'TE202201', TE202201)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TE203202 with content type ELEMENT_ONLY
class TE203202 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TE203202 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TE203202')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 415, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}xDesc uses Python identifier xDesc
    __xDesc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xDesc'), 'xDesc', '__httpwww_sped_fazenda_gov_brnfse_TE203202_httpwww_sped_fazenda_gov_brnfsexDesc', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 417, 6), )

    
    xDesc = property(__xDesc.value, __xDesc.set, None, '\n            Descrição do evento: "Confirmação do Tomador".\n          ')

    _ElementMap.update({
        __xDesc.name() : __xDesc
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TE203202 = TE203202
Namespace.addCategoryObject('typeBinding', 'TE203202', TE203202)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TE204203 with content type ELEMENT_ONLY
class TE204203 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TE204203 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TE204203')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 434, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}xDesc uses Python identifier xDesc
    __xDesc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xDesc'), 'xDesc', '__httpwww_sped_fazenda_gov_brnfse_TE204203_httpwww_sped_fazenda_gov_brnfsexDesc', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 436, 6), )

    
    xDesc = property(__xDesc.value, __xDesc.set, None, '\n            Descrição do evento: "Confirmação do Intermediário".\n          ')

    _ElementMap.update({
        __xDesc.name() : __xDesc
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TE204203 = TE204203
Namespace.addCategoryObject('typeBinding', 'TE204203', TE204203)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TE205204 with content type ELEMENT_ONLY
class TE205204 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TE205204 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TE205204')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 453, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}xDesc uses Python identifier xDesc
    __xDesc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xDesc'), 'xDesc', '__httpwww_sped_fazenda_gov_brnfse_TE205204_httpwww_sped_fazenda_gov_brnfsexDesc', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 455, 6), )

    
    xDesc = property(__xDesc.value, __xDesc.set, None, '\n            Descrição do evento: "Confirmação Tácita".\n          ')

    _ElementMap.update({
        __xDesc.name() : __xDesc
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TE205204 = TE205204
Namespace.addCategoryObject('typeBinding', 'TE205204', TE205204)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TE202205 with content type ELEMENT_ONLY
class TE202205 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TE202205 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TE202205')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 472, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}xDesc uses Python identifier xDesc
    __xDesc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xDesc'), 'xDesc', '__httpwww_sped_fazenda_gov_brnfse_TE202205_httpwww_sped_fazenda_gov_brnfsexDesc', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 474, 6), )

    
    xDesc = property(__xDesc.value, __xDesc.set, None, '\n            Descrição do evento: "Rejeição do Prestador".\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}infRej uses Python identifier infRej
    __infRej = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'infRej'), 'infRej', '__httpwww_sped_fazenda_gov_brnfse_TE202205_httpwww_sped_fazenda_gov_brnfseinfRej', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 487, 6), )

    
    infRej = property(__infRej.value, __infRej.set, None, '\n          ')

    _ElementMap.update({
        __xDesc.name() : __xDesc,
        __infRej.name() : __infRej
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TE202205 = TE202205
Namespace.addCategoryObject('typeBinding', 'TE202205', TE202205)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TE203206 with content type ELEMENT_ONLY
class TE203206 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TE203206 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TE203206')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 497, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}xDesc uses Python identifier xDesc
    __xDesc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xDesc'), 'xDesc', '__httpwww_sped_fazenda_gov_brnfse_TE203206_httpwww_sped_fazenda_gov_brnfsexDesc', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 499, 6), )

    
    xDesc = property(__xDesc.value, __xDesc.set, None, '\n            Descrição do evento: "Rejeição do Tomador".\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}infRej uses Python identifier infRej
    __infRej = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'infRej'), 'infRej', '__httpwww_sped_fazenda_gov_brnfse_TE203206_httpwww_sped_fazenda_gov_brnfseinfRej', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 512, 6), )

    
    infRej = property(__infRej.value, __infRej.set, None, '\n          ')

    _ElementMap.update({
        __xDesc.name() : __xDesc,
        __infRej.name() : __infRej
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TE203206 = TE203206
Namespace.addCategoryObject('typeBinding', 'TE203206', TE203206)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TE204207 with content type ELEMENT_ONLY
class TE204207 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TE204207 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TE204207')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 522, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}xDesc uses Python identifier xDesc
    __xDesc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xDesc'), 'xDesc', '__httpwww_sped_fazenda_gov_brnfse_TE204207_httpwww_sped_fazenda_gov_brnfsexDesc', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 524, 6), )

    
    xDesc = property(__xDesc.value, __xDesc.set, None, '\n            Descrição do evento: "Rejeição do Intermediário".\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}infRej uses Python identifier infRej
    __infRej = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'infRej'), 'infRej', '__httpwww_sped_fazenda_gov_brnfse_TE204207_httpwww_sped_fazenda_gov_brnfseinfRej', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 537, 6), )

    
    infRej = property(__infRej.value, __infRej.set, None, '\n          ')

    _ElementMap.update({
        __xDesc.name() : __xDesc,
        __infRej.name() : __infRej
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TE204207 = TE204207
Namespace.addCategoryObject('typeBinding', 'TE204207', TE204207)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TE205208 with content type ELEMENT_ONLY
class TE205208 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TE205208 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TE205208')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 547, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}xDesc uses Python identifier xDesc
    __xDesc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xDesc'), 'xDesc', '__httpwww_sped_fazenda_gov_brnfse_TE205208_httpwww_sped_fazenda_gov_brnfsexDesc', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 549, 6), )

    
    xDesc = property(__xDesc.value, __xDesc.set, None, '\n            Descrição do evento: "Anulação da Rejeição".\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}infAnRej uses Python identifier infAnRej
    __infAnRej = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'infAnRej'), 'infAnRej', '__httpwww_sped_fazenda_gov_brnfse_TE205208_httpwww_sped_fazenda_gov_brnfseinfAnRej', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 562, 6), )

    
    infAnRej = property(__infAnRej.value, __infAnRej.set, None, '\n          ')

    _ElementMap.update({
        __xDesc.name() : __xDesc,
        __infAnRej.name() : __infAnRej
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TE205208 = TE205208
Namespace.addCategoryObject('typeBinding', 'TE205208', TE205208)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TE305101 with content type ELEMENT_ONLY
class TE305101 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TE305101 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TE305101')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 572, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}xDesc uses Python identifier xDesc
    __xDesc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xDesc'), 'xDesc', '__httpwww_sped_fazenda_gov_brnfse_TE305101_httpwww_sped_fazenda_gov_brnfsexDesc', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 574, 6), )

    
    xDesc = property(__xDesc.value, __xDesc.set, None, '\n            Descrição do evento: "Cancelamento de NFS-e por Ofício".\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}CPFAgTrib uses Python identifier CPFAgTrib
    __CPFAgTrib = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CPFAgTrib'), 'CPFAgTrib', '__httpwww_sped_fazenda_gov_brnfse_TE305101_httpwww_sped_fazenda_gov_brnfseCPFAgTrib', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 587, 6), )

    
    CPFAgTrib = property(__CPFAgTrib.value, __CPFAgTrib.set, None, '\n            CPF do agente da administração tributária municipal que efetuou o cancelamento por ofício de NFS-e.\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}nProcAdm uses Python identifier nProcAdm
    __nProcAdm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nProcAdm'), 'nProcAdm', '__httpwww_sped_fazenda_gov_brnfse_TE305101_httpwww_sped_fazenda_gov_brnfsenProcAdm', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 594, 6), )

    
    nProcAdm = property(__nProcAdm.value, __nProcAdm.set, None, '\n            Número do processo administrativo municipal vinculado ao cancelamento de NFS-e por ofício.\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xProcAdm uses Python identifier xProcAdm
    __xProcAdm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xProcAdm'), 'xProcAdm', '__httpwww_sped_fazenda_gov_brnfse_TE305101_httpwww_sped_fazenda_gov_brnfsexProcAdm', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 601, 6), )

    
    xProcAdm = property(__xProcAdm.value, __xProcAdm.set, None, '\n            Descrição para explicitar o motivo indicado neste evento.\n          ')

    _ElementMap.update({
        __xDesc.name() : __xDesc,
        __CPFAgTrib.name() : __CPFAgTrib,
        __nProcAdm.name() : __nProcAdm,
        __xProcAdm.name() : __xProcAdm
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TE305101 = TE305101
Namespace.addCategoryObject('typeBinding', 'TE305101', TE305101)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TE305102 with content type ELEMENT_ONLY
class TE305102 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TE305102 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TE305102')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 612, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}xDesc uses Python identifier xDesc
    __xDesc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xDesc'), 'xDesc', '__httpwww_sped_fazenda_gov_brnfse_TE305102_httpwww_sped_fazenda_gov_brnfsexDesc', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 614, 6), )

    
    xDesc = property(__xDesc.value, __xDesc.set, None, '\n            Descrição do evento: "Bloqueio de NFS-e por Ofício".\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}CPFAgTrib uses Python identifier CPFAgTrib
    __CPFAgTrib = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CPFAgTrib'), 'CPFAgTrib', '__httpwww_sped_fazenda_gov_brnfse_TE305102_httpwww_sped_fazenda_gov_brnfseCPFAgTrib', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 627, 6), )

    
    CPFAgTrib = property(__CPFAgTrib.value, __CPFAgTrib.set, None, '\n            CPF do agente da administração tributária municipal que efetuou o cancelamento por ofício de NFS-e.\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xMotivo uses Python identifier xMotivo
    __xMotivo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xMotivo'), 'xMotivo', '__httpwww_sped_fazenda_gov_brnfse_TE305102_httpwww_sped_fazenda_gov_brnfsexMotivo', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 634, 6), )

    
    xMotivo = property(__xMotivo.value, __xMotivo.set, None, 'Descrição para explicitar o motivo indicado neste evento')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}codEvento uses Python identifier codEvento
    __codEvento = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'codEvento'), 'codEvento', '__httpwww_sped_fazenda_gov_brnfse_TE305102_httpwww_sped_fazenda_gov_brnfsecodEvento', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 639, 6), )

    
    codEvento = property(__codEvento.value, __codEvento.set, None, 'Descrição para explicitar o motivo indicado neste evento')

    _ElementMap.update({
        __xDesc.name() : __xDesc,
        __CPFAgTrib.name() : __CPFAgTrib,
        __xMotivo.name() : __xMotivo,
        __codEvento.name() : __codEvento
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TE305102 = TE305102
Namespace.addCategoryObject('typeBinding', 'TE305102', TE305102)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TE305103 with content type ELEMENT_ONLY
class TE305103 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TE305103 with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TE305103')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 648, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}xDesc uses Python identifier xDesc
    __xDesc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xDesc'), 'xDesc', '__httpwww_sped_fazenda_gov_brnfse_TE305103_httpwww_sped_fazenda_gov_brnfsexDesc', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 650, 6), )

    
    xDesc = property(__xDesc.value, __xDesc.set, None, '\n            Descrição do evento: "Desbloqueio de NFS-e por Ofício".\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}CPFAgTrib uses Python identifier CPFAgTrib
    __CPFAgTrib = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CPFAgTrib'), 'CPFAgTrib', '__httpwww_sped_fazenda_gov_brnfse_TE305103_httpwww_sped_fazenda_gov_brnfseCPFAgTrib', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 663, 6), )

    
    CPFAgTrib = property(__CPFAgTrib.value, __CPFAgTrib.set, None, '\n            CPF do agente da administração tributária municipal que efetuou o cancelamento por ofício de NFS-e.\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}idBloqOfic uses Python identifier idBloqOfic
    __idBloqOfic = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'idBloqOfic'), 'idBloqOfic', '__httpwww_sped_fazenda_gov_brnfse_TE305103_httpwww_sped_fazenda_gov_brnfseidBloqOfic', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 670, 6), )

    
    idBloqOfic = property(__idBloqOfic.value, __idBloqOfic.set, None, '\n            Referência ao Id da "Manifestação de rejeição da NFS-e" que originou o presente evento de anulação.\n          ')

    _ElementMap.update({
        __xDesc.name() : __xDesc,
        __CPFAgTrib.name() : __CPFAgTrib,
        __idBloqOfic.name() : __idBloqOfic
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TE305103 = TE305103
Namespace.addCategoryObject('typeBinding', 'TE305103', TE305103)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCListaEventos with content type ELEMENT_ONLY
class TCListaEventos (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCListaEventos with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCListaEventos')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 681, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}codEvento uses Python identifier codEvento
    __codEvento = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'codEvento'), 'codEvento', '__httpwww_sped_fazenda_gov_brnfse_TCListaEventos_httpwww_sped_fazenda_gov_brnfsecodEvento', True, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 683, 6), )

    
    codEvento = property(__codEvento.value, __codEvento.set, None, '\n            Grupo de informações de documento utilizado para Dedução/Redução do valor do serviço\n          ')

    _ElementMap.update({
        __codEvento.name() : __codEvento
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCListaEventos = TCListaEventos
Namespace.addCategoryObject('typeBinding', 'TCListaEventos', TCListaEventos)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCInfoEventoRejeicao with content type ELEMENT_ONLY
class TCInfoEventoRejeicao (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCInfoEventoRejeicao with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCInfoEventoRejeicao')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 694, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}cMotivo uses Python identifier cMotivo
    __cMotivo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cMotivo'), 'cMotivo', '__httpwww_sped_fazenda_gov_brnfse_TCInfoEventoRejeicao_httpwww_sped_fazenda_gov_brnfsecMotivo', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 696, 6), )

    
    cMotivo = property(__cMotivo.value, __cMotivo.set, None, '\n            Motivo da Rejeição da NFS-e:\n\n            1 - NFS-e em duplicidade;\n            2 - NFS-e já emitida pelo tomador;\n            3 - Não ocorrência do fato gerador;\n            4 - Erro quanto a responsabilidade tributária;\n            5 - Erro quanto ao valor do serviço, valor das deduções ou serviço prestado ou data do fato gerador;\n            9 - Outros;\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xMotivo uses Python identifier xMotivo
    __xMotivo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xMotivo'), 'xMotivo', '__httpwww_sped_fazenda_gov_brnfse_TCInfoEventoRejeicao_httpwww_sped_fazenda_gov_brnfsexMotivo', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 710, 6), )

    
    xMotivo = property(__xMotivo.value, __xMotivo.set, None, 'Descrição para explicitar o motivo indicado neste evento')

    _ElementMap.update({
        __cMotivo.name() : __cMotivo,
        __xMotivo.name() : __xMotivo
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCInfoEventoRejeicao = TCInfoEventoRejeicao
Namespace.addCategoryObject('typeBinding', 'TCInfoEventoRejeicao', TCInfoEventoRejeicao)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCInfoEventoAnulacaoRejeicao with content type ELEMENT_ONLY
class TCInfoEventoAnulacaoRejeicao (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCInfoEventoAnulacaoRejeicao with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCInfoEventoAnulacaoRejeicao')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 719, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}CPFAgTrib uses Python identifier CPFAgTrib
    __CPFAgTrib = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CPFAgTrib'), 'CPFAgTrib', '__httpwww_sped_fazenda_gov_brnfse_TCInfoEventoAnulacaoRejeicao_httpwww_sped_fazenda_gov_brnfseCPFAgTrib', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 721, 6), )

    
    CPFAgTrib = property(__CPFAgTrib.value, __CPFAgTrib.set, None, '\n            CPF do agente da administração tributária municipal que efetuou o anulação da manifestação de rejeição da NFS-e.\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}idEvManifRej uses Python identifier idEvManifRej
    __idEvManifRej = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'idEvManifRej'), 'idEvManifRej', '__httpwww_sped_fazenda_gov_brnfse_TCInfoEventoAnulacaoRejeicao_httpwww_sped_fazenda_gov_brnfseidEvManifRej', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 728, 6), )

    
    idEvManifRej = property(__idEvManifRej.value, __idEvManifRej.set, None, '\n            Referência ao Id da "Manifestação de rejeição da NFS-e" que originou o presente evento de anulação.\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xMotivo uses Python identifier xMotivo
    __xMotivo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xMotivo'), 'xMotivo', '__httpwww_sped_fazenda_gov_brnfse_TCInfoEventoAnulacaoRejeicao_httpwww_sped_fazenda_gov_brnfsexMotivo', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 735, 6), )

    
    xMotivo = property(__xMotivo.value, __xMotivo.set, None, 'Descrição para explicitar o motivo da anluação')

    _ElementMap.update({
        __CPFAgTrib.name() : __CPFAgTrib,
        __idEvManifRej.name() : __idEvManifRej,
        __xMotivo.name() : __xMotivo
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TCInfoEventoAnulacaoRejeicao = TCInfoEventoAnulacaoRejeicao
Namespace.addCategoryObject('typeBinding', 'TCInfoEventoAnulacaoRejeicao', TCInfoEventoAnulacaoRejeicao)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCNFSe with content type ELEMENT_ONLY
class TCNFSe (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCNFSe with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCNFSe')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 6, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}infNFSe uses Python identifier infNFSe
    __infNFSe = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'infNFSe'), 'infNFSe', '__httpwww_sped_fazenda_gov_brnfse_TCNFSe_httpwww_sped_fazenda_gov_brnfseinfNFSe', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 8, 6), )

    
    infNFSe = property(__infNFSe.value, __infNFSe.set, None, None)

    
    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature'), 'Signature', '__httpwww_sped_fazenda_gov_brnfse_TCNFSe_httpwww_w3_org200009xmldsigSignature', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/xmldsig-core-schema.xsd', 43, 0), )

    
    Signature = property(__Signature.value, __Signature.set, None, None)

    
    # Attribute versao uses Python identifier versao
    __versao = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'versao'), 'versao', '__httpwww_sped_fazenda_gov_brnfse_TCNFSe_versao', _module_typeBindings.TVerNFSe, required=True)
    __versao._DeclarationLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 11, 4)
    __versao._UseLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 11, 4)
    
    versao = property(__versao.value, __versao.set, None, None)

    _ElementMap.update({
        __infNFSe.name() : __infNFSe,
        __Signature.name() : __Signature
    })
    _AttributeMap.update({
        __versao.name() : __versao
    })
_module_typeBindings.TCNFSe = TCNFSe
Namespace.addCategoryObject('typeBinding', 'TCNFSe', TCNFSe)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCInfNFSe with content type ELEMENT_ONLY
class TCInfNFSe (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCInfNFSe with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCInfNFSe')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 14, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}xLocEmi uses Python identifier xLocEmi
    __xLocEmi = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xLocEmi'), 'xLocEmi', '__httpwww_sped_fazenda_gov_brnfse_TCInfNFSe_httpwww_sped_fazenda_gov_brnfsexLocEmi', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 16, 6), )

    
    xLocEmi = property(__xLocEmi.value, __xLocEmi.set, None, 'Descrição do código do IBGE do município emissor da NFS-e.\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xLocPrestacao uses Python identifier xLocPrestacao
    __xLocPrestacao = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xLocPrestacao'), 'xLocPrestacao', '__httpwww_sped_fazenda_gov_brnfse_TCInfNFSe_httpwww_sped_fazenda_gov_brnfsexLocPrestacao', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 22, 6), )

    
    xLocPrestacao = property(__xLocPrestacao.value, __xLocPrestacao.set, None, 'Descrição do local da prestação do serviço.\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}nNFSe uses Python identifier nNFSe
    __nNFSe = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nNFSe'), 'nNFSe', '__httpwww_sped_fazenda_gov_brnfse_TCInfNFSe_httpwww_sped_fazenda_gov_brnfsenNFSe', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 28, 6), )

    
    nNFSe = property(__nNFSe.value, __nNFSe.set, None, 'Número sequencial por tipo de emitente da NFS-e.\n            A Sefin Nacional NFS-e irá gerar o número da NFS-e de forma sequencial por emitente. Por se tratar de um ambiente altamente transacional, a Sefin Nacional NFS-e não irá reutilizar números inutilizados durante a geração da NFS-e.\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}cLocIncid uses Python identifier cLocIncid
    __cLocIncid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cLocIncid'), 'cLocIncid', '__httpwww_sped_fazenda_gov_brnfse_TCInfNFSe_httpwww_sped_fazenda_gov_brnfsecLocIncid', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 35, 6), )

    
    cLocIncid = property(__cLocIncid.value, __cLocIncid.set, None, '\n            O código de município utilizado pelo Sistema Nacional NFS-e é o código definido para cada município pertencente ao ""Anexo V – Tabela de Código de Municípios do IBGE"", que consta ao final do Manual de Orientação ao Contribuinte do ISSQN para a Sefin Nacional NFS-e.\n            O município de incidência do ISSQN é determinado automaticamente pelo sistema, conforme regras do aspecto espacial da lei complementar federal (LC 116/03) que são válidas para todos  os municípios.\n            http://www.planalto.gov.br/ccivil_03/Leis/LCP/Lcp116.htm\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xLocIncid uses Python identifier xLocIncid
    __xLocIncid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xLocIncid'), 'xLocIncid', '__httpwww_sped_fazenda_gov_brnfse_TCInfNFSe_httpwww_sped_fazenda_gov_brnfsexLocIncid', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 44, 6), )

    
    xLocIncid = property(__xLocIncid.value, __xLocIncid.set, None, '\n            A descrição do código de município utilizado pelo Sistema Nacional NFS-e é o nome de cada município pertencente ao "Anexo V – Tabela de Código de Municípios do IBGE", que consta ao final do Manual de Orientação ao Contribuinte do ISSQN para a Sefin Nacional NFS-e.\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xTribNac uses Python identifier xTribNac
    __xTribNac = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xTribNac'), 'xTribNac', '__httpwww_sped_fazenda_gov_brnfse_TCInfNFSe_httpwww_sped_fazenda_gov_brnfsexTribNac', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 51, 6), )

    
    xTribNac = property(__xTribNac.value, __xTribNac.set, None, '\n            Descrição do código de tributação nacional do ISSQN.\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xTribMun uses Python identifier xTribMun
    __xTribMun = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xTribMun'), 'xTribMun', '__httpwww_sped_fazenda_gov_brnfse_TCInfNFSe_httpwww_sped_fazenda_gov_brnfsexTribMun', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 58, 6), )

    
    xTribMun = property(__xTribMun.value, __xTribMun.set, None, '\n            Descrição do código de tributação municipal do ISSQN.\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}xNBS uses Python identifier xNBS
    __xNBS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xNBS'), 'xNBS', '__httpwww_sped_fazenda_gov_brnfse_TCInfNFSe_httpwww_sped_fazenda_gov_brnfsexNBS', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 65, 6), )

    
    xNBS = property(__xNBS.value, __xNBS.set, None, '\n            Descrição do código da NBS.\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}verAplic uses Python identifier verAplic
    __verAplic = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'verAplic'), 'verAplic', '__httpwww_sped_fazenda_gov_brnfse_TCInfNFSe_httpwww_sped_fazenda_gov_brnfseverAplic', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 72, 6), )

    
    verAplic = property(__verAplic.value, __verAplic.set, None, 'Versão do aplicativo que gerou a NFS-e')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}ambGer uses Python identifier ambGer
    __ambGer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ambGer'), 'ambGer', '__httpwww_sped_fazenda_gov_brnfse_TCInfNFSe_httpwww_sped_fazenda_gov_brnfseambGer', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 77, 6), )

    
    ambGer = property(__ambGer.value, __ambGer.set, None, 'Ambiente gerador da NFS-e')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}tpEmis uses Python identifier tpEmis
    __tpEmis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tpEmis'), 'tpEmis', '__httpwww_sped_fazenda_gov_brnfse_TCInfNFSe_httpwww_sped_fazenda_gov_brnfsetpEmis', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 82, 6), )

    
    tpEmis = property(__tpEmis.value, __tpEmis.set, None, '\n            Processo de Emissão da DPS:\n            1 - Emissão com aplicativo do contribuinte (via Web Service);\n            2 - Emissão com aplicativo disponibilizado pelo fisco (Web);\n            3 - Emissão com aplicativo disponibilizado pelo fisco (App);\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}procEmi uses Python identifier procEmi
    __procEmi = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'procEmi'), 'procEmi', '__httpwww_sped_fazenda_gov_brnfse_TCInfNFSe_httpwww_sped_fazenda_gov_brnfseprocEmi', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 92, 6), )

    
    procEmi = property(__procEmi.value, __procEmi.set, None, '\n            Processo de Emissão da DPS:\n            1 - Emissão com aplicativo do contribuinte (via Web Service);\n            2 - Emissão com aplicativo disponibilizado pelo fisco (Web);\n            3 - Emissão com aplicativo disponibilizado pelo fisco (App);\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}cStat uses Python identifier cStat
    __cStat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cStat'), 'cStat', '__httpwww_sped_fazenda_gov_brnfse_TCInfNFSe_httpwww_sped_fazenda_gov_brnfsecStat', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 102, 6), )

    
    cStat = property(__cStat.value, __cStat.set, None, 'Código do Status da mensagem')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}dhProc uses Python identifier dhProc
    __dhProc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dhProc'), 'dhProc', '__httpwww_sped_fazenda_gov_brnfse_TCInfNFSe_httpwww_sped_fazenda_gov_brnfsedhProc', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 107, 6), )

    
    dhProc = property(__dhProc.value, __dhProc.set, None, '\n            Data/Hora da validação da DPS e geração da NFS-e. Data e hora no formato UTC (Universal Coordinated Time):AAAA-MM-DDThh:mm:ssTZD\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}nDFSe uses Python identifier nDFSe
    __nDFSe = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nDFSe'), 'nDFSe', '__httpwww_sped_fazenda_gov_brnfse_TCInfNFSe_httpwww_sped_fazenda_gov_brnfsenDFSe', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 114, 6), )

    
    nDFSe = property(__nDFSe.value, __nDFSe.set, None, '\n            Número sequencial do documento gerado por ambiente gerador de DFSe do múnicípio.\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}emit uses Python identifier emit
    __emit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'emit'), 'emit', '__httpwww_sped_fazenda_gov_brnfse_TCInfNFSe_httpwww_sped_fazenda_gov_brnfseemit', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 121, 6), )

    
    emit = property(__emit.value, __emit.set, None, '\n            Grupo de informações da DPS relativas ao emitente da NFS-e\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}valores uses Python identifier valores
    __valores = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'valores'), 'valores', '__httpwww_sped_fazenda_gov_brnfse_TCInfNFSe_httpwww_sped_fazenda_gov_brnfsevalores', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 128, 6), )

    
    valores = property(__valores.value, __valores.set, None, 'Grupo de valores referentes ao Serviço Prestado')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}DPS uses Python identifier DPS
    __DPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DPS'), 'DPS', '__httpwww_sped_fazenda_gov_brnfse_TCInfNFSe_httpwww_sped_fazenda_gov_brnfseDPS', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 133, 6), )

    
    DPS = property(__DPS.value, __DPS.set, None, '\n            Grupo de informações da DPS relativas ao serviço prestado\n          ')

    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httpwww_sped_fazenda_gov_brnfse_TCInfNFSe_Id', _module_typeBindings.TSIdNFSe, required=True)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 141, 4)
    __Id._UseLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 141, 4)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __xLocEmi.name() : __xLocEmi,
        __xLocPrestacao.name() : __xLocPrestacao,
        __nNFSe.name() : __nNFSe,
        __cLocIncid.name() : __cLocIncid,
        __xLocIncid.name() : __xLocIncid,
        __xTribNac.name() : __xTribNac,
        __xTribMun.name() : __xTribMun,
        __xNBS.name() : __xNBS,
        __verAplic.name() : __verAplic,
        __ambGer.name() : __ambGer,
        __tpEmis.name() : __tpEmis,
        __procEmi.name() : __procEmi,
        __cStat.name() : __cStat,
        __dhProc.name() : __dhProc,
        __nDFSe.name() : __nDFSe,
        __emit.name() : __emit,
        __valores.name() : __valores,
        __DPS.name() : __DPS
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.TCInfNFSe = TCInfNFSe
Namespace.addCategoryObject('typeBinding', 'TCInfNFSe', TCInfNFSe)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCDPS with content type ELEMENT_ONLY
class TCDPS (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCDPS with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCDPS')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 278, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}infDPS uses Python identifier infDPS
    __infDPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'infDPS'), 'infDPS', '__httpwww_sped_fazenda_gov_brnfse_TCDPS_httpwww_sped_fazenda_gov_brnfseinfDPS', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 280, 6), )

    
    infDPS = property(__infDPS.value, __infDPS.set, None, None)

    
    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature'), 'Signature', '__httpwww_sped_fazenda_gov_brnfse_TCDPS_httpwww_w3_org200009xmldsigSignature', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/xmldsig-core-schema.xsd', 43, 0), )

    
    Signature = property(__Signature.value, __Signature.set, None, None)

    
    # Attribute versao uses Python identifier versao
    __versao = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'versao'), 'versao', '__httpwww_sped_fazenda_gov_brnfse_TCDPS_versao', _module_typeBindings.TVerNFSe, required=True)
    __versao._DeclarationLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 283, 4)
    __versao._UseLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 283, 4)
    
    versao = property(__versao.value, __versao.set, None, None)

    _ElementMap.update({
        __infDPS.name() : __infDPS,
        __Signature.name() : __Signature
    })
    _AttributeMap.update({
        __versao.name() : __versao
    })
_module_typeBindings.TCDPS = TCDPS
Namespace.addCategoryObject('typeBinding', 'TCDPS', TCDPS)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCInfDPS with content type ELEMENT_ONLY
class TCInfDPS (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCInfDPS with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCInfDPS')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 286, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}tpAmb uses Python identifier tpAmb
    __tpAmb = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tpAmb'), 'tpAmb', '__httpwww_sped_fazenda_gov_brnfse_TCInfDPS_httpwww_sped_fazenda_gov_brnfsetpAmb', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 288, 6), )

    
    tpAmb = property(__tpAmb.value, __tpAmb.set, None, 'Identificação do Ambiente: 1 - Produção; 2 - Homologação')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}dhEmi uses Python identifier dhEmi
    __dhEmi = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dhEmi'), 'dhEmi', '__httpwww_sped_fazenda_gov_brnfse_TCInfDPS_httpwww_sped_fazenda_gov_brnfsedhEmi', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 293, 6), )

    
    dhEmi = property(__dhEmi.value, __dhEmi.set, None, 'Data e hora da emissão do DPS. Data e hora no formato UTC (Universal Coordinated Time): AAAA-MM-DDThh:mm:ssTZD')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}verAplic uses Python identifier verAplic
    __verAplic = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'verAplic'), 'verAplic', '__httpwww_sped_fazenda_gov_brnfse_TCInfDPS_httpwww_sped_fazenda_gov_brnfseverAplic', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 298, 6), )

    
    verAplic = property(__verAplic.value, __verAplic.set, None, 'Versão do aplicativo que gerou o DPS')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}serie uses Python identifier serie
    __serie = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'serie'), 'serie', '__httpwww_sped_fazenda_gov_brnfse_TCInfDPS_httpwww_sped_fazenda_gov_brnfseserie', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 303, 6), )

    
    serie = property(__serie.value, __serie.set, None, 'Número do equipamento emissor do DPS ou série do DPS')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}nDPS uses Python identifier nDPS
    __nDPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nDPS'), 'nDPS', '__httpwww_sped_fazenda_gov_brnfse_TCInfDPS_httpwww_sped_fazenda_gov_brnfsenDPS', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 308, 6), )

    
    nDPS = property(__nDPS.value, __nDPS.set, None, 'Número do DPS')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}dCompet uses Python identifier dCompet
    __dCompet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dCompet'), 'dCompet', '__httpwww_sped_fazenda_gov_brnfse_TCInfDPS_httpwww_sped_fazenda_gov_brnfsedCompet', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 313, 6), )

    
    dCompet = property(__dCompet.value, __dCompet.set, None, 'Data em que se iniciou a prestação do serviço: Dia, mês e ano (AAAAMMDD)')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}tpEmit uses Python identifier tpEmit
    __tpEmit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tpEmit'), 'tpEmit', '__httpwww_sped_fazenda_gov_brnfse_TCInfDPS_httpwww_sped_fazenda_gov_brnfsetpEmit', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 318, 6), )

    
    tpEmit = property(__tpEmit.value, __tpEmit.set, None, 'Emitente da DPS: 1 - Prestador; 2 - Tomador; 3 - Intermediário')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}cMotivoEmisTI uses Python identifier cMotivoEmisTI
    __cMotivoEmisTI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cMotivoEmisTI'), 'cMotivoEmisTI', '__httpwww_sped_fazenda_gov_brnfse_TCInfDPS_httpwww_sped_fazenda_gov_brnfsecMotivoEmisTI', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 323, 6), )

    
    cMotivoEmisTI = property(__cMotivoEmisTI.value, __cMotivoEmisTI.set, None, 'Motivo da Emissão da DPS pelo Tomador/Intermediário:\n            1 - Importação de Serviço;\n            2 - Tomador/Intermediário obrigado a emitir NFS-e por legislação municipal;\n            3 - Tomador/Intermediário emitindo NFS-e por recusa de emissão pelo prestador;\n            4 - Tomador/Intermediário emitindo por rejeitar a NFS-e emitida pelo prestador;\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}chNFSeRej uses Python identifier chNFSeRej
    __chNFSeRej = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'chNFSeRej'), 'chNFSeRej', '__httpwww_sped_fazenda_gov_brnfse_TCInfDPS_httpwww_sped_fazenda_gov_brnfsechNFSeRej', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 333, 6), )

    
    chNFSeRej = property(__chNFSeRej.value, __chNFSeRej.set, None, '\n            Chave de Acesso da NFS-e rejeitada pelo Tomador/Intermediário.\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}cLocEmi uses Python identifier cLocEmi
    __cLocEmi = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cLocEmi'), 'cLocEmi', '__httpwww_sped_fazenda_gov_brnfse_TCInfDPS_httpwww_sped_fazenda_gov_brnfsecLocEmi', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 340, 6), )

    
    cLocEmi = property(__cLocEmi.value, __cLocEmi.set, None, 'O código de município utilizado pelo Sistema Nacional NFS-e é o código definido para cada município pertencente ao ""Anexo V – Tabela de Código de Municípios do IBGE"", que consta ao final do Manual de Orientação ao Contribuinte do ISSQN para a Sefin Nacional NFS-e.\n            O município emissor da NFS-e é aquele município em que o emitente da DPS está cadastrado e autorizado a "emitir uma NFS-e", ou seja, emitir uma DPS para que o sistema nacional valide as informações nela prestadas e gere a NFS-e correspondente para o emitente.\n            Para que o sistema nacional emita a NFS-e o município emissor deve ser conveniado e estar ativo no sistema nacional. Além disso o convênio do município deve permitir que os contribuintes do município utilize os emissores públicos do Sistema Nacional NFS-e\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}subst uses Python identifier subst
    __subst = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'subst'), 'subst', '__httpwww_sped_fazenda_gov_brnfse_TCInfDPS_httpwww_sped_fazenda_gov_brnfsesubst', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 348, 6), )

    
    subst = property(__subst.value, __subst.set, None, 'Dados da NFS-e a ser substituída')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}prest uses Python identifier prest
    __prest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'prest'), 'prest', '__httpwww_sped_fazenda_gov_brnfse_TCInfDPS_httpwww_sped_fazenda_gov_brnfseprest', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 353, 6), )

    
    prest = property(__prest.value, __prest.set, None, 'Grupo de informações do DPS relativas ao Prestador de Serviços')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}toma uses Python identifier toma
    __toma = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'toma'), 'toma', '__httpwww_sped_fazenda_gov_brnfse_TCInfDPS_httpwww_sped_fazenda_gov_brnfsetoma', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 358, 6), )

    
    toma = property(__toma.value, __toma.set, None, 'Grupo de informações do DPS relativas ao Tomador de Serviços')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}interm uses Python identifier interm
    __interm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'interm'), 'interm', '__httpwww_sped_fazenda_gov_brnfse_TCInfDPS_httpwww_sped_fazenda_gov_brnfseinterm', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 363, 6), )

    
    interm = property(__interm.value, __interm.set, None, 'Grupo de informações do DPS relativas ao Intermediário de Serviços')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}serv uses Python identifier serv
    __serv = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'serv'), 'serv', '__httpwww_sped_fazenda_gov_brnfse_TCInfDPS_httpwww_sped_fazenda_gov_brnfseserv', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 368, 6), )

    
    serv = property(__serv.value, __serv.set, None, 'Grupo de informações do DPS relativas ao Serviço Prestado')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}valores uses Python identifier valores
    __valores = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'valores'), 'valores', '__httpwww_sped_fazenda_gov_brnfse_TCInfDPS_httpwww_sped_fazenda_gov_brnfsevalores', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 373, 6), )

    
    valores = property(__valores.value, __valores.set, None, '\n            Grupo de informações relativas à valores do serviço prestado\n          ')

    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httpwww_sped_fazenda_gov_brnfse_TCInfDPS_Id', _module_typeBindings.TSIdDPS, required=True)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 381, 4)
    __Id._UseLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 381, 4)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __tpAmb.name() : __tpAmb,
        __dhEmi.name() : __dhEmi,
        __verAplic.name() : __verAplic,
        __serie.name() : __serie,
        __nDPS.name() : __nDPS,
        __dCompet.name() : __dCompet,
        __tpEmit.name() : __tpEmit,
        __cMotivoEmisTI.name() : __cMotivoEmisTI,
        __chNFSeRej.name() : __chNFSeRej,
        __cLocEmi.name() : __cLocEmi,
        __subst.name() : __subst,
        __prest.name() : __prest,
        __toma.name() : __toma,
        __interm.name() : __interm,
        __serv.name() : __serv,
        __valores.name() : __valores
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.TCInfDPS = TCInfDPS
Namespace.addCategoryObject('typeBinding', 'TCInfDPS', TCInfDPS)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCEvento with content type ELEMENT_ONLY
class TCEvento (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCEvento with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCEvento')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 13, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}infEvento uses Python identifier infEvento
    __infEvento = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'infEvento'), 'infEvento', '__httpwww_sped_fazenda_gov_brnfse_TCEvento_httpwww_sped_fazenda_gov_brnfseinfEvento', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 15, 6), )

    
    infEvento = property(__infEvento.value, __infEvento.set, None, None)

    
    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature'), 'Signature', '__httpwww_sped_fazenda_gov_brnfse_TCEvento_httpwww_w3_org200009xmldsigSignature', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/xmldsig-core-schema.xsd', 43, 0), )

    
    Signature = property(__Signature.value, __Signature.set, None, None)

    
    # Attribute versao uses Python identifier versao
    __versao = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'versao'), 'versao', '__httpwww_sped_fazenda_gov_brnfse_TCEvento_versao', _module_typeBindings.TVerNFSe, required=True)
    __versao._DeclarationLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 18, 4)
    __versao._UseLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 18, 4)
    
    versao = property(__versao.value, __versao.set, None, None)

    _ElementMap.update({
        __infEvento.name() : __infEvento,
        __Signature.name() : __Signature
    })
    _AttributeMap.update({
        __versao.name() : __versao
    })
_module_typeBindings.TCEvento = TCEvento
Namespace.addCategoryObject('typeBinding', 'TCEvento', TCEvento)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCInfEvento with content type ELEMENT_ONLY
class TCInfEvento (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCInfEvento with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCInfEvento')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 22, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}verAplic uses Python identifier verAplic
    __verAplic = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'verAplic'), 'verAplic', '__httpwww_sped_fazenda_gov_brnfse_TCInfEvento_httpwww_sped_fazenda_gov_brnfseverAplic', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 24, 6), )

    
    verAplic = property(__verAplic.value, __verAplic.set, None, 'Versão do aplicativo que gerou o pedido do evento.')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}ambGer uses Python identifier ambGer
    __ambGer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ambGer'), 'ambGer', '__httpwww_sped_fazenda_gov_brnfse_TCInfEvento_httpwww_sped_fazenda_gov_brnfseambGer', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 29, 6), )

    
    ambGer = property(__ambGer.value, __ambGer.set, None, 'Ambiente gerador do evento')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}nSeqEvento uses Python identifier nSeqEvento
    __nSeqEvento = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nSeqEvento'), 'nSeqEvento', '__httpwww_sped_fazenda_gov_brnfse_TCInfEvento_httpwww_sped_fazenda_gov_brnfsenSeqEvento', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 34, 6), )

    
    nSeqEvento = property(__nSeqEvento.value, __nSeqEvento.set, None, 'Sequencial do evento para o mesmo tipo de evento. Para maioria dos eventos nSeqEvento=1. Nos casos em que possa existir mais de um evento do mesmo tipo o ambiente gerador deverá numerar de forma sequencial.')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}dhProc uses Python identifier dhProc
    __dhProc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dhProc'), 'dhProc', '__httpwww_sped_fazenda_gov_brnfse_TCInfEvento_httpwww_sped_fazenda_gov_brnfsedhProc', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 39, 6), )

    
    dhProc = property(__dhProc.value, __dhProc.set, None, '\n            Data/Hora do registro do evento.\n            Data e hora no formato UTC (Universal Coordinated Time): AAAA-MM-DDThh:mm:ssTZD"\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}nDFe uses Python identifier nDFe
    __nDFe = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nDFe'), 'nDFe', '__httpwww_sped_fazenda_gov_brnfse_TCInfEvento_httpwww_sped_fazenda_gov_brnfsenDFe', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 47, 6), )

    
    nDFe = property(__nDFe.value, __nDFe.set, None, 'Ambiente gerador do evento')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}pedRegEvento uses Python identifier pedRegEvento
    __pedRegEvento = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'pedRegEvento'), 'pedRegEvento', '__httpwww_sped_fazenda_gov_brnfse_TCInfEvento_httpwww_sped_fazenda_gov_brnfsepedRegEvento', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 52, 6), )

    
    pedRegEvento = property(__pedRegEvento.value, __pedRegEvento.set, None, 'Leiaute do pedido de registro do evento gerado pelo autor do evento')

    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httpwww_sped_fazenda_gov_brnfse_TCInfEvento_Id', _module_typeBindings.TSIdEvento, required=True)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 58, 4)
    __Id._UseLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 58, 4)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __verAplic.name() : __verAplic,
        __ambGer.name() : __ambGer,
        __nSeqEvento.name() : __nSeqEvento,
        __dhProc.name() : __dhProc,
        __nDFe.name() : __nDFe,
        __pedRegEvento.name() : __pedRegEvento
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.TCInfEvento = TCInfEvento
Namespace.addCategoryObject('typeBinding', 'TCInfEvento', TCInfEvento)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCPedRegEvt with content type ELEMENT_ONLY
class TCPedRegEvt (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCPedRegEvt with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCPedRegEvt')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 62, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}infPedReg uses Python identifier infPedReg
    __infPedReg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'infPedReg'), 'infPedReg', '__httpwww_sped_fazenda_gov_brnfse_TCPedRegEvt_httpwww_sped_fazenda_gov_brnfseinfPedReg', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 64, 6), )

    
    infPedReg = property(__infPedReg.value, __infPedReg.set, None, None)

    
    # Element {http://www.w3.org/2000/09/xmldsig#}Signature uses Python identifier Signature
    __Signature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature'), 'Signature', '__httpwww_sped_fazenda_gov_brnfse_TCPedRegEvt_httpwww_w3_org200009xmldsigSignature', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/xmldsig-core-schema.xsd', 43, 0), )

    
    Signature = property(__Signature.value, __Signature.set, None, None)

    
    # Attribute versao uses Python identifier versao
    __versao = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'versao'), 'versao', '__httpwww_sped_fazenda_gov_brnfse_TCPedRegEvt_versao', _module_typeBindings.TVerNFSe, required=True)
    __versao._DeclarationLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 67, 4)
    __versao._UseLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 67, 4)
    
    versao = property(__versao.value, __versao.set, None, None)

    _ElementMap.update({
        __infPedReg.name() : __infPedReg,
        __Signature.name() : __Signature
    })
    _AttributeMap.update({
        __versao.name() : __versao
    })
_module_typeBindings.TCPedRegEvt = TCPedRegEvt
Namespace.addCategoryObject('typeBinding', 'TCPedRegEvt', TCPedRegEvt)


# Complex type {http://www.sped.fazenda.gov.br/nfse}TCInfPedReg with content type ELEMENT_ONLY
class TCInfPedReg (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.sped.fazenda.gov.br/nfse}TCInfPedReg with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TCInfPedReg')
    _XSDLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 71, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.sped.fazenda.gov.br/nfse}tpAmb uses Python identifier tpAmb
    __tpAmb = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tpAmb'), 'tpAmb', '__httpwww_sped_fazenda_gov_brnfse_TCInfPedReg_httpwww_sped_fazenda_gov_brnfsetpAmb', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 73, 6), )

    
    tpAmb = property(__tpAmb.value, __tpAmb.set, None, 'Identificação do Ambiente: 1 - Produção; 2 - Homologação')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}verAplic uses Python identifier verAplic
    __verAplic = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'verAplic'), 'verAplic', '__httpwww_sped_fazenda_gov_brnfse_TCInfPedReg_httpwww_sped_fazenda_gov_brnfseverAplic', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 78, 6), )

    
    verAplic = property(__verAplic.value, __verAplic.set, None, 'Versão do aplicativo que gerou o pedido de registro de evento.')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}dhEvento uses Python identifier dhEvento
    __dhEvento = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'dhEvento'), 'dhEvento', '__httpwww_sped_fazenda_gov_brnfse_TCInfPedReg_httpwww_sped_fazenda_gov_brnfsedhEvento', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 83, 6), )

    
    dhEvento = property(__dhEvento.value, __dhEvento.set, None, '\n            Data e hora do evento no formato AAAA-MM-DDThh:mm:ssTZD (UTC - Universal Coordinated Time, onde TZD pode ser -02:00 (Fernando de Noronha), -03:00 (Brasília) ou -04:00 (Manaus), no horário de verão serão -01:00, -02:00 e -03:00.\n            Ex.: 2010-08-19T13:00:15-03:00.\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}CNPJAutor uses Python identifier CNPJAutor
    __CNPJAutor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CNPJAutor'), 'CNPJAutor', '__httpwww_sped_fazenda_gov_brnfse_TCInfPedReg_httpwww_sped_fazenda_gov_brnfseCNPJAutor', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 95, 8), )

    
    CNPJAutor = property(__CNPJAutor.value, __CNPJAutor.set, None, 'CNPJ do autor do evento.')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}CPFAutor uses Python identifier CPFAutor
    __CPFAutor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CPFAutor'), 'CPFAutor', '__httpwww_sped_fazenda_gov_brnfse_TCInfPedReg_httpwww_sped_fazenda_gov_brnfseCPFAutor', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 100, 8), )

    
    CPFAutor = property(__CPFAutor.value, __CPFAutor.set, None, 'CPF do autor do evento.')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}chNFSe uses Python identifier chNFSe
    __chNFSe = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'chNFSe'), 'chNFSe', '__httpwww_sped_fazenda_gov_brnfse_TCInfPedReg_httpwww_sped_fazenda_gov_brnfsechNFSe', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 106, 6), )

    
    chNFSe = property(__chNFSe.value, __chNFSe.set, None, 'Chave de Acesso da NFS-e vinculada ao Evento')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}nPedRegEvento uses Python identifier nPedRegEvento
    __nPedRegEvento = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'nPedRegEvento'), 'nPedRegEvento', '__httpwww_sped_fazenda_gov_brnfse_TCInfPedReg_httpwww_sped_fazenda_gov_brnfsenPedRegEvento', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 111, 6), )

    
    nPedRegEvento = property(__nPedRegEvento.value, __nPedRegEvento.set, None, '\n            Número do pedido do registro de evento para o mesmo tipo de evento.\n            Para os eventos que ocorrem somente uma vez, como é o caso do cancelamento, o nPedRegEvento deve ser igual a 1.\n            Os eventos que podem ocorrer mais de uma vez devem ter o nPedRegEvento único.\n          ')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}e101101 uses Python identifier e101101
    __e101101 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'e101101'), 'e101101', '__httpwww_sped_fazenda_gov_brnfse_TCInfPedReg_httpwww_sped_fazenda_gov_brnfsee101101', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 121, 8), )

    
    e101101 = property(__e101101.value, __e101101.set, None, 'Evento de cancelamento')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}e105102 uses Python identifier e105102
    __e105102 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'e105102'), 'e105102', '__httpwww_sped_fazenda_gov_brnfse_TCInfPedReg_httpwww_sped_fazenda_gov_brnfsee105102', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 126, 8), )

    
    e105102 = property(__e105102.value, __e105102.set, None, 'Evento de cancelamento por substituição')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}e101103 uses Python identifier e101103
    __e101103 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'e101103'), 'e101103', '__httpwww_sped_fazenda_gov_brnfse_TCInfPedReg_httpwww_sped_fazenda_gov_brnfsee101103', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 131, 8), )

    
    e101103 = property(__e101103.value, __e101103.set, None, 'Solicitação de Análise Fiscal para Cancelamento de NFS-e')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}e105104 uses Python identifier e105104
    __e105104 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'e105104'), 'e105104', '__httpwww_sped_fazenda_gov_brnfse_TCInfPedReg_httpwww_sped_fazenda_gov_brnfsee105104', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 136, 8), )

    
    e105104 = property(__e105104.value, __e105104.set, None, 'Cancelamento de NFS-e Deferido por Análise Fiscal')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}e105105 uses Python identifier e105105
    __e105105 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'e105105'), 'e105105', '__httpwww_sped_fazenda_gov_brnfse_TCInfPedReg_httpwww_sped_fazenda_gov_brnfsee105105', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 141, 8), )

    
    e105105 = property(__e105105.value, __e105105.set, None, 'Cancelamento de NFS-e Indeferido por Análise Fiscal')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}e202201 uses Python identifier e202201
    __e202201 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'e202201'), 'e202201', '__httpwww_sped_fazenda_gov_brnfse_TCInfPedReg_httpwww_sped_fazenda_gov_brnfsee202201', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 147, 8), )

    
    e202201 = property(__e202201.value, __e202201.set, None, 'Confirmação do Prestador')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}e203202 uses Python identifier e203202
    __e203202 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'e203202'), 'e203202', '__httpwww_sped_fazenda_gov_brnfse_TCInfPedReg_httpwww_sped_fazenda_gov_brnfsee203202', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 152, 8), )

    
    e203202 = property(__e203202.value, __e203202.set, None, 'Confirmação do Tomador')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}e204203 uses Python identifier e204203
    __e204203 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'e204203'), 'e204203', '__httpwww_sped_fazenda_gov_brnfse_TCInfPedReg_httpwww_sped_fazenda_gov_brnfsee204203', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 157, 8), )

    
    e204203 = property(__e204203.value, __e204203.set, None, 'Confirmação do Intermediário')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}e205204 uses Python identifier e205204
    __e205204 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'e205204'), 'e205204', '__httpwww_sped_fazenda_gov_brnfse_TCInfPedReg_httpwww_sped_fazenda_gov_brnfsee205204', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 162, 8), )

    
    e205204 = property(__e205204.value, __e205204.set, None, 'Confirmação Tácita')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}e202205 uses Python identifier e202205
    __e202205 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'e202205'), 'e202205', '__httpwww_sped_fazenda_gov_brnfse_TCInfPedReg_httpwww_sped_fazenda_gov_brnfsee202205', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 167, 8), )

    
    e202205 = property(__e202205.value, __e202205.set, None, 'Rejeição do Prestador')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}e203206 uses Python identifier e203206
    __e203206 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'e203206'), 'e203206', '__httpwww_sped_fazenda_gov_brnfse_TCInfPedReg_httpwww_sped_fazenda_gov_brnfsee203206', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 172, 8), )

    
    e203206 = property(__e203206.value, __e203206.set, None, 'Rejeição do Tomador')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}e204207 uses Python identifier e204207
    __e204207 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'e204207'), 'e204207', '__httpwww_sped_fazenda_gov_brnfse_TCInfPedReg_httpwww_sped_fazenda_gov_brnfsee204207', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 177, 8), )

    
    e204207 = property(__e204207.value, __e204207.set, None, 'Rejeição do Intermediário')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}e205208 uses Python identifier e205208
    __e205208 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'e205208'), 'e205208', '__httpwww_sped_fazenda_gov_brnfse_TCInfPedReg_httpwww_sped_fazenda_gov_brnfsee205208', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 182, 8), )

    
    e205208 = property(__e205208.value, __e205208.set, None, 'Anulação da Rejeição')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}e305101 uses Python identifier e305101
    __e305101 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'e305101'), 'e305101', '__httpwww_sped_fazenda_gov_brnfse_TCInfPedReg_httpwww_sped_fazenda_gov_brnfsee305101', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 188, 8), )

    
    e305101 = property(__e305101.value, __e305101.set, None, 'Cancelamento de NFS-e por Ofício')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}e305102 uses Python identifier e305102
    __e305102 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'e305102'), 'e305102', '__httpwww_sped_fazenda_gov_brnfse_TCInfPedReg_httpwww_sped_fazenda_gov_brnfsee305102', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 193, 8), )

    
    e305102 = property(__e305102.value, __e305102.set, None, 'Bloqueio de NFS-e por Ofício')

    
    # Element {http://www.sped.fazenda.gov.br/nfse}e305103 uses Python identifier e305103
    __e305103 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'e305103'), 'e305103', '__httpwww_sped_fazenda_gov_brnfse_TCInfPedReg_httpwww_sped_fazenda_gov_brnfsee305103', False, pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 198, 8), )

    
    e305103 = property(__e305103.value, __e305103.set, None, 'Desbloqueio de NFS-e por Ofício')

    
    # Attribute Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Id'), 'Id', '__httpwww_sped_fazenda_gov_brnfse_TCInfPedReg_Id', _module_typeBindings.TSIdPedRefEvt, required=True)
    __Id._DeclarationLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 205, 4)
    __Id._UseLocation = pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 205, 4)
    
    Id = property(__Id.value, __Id.set, None, None)

    _ElementMap.update({
        __tpAmb.name() : __tpAmb,
        __verAplic.name() : __verAplic,
        __dhEvento.name() : __dhEvento,
        __CNPJAutor.name() : __CNPJAutor,
        __CPFAutor.name() : __CPFAutor,
        __chNFSe.name() : __chNFSe,
        __nPedRegEvento.name() : __nPedRegEvento,
        __e101101.name() : __e101101,
        __e105102.name() : __e105102,
        __e101103.name() : __e101103,
        __e105104.name() : __e105104,
        __e105105.name() : __e105105,
        __e202201.name() : __e202201,
        __e203202.name() : __e203202,
        __e204203.name() : __e204203,
        __e205204.name() : __e205204,
        __e202205.name() : __e202205,
        __e203206.name() : __e203206,
        __e204207.name() : __e204207,
        __e205208.name() : __e205208,
        __e305101.name() : __e305101,
        __e305102.name() : __e305102,
        __e305103.name() : __e305103
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
_module_typeBindings.TCInfPedReg = TCInfPedReg
Namespace.addCategoryObject('typeBinding', 'TCInfPedReg', TCInfPedReg)


pedRegEvento = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pedRegEvento'), TCPedRegEvt, documentation='Schema XML do Pedido de Registro de Eventos', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/pedRegEvento_v1.00.xsd', 10, 2))
Namespace.addCategoryObject('elementBinding', pedRegEvento.name().localName(), pedRegEvento)



TCEmitente._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CNPJ'), TSCNPJ, scope=TCEmitente, documentation='\n              Número do CNPJ do emitente da NFS-e.\n            ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 147, 8)))

TCEmitente._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CPF'), TSCPF, scope=TCEmitente, documentation='\n              Número do CPF do emitente da NFS-e.\n            ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 154, 8)))

TCEmitente._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IM'), TSInscMun, scope=TCEmitente, documentation='Número da inscrição municipal', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 162, 6)))

TCEmitente._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xNome'), TSNomeRazaoSocial, scope=TCEmitente, documentation='\n            Nome / Razão Social do emitente.\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 167, 6)))

TCEmitente._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xFant'), TSNomeFantasia, scope=TCEmitente, documentation='\n            Nome / Fantasia do emitente.\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 174, 6)))

TCEmitente._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'enderNac'), TCEnderecoEmitente, scope=TCEmitente, documentation='Grupo de informações do endereço nacional do Emitente da NFS-e', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 181, 6)))

TCEmitente._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fone'), TSTelefone, scope=TCEmitente, documentation='\n            Número do telefone do emitente.\n            (Preencher com o Código DDD + número do telefone.\n            Nas operações com exterior é permitido informar o código do país + código da localidade + número do telefone)\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 186, 6)))

TCEmitente._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'email'), TSEmail, scope=TCEmitente, documentation='E-mail do emitente.', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 195, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 162, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 174, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 186, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 195, 6))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCEmitente._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CNPJ')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 147, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCEmitente._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CPF')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 154, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCEmitente._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IM')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 162, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCEmitente._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xNome')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 167, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCEmitente._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xFant')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 174, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCEmitente._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'enderNac')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 181, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TCEmitente._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fone')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 186, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(TCEmitente._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'email')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 195, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCEmitente._Automaton = _BuildAutomaton()




TCValoresNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vCalcDR'), TSDec15V2, scope=TCValoresNFSe, documentation='\n            Valor monetário (R$) de dedução/redução da base de cálculo (BC) do ISSQN.\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 205, 6)))

TCValoresNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tpBM'), TBMISSQN, scope=TCValoresNFSe, documentation="\n            Tipo Benefício Municipal (BM):\n\n\t\t\t1) Isenção;\n            2) Redução da BC em 'ppBM' %;\n            3) Redução da BC em R$ 'vInfoBM';\n            4) Alíquota Diferenciada de 'aliqDifBM' %;\n          ", location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 212, 6)))

TCValoresNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vCalcBM'), TSDec15V2, scope=TCValoresNFSe, documentation='\n            Valor monetário (R$) do percentual de redução da base de cálculo (BC) do ISSQN devido a um benefício municipal (BM).\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 224, 6)))

TCValoresNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vBC'), TSDec15V2, scope=TCValoresNFSe, documentation='\n            Valor monetário (R$) do percentual de redução da base de cálculo (BC) do ISSQN devido a um benefício municipal (BM).\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 231, 6)))

TCValoresNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pAliqAplic'), TSDec1V2, scope=TCValoresNFSe, documentation='\n            Alíquota aplicada sobre a base de cálculo para apuração do ISSQN.\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 238, 6)))

TCValoresNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vISSQN'), TSDec15V2, scope=TCValoresNFSe, documentation='\n            Valor do ISSQN (R$) = Valor da Base de Cálculo x Alíquota ISSQN = vBC x pAliqAplic\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 245, 6)))

TCValoresNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vTotalRet'), TSDec15V2, scope=TCValoresNFSe, documentation='\n            Valor total de retenções = Σ(CP + IRRF + CSLL  + ISSQN* +  (PIS + COFINS)**)\n            vTotalRet (R$) = (vRetCP + vRetIRRF + vRetCSLL) + vISSQN* + (vPIS + vCOFINS)**\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 252, 6)))

TCValoresNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vLiq'), TSDec15V2, scope=TCValoresNFSe, documentation='\n            Valor líquido = Valor do serviço - Desconto condicionado - Desconto incondicionado - Valores retidos (CP, IRRF, CSLL)* - Valores, se retidos (ISSQN, PIS, COFINS)**\n            Valor Líquido (R$) = vServ – vDescIncond – vDescCond – (vRetCP + vRetIRRF + vRetCSLL)* – (vISSQN - vPIS + vCOFINS)**\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 260, 6)))

TCValoresNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xOutInf'), TSDesc2000, scope=TCValoresNFSe, documentation='\n            Uso da Administração Tributária Municipal.\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 268, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 205, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 212, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 224, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 231, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 238, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 245, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 252, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 268, 6))
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCValoresNFSe._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vCalcDR')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 205, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCValoresNFSe._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tpBM')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 212, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCValoresNFSe._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vCalcBM')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 224, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCValoresNFSe._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vBC')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 231, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCValoresNFSe._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'pAliqAplic')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 238, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCValoresNFSe._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vISSQN')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 245, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCValoresNFSe._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vTotalRet')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 252, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCValoresNFSe._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vLiq')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 260, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(TCValoresNFSe._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xOutInf')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 268, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCValoresNFSe._Automaton = _BuildAutomaton_()




TCSubstituicao._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'chSubstda'), TSChaveNFSe, scope=TCSubstituicao, documentation='Chave de acesso da NFS-e a ser substituída', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 386, 6)))

TCSubstituicao._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cMotivo'), TSCodJustSubst, scope=TCSubstituicao, documentation='\n            Código de justificativa para substituição de NFS-e:\n            01 - Desenquadramento de NFS-e do Simples Nacional;\n            02 - Enquadramento de NFS-e no Simples Nacional;\n            03 - Inclusão Retroativa de Imunidade/Isenção para NFS-e;\n            04 - Exclusão Retroativa de Imunidade/Isenção para NFS-e;\n            05 - Rejeição de NFS-e pelo tomador ou pelo intermediário se responsável pelo recolhimento do tributo;\n            99 - Outros;\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 391, 6)))

TCSubstituicao._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xMotivo'), TSMotivo, scope=TCSubstituicao, documentation='Descrição do motivo da substituição da NFS-e', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 404, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 404, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCSubstituicao._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'chSubstda')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 386, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCSubstituicao._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cMotivo')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 391, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TCSubstituicao._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xMotivo')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 404, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCSubstituicao._Automaton = _BuildAutomaton_2()




TCInfoPrestador._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CNPJ'), TSCNPJ, scope=TCInfoPrestador, documentation='Número do CNPJ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 418, 8)))

TCInfoPrestador._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CPF'), TSCPF, scope=TCInfoPrestador, documentation='Número do CPF', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 423, 8)))

TCInfoPrestador._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NIF'), TSNIF, scope=TCInfoPrestador, documentation='Número de Identificação Fiscal fornecido por órgão de administração tributária no exterior', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 428, 8)))

TCInfoPrestador._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cNaoNIF'), TSCodNaoNIF, scope=TCInfoPrestador, documentation='\n              Motivo para não informação do NIF:\n              0 - Não informado na nota de origem;\n              1 - Dispensado do NIF;\n              2 - Não exigência do NIF;\n            ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 433, 8)))

TCInfoPrestador._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CAEPF'), TSCAEPF, scope=TCInfoPrestador, documentation='Número do Cadastro de Atividade Econômica da Pessoa Física (CAEPF) do prestador do serviço.', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 444, 6)))

TCInfoPrestador._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IM'), TSInscMun, scope=TCInfoPrestador, documentation='Número da inscrição municipal', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 449, 6)))

TCInfoPrestador._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xNome'), TSNomeRazaoSocial, scope=TCInfoPrestador, documentation='Nome/Nome Empresarial do prestador', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 454, 6)))

TCInfoPrestador._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'end'), TCEndereco, scope=TCInfoPrestador, documentation='Dados de endereço do prestador', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 459, 6)))

TCInfoPrestador._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fone'), TSTelefone, scope=TCInfoPrestador, documentation='\n            Número do telefone do prestador:\n            Preencher com o Código DDD + número do telefone.\n            Nas operações com exterior é permitido informar o código do país + código da localidade + número do telefone)\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 464, 6)))

TCInfoPrestador._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'email'), TSEmail, scope=TCInfoPrestador, documentation='E-mail', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 473, 6)))

TCInfoPrestador._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'regTrib'), TCRegTrib, scope=TCInfoPrestador, documentation='\n            Grupo de informações relativas aos regimes de tributação do prestador de serviços\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 478, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 444, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 449, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 454, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 459, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 464, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 473, 6))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfoPrestador._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CNPJ')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 418, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfoPrestador._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CPF')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 423, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfoPrestador._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NIF')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 428, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfoPrestador._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cNaoNIF')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 433, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfoPrestador._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CAEPF')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 444, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfoPrestador._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IM')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 449, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfoPrestador._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xNome')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 454, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfoPrestador._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'end')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 459, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfoPrestador._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fone')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 464, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfoPrestador._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'email')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 473, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCInfoPrestador._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'regTrib')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 478, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCInfoPrestador._Automaton = _BuildAutomaton_3()




TCRegTrib._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'opSimpNac'), TSOpSimpNac, scope=TCRegTrib, documentation='\n            Situação perante o Simples Nacional:\n            1 - Não Optante;\n            2 - Optante - Microempreendedor Individual (MEI);\n            3 - Optante - Microempresa ou Empresa de Pequeno Porte (ME/EPP);\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 490, 6)))

TCRegTrib._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'regApTribSN'), TSRegimeApuracaoSimpNac, scope=TCRegTrib, documentation='\n            Opção para que o contribuinte optante pelo Simples Nacional ME/EPP (opSimpNac = 3) possa indicar, ao emitir o documento fiscal, em qual regime de apuração os tributos federais e municipal estão inseridos, caso tenha ultrapassado algum sublimite ou limite definido para o Simples Nacional.\n            1 – Regime de apuração dos tributos federais e municipal pelo SN;\n            2 – Regime de apuração dos tributos federais pelo SN e ISSQN  por fora do SN conforme respectiva legislação municipal do tributo;\n            3 – Regime de apuração dos tributos federais e municipal por fora do SN conforme respectivas legilações federal e municipal de cada tributo;\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 500, 6)))

TCRegTrib._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'regEspTrib'), TSRegEspTrib, scope=TCRegTrib, documentation='\n            Tipos de Regimes Especiais de Tributação:\n            0 - Nenhum;\n            1 - Ato Cooperado (Cooperativa);\n            2 - Estimativa;\n            3 - Microempresa Municipal;\n            4 - Notário ou Registrador;\n            5 - Profissional Autônomo;\n            6 - Sociedade de Profissionais;\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 510, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 500, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCRegTrib._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'opSimpNac')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 490, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCRegTrib._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'regApTribSN')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 500, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCRegTrib._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'regEspTrib')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 510, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCRegTrib._Automaton = _BuildAutomaton_4()




TCInfoPessoa._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CNPJ'), TSCNPJ, scope=TCInfoPessoa, documentation='Número do CNPJ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 533, 8)))

TCInfoPessoa._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CPF'), TSCPF, scope=TCInfoPessoa, documentation='Número do CPF', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 538, 8)))

TCInfoPessoa._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NIF'), TSNIF, scope=TCInfoPessoa, documentation='Número de Identificação Fiscal fornecido por órgão de administração tributária no exterior', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 543, 8)))

TCInfoPessoa._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cNaoNIF'), TSCodNaoNIF, scope=TCInfoPessoa, documentation='\n              Motivo para não informação do NIF:\n              0 - Não informado na nota de origem;\n              1 - Dispensado do NIF;\n              2 - Não exigência do NIF;\n            ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 548, 8)))

TCInfoPessoa._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CAEPF'), TSCAEPF, scope=TCInfoPessoa, documentation='Número do Cadastro de Atividade Econômica da Pessoa Física (CAEPF)', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 559, 6)))

TCInfoPessoa._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IM'), TSInscMun, scope=TCInfoPessoa, documentation='Número da inscrição municipal', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 564, 6)))

TCInfoPessoa._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xNome'), TSNomeRazaoSocial, scope=TCInfoPessoa, documentation='Nome/Nome Empresarial', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 569, 6)))

TCInfoPessoa._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'end'), TCEndereco, scope=TCInfoPessoa, documentation='Dados de endereço', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 574, 6)))

TCInfoPessoa._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fone'), TSTelefone, scope=TCInfoPessoa, documentation='\n            Número do telefone do prestador:\n            Preencher com o Código DDD + número do telefone.\n            Nas operações com exterior é permitido informar o código do país + código da localidade + número do telefone)\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 579, 6)))

TCInfoPessoa._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'email'), TSEmail, scope=TCInfoPessoa, documentation='E-mail', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 588, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 559, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 564, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 574, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 579, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 588, 6))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfoPessoa._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CNPJ')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 533, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfoPessoa._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CPF')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 538, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfoPessoa._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NIF')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 543, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfoPessoa._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cNaoNIF')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 548, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfoPessoa._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CAEPF')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 559, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfoPessoa._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IM')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 564, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCInfoPessoa._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xNome')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 569, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TCInfoPessoa._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'end')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 574, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(TCInfoPessoa._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fone')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 579, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(TCInfoPessoa._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'email')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 588, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCInfoPessoa._Automaton = _BuildAutomaton_5()




TCEndereco._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'endNac'), TCEnderNac, scope=TCEndereco, documentation='Grupo de informações específicas de endereço nacional', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 599, 8)))

TCEndereco._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'endExt'), TCEnderExt, scope=TCEndereco, documentation='Grupo de informações específicas de endereço no exterior', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 604, 8)))

TCEndereco._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xLgr'), TSLogradouro, scope=TCEndereco, documentation='Tipo e nome do logradouro da localização do imóvel', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 610, 6)))

TCEndereco._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nro'), TSNumeroEndereco, scope=TCEndereco, documentation='Número do imóvel', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 615, 6)))

TCEndereco._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xCpl'), TSComplementoEndereco, scope=TCEndereco, documentation='Complemento do endereço', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 620, 6)))

TCEndereco._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xBairro'), TSBairro, scope=TCEndereco, documentation='Bairro', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 625, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 598, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 620, 6))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCEndereco._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'endNac')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 599, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCEndereco._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'endExt')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 604, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCEndereco._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xLgr')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 610, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCEndereco._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nro')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 615, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCEndereco._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xCpl')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 620, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCEndereco._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xBairro')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 625, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCEndereco._Automaton = _BuildAutomaton_6()




TCEnderecoEmitente._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xLgr'), TSLogradouro, scope=TCEnderecoEmitente, documentation='Tipo e nome do logradouro da localização do imóvel', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 635, 6)))

TCEnderecoEmitente._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nro'), TSNumeroEndereco, scope=TCEnderecoEmitente, documentation='Número do imóvel', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 640, 6)))

TCEnderecoEmitente._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xCpl'), TSComplementoEndereco, scope=TCEnderecoEmitente, documentation='Complemento do endereço', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 645, 6)))

TCEnderecoEmitente._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xBairro'), TSBairro, scope=TCEnderecoEmitente, documentation='Bairro', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 650, 6)))

TCEnderecoEmitente._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cMun'), TSCodMunIBGE, scope=TCEnderecoEmitente, documentation='Código do município, conforme Tabela do IBGE', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 655, 6)))

TCEnderecoEmitente._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UF'), TSUF, scope=TCEnderecoEmitente, documentation='Sigla da unidade da federação do município do endereço do emitente.', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 660, 6)))

TCEnderecoEmitente._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CEP'), TSCEP, scope=TCEnderecoEmitente, documentation='Número do CEP', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 665, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 645, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCEnderecoEmitente._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xLgr')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 635, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCEnderecoEmitente._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nro')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 640, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCEnderecoEmitente._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xCpl')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 645, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCEnderecoEmitente._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xBairro')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 650, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCEnderecoEmitente._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cMun')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 655, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCEnderecoEmitente._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UF')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 660, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCEnderecoEmitente._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CEP')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 665, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCEnderecoEmitente._Automaton = _BuildAutomaton_7()




TCEnderecoSimples._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CEP'), TSCEP, scope=TCEnderecoSimples, documentation='Número do CEP', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 676, 8)))

TCEnderecoSimples._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'endExt'), TCEnderExtSimples, scope=TCEnderecoSimples, documentation='Grupo de informações específicas de endereço no exterior', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 681, 8)))

TCEnderecoSimples._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xLgr'), TSLogradouro, scope=TCEnderecoSimples, documentation='Tipo e nome do logradouro da localização do imóvel', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 687, 6)))

TCEnderecoSimples._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nro'), TSNumeroEndereco, scope=TCEnderecoSimples, documentation='Número do imóvel', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 692, 6)))

TCEnderecoSimples._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xCpl'), TSComplementoEndereco, scope=TCEnderecoSimples, documentation='Complemento do endereço', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 697, 6)))

TCEnderecoSimples._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xBairro'), TSBairro, scope=TCEnderecoSimples, documentation='Bairro', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 702, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 697, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCEnderecoSimples._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CEP')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 676, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCEnderecoSimples._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'endExt')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 681, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCEnderecoSimples._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xLgr')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 687, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCEnderecoSimples._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nro')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 692, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCEnderecoSimples._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xCpl')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 697, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCEnderecoSimples._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xBairro')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 702, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCEnderecoSimples._Automaton = _BuildAutomaton_8()




TCEnderNac._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cMun'), TSCodMunIBGE, scope=TCEnderNac, documentation='Código do município, conforme Tabela do IBGE', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 712, 6)))

TCEnderNac._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CEP'), TSCEP, scope=TCEnderNac, documentation='Número do CEP', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 717, 6)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCEnderNac._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cMun')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 712, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCEnderNac._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CEP')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 717, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCEnderNac._Automaton = _BuildAutomaton_9()




TCEnderExt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cPais'), TSCodPaisISO, scope=TCEnderExt, documentation='Código do país (Tabela de Países ISO)', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 727, 6)))

TCEnderExt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cEndPost'), TSCodigoEndPostal, scope=TCEnderExt, documentation='Código alfanumérico do Endereçamento Postal no exterior do prestador do serviço.', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 732, 6)))

TCEnderExt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xCidade'), TSCidade, scope=TCEnderExt, documentation='Nome da cidade no exterior do prestador do serviço.', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 737, 6)))

TCEnderExt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xEstProvReg'), TSEstadoProvRegiao, scope=TCEnderExt, documentation='Estado, província ou região da cidade no exterior do prestador do serviço.', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 742, 6)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCEnderExt._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cPais')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 727, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCEnderExt._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cEndPost')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 732, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCEnderExt._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xCidade')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 737, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCEnderExt._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xEstProvReg')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 742, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCEnderExt._Automaton = _BuildAutomaton_10()




TCEnderExtSimples._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cEndPost'), TSCodigoEndPostal, scope=TCEnderExtSimples, documentation='Código alfanumérico do Endereçamento Postal no exterior do prestador do serviço.', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 752, 6)))

TCEnderExtSimples._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xCidade'), TSCidade, scope=TCEnderExtSimples, documentation='Nome da cidade no exterior do prestador do serviço.', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 757, 6)))

TCEnderExtSimples._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xEstProvReg'), TSEstadoProvRegiao, scope=TCEnderExtSimples, documentation='Estado, província ou região da cidade no exterior do prestador do serviço.', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 762, 6)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCEnderExtSimples._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cEndPost')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 752, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCEnderExtSimples._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xCidade')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 757, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCEnderExtSimples._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xEstProvReg')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 762, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCEnderExtSimples._Automaton = _BuildAutomaton_11()




TCEnderObraEvento._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CEP'), TSCEP, scope=TCEnderObraEvento, documentation='Número do CEP', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 773, 8)))

TCEnderObraEvento._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'endExt'), TCEnderExtSimples, scope=TCEnderObraEvento, documentation='Grupo de informações específicas de endereço no exterior', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 778, 8)))

TCEnderObraEvento._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xLgr'), TSLogradouro, scope=TCEnderObraEvento, documentation='Tipo e nome do logradouro da localização do imóvel', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 784, 6)))

TCEnderObraEvento._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nro'), TSNumeroEndereco, scope=TCEnderObraEvento, documentation='Número do imóvel', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 789, 6)))

TCEnderObraEvento._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xCpl'), TSComplementoEndereco, scope=TCEnderObraEvento, documentation='Complemento do endereço', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 794, 6)))

TCEnderObraEvento._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xBairro'), TSBairro, scope=TCEnderObraEvento, documentation='Bairro', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 799, 6)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 794, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCEnderObraEvento._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CEP')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 773, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCEnderObraEvento._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'endExt')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 778, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCEnderObraEvento._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xLgr')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 784, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCEnderObraEvento._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nro')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 789, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCEnderObraEvento._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xCpl')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 794, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCEnderObraEvento._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xBairro')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 799, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCEnderObraEvento._Automaton = _BuildAutomaton_12()




TCServ._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'locPrest'), TCLocPrest, scope=TCServ, documentation='\n            Grupo de informações relativas ao local da prestação do serviço\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 809, 6)))

TCServ._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cServ'), TCCServ, scope=TCServ, documentation='\n            Grupo de informações relativas ao código do serviço prestado\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 816, 6)))

TCServ._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'comExt'), TCComExterior, scope=TCServ, documentation='Grupo de informações relativas à exportação/importação de serviço prestado', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 823, 6)))

TCServ._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lsadppu'), TCLocacaoSublocacao, scope=TCServ, documentation='Grupo de informações relativas a atividades de Locação, sublocação, arrendamento, direito de passagem ou permissão de uso, compartilhado ou não, de ferrovia, rodovia, postes, cabos, dutos e condutos de qualquer natureza', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 828, 6)))

TCServ._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'obra'), TCInfoObra, scope=TCServ, documentation='Grupo de informações do DPS relativas à serviço de obra', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 833, 6)))

TCServ._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'atvEvento'), TCAtvEvento, scope=TCServ, documentation='Grupo de informações do DPS relativas à Evento', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 838, 6)))

TCServ._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'explRod'), TCExploracaoRodoviaria, scope=TCServ, documentation='Grupo de informações relativas a pedágio', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 843, 6)))

TCServ._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'infoCompl'), TCInfoCompl, scope=TCServ, documentation='\n            Grupo de informações complementares disponível para todos os serviços prestados\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 848, 6)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 823, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 828, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 833, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 838, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 843, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 848, 6))
    counters.add(cc_5)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCServ._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'locPrest')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 809, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCServ._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cServ')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 816, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TCServ._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'comExt')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 823, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TCServ._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lsadppu')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 828, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TCServ._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'obra')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 833, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(TCServ._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'atvEvento')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 838, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(TCServ._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'explRod')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 843, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(TCServ._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'infoCompl')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 848, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCServ._Automaton = _BuildAutomaton_13()




TCLocPrest._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cLocPrestacao'), TSCodMunIBGE, scope=TCLocPrest, documentation='Código do município onde o serviço foi prestado (tabela do IBGE)', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 860, 6)))

TCLocPrest._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cPaisPrestacao'), TSCodPaisISO, scope=TCLocPrest, documentation='Código do país onde o serviço foi prestado (Tabela de Países ISO)', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 865, 6)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCLocPrest._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cLocPrestacao')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 860, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCLocPrest._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cPaisPrestacao')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 865, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCLocPrest._Automaton = _BuildAutomaton_14()




TCCServ._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cTribNac'), TSCodTribNac, scope=TCCServ, documentation='\n            Código de tributação nacional do ISSQN:\n            Regra de formação - 6 dígitos numéricos sendo: 2 para Item (LC 116/2003), 2 para Subitem (LC 116/2003) e 2 para Desdobro Nacional\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 875, 6)))

TCCServ._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cTribMun'), TCCodTribMun, scope=TCCServ, documentation='Código de tributação municipal do ISSQN', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 883, 6)))

TCCServ._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xDescServ'), TSDesc2000, scope=TCCServ, documentation='Descrição completa do serviço prestado', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 888, 6)))

TCCServ._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cNBS'), TSCodNBS, scope=TCCServ, documentation='Código NBS (Nomenclatura Brasileira de Serviços, Intangíveis e outras Operações que produzam Variações no Patrimônio) correspondente ao serviço prestado', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 893, 6)))

TCCServ._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cIntContrib'), TSCodigoInternoContribuinte, scope=TCCServ, documentation='\n            Código interno do contribuinte\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 898, 6)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 883, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 893, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 898, 6))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCCServ._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cTribNac')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 875, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCCServ._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cTribMun')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 883, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCCServ._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xDescServ')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 888, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TCCServ._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cNBS')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 893, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TCCServ._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cIntContrib')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 898, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCCServ._Automaton = _BuildAutomaton_15()




TCComExterior._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mdPrestacao'), TSModoPrestacao, scope=TCComExterior, documentation='\n            Modo de Prestação:\n            0 - Desconhecido (tipo não informado na nota de origem);\n            1 - Transfronteiriço;\n            2 - Consumo no Brasil;\n            3 - Movimento Temporário de Pessoas Físicas;\n            4 - Consumo no Exterior;\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 910, 6)))

TCComExterior._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vincPrest'), TSVincPrest, scope=TCComExterior, documentation='Vínculo entre as partes no negócio:\n            0 - Sem vínculo com o Tomador/Prestador\n            1 - Controlada;\n            2 - Controladora;\n            3 - Coligada;\n            4 - Matriz;\n            5 - Filial ou sucursal;\n            6 - Outro vínculo;\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 922, 6)))

TCComExterior._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tpMoeda'), TSCodMoeda, scope=TCComExterior, documentation='Identifica a moeda da transação comercial', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 935, 6)))

TCComExterior._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vServMoeda'), TSDec15V2, scope=TCComExterior, documentation='Valor do serviço prestado expresso em moeda estrangeira especificada em tpmoeda', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 940, 6)))

TCComExterior._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mecAFComexP'), TSMecAFComExPrest, scope=TCComExterior, documentation='\n            Mecanismo de apoio/fomento ao Comércio Exterior utilizado pelo prestador do serviço:\n            00 - Desconhecido (tipo não informado na nota de origem);\n            01 - Nenhum;\n            02 - ACC - Adiantamento sobre Contrato de Câmbio – Redução a Zero do IR e do IOF;\n            03 - ACE – Adiantamento sobre Cambiais Entregues - Redução a Zero do IR e do IOF;\n            04 - BNDES-Exim Pós-Embarque – Serviços;\n            05 - BNDES-Exim Pré-Embarque - Serviços;\n            06 - FGE - Fundo de Garantia à Exportação;\n            07 - PROEX - EQUALIZAÇÃO\n            08 - PROEX - Financiamento;\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 945, 6)))

TCComExterior._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mecAFComexT'), TSMecAFComExToma, scope=TCComExterior, documentation='\n            Mecanismo de apoio/fomento ao Comércio Exterior utilizado pelo tomador do serviço:\n            00 - Desconhecido (tipo não informado na nota de origem);\n            01 - Nenhum;\n            02 - Adm. Pública e Repr. Internacional;\n            03 - Alugueis e Arrend. Mercantil de maquinas, equip., embarc. e aeronaves;\n            04 - Arrendamento Mercantil de aeronave para empresa de transporte aéreo público;\n            05 - Comissão a agentes externos na exportação;\n            06 - Despesas de armazenagem, mov. e transporte de carga no exterior;\n            07 - Eventos FIFA (subsidiária);\n            08 - Eventos FIFA;\n            09 - Fretes, arrendamentos de embarcações ou aeronaves e outros;\n            10 - Material Aeronáutico;\n            11 - Promoção de Bens no Exterior;\n            12 - Promoção de Dest. Turísticos Brasileiros;\n            13 - Promoção do Brasil no Exterior;\n            14 - Promoção Serviços no Exterior;\n            15 - RECINE;\n            16 - RECOPA;\n            17 - Registro e Manutenção de marcas, patentes e cultivares;\n            18 - REICOMP;\n            19 - REIDI;\n            20 - REPENEC;\n            21 - REPES;\n            22 - RETAERO; \n            23 - RETID;\n            24 - Royalties, Assistência Técnica, Científica e Assemelhados;\n            25 - Serviços de avaliação da conformidade vinculados aos Acordos da OMC;\n            26 - ZPE;\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 961, 6)))

TCComExterior._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'movTempBens'), TSMovTempBens, scope=TCComExterior, documentation='\n            Vínculo da Operação à Movimentação Temporária de Bens:\n            0 - Desconhecido (tipo não informado na nota de origem);\n            1 - Não;\n            2 - Vinculada - Declaração de Importação;\n            3 - Vinculada - Declaração de Exportação;\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 995, 6)))

TCComExterior._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nDI'), TSNumDocImport, scope=TCComExterior, documentation='Número da Declaração de Importação (DI/DSI/DA/DRI-E) averbado', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1006, 6)))

TCComExterior._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nRE'), TSNumRegExport, scope=TCComExterior, documentation='Número do Registro de Exportação (RE) averbado', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1011, 6)))

TCComExterior._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mdic'), TSEnvMDIC, scope=TCComExterior, documentation='\n            Compartilhar as informações da NFS-e gerada a partir desta DPS com a Secretaria de Comércio Exterior:\n            0 - Não enviar para o MDIC;\n            1 - Enviar para o MDIC;\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1016, 6)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1006, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1011, 6))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCComExterior._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mdPrestacao')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 910, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCComExterior._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vincPrest')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 922, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCComExterior._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tpMoeda')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 935, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCComExterior._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vServMoeda')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 940, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCComExterior._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mecAFComexP')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 945, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCComExterior._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mecAFComexT')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 961, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCComExterior._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'movTempBens')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 995, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCComExterior._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nDI')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1006, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCComExterior._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nRE')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1011, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCComExterior._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mdic')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1016, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCComExterior._Automaton = _BuildAutomaton_16()




TCExploracaoRodoviaria._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'categVeic'), TSCategVeic, scope=TCExploracaoRodoviaria, documentation='\n            Categorias de veículos para cobrança:\n            00 - Categoria de veículos (tipo não informado na nota de origem)\n            01 - Automóvel, caminhonete e furgão;\n            02 - Caminhão leve, ônibus, caminhão trator e furgão;\n            03 - Automóvel e caminhonete com semireboque;\n            04 - Caminhão, caminhão-trator, caminhão-trator com semi-reboque e ônibus;\n            05 - Automóvel e caminhonete com reboque;\n            06 - Caminhão com reboque;\n            07 - Caminhão trator com semi-reboque;\n            08 - Motocicletas, motonetas e bicicletas motorizadas;\n            09 - Veículo especial;\n            10 - Veículo Isento;\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1030, 6)))

TCExploracaoRodoviaria._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nEixos'), TSNumEixos, scope=TCExploracaoRodoviaria, documentation='Número de eixos para fins de cobrança', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1048, 6)))

TCExploracaoRodoviaria._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rodagem'), TSRodagem, scope=TCExploracaoRodoviaria, documentation='Tipo de rodagem', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1053, 6)))

TCExploracaoRodoviaria._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'sentido'), TSSentido, scope=TCExploracaoRodoviaria, documentation='Placa do veículo', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1058, 6)))

TCExploracaoRodoviaria._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'placa'), TSPlaca, scope=TCExploracaoRodoviaria, documentation='Placa do veículo', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1063, 6)))

TCExploracaoRodoviaria._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'codAcessoPed'), TSCodAcessoPed, scope=TCExploracaoRodoviaria, documentation='Código de acesso gerado automaticamente pelo sistema emissor da concessionária.', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1068, 6)))

TCExploracaoRodoviaria._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'codContrato'), TSCodContrato, scope=TCExploracaoRodoviaria, documentation='Código de contrato gerado automaticamente pelo sistema nacional no cadastro da concessionária.', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1073, 6)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCExploracaoRodoviaria._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'categVeic')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1030, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCExploracaoRodoviaria._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nEixos')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1048, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCExploracaoRodoviaria._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'rodagem')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1053, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCExploracaoRodoviaria._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'sentido')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1058, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCExploracaoRodoviaria._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'placa')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1063, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCExploracaoRodoviaria._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'codAcessoPed')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1068, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCExploracaoRodoviaria._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'codContrato')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1073, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCExploracaoRodoviaria._Automaton = _BuildAutomaton_17()




TCLocacaoSublocacao._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'categ'), TSCategoriaServico, scope=TCLocacaoSublocacao, documentation='Categoria do serviço', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1083, 6)))

TCLocacaoSublocacao._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'objeto'), TCObjetoLocacao, scope=TCLocacaoSublocacao, documentation='Tipo de objetos da locação, sublocação, arrendamento, direito de passagem ou permissão de uso', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1088, 6)))

TCLocacaoSublocacao._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extensao'), TSExtensaoTotal, scope=TCLocacaoSublocacao, documentation='Extensão total da ferrovia, rodovia, cabos, dutos ou condutos', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1093, 6)))

TCLocacaoSublocacao._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nPostes'), TSNumeroPostes, scope=TCLocacaoSublocacao, documentation='Número total de postes', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1098, 6)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCLocacaoSublocacao._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'categ')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1083, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCLocacaoSublocacao._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'objeto')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1088, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCLocacaoSublocacao._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensao')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1093, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCLocacaoSublocacao._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nPostes')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1098, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCLocacaoSublocacao._Automaton = _BuildAutomaton_18()




TCAtvEvento._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xNome'), TSDesc255, scope=TCAtvEvento, documentation='Descrição do evento Artístico, Cultural, Esportivo, etc', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1108, 6)))

TCAtvEvento._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dtIni'), TSData, scope=TCAtvEvento, documentation='Data de início da atividade de evento. Ano, Mês e Dia (AAAA-MM-DD)', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1113, 6)))

TCAtvEvento._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dtFim'), TSData, scope=TCAtvEvento, documentation='Data de fim da atividade de evento. Ano, Mês e Dia (AAAA-MM-DD)', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1118, 6)))

TCAtvEvento._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'idAtvEvt'), TSIdeEvento, scope=TCAtvEvento, documentation='Identificação da Atividade de Evento (código identificador de evento determinado pela Administração Tributária Municipal)', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1124, 8)))

TCAtvEvento._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'end'), TCEnderecoSimples, scope=TCAtvEvento, documentation='Grupo de informações relativas ao endereço da atividade, evento ou local do serviço prestado', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1129, 8)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCAtvEvento._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xNome')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1108, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCAtvEvento._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dtIni')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1113, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCAtvEvento._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dtFim')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1118, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCAtvEvento._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'idAtvEvt')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1124, 8))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCAtvEvento._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'end')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1129, 8))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCAtvEvento._Automaton = _BuildAutomaton_19()




TCInfoObra._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inscImobFisc'), TSInscImobFisc, scope=TCInfoObra, documentation='Inscrição imobiliária fiscal (código fornecido pela Prefeitura Municipal para a identificação da obra ou para fins de recolhimento do IPTU)', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1140, 6)))

TCInfoObra._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cObra'), TSCodObra, scope=TCInfoObra, documentation='Número de identificação da obra.\n              Cadastro Nacional de Obras (CNO) ou Cadastro Específico do INSS (CEI).\n            ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1146, 8)))

TCInfoObra._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'end'), TCEnderObraEvento, scope=TCInfoObra, documentation='Grupo de informações do endereço da obra do serviço prestado\n            ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1153, 8)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1140, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfoObra._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inscImobFisc')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1140, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCInfoObra._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cObra')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1146, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCInfoObra._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'end')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1153, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCInfoObra._Automaton = _BuildAutomaton_20()




TCInfoCompl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'idDocTec'), TSDRT, scope=TCInfoCompl, documentation='\n            Identificador de Documento de Responsabilidade Técnica: ART, RRT, DRT, Outros.\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1165, 6)))

TCInfoCompl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'docRef'), TSDesc255, scope=TCInfoCompl, documentation='\n            Chave da nota, número identificador da nota, número do contrato ou outro identificador de documento emitido pelo prestador de serviços, que subsidia a emissão dessa nota pelo tomador do serviço ou intermediário (preenchimento obrigatório caso a nota esteja sendo emitida pelo Tomador ou intermediário do serviço).\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1172, 6)))

TCInfoCompl._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xInfComp'), TSDescInfCompl, scope=TCInfoCompl, documentation='\n            Informações complementares\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1179, 6)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1165, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1172, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1179, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TCInfoCompl._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'idDocTec')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1165, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TCInfoCompl._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'docRef')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1172, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TCInfoCompl._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xInfComp')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1179, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TCInfoCompl._Automaton = _BuildAutomaton_21()




TCInfoValores._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vServPrest'), TCVServPrest, scope=TCInfoValores, documentation='\n            Grupo de informações relativas aos valores do serviço prestado\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1191, 6)))

TCInfoValores._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vDescCondIncond'), TCVDescCondIncond, scope=TCInfoValores, documentation='\n            Grupo de informações relativas aos descontos condicionados e incondicionados\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1198, 6)))

TCInfoValores._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vDedRed'), TCInfoDedRed, scope=TCInfoValores, documentation='\n            Grupo de informações relativas ao valores para dedução/redução do valor da base de cálculo (valor do serviço)\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1205, 6)))

TCInfoValores._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'trib'), TCInfoTributacao, scope=TCInfoValores, documentation='\n            Grupo de informações relacionados aos tributos relacionados ao serviço prestado\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1212, 6)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1198, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1205, 6))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfoValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vServPrest')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1191, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfoValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vDescCondIncond')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1198, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfoValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vDedRed')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1205, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCInfoValores._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'trib')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1212, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCInfoValores._Automaton = _BuildAutomaton_22()




TCInfoTributacao._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tribMun'), TCTribMunicipal, scope=TCInfoTributacao, documentation='\n            Grupo de informações relacionados ao Imposto Sobre Serviços de Qualquer Natureza - ISSQN\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1224, 6)))

TCInfoTributacao._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tribFed'), TCTribFederal, scope=TCInfoTributacao, documentation='\n            Grupo de informações de outros tributos relacionados ao serviço prestado\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1231, 6)))

TCInfoTributacao._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'totTrib'), TCTribTotal, scope=TCInfoTributacao, documentation='\n            Grupo de informações para totais aproximados dos tributos relacionados ao serviço prestado\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1238, 6)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1231, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfoTributacao._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tribMun')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1224, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfoTributacao._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tribFed')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1231, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCInfoTributacao._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'totTrib')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1238, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCInfoTributacao._Automaton = _BuildAutomaton_23()




TCVServPrest._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vReceb'), TSDec15V2, scope=TCVServPrest, documentation='Valor monetário recebido pelo intermediário do serviço (R$)', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1250, 6)))

TCVServPrest._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vServ'), TSDec15V2, scope=TCVServPrest, documentation='Valor dos serviços em R$', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1255, 6)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1250, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCVServPrest._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vReceb')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1250, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCVServPrest._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vServ')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1255, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCVServPrest._Automaton = _BuildAutomaton_24()




TCVDescCondIncond._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vDescIncond'), TSDec15V2, scope=TCVDescCondIncond, documentation='Valor monetário do desconto incondicionado (R$)', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1265, 6)))

TCVDescCondIncond._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vDescCond'), TSDec15V2, scope=TCVDescCondIncond, documentation='Valor monetário do desconto condicionado (R$)', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1270, 6)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1265, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1270, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TCVDescCondIncond._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vDescIncond')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1265, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TCVDescCondIncond._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vDescCond')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1270, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TCVDescCondIncond._Automaton = _BuildAutomaton_25()




TCInfoDedRed._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pDR'), TSDec3V2, scope=TCInfoDedRed, documentation='\n              Valor percentual padrão para dedução/redução do valor do serviço\n            ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1281, 8)))

TCInfoDedRed._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vDR'), TSDec15V2, scope=TCInfoDedRed, documentation='\n              Valor monetário padrão para dedução/redução do valor do serviço\n            ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1288, 8)))

TCInfoDedRed._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'documentos'), TCListaDocDedRed, scope=TCInfoDedRed, documentation='\n              Grupo de informações de documento utilizado para Dedução/Redução do valor do serviço\n            ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1295, 8)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCInfoDedRed._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'pDR')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1281, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCInfoDedRed._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vDR')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1288, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCInfoDedRed._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'documentos')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1295, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCInfoDedRed._Automaton = _BuildAutomaton_26()




TCListaDocDedRed._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'docDedRed'), TCDocDedRed, scope=TCListaDocDedRed, documentation='\n            Grupo de informações de documento utilizado para Dedução/Redução do valor do serviço\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1308, 6)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=1000, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1308, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TCListaDocDedRed._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'docDedRed')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1308, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCListaDocDedRed._Automaton = _BuildAutomaton_27()




TCDocDedRed._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'chNFSe'), TSChaveNFSe, scope=TCDocDedRed, documentation='Chave de Acesso da NFS-e (Padrão Nacional)', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1321, 8)))

TCDocDedRed._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'chNFe'), TSChaveNFe, scope=TCDocDedRed, documentation='Chave de Acesso da NF-e', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1326, 8)))

TCDocDedRed._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NFSeMun'), TCDocOutNFSe, scope=TCDocDedRed, documentation='Grupo de informações de Outras NFS-e (Padrão anterior de NFS-e)', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1331, 8)))

TCDocDedRed._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NFNFS'), TCDocNFNFS, scope=TCDocDedRed, documentation='Grupo de informações de NF ou NFS (Modelo não eletrônico)', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1336, 8)))

TCDocDedRed._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nDocFisc'), TSDesc255, scope=TCDocDedRed, documentation='Número de documento fiscal', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1341, 8)))

TCDocDedRed._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nDoc'), TSDesc255, scope=TCDocDedRed, documentation='Número de documento não fiscal', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1346, 8)))

TCDocDedRed._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tpDedRed'), TSIdeDedRed, scope=TCDocDedRed, documentation='\n            Identificação da Dedução/Redução:\n            1 – Alimentação e bebidas/frigobar;\n            2 – Materiais;\n            3 – Produção externa;\n            4 – Reembolso de despesas;\n            5 – Repasse consorciado;\n            6 – Repasse plano de saúde;\n            7 – Serviços;\n            8 – Subempreitada de mão de obra;\n            99 – Outras deduções;\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1352, 6)))

TCDocDedRed._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xDescOutDed'), TSDescOutDedRed, scope=TCDocDedRed, documentation='Descrição da Dedução/Redução quando a opção é "99 – Outras Deduções"', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1368, 6)))

TCDocDedRed._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dtEmiDoc'), pyxb.binding.datatypes.date, scope=TCDocDedRed, documentation='Data da emissão do documento dedutível. Ano, mês e dia (AAAA-MM-DD)', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1373, 6)))

TCDocDedRed._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vDedutivelRedutivel'), TSDec15V2, scope=TCDocDedRed, documentation='\n            Valor monetário total dedutível/redutível no documento informado (R$).\n            Este é o valor total no documento informado que é passível de dedução/redução.\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1378, 6)))

TCDocDedRed._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vDeducaoReducao'), TSDec15V2, scope=TCDocDedRed, documentation='\n            Valor monetário utilizado para dedução/redução do valor do serviço da NFS-e que está sendo emitida (R$).\n            Deve ser menor ou igual ao valor deduzível/redutível (vDedutivelRedutivel).\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1386, 6)))

TCDocDedRed._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'fornec'), TCInfoPessoa, scope=TCDocDedRed, documentation='Grupo de informações do Fornecedor em Deduções de Serviços', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1394, 6)))

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1368, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1394, 6))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCDocDedRed._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'chNFSe')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1321, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCDocDedRed._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'chNFe')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1326, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCDocDedRed._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NFSeMun')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1331, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCDocDedRed._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NFNFS')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1336, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCDocDedRed._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nDocFisc')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1341, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCDocDedRed._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nDoc')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1346, 8))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCDocDedRed._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tpDedRed')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1352, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCDocDedRed._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xDescOutDed')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1368, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCDocDedRed._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dtEmiDoc')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1373, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCDocDedRed._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vDedutivelRedutivel')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1378, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCDocDedRed._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vDeducaoReducao')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1386, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TCDocDedRed._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'fornec')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1394, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCDocDedRed._Automaton = _BuildAutomaton_28()




TCDocOutNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cMunNFSeMun'), TSCodMunIBGE, scope=TCDocOutNFSe, documentation='Código Município emissor da nota eletrônica municipal (Tabela do IBGE)', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1404, 6)))

TCDocOutNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nNFSeMun'), TSNum15Dig, scope=TCDocOutNFSe, documentation='Número da nota eletrônica municipal', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1409, 6)))

TCDocOutNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cVerifNFSeMun'), TSCodVerificacao, scope=TCDocOutNFSe, documentation='Código de Verificação da nota eletrônica municipal', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1414, 6)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCDocOutNFSe._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cMunNFSeMun')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1404, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCDocOutNFSe._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nNFSeMun')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1409, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCDocOutNFSe._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cVerifNFSeMun')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1414, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCDocOutNFSe._Automaton = _BuildAutomaton_29()




TCDocNFNFS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nNFS'), TSNum7Dig, scope=TCDocNFNFS, documentation='Número da Nota Fiscal NF ou NFS', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1424, 6)))

TCDocNFNFS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'modNFS'), TSNum15Dig, scope=TCDocNFNFS, documentation='Modelo da Nota Fiscal NF ou NFS', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1429, 6)))

TCDocNFNFS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'serieNFS'), TSSerieNFNFS, scope=TCDocNFNFS, documentation='Série Nota Fiscal NF ou NFS', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1434, 6)))

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCDocNFNFS._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nNFS')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1424, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCDocNFNFS._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'modNFS')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1429, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCDocNFNFS._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'serieNFS')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1434, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCDocNFNFS._Automaton = _BuildAutomaton_30()




TCTribMunicipal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tribISSQN'), TSTribISSQN, scope=TCTribMunicipal, documentation='\n            Tributação do ISSQN sobre o serviço prestado:\n            1 - Operação tributável;\n            2 - Imunidade;\n            3 - Exportação de serviço;\n            4 - Não Incidência;\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1444, 6)))

TCTribMunicipal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cPaisResult'), TSCodPaisISO, scope=TCTribMunicipal, documentation='\n            Código do país onde se verficou o resultado da prestação do serviço para o caso de Exportação de Serviço.(Tabela de Países ISO)\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1455, 6)))

TCTribMunicipal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tpImunidade'), TSTipoImunidadeISSQN, scope=TCTribMunicipal, documentation='\n            Identificação da Imunidade do ISSQN – somente para o caso de Imunidade.\n            Tipos de Imunidades:            \n            0 - Imunidade (tipo não informado na nota de origem);\n            1 - Patrimônio, renda ou serviços, uns dos outros (CF88, Art 150, VI, a);\n            2 - Templos de qualquer culto (CF88, Art 150, VI, b);\n            3 - Patrimônio, renda ou serviços dos partidos políticos, inclusive suas fundações, das entidades sindicais dos trabalhadores, das instituições de educação e de assistência social, sem fins lucrativos, atendidos os requisitos da lei (CF88, Art 150, VI, c);\n            4 - Livros, jornais, periódicos e o papel destinado a sua impressão (CF88, Art 150, VI, d);\n            5 - Fonogramas e videofonogramas musicais produzidos no Brasil contendo obras musicais ou literomusicais de autores brasileiros e/ou obras em geral interpretadas por artistas brasileiros bem como os suportes materiais ou arquivos digitais que os contenham, salvo na etapa de replicação industrial de mídias ópticas de leitura a laser.   (CF88, Art 150, VI, e);\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1462, 6)))

TCTribMunicipal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'exigSusp'), TCExigSuspensa, scope=TCTribMunicipal, documentation='\n            Informações para a suspensão da Exigibilidade do ISSQN\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1476, 6)))

TCTribMunicipal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BM'), TCBeneficioMunicipal, scope=TCTribMunicipal, documentation='\n            Tributação do ISSQN sobre o serviço prestado:\n            1 - Operação tributável;\n            2 - Exportação de serviço;\n            3 - Não Incidência;\n            4 - Imunidade;\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1483, 6)))

TCTribMunicipal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tpRetISSQN'), TSTipoRetISSQN, scope=TCTribMunicipal, documentation='\n            Tipo de retencao do ISSQN:\n            1 - Não Retido;\n            2 - Retido pelo Tomador;\n            3 - Retido pelo Intermediario;\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1494, 6)))

TCTribMunicipal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pAliq'), TSDec1V2, scope=TCTribMunicipal, documentation='\n            Valor da alíquota (%) do serviço prestado relativo ao município sujeito ativo (município de incidência) do ISSQN.\n            Se o município de incidência pertence ao Sistema Nacional NFS-e a alíquota estará parametrizada e, portanto, será fornecida pelo sistema.\n            Se o município de incidência não pertence ao Sistema Nacional NFS-e a alíquota não estará parametrizada e, por isso, deverá ser fornecida pelo emitente.\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1504, 6)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1455, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1462, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1476, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1483, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1504, 6))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCTribMunicipal._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tribISSQN')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1444, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCTribMunicipal._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cPaisResult')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1455, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCTribMunicipal._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tpImunidade')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1462, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCTribMunicipal._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'exigSusp')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1476, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCTribMunicipal._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BM')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1483, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCTribMunicipal._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tpRetISSQN')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1494, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(TCTribMunicipal._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'pAliq')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1504, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCTribMunicipal._Automaton = _BuildAutomaton_31()




TCBeneficioMunicipal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nBM'), TSNumBeneficioMunicipal, scope=TCBeneficioMunicipal, documentation='\n            Identificador do benefício parametrizado pelo município.\n\n            Trata-se de um identificador único que foi gerado pelo Sistema Nacional no momento em que o município de incidência do ISSQN incluiu o benefício no sistema.\n            \n            Critério de formação do número de identificação de parâmetros municipais:\n            7 dígitos - posição 1 a 7: número identificador do Município, conforme código IBGE;\n            2 dígitos - posições 8 e 9 : número identificador do tipo de parametrização (01-legislação, 02-regimes especiais, 03-retenções, 04-outros benefícios);\n            5 dígitos - posição 10 a 14 : número sequencial definido pelo sistema quando do registro específico do parâmetro dentro do tipo de parametrização no sistema;\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1518, 6)))

TCBeneficioMunicipal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vRedBCBM'), TSDec15V2, scope=TCBeneficioMunicipal, documentation='\n              Valor monetário informado pelo emitente para redução da base de cálculo (BC) do ISSQN devido a um Benefício Municipal (BM).\n            ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1533, 8)))

TCBeneficioMunicipal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pRedBCBM'), TSDec3V2, scope=TCBeneficioMunicipal, documentation='\n              Valor percentual informado pelo emitente para redução da base de cálculo (BC) do ISSQN devido a um Benefício Municipal (BM).\n            ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1540, 8)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1533, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1540, 8))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCBeneficioMunicipal._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nBM')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1518, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TCBeneficioMunicipal._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vRedBCBM')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1533, 8))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TCBeneficioMunicipal._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'pRedBCBM')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1540, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCBeneficioMunicipal._Automaton = _BuildAutomaton_32()




TCExigSuspensa._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tpSusp'), TSOpExigSuspensa, scope=TCExigSuspensa, documentation='\n            Opção para Exigibilidade Suspensa:\n            1 - Exigibilidade Suspensa por Decisão Judicial;\n            2 - Exigibilidade Suspensa por Processo Administrativo;\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1553, 6)))

TCExigSuspensa._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nProcesso'), TSNumProcExigSuspensa, scope=TCExigSuspensa, documentation='\n            Número do processo judicial ou administrativo de suspensão da exigibilidade\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1562, 6)))

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCExigSuspensa._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tpSusp')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1553, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCExigSuspensa._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nProcesso')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1562, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCExigSuspensa._Automaton = _BuildAutomaton_33()




TCTribFederal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'piscofins'), TCTribOutrosPisCofins, scope=TCTribFederal, documentation='\n            Grupo de informações dos tributos PIS/COFINS\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1574, 6)))

TCTribFederal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vRetCP'), TSDec15V2, scope=TCTribFederal, documentation='\n            Valor monetário do CP(R$).\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1581, 6)))

TCTribFederal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vRetIRRF'), TSDec15V2, scope=TCTribFederal, documentation='\n            Valor monetário do IRRF (R$).\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1588, 6)))

TCTribFederal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vRetCSLL'), TSDec15V2, scope=TCTribFederal, documentation='\n            Valor monetário do CSLL (R$).\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1595, 6)))

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1574, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1581, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1588, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1595, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TCTribFederal._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'piscofins')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1574, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TCTribFederal._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vRetCP')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1581, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TCTribFederal._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vRetIRRF')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1588, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(TCTribFederal._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vRetCSLL')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1595, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TCTribFederal._Automaton = _BuildAutomaton_34()




TCTribOutrosPisCofins._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CST'), TSTipoCST, scope=TCTribOutrosPisCofins, documentation='\n            Código de Situação Tributária do PIS/COFINS (CST):\n            00 - Nenhum;      \n            01 - Operação Tributável com Alíquota Básica;\n            02 - Operação Tributável com Alíquota Diferenciada;\n            03 - Operação Tributável com Alíquota por Unidade de Medida de Produto;\n            04 - Operação Tributável monofásica - Revenda a Alíquota Zero;\n            05 - Operação Tributável por Substituição Tributária;\n            06 - Operação Tributável a Alíquota Zero;\n            07 - Operação Tributável da Contribuição;\n            08 - Operação sem Incidência da Contribuição;\n            09 - Operação com Suspensão da Contribuição;\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1607, 6)))

TCTribOutrosPisCofins._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vBCPisCofins'), TSDec15V2, scope=TCTribOutrosPisCofins, documentation='\n            Valor da Base de Cálculo do PIS/COFINS (R$).\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1624, 6)))

TCTribOutrosPisCofins._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pAliqPis'), TSDec2V2, scope=TCTribOutrosPisCofins, documentation='\n            Valor da Alíquota do PIS (%).\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1631, 6)))

TCTribOutrosPisCofins._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pAliqCofins'), TSDec2V2, scope=TCTribOutrosPisCofins, documentation='\n            Valor da Alíquota da COFINS (%).\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1638, 6)))

TCTribOutrosPisCofins._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vPis'), TSDec15V2, scope=TCTribOutrosPisCofins, documentation='\n            Valor monetário do PIS (R$).\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1645, 6)))

TCTribOutrosPisCofins._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vCofins'), TSDec15V2, scope=TCTribOutrosPisCofins, documentation='\n            Valor monetário do COFINS (R$).\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1652, 6)))

TCTribOutrosPisCofins._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tpRetPisCofins'), TSTipoRetPISCofins, scope=TCTribOutrosPisCofins, documentation='\n            Tipo de retencao do Pis/Cofins:\n            1 - Retido;\n            2 - Não Retido;\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1659, 6)))

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1624, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1631, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1638, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1645, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1652, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1659, 6))
    counters.add(cc_5)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCTribOutrosPisCofins._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CST')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1607, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TCTribOutrosPisCofins._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vBCPisCofins')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1624, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(TCTribOutrosPisCofins._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'pAliqPis')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1631, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(TCTribOutrosPisCofins._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'pAliqCofins')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1638, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(TCTribOutrosPisCofins._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vPis')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1645, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(TCTribOutrosPisCofins._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vCofins')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1652, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(TCTribOutrosPisCofins._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tpRetPisCofins')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1659, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCTribOutrosPisCofins._Automaton = _BuildAutomaton_35()




TCTribTotal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vTotTrib'), TCTribTotalMonet, scope=TCTribTotal, documentation='\n              Valor monetário total aproximado dos tributos, em conformidade com o artigo 1o da Lei no 12.741/2012\n            ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1674, 8)))

TCTribTotal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pTotTrib'), TCTribTotalPercent, scope=TCTribTotal, documentation='\n              Valor percentual total aproximado dos tributos, em conformidade com o artigo 1o da Lei no 12.741/2012\n            ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1681, 8)))

TCTribTotal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'indTotTrib'), TSTipoIndTotTrib, scope=TCTribTotal, documentation='\n              Indicador de informação de valor total de tributos. Possui valor fixo igual a zero (indTotTrib=0).\n              Não informar nenhum valor estimado para os Tributos (Decreto 8.264/2014).\n              0 - Não;\n            ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1688, 8)))

TCTribTotal._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pTotTribSN'), TSDec2V2, scope=TCTribTotal, documentation='\n              Valor percentual aproximado do total dos tributos da alíquota do Simples Nacional (%)\n            ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1697, 8)))

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCTribTotal._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vTotTrib')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1674, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCTribTotal._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'pTotTrib')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1681, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCTribTotal._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'indTotTrib')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1688, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCTribTotal._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'pTotTribSN')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1697, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCTribTotal._Automaton = _BuildAutomaton_36()




TCTribTotalMonet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vTotTribFed'), TSDec15V2, scope=TCTribTotalMonet, documentation='\n            Valor monetário total aproximado dos tributos federais (R$).\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1710, 6)))

TCTribTotalMonet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vTotTribEst'), TSDec15V2, scope=TCTribTotalMonet, documentation='\n            Valor monetário total aproximado dos tributos estaduais (R$).\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1717, 6)))

TCTribTotalMonet._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'vTotTribMun'), TSDec15V2, scope=TCTribTotalMonet, documentation='\n            Valor monetário total aproximado dos tributos municipais (R$).\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1724, 6)))

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCTribTotalMonet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vTotTribFed')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1710, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCTribTotalMonet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vTotTribEst')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1717, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCTribTotalMonet._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'vTotTribMun')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1724, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCTribTotalMonet._Automaton = _BuildAutomaton_37()




TCTribTotalPercent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pTotTribFed'), TSDec3V2, scope=TCTribTotalPercent, documentation='\n            Valor percentual total aproximado dos tributos federais (%).\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1736, 6)))

TCTribTotalPercent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pTotTribEst'), TSDec3V2, scope=TCTribTotalPercent, documentation='\n            Valor percentual total aproximado dos tributos estaduais (%).\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1743, 6)))

TCTribTotalPercent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pTotTribMun'), TSDec3V2, scope=TCTribTotalPercent, documentation='\n            Valor percentual total aproximado dos tributos municipais (%).\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1750, 6)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCTribTotalPercent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'pTotTribFed')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1736, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCTribTotalPercent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'pTotTribEst')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1743, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCTribTotalPercent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'pTotTribMun')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 1750, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCTribTotalPercent._Automaton = _BuildAutomaton_38()




TE101101._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xDesc'), STD_ANON, scope=TE101101, documentation='\n            Descrição do Evento: Descrição do evento: "Cancelamento de NFS-e".\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 211, 6)))

TE101101._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cMotivo'), TSCodJustCanc, scope=TE101101, documentation='Código de justificativa de cancelamento', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 224, 6)))

TE101101._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xMotivo'), TSMotivo, scope=TE101101, documentation='Descrição para explicitar o motivo indicado neste evento', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 229, 6)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TE101101._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xDesc')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 211, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TE101101._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cMotivo')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 224, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TE101101._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xMotivo')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 229, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TE101101._Automaton = _BuildAutomaton_39()




TE105102._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xDesc'), STD_ANON_, scope=TE105102, documentation='\n            Descrição do Evento: Descrição do evento: "Cancelamento de NFS-e por Substituição".\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 240, 6)))

TE105102._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cMotivo'), TSCodJustSubst, scope=TE105102, documentation='Código de justificativa de cancelamento substituição', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 253, 6)))

TE105102._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xMotivo'), TSMotivo, scope=TE105102, documentation='Descrição para explicitar o motivo indicado neste evento', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 258, 6)))

TE105102._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'chSubstituta'), TSChaveNFSe, scope=TE105102, documentation='Chave de Acesso da NFS-e substituta.', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 263, 6)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 258, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TE105102._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xDesc')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 240, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TE105102._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cMotivo')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 253, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TE105102._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xMotivo')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 258, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TE105102._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'chSubstituta')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 263, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TE105102._Automaton = _BuildAutomaton_40()




TE101103._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xDesc'), STD_ANON_2, scope=TE101103, documentation='\n            Descrição do evento: "Solicitação de Análise Fiscal para Cancelamento de NFS-e"\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 274, 6)))

TE101103._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cMotivo'), TSCodJustAnaliseFiscalCanc, scope=TE101103, documentation='Código do motivo da solicitação de análise fiscal para cancelamento de NFS-e:', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 287, 6)))

TE101103._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xMotivo'), TSMotivo, scope=TE101103, documentation='Descrição para explicitar o motivo indicado neste evento', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 292, 6)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TE101103._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xDesc')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 274, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TE101103._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cMotivo')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 287, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TE101103._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xMotivo')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 292, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TE101103._Automaton = _BuildAutomaton_41()




TE105104._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xDesc'), STD_ANON_3, scope=TE105104, documentation='\n            Descrição do evento: "Cancelamento de NFS-e Deferido por Análise Fiscal"\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 303, 6)))

TE105104._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CPFAgTrib'), TSCPF, scope=TE105104, documentation='\n            CPF do agente da administração tributária municipal que efetuou o deferimento da  solicitação de análise fiscal para cancelamento de NFS-e.\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 316, 6)))

TE105104._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nProcAdm'), TSNumProcAdmAnaliseFiscalCanc, scope=TE105104, documentation='\n            Número do processo administrativo municipal vinculado à solicitação de análise fiscal para cancelamento de NFS-e.\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 323, 6)))

TE105104._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cMotivo'), TSCodJustAnaliseFiscalCancDef, scope=TE105104, documentation='\n            Resposta da solicitação de análise fiscal para cancelamento de NFS-e:\n            1 - Cancelamento de NFS-e Deferido.\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 330, 6)))

TE105104._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xMotivo'), TSMotivo, scope=TE105104, documentation='\n            Descrição para explicitar o motivo indicado neste evento\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 338, 6)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 323, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TE105104._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xDesc')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 303, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TE105104._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CPFAgTrib')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 316, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TE105104._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nProcAdm')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 323, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TE105104._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cMotivo')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 330, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TE105104._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xMotivo')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 338, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TE105104._Automaton = _BuildAutomaton_42()




TE105105._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xDesc'), STD_ANON_4, scope=TE105105, documentation='\n            Descrição do evento: "Cancelamento de NFS-e Indeferido por Análise Fiscal".\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 351, 6)))

TE105105._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CPFAgTrib'), TSCPF, scope=TE105105, documentation='\n            CPF do agente da administração tributária municipal que efetuou o indeferimento da solicitação de análise fiscal para cancelamento de NFS-e.\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 364, 6)))

TE105105._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nProcAdm'), TSNumProcAdmAnaliseFiscalCanc, scope=TE105105, documentation='\n            Número do processo administrativo municipal vinculado à solicitação de análise fiscal para cancelamento de NFS-e.\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 371, 6)))

TE105105._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cMotivo'), TSCodJustAnaliseFiscalCancIndef, scope=TE105105, documentation='\n            Resposta da solicitação de análise fiscal para cancelamento de NFS-e:\n            1 - Cancelamento de NFS-e Indeferido;\n            2 - Cancelamento de NFS-e Indeferido Sem Análise de Mérito.\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 378, 6)))

TE105105._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xMotivo'), TSMotivo, scope=TE105105, documentation='Descrição para explicitar o motivo indicado neste evento', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 387, 6)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 371, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TE105105._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xDesc')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 351, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TE105105._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CPFAgTrib')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 364, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TE105105._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nProcAdm')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 371, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TE105105._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cMotivo')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 378, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TE105105._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xMotivo')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 387, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TE105105._Automaton = _BuildAutomaton_43()




TE202201._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xDesc'), STD_ANON_5, scope=TE202201, documentation='\n            Descrição do evento: "Confirmação do Prestador".\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 398, 6)))

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TE202201._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xDesc')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 398, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TE202201._Automaton = _BuildAutomaton_44()




TE203202._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xDesc'), STD_ANON_6, scope=TE203202, documentation='\n            Descrição do evento: "Confirmação do Tomador".\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 417, 6)))

def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TE203202._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xDesc')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 417, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TE203202._Automaton = _BuildAutomaton_45()




TE204203._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xDesc'), STD_ANON_7, scope=TE204203, documentation='\n            Descrição do evento: "Confirmação do Intermediário".\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 436, 6)))

def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TE204203._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xDesc')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 436, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TE204203._Automaton = _BuildAutomaton_46()




TE205204._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xDesc'), STD_ANON_8, scope=TE205204, documentation='\n            Descrição do evento: "Confirmação Tácita".\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 455, 6)))

def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TE205204._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xDesc')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 455, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TE205204._Automaton = _BuildAutomaton_47()




TE202205._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xDesc'), STD_ANON_9, scope=TE202205, documentation='\n            Descrição do evento: "Rejeição do Prestador".\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 474, 6)))

TE202205._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'infRej'), TCInfoEventoRejeicao, scope=TE202205, documentation='\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 487, 6)))

def _BuildAutomaton_48 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TE202205._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xDesc')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 474, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TE202205._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'infRej')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 487, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TE202205._Automaton = _BuildAutomaton_48()




TE203206._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xDesc'), STD_ANON_10, scope=TE203206, documentation='\n            Descrição do evento: "Rejeição do Tomador".\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 499, 6)))

TE203206._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'infRej'), TCInfoEventoRejeicao, scope=TE203206, documentation='\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 512, 6)))

def _BuildAutomaton_49 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_49
    del _BuildAutomaton_49
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TE203206._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xDesc')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 499, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TE203206._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'infRej')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 512, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TE203206._Automaton = _BuildAutomaton_49()




TE204207._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xDesc'), STD_ANON_11, scope=TE204207, documentation='\n            Descrição do evento: "Rejeição do Intermediário".\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 524, 6)))

TE204207._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'infRej'), TCInfoEventoRejeicao, scope=TE204207, documentation='\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 537, 6)))

def _BuildAutomaton_50 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_50
    del _BuildAutomaton_50
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TE204207._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xDesc')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 524, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TE204207._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'infRej')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 537, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TE204207._Automaton = _BuildAutomaton_50()




TE205208._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xDesc'), STD_ANON_12, scope=TE205208, documentation='\n            Descrição do evento: "Anulação da Rejeição".\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 549, 6)))

TE205208._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'infAnRej'), TCInfoEventoAnulacaoRejeicao, scope=TE205208, documentation='\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 562, 6)))

def _BuildAutomaton_51 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_51
    del _BuildAutomaton_51
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TE205208._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xDesc')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 549, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TE205208._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'infAnRej')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 562, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TE205208._Automaton = _BuildAutomaton_51()




TE305101._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xDesc'), STD_ANON_13, scope=TE305101, documentation='\n            Descrição do evento: "Cancelamento de NFS-e por Ofício".\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 574, 6)))

TE305101._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CPFAgTrib'), TSCPF, scope=TE305101, documentation='\n            CPF do agente da administração tributária municipal que efetuou o cancelamento por ofício de NFS-e.\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 587, 6)))

TE305101._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nProcAdm'), TSNumProcAdmAnaliseFiscalCanc, scope=TE305101, documentation='\n            Número do processo administrativo municipal vinculado ao cancelamento de NFS-e por ofício.\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 594, 6)))

TE305101._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xProcAdm'), TSMotivo, scope=TE305101, documentation='\n            Descrição para explicitar o motivo indicado neste evento.\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 601, 6)))

def _BuildAutomaton_52 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_52
    del _BuildAutomaton_52
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TE305101._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xDesc')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 574, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TE305101._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CPFAgTrib')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 587, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TE305101._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nProcAdm')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 594, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TE305101._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xProcAdm')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 601, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TE305101._Automaton = _BuildAutomaton_52()




TE305102._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xDesc'), STD_ANON_14, scope=TE305102, documentation='\n            Descrição do evento: "Bloqueio de NFS-e por Ofício".\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 614, 6)))

TE305102._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CPFAgTrib'), TSCPF, scope=TE305102, documentation='\n            CPF do agente da administração tributária municipal que efetuou o cancelamento por ofício de NFS-e.\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 627, 6)))

TE305102._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xMotivo'), TSMotivo, scope=TE305102, documentation='Descrição para explicitar o motivo indicado neste evento', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 634, 6)))

TE305102._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'codEvento'), TSCodigoEventoNFSe, scope=TE305102, documentation='Descrição para explicitar o motivo indicado neste evento', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 639, 6)))

def _BuildAutomaton_53 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_53
    del _BuildAutomaton_53
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TE305102._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xDesc')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 614, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TE305102._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CPFAgTrib')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 627, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TE305102._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xMotivo')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 634, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TE305102._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'codEvento')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 639, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TE305102._Automaton = _BuildAutomaton_53()




TE305103._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xDesc'), STD_ANON_15, scope=TE305103, documentation='\n            Descrição do evento: "Desbloqueio de NFS-e por Ofício".\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 650, 6)))

TE305103._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CPFAgTrib'), TSCPF, scope=TE305103, documentation='\n            CPF do agente da administração tributária municipal que efetuou o cancelamento por ofício de NFS-e.\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 663, 6)))

TE305103._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'idBloqOfic'), TSIdNumEvento, scope=TE305103, documentation='\n            Referência ao Id da "Manifestação de rejeição da NFS-e" que originou o presente evento de anulação.\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 670, 6)))

def _BuildAutomaton_54 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_54
    del _BuildAutomaton_54
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TE305103._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xDesc')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 650, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TE305103._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CPFAgTrib')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 663, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TE305103._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'idBloqOfic')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 670, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TE305103._Automaton = _BuildAutomaton_54()




TCListaEventos._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'codEvento'), TSCodigoEventoNFSe, scope=TCListaEventos, documentation='\n            Grupo de informações de documento utilizado para Dedução/Redução do valor do serviço\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 683, 6)))

def _BuildAutomaton_55 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_55
    del _BuildAutomaton_55
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=9, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 683, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TCListaEventos._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'codEvento')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 683, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCListaEventos._Automaton = _BuildAutomaton_55()




TCInfoEventoRejeicao._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cMotivo'), TSCodMotivoRejeicao, scope=TCInfoEventoRejeicao, documentation='\n            Motivo da Rejeição da NFS-e:\n\n            1 - NFS-e em duplicidade;\n            2 - NFS-e já emitida pelo tomador;\n            3 - Não ocorrência do fato gerador;\n            4 - Erro quanto a responsabilidade tributária;\n            5 - Erro quanto ao valor do serviço, valor das deduções ou serviço prestado ou data do fato gerador;\n            9 - Outros;\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 696, 6)))

TCInfoEventoRejeicao._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xMotivo'), TSMotivo, scope=TCInfoEventoRejeicao, documentation='Descrição para explicitar o motivo indicado neste evento', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 710, 6)))

def _BuildAutomaton_56 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_56
    del _BuildAutomaton_56
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 710, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCInfoEventoRejeicao._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cMotivo')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 696, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TCInfoEventoRejeicao._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xMotivo')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 710, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCInfoEventoRejeicao._Automaton = _BuildAutomaton_56()




TCInfoEventoAnulacaoRejeicao._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CPFAgTrib'), TSCPF, scope=TCInfoEventoAnulacaoRejeicao, documentation='\n            CPF do agente da administração tributária municipal que efetuou o anulação da manifestação de rejeição da NFS-e.\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 721, 6)))

TCInfoEventoAnulacaoRejeicao._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'idEvManifRej'), TSIdNumEvento, scope=TCInfoEventoAnulacaoRejeicao, documentation='\n            Referência ao Id da "Manifestação de rejeição da NFS-e" que originou o presente evento de anulação.\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 728, 6)))

TCInfoEventoAnulacaoRejeicao._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xMotivo'), TSMotivo, scope=TCInfoEventoAnulacaoRejeicao, documentation='Descrição para explicitar o motivo da anluação', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 735, 6)))

def _BuildAutomaton_57 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_57
    del _BuildAutomaton_57
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfoEventoAnulacaoRejeicao._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CPFAgTrib')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 721, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfoEventoAnulacaoRejeicao._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'idEvManifRej')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 728, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCInfoEventoAnulacaoRejeicao._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xMotivo')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 735, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCInfoEventoAnulacaoRejeicao._Automaton = _BuildAutomaton_57()




TCNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'infNFSe'), TCInfNFSe, scope=TCNFSe, location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 8, 6)))

TCNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature'), _ImportedBinding__ds.SignatureType, scope=TCNFSe, location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/xmldsig-core-schema.xsd', 43, 0)))

def _BuildAutomaton_58 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_58
    del _BuildAutomaton_58
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCNFSe._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'infNFSe')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 8, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCNFSe._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 9, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCNFSe._Automaton = _BuildAutomaton_58()




TCInfNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xLocEmi'), TSDesc150, scope=TCInfNFSe, documentation='Descrição do código do IBGE do município emissor da NFS-e.\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 16, 6)))

TCInfNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xLocPrestacao'), TSDesc150, scope=TCInfNFSe, documentation='Descrição do local da prestação do serviço.\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 22, 6)))

TCInfNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nNFSe'), TSNNFSe, scope=TCInfNFSe, documentation='Número sequencial por tipo de emitente da NFS-e.\n            A Sefin Nacional NFS-e irá gerar o número da NFS-e de forma sequencial por emitente. Por se tratar de um ambiente altamente transacional, a Sefin Nacional NFS-e não irá reutilizar números inutilizados durante a geração da NFS-e.\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 28, 6)))

TCInfNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cLocIncid'), TSCodMunIBGE, scope=TCInfNFSe, documentation='\n            O código de município utilizado pelo Sistema Nacional NFS-e é o código definido para cada município pertencente ao ""Anexo V – Tabela de Código de Municípios do IBGE"", que consta ao final do Manual de Orientação ao Contribuinte do ISSQN para a Sefin Nacional NFS-e.\n            O município de incidência do ISSQN é determinado automaticamente pelo sistema, conforme regras do aspecto espacial da lei complementar federal (LC 116/03) que são válidas para todos  os municípios.\n            http://www.planalto.gov.br/ccivil_03/Leis/LCP/Lcp116.htm\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 35, 6)))

TCInfNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xLocIncid'), TSDesc150, scope=TCInfNFSe, documentation='\n            A descrição do código de município utilizado pelo Sistema Nacional NFS-e é o nome de cada município pertencente ao "Anexo V – Tabela de Código de Municípios do IBGE", que consta ao final do Manual de Orientação ao Contribuinte do ISSQN para a Sefin Nacional NFS-e.\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 44, 6)))

TCInfNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xTribNac'), TSDesc600, scope=TCInfNFSe, documentation='\n            Descrição do código de tributação nacional do ISSQN.\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 51, 6)))

TCInfNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xTribMun'), TSDesc600, scope=TCInfNFSe, documentation='\n            Descrição do código de tributação municipal do ISSQN.\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 58, 6)))

TCInfNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xNBS'), TSDesc600, scope=TCInfNFSe, documentation='\n            Descrição do código da NBS.\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 65, 6)))

TCInfNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'verAplic'), TSVerAplic, scope=TCInfNFSe, documentation='Versão do aplicativo que gerou a NFS-e', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 72, 6)))

TCInfNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ambGer'), TSAmbGeradorNFSe, scope=TCInfNFSe, documentation='Ambiente gerador da NFS-e', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 77, 6)))

TCInfNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tpEmis'), TSTipoEmissao, scope=TCInfNFSe, documentation='\n            Processo de Emissão da DPS:\n            1 - Emissão com aplicativo do contribuinte (via Web Service);\n            2 - Emissão com aplicativo disponibilizado pelo fisco (Web);\n            3 - Emissão com aplicativo disponibilizado pelo fisco (App);\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 82, 6)))

TCInfNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'procEmi'), TSProcEmissao, scope=TCInfNFSe, documentation='\n            Processo de Emissão da DPS:\n            1 - Emissão com aplicativo do contribuinte (via Web Service);\n            2 - Emissão com aplicativo disponibilizado pelo fisco (Web);\n            3 - Emissão com aplicativo disponibilizado pelo fisco (App);\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 92, 6)))

TCInfNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cStat'), TStat, scope=TCInfNFSe, documentation='Código do Status da mensagem', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 102, 6)))

TCInfNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dhProc'), TSDateTimeUTC, scope=TCInfNFSe, documentation='\n            Data/Hora da validação da DPS e geração da NFS-e. Data e hora no formato UTC (Universal Coordinated Time):AAAA-MM-DDThh:mm:ssTZD\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 107, 6)))

TCInfNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nDFSe'), TSNDFSe, scope=TCInfNFSe, documentation='\n            Número sequencial do documento gerado por ambiente gerador de DFSe do múnicípio.\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 114, 6)))

TCInfNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'emit'), TCEmitente, scope=TCInfNFSe, documentation='\n            Grupo de informações da DPS relativas ao emitente da NFS-e\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 121, 6)))

TCInfNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'valores'), TCValoresNFSe, scope=TCInfNFSe, documentation='Grupo de valores referentes ao Serviço Prestado', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 128, 6)))

TCInfNFSe._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DPS'), TCDPS, scope=TCInfNFSe, documentation='\n            Grupo de informações da DPS relativas ao serviço prestado\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 133, 6)))

def _BuildAutomaton_59 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_59
    del _BuildAutomaton_59
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 35, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 44, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 58, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 65, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 92, 6))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfNFSe._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xLocEmi')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 16, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfNFSe._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xLocPrestacao')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 22, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfNFSe._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nNFSe')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 28, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfNFSe._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cLocIncid')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 35, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfNFSe._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xLocIncid')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 44, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfNFSe._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xTribNac')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 51, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfNFSe._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xTribMun')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 58, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfNFSe._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xNBS')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 65, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfNFSe._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'verAplic')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 72, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfNFSe._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ambGer')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 77, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfNFSe._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tpEmis')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 82, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfNFSe._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'procEmi')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 92, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfNFSe._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cStat')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 102, 6))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfNFSe._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dhProc')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 107, 6))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfNFSe._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nDFSe')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 114, 6))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfNFSe._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'emit')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 121, 6))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfNFSe._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'valores')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 128, 6))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCInfNFSe._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DPS')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 133, 6))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
         ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
         ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
         ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
         ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    st_17._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCInfNFSe._Automaton = _BuildAutomaton_59()




TCDPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'infDPS'), TCInfDPS, scope=TCDPS, location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 280, 6)))

TCDPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature'), _ImportedBinding__ds.SignatureType, scope=TCDPS, location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/xmldsig-core-schema.xsd', 43, 0)))

def _BuildAutomaton_60 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_60
    del _BuildAutomaton_60
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 281, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCDPS._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'infDPS')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 280, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TCDPS._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 281, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCDPS._Automaton = _BuildAutomaton_60()




TCInfDPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tpAmb'), TSTipoAmbiente, scope=TCInfDPS, documentation='Identificação do Ambiente: 1 - Produção; 2 - Homologação', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 288, 6)))

TCInfDPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dhEmi'), TSDateTimeUTC, scope=TCInfDPS, documentation='Data e hora da emissão do DPS. Data e hora no formato UTC (Universal Coordinated Time): AAAA-MM-DDThh:mm:ssTZD', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 293, 6)))

TCInfDPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'verAplic'), TSVerAplic, scope=TCInfDPS, documentation='Versão do aplicativo que gerou o DPS', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 298, 6)))

TCInfDPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'serie'), TSSerieDPS, scope=TCInfDPS, documentation='Número do equipamento emissor do DPS ou série do DPS', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 303, 6)))

TCInfDPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nDPS'), TSNumDPS, scope=TCInfDPS, documentation='Número do DPS', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 308, 6)))

TCInfDPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dCompet'), TSData, scope=TCInfDPS, documentation='Data em que se iniciou a prestação do serviço: Dia, mês e ano (AAAAMMDD)', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 313, 6)))

TCInfDPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tpEmit'), TSEmitenteDPS, scope=TCInfDPS, documentation='Emitente da DPS: 1 - Prestador; 2 - Tomador; 3 - Intermediário', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 318, 6)))

TCInfDPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cMotivoEmisTI'), TSMotivoEmisTI, scope=TCInfDPS, documentation='Motivo da Emissão da DPS pelo Tomador/Intermediário:\n            1 - Importação de Serviço;\n            2 - Tomador/Intermediário obrigado a emitir NFS-e por legislação municipal;\n            3 - Tomador/Intermediário emitindo NFS-e por recusa de emissão pelo prestador;\n            4 - Tomador/Intermediário emitindo por rejeitar a NFS-e emitida pelo prestador;\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 323, 6)))

TCInfDPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'chNFSeRej'), TSChaveNFSe, scope=TCInfDPS, documentation='\n            Chave de Acesso da NFS-e rejeitada pelo Tomador/Intermediário.\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 333, 6)))

TCInfDPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cLocEmi'), TSCodMunIBGE, scope=TCInfDPS, documentation='O código de município utilizado pelo Sistema Nacional NFS-e é o código definido para cada município pertencente ao ""Anexo V – Tabela de Código de Municípios do IBGE"", que consta ao final do Manual de Orientação ao Contribuinte do ISSQN para a Sefin Nacional NFS-e.\n            O município emissor da NFS-e é aquele município em que o emitente da DPS está cadastrado e autorizado a "emitir uma NFS-e", ou seja, emitir uma DPS para que o sistema nacional valide as informações nela prestadas e gere a NFS-e correspondente para o emitente.\n            Para que o sistema nacional emita a NFS-e o município emissor deve ser conveniado e estar ativo no sistema nacional. Além disso o convênio do município deve permitir que os contribuintes do município utilize os emissores públicos do Sistema Nacional NFS-e\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 340, 6)))

TCInfDPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'subst'), TCSubstituicao, scope=TCInfDPS, documentation='Dados da NFS-e a ser substituída', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 348, 6)))

TCInfDPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'prest'), TCInfoPrestador, scope=TCInfDPS, documentation='Grupo de informações do DPS relativas ao Prestador de Serviços', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 353, 6)))

TCInfDPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'toma'), TCInfoPessoa, scope=TCInfDPS, documentation='Grupo de informações do DPS relativas ao Tomador de Serviços', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 358, 6)))

TCInfDPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'interm'), TCInfoPessoa, scope=TCInfDPS, documentation='Grupo de informações do DPS relativas ao Intermediário de Serviços', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 363, 6)))

TCInfDPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'serv'), TCServ, scope=TCInfDPS, documentation='Grupo de informações do DPS relativas ao Serviço Prestado', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 368, 6)))

TCInfDPS._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'valores'), TCInfoValores, scope=TCInfDPS, documentation='\n            Grupo de informações relativas à valores do serviço prestado\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 373, 6)))

def _BuildAutomaton_61 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_61
    del _BuildAutomaton_61
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 323, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 333, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 348, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 358, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 363, 6))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfDPS._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tpAmb')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 288, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfDPS._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dhEmi')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 293, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfDPS._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'verAplic')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 298, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfDPS._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'serie')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 303, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfDPS._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nDPS')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 308, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfDPS._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dCompet')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 313, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfDPS._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tpEmit')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 318, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfDPS._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cMotivoEmisTI')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 323, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfDPS._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'chNFSeRej')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 333, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfDPS._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cLocEmi')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 340, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfDPS._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'subst')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 348, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfDPS._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'prest')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 353, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfDPS._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'toma')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 358, 6))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfDPS._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'interm')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 363, 6))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfDPS._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'serv')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 368, 6))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCInfDPS._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'valores')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposComplexos_v1.00.xsd', 373, 6))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
         ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    st_15._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCInfDPS._Automaton = _BuildAutomaton_61()




TCEvento._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'infEvento'), TCInfEvento, scope=TCEvento, location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 15, 6)))

TCEvento._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature'), _ImportedBinding__ds.SignatureType, scope=TCEvento, location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/xmldsig-core-schema.xsd', 43, 0)))

def _BuildAutomaton_62 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_62
    del _BuildAutomaton_62
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCEvento._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'infEvento')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 15, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCEvento._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 16, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCEvento._Automaton = _BuildAutomaton_62()




TCInfEvento._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'verAplic'), TSVerAplic, scope=TCInfEvento, documentation='Versão do aplicativo que gerou o pedido do evento.', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 24, 6)))

TCInfEvento._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ambGer'), TSAmbGeradorEvt, scope=TCInfEvento, documentation='Ambiente gerador do evento', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 29, 6)))

TCInfEvento._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nSeqEvento'), TSNum3Dig, scope=TCInfEvento, documentation='Sequencial do evento para o mesmo tipo de evento. Para maioria dos eventos nSeqEvento=1. Nos casos em que possa existir mais de um evento do mesmo tipo o ambiente gerador deverá numerar de forma sequencial.', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 34, 6)))

TCInfEvento._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dhProc'), TSDateTimeUTC, scope=TCInfEvento, documentation='\n            Data/Hora do registro do evento.\n            Data e hora no formato UTC (Universal Coordinated Time): AAAA-MM-DDThh:mm:ssTZD"\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 39, 6)))

TCInfEvento._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nDFe'), TSNumDFe, scope=TCInfEvento, documentation='Ambiente gerador do evento', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 47, 6)))

TCInfEvento._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'pedRegEvento'), TCPedRegEvt, scope=TCInfEvento, documentation='Leiaute do pedido de registro do evento gerado pelo autor do evento', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 52, 6)))

def _BuildAutomaton_63 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_63
    del _BuildAutomaton_63
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 24, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfEvento._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'verAplic')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 24, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfEvento._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ambGer')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 29, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfEvento._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nSeqEvento')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 34, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfEvento._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dhProc')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 39, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfEvento._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nDFe')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 47, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCInfEvento._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'pedRegEvento')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 52, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCInfEvento._Automaton = _BuildAutomaton_63()




TCPedRegEvt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'infPedReg'), TCInfPedReg, scope=TCPedRegEvt, location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 64, 6)))

TCPedRegEvt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature'), _ImportedBinding__ds.SignatureType, scope=TCPedRegEvt, location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/xmldsig-core-schema.xsd', 43, 0)))

def _BuildAutomaton_64 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_64
    del _BuildAutomaton_64
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 65, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCPedRegEvt._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'infPedReg')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 64, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TCPedRegEvt._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ds, 'Signature')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 65, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCPedRegEvt._Automaton = _BuildAutomaton_64()




TCInfPedReg._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tpAmb'), TSTipoAmbiente, scope=TCInfPedReg, documentation='Identificação do Ambiente: 1 - Produção; 2 - Homologação', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 73, 6)))

TCInfPedReg._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'verAplic'), TSVerAplic, scope=TCInfPedReg, documentation='Versão do aplicativo que gerou o pedido de registro de evento.', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 78, 6)))

TCInfPedReg._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dhEvento'), TSDateTimeUTC, scope=TCInfPedReg, documentation='\n            Data e hora do evento no formato AAAA-MM-DDThh:mm:ssTZD (UTC - Universal Coordinated Time, onde TZD pode ser -02:00 (Fernando de Noronha), -03:00 (Brasília) ou -04:00 (Manaus), no horário de verão serão -01:00, -02:00 e -03:00.\n            Ex.: 2010-08-19T13:00:15-03:00.\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 83, 6)))

TCInfPedReg._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CNPJAutor'), TSCNPJ, scope=TCInfPedReg, documentation='CNPJ do autor do evento.', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 95, 8)))

TCInfPedReg._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CPFAutor'), TSCPF, scope=TCInfPedReg, documentation='CPF do autor do evento.', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 100, 8)))

TCInfPedReg._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'chNFSe'), TSChaveNFSe, scope=TCInfPedReg, documentation='Chave de Acesso da NFS-e vinculada ao Evento', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 106, 6)))

TCInfPedReg._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'nPedRegEvento'), TSNum3Dig, scope=TCInfPedReg, documentation='\n            Número do pedido do registro de evento para o mesmo tipo de evento.\n            Para os eventos que ocorrem somente uma vez, como é o caso do cancelamento, o nPedRegEvento deve ser igual a 1.\n            Os eventos que podem ocorrer mais de uma vez devem ter o nPedRegEvento único.\n          ', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 111, 6)))

TCInfPedReg._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'e101101'), TE101101, scope=TCInfPedReg, documentation='Evento de cancelamento', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 121, 8)))

TCInfPedReg._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'e105102'), TE105102, scope=TCInfPedReg, documentation='Evento de cancelamento por substituição', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 126, 8)))

TCInfPedReg._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'e101103'), TE101103, scope=TCInfPedReg, documentation='Solicitação de Análise Fiscal para Cancelamento de NFS-e', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 131, 8)))

TCInfPedReg._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'e105104'), TE105104, scope=TCInfPedReg, documentation='Cancelamento de NFS-e Deferido por Análise Fiscal', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 136, 8)))

TCInfPedReg._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'e105105'), TE105105, scope=TCInfPedReg, documentation='Cancelamento de NFS-e Indeferido por Análise Fiscal', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 141, 8)))

TCInfPedReg._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'e202201'), TE202201, scope=TCInfPedReg, documentation='Confirmação do Prestador', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 147, 8)))

TCInfPedReg._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'e203202'), TE203202, scope=TCInfPedReg, documentation='Confirmação do Tomador', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 152, 8)))

TCInfPedReg._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'e204203'), TE204203, scope=TCInfPedReg, documentation='Confirmação do Intermediário', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 157, 8)))

TCInfPedReg._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'e205204'), TE205204, scope=TCInfPedReg, documentation='Confirmação Tácita', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 162, 8)))

TCInfPedReg._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'e202205'), TE202205, scope=TCInfPedReg, documentation='Rejeição do Prestador', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 167, 8)))

TCInfPedReg._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'e203206'), TE203206, scope=TCInfPedReg, documentation='Rejeição do Tomador', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 172, 8)))

TCInfPedReg._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'e204207'), TE204207, scope=TCInfPedReg, documentation='Rejeição do Intermediário', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 177, 8)))

TCInfPedReg._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'e205208'), TE205208, scope=TCInfPedReg, documentation='Anulação da Rejeição', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 182, 8)))

TCInfPedReg._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'e305101'), TE305101, scope=TCInfPedReg, documentation='Cancelamento de NFS-e por Ofício', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 188, 8)))

TCInfPedReg._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'e305102'), TE305102, scope=TCInfPedReg, documentation='Bloqueio de NFS-e por Ofício', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 193, 8)))

TCInfPedReg._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'e305103'), TE305103, scope=TCInfPedReg, documentation='Desbloqueio de NFS-e por Ofício', location=pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 198, 8)))

def _BuildAutomaton_65 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_65
    del _BuildAutomaton_65
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfPedReg._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tpAmb')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 73, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfPedReg._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'verAplic')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 78, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfPedReg._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'dhEvento')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 83, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfPedReg._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CNPJAutor')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 95, 8))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfPedReg._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CPFAutor')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 100, 8))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfPedReg._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'chNFSe')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 106, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TCInfPedReg._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'nPedRegEvento')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 111, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCInfPedReg._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'e101101')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 121, 8))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCInfPedReg._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'e105102')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 126, 8))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCInfPedReg._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'e101103')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 131, 8))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCInfPedReg._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'e105104')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 136, 8))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCInfPedReg._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'e105105')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 141, 8))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCInfPedReg._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'e202201')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 147, 8))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCInfPedReg._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'e203202')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 152, 8))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCInfPedReg._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'e204203')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 157, 8))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCInfPedReg._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'e205204')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 162, 8))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCInfPedReg._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'e202205')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 167, 8))
    st_16 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCInfPedReg._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'e203206')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 172, 8))
    st_17 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCInfPedReg._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'e204207')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 177, 8))
    st_18 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCInfPedReg._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'e205208')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 182, 8))
    st_19 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCInfPedReg._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'e305101')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 188, 8))
    st_20 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCInfPedReg._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'e305102')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 193, 8))
    st_21 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TCInfPedReg._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'e305103')), pyxb.utils.utility.Location('file:///app/pynfe_nasajon/pynfe/data/XSDs/NFS-e/nacional/tiposEventos_v1.00.xsd', 198, 8))
    st_22 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    transitions.append(fac.Transition(st_16, [
         ]))
    transitions.append(fac.Transition(st_17, [
         ]))
    transitions.append(fac.Transition(st_18, [
         ]))
    transitions.append(fac.Transition(st_19, [
         ]))
    transitions.append(fac.Transition(st_20, [
         ]))
    transitions.append(fac.Transition(st_21, [
         ]))
    transitions.append(fac.Transition(st_22, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    transitions = []
    st_8._set_transitionSet(transitions)
    transitions = []
    st_9._set_transitionSet(transitions)
    transitions = []
    st_10._set_transitionSet(transitions)
    transitions = []
    st_11._set_transitionSet(transitions)
    transitions = []
    st_12._set_transitionSet(transitions)
    transitions = []
    st_13._set_transitionSet(transitions)
    transitions = []
    st_14._set_transitionSet(transitions)
    transitions = []
    st_15._set_transitionSet(transitions)
    transitions = []
    st_16._set_transitionSet(transitions)
    transitions = []
    st_17._set_transitionSet(transitions)
    transitions = []
    st_18._set_transitionSet(transitions)
    transitions = []
    st_19._set_transitionSet(transitions)
    transitions = []
    st_20._set_transitionSet(transitions)
    transitions = []
    st_21._set_transitionSet(transitions)
    transitions = []
    st_22._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TCInfPedReg._Automaton = _BuildAutomaton_65()

