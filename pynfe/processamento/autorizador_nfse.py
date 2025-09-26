from datetime import datetime
from pyxb import BIND
from importlib import import_module
import re
from pynfe.entidades.evento import EventoNFSe, EventoNFSeCancelarNota
from pynfe.entidades.notafiscal import NotaFiscalServico
from pynfe.utils import obter_codigo_por_municipio

# Type imports for autocomplete - these won't cause runtime conflicts
# since they're only used for type hints
from typing import TYPE_CHECKING, Any, Optional


class InterfaceAutorizador:
    # TODO Colocar raise Exception Not Implemented nos metodos
    def consultar_rps(self):
        pass

    def cancelar(self):
        pass


class SerializacaoBetha(InterfaceAutorizador):
    def __init__(self):
        # importa
        global nfse_schema
        try:
            import pynfe.utils.nfse.betha.nfse_v202
            nfse_schema = pynfe.utils.nfse.betha.nfse_v202
        except ImportError:
            pass

    def gerar(self, nfse):
        """Retorna string de um XML gerado a partir do
        XML Schema (XSD). Binding gerado pelo modulo PyXB."""

        servico = nfse_schema.tcDadosServico()
        valores_servico = nfse_schema.tcValoresDeclaracaoServico()
        valores_servico.ValorServicos = nfse.servico.valor_servico

        servico.IssRetido = nfse.servico.iss_retido
        servico.ItemListaServico = nfse.servico.item_lista
        servico.Discriminacao = nfse.servico.discriminacao
        servico.CodigoMunicipio = nfse.servico.codigo_municipio
        servico.ExigibilidadeISS = nfse.servico.exigibilidade
        servico.MunicipioIncidencia = nfse.servico.municipio_incidencia
        servico.Valores = valores_servico

        # Prestador
        id_prestador = nfse_schema.tcIdentificacaoPrestador()
        id_prestador.CpfCnpj = nfse.emitente.cnpj
        id_prestador.InscricaoMunicipal = nfse.emitente.inscricao_municipal

        # Cliente
        id_tomador = nfse_schema.tcIdentificacaoTomador()
        id_tomador.CpfCnpj = nfse.cliente.numero_documento
        if nfse.cliente.inscricao_municipal:
            id_tomador.InscricaoMunicipal = nfse.cliente.inscricao_municipal

        endereco_tomador = nfse_schema.tcEndereco()
        endereco_tomador.Endereco = nfse.cliente.endereco_logradouro
        endereco_tomador.Numero = nfse.cliente.endereco_numero
        endereco_tomador.Bairro = nfse.cliente.endereco_bairro
        endereco_tomador.CodigoMunicipio = nfse.cliente.endereco_cod_municipio
        endereco_tomador.Uf = nfse.cliente.endereco_uf
        endereco_tomador.CodigoPais = nfse.cliente.endereco_pais
        endereco_tomador.Cep = nfse.cliente.endereco_cep

        tomador = nfse_schema.tcDadosTomador()
        tomador.IdentificacaoPrestador = id_tomador
        tomador.RazaoSocial = nfse.cliente.razao_social
        tomador.Endereco = endereco_tomador

        id_rps = nfse_schema.tcIdentificacaoRps()
        id_rps.Numero = nfse.numero
        id_rps.Serie = nfse.serie
        id_rps.Tipo = nfse.tipo

        rps = nfse_schema.tcInfRps()
        rps.IdentificacaoRps = id_rps
        rps.DataEmissao = nfse.data_emissao.strftime("%Y-%m-%d")
        rps.Status = 1

        inf_declaracao_servico = nfse_schema.tcInfDeclaracaoPrestacaoServico()
        inf_declaracao_servico.Competencia = nfse.data_emissao.strftime("%Y-%m-%d")
        inf_declaracao_servico.Servico = servico
        inf_declaracao_servico.Prestador = id_prestador
        inf_declaracao_servico.Tomador = tomador
        inf_declaracao_servico.OptanteSimplesNacional = nfse.simples
        inf_declaracao_servico.IncentivoFiscal = nfse.incentivo
        inf_declaracao_servico.Id = nfse.numero
        inf_declaracao_servico.Rps = rps

        declaracao_servico = nfse_schema.tcDeclaracaoPrestacaoServico()
        declaracao_servico.InfDeclaracaoPrestacaoServico = inf_declaracao_servico

        gnfse = nfse_schema.GerarNfseEnvio()
        gnfse.Rps = declaracao_servico

        return gnfse.toxml(element_name="GerarNfseEnvio")

    def consultar_rps(self, nfse):
        """Retorna string de um XML gerado a partir do
        XML Schema (XSD). Binding gerado pelo modulo PyXB."""

        # Rps
        id_rps = nfse_schema.tcIdentificacaoRps()
        id_rps.Numero = nfse.numero
        id_rps.Serie = nfse.serie
        id_rps.Tipo = nfse.tipo

        # Prestador
        id_prestador = nfse_schema.tcIdentificacaoPrestador()
        id_prestador.CpfCnpj = nfse.emitente.cnpj
        id_prestador.InscricaoMunicipal = nfse.emitente.inscricao_municipal

        consulta = nfse_schema.ConsultarNfseRpsEnvio()
        consulta.IdentificacaoRps = id_rps
        consulta.Prestador = id_prestador

        consulta = (
            consulta.toxml(element_name="ConsultarNfseRpsEnvio")
            .replace("ns1:", "")
            .replace(":ns1", "")
            .replace('<?xml version="1.0" ?>', "")
        )

        return consulta

    def consultar_faixa(self, emitente, inicio, fim, pagina):
        """Retorna string de um XML gerado a partir do
        XML Schema (XSD). Binding gerado pelo modulo PyXB."""

        # Prestador
        id_prestador = nfse_schema.tcIdentificacaoPrestador()
        id_prestador.CpfCnpj = emitente.cnpj
        id_prestador.InscricaoMunicipal = emitente.inscricao_municipal

        consulta = nfse_schema.ConsultarNfseFaixaEnvio()
        consulta.Prestador = id_prestador
        consulta.Pagina = pagina
        # É necessário BIND antes de atribuir numero final e numero inicial
        consulta.Faixa = BIND()
        consulta.Faixa.NumeroNfseInicial = inicio
        consulta.Faixa.NumeroNfseFinal = fim

        consulta = (
            consulta.toxml(element_name="ConsultarNfseFaixaEnvio")
            .replace("ns1:", "")
            .replace(":ns1", "")
            .replace('<?xml version="1.0" ?>', "")
        )

        return consulta

    def cancelar(self, nfse):
        """Retorna string de um XML gerado a partir do
        XML Schema (XSD). Binding gerado pelo modulo PyXB."""

        # id nfse
        id_nfse = nfse_schema.tcIdentificacaoNfse()
        id_nfse.Numero = nfse.numero
        id_nfse.CpfCnpj = nfse.emitente.cnpj
        id_nfse.InscricaoMunicipal = nfse.emitente.inscricao_municipal
        id_nfse.CodigoMunicipio = nfse.emitente.endereco_cod_municipio

        # Info Pedido de cancelamento
        info_pedido = nfse_schema.tcInfPedidoCancelamento()
        info_pedido.Id = "1"
        info_pedido.IdentificacaoNfse = id_nfse
        # pedido.CodigoCancelamento =

        # Pedido
        pedido = nfse_schema.tcPedidoCancelamento()
        pedido.InfPedidoCancelamento = info_pedido

        # Cancelamento
        cancelar = nfse_schema.CancelarNfseEnvio()
        cancelar.Pedido = pedido

        return cancelar.toxml(element_name="CancelarNfseEnvio")

    def serializar_lote_sincrono(self, nfse):
        """Retorna string de um XML gerado a partir do
        XML Schema (XSD). Binding gerado pelo modulo PyXB."""

        servico = nfse_schema.tcDadosServico()
        valores_servico = nfse_schema.tcValoresDeclaracaoServico()
        valores_servico.ValorServicos = nfse.servico.valor_servico

        servico.IssRetido = nfse.servico.iss_retido
        servico.ItemListaServico = nfse.servico.item_lista
        servico.Discriminacao = nfse.servico.discriminacao
        servico.CodigoMunicipio = nfse.servico.codigo_municipio
        servico.ExigibilidadeISS = nfse.servico.exigibilidade
        servico.MunicipioIncidencia = nfse.servico.municipio_incidencia
        servico.Valores = valores_servico

        # Prestador
        id_prestador = nfse_schema.tcIdentificacaoPrestador()
        id_prestador.CpfCnpj = nfse.emitente.cnpj
        id_prestador.InscricaoMunicipal = nfse.emitente.inscricao_municipal

        # Cliente
        id_tomador = nfse_schema.tcIdentificacaoTomador()
        id_tomador.CpfCnpj = nfse.cliente.numero_documento
        if nfse.cliente.inscricao_municipal:
            id_tomador.InscricaoMunicipal = nfse.cliente.inscricao_municipal

        endereco_tomador = nfse_schema.tcEndereco()
        endereco_tomador.Endereco = nfse.cliente.endereco_logradouro
        endereco_tomador.Numero = nfse.cliente.endereco_numero
        endereco_tomador.Bairro = nfse.cliente.endereco_bairro
        endereco_tomador.CodigoMunicipio = nfse.cliente.endereco_cod_municipio
        endereco_tomador.Uf = nfse.cliente.endereco_uf
        endereco_tomador.CodigoPais = nfse.cliente.endereco_pais
        endereco_tomador.Cep = nfse.cliente.endereco_cep

        tomador = nfse_schema.tcDadosTomador()
        tomador.IdentificacaoPrestador = id_tomador
        tomador.RazaoSocial = nfse.cliente.razao_social
        tomador.Endereco = endereco_tomador

        id_rps = nfse_schema.tcIdentificacaoRps()
        id_rps.Numero = nfse.numero
        id_rps.Serie = nfse.serie
        id_rps.Tipo = nfse.tipo

        rps = nfse_schema.tcInfRps()
        rps.IdentificacaoRps = id_rps
        rps.DataEmissao = nfse.data_emissao.strftime("%Y-%m-%d")
        rps.Status = 1

        inf_declaracao_servico = nfse_schema.tcInfDeclaracaoPrestacaoServico()
        inf_declaracao_servico.Competencia = nfse.data_emissao.strftime("%Y-%m-%d")
        inf_declaracao_servico.Servico = servico
        inf_declaracao_servico.Prestador = id_prestador
        inf_declaracao_servico.Tomador = tomador
        inf_declaracao_servico.OptanteSimplesNacional = nfse.simples
        inf_declaracao_servico.IncentivoFiscal = nfse.incentivo
        inf_declaracao_servico.Id = nfse.numero
        inf_declaracao_servico.Rps = rps

        declaracao_servico = nfse_schema.tcDeclaracaoPrestacaoServico()
        declaracao_servico.InfDeclaracaoPrestacaoServico = inf_declaracao_servico

        lote = nfse_schema.tcLoteRps()
        lote.NumeroLote = 1
        lote.Id = 1
        lote.CpfCnpj = nfse.emitente.cnpj
        lote.InscricaoMunicipal = nfse.emitente.inscricao_municipal
        lote.QuantidadeRps = 1
        if nfse.autorizador.upper() == "BETHA":
            lote.versao = "2.02"
        lote.ListaRps = BIND(declaracao_servico)

        gnfse = nfse_schema.EnviarLoteRpsSincronoEnvio()
        gnfse.LoteRps = lote

        return gnfse.toxml(element_name="EnviarLoteRpsSincronoEnvio")


class SerializacaoGinfes(InterfaceAutorizador):
    def __init__(self):
        # importa
        global _tipos, servico_consultar_nfse_envio_v03
        global servico_enviar_lote_rps_envio_v03, cabecalho_v03
        global servico_cancelar_nfse_envio_v03
        global servico_consultar_lote_rps_envio_v03
        global servico_consultar_situacao_lote_rps_envio_v03
        global servico_consultar_nfse_rps_envio_v03
        _tipos = import_module("pynfe.utils.nfse.ginfes._tipos")
        servico_consultar_nfse_envio_v03 = import_module(
            "pynfe.utils.nfse.ginfes.servico_consultar_nfse_envio_v03"
        )
        servico_cancelar_nfse_envio_v03 = import_module(
            "pynfe.utils.nfse.ginfes.servico_cancelar_nfse_envio_v03"
        )
        servico_enviar_lote_rps_envio_v03 = import_module(
            "pynfe.utils.nfse.ginfes.servico_enviar_lote_rps_envio_v03"
        )
        cabecalho_v03 = import_module("pynfe.utils.nfse.ginfes.cabecalho_v03")
        servico_consultar_lote_rps_envio_v03 = import_module(
            "pynfe.utils.nfse.ginfes.servico_consultar_lote_rps_envio_v03"
        )
        servico_consultar_situacao_lote_rps_envio_v03 = import_module(
            "pynfe.utils.nfse.ginfes.servico_consultar_situacao_lote_rps_envio_v03"
        )
        servico_consultar_nfse_rps_envio_v03 = import_module(
            "pynfe.utils.nfse.ginfes.servico_consultar_nfse_rps_envio_v03"
        )

    def consultar_rps(self, emitente, numero, serie, tipo):
        """Retorna string de um XML de consulta por Rps gerado a partir do
        XML Schema (XSD). Binding gerado pelo modulo PyXB.
        servico_consultar_nfse_rps_envio_v03.xsd
        """
        # Rps
        id_rps = _tipos.tcIdentificacaoRps()
        id_rps.Numero = numero
        id_rps.Serie = serie
        id_rps.Tipo = tipo

        # Prestador
        id_prestador = _tipos.tcIdentificacaoPrestador()
        id_prestador.Cnpj = emitente.cnpj
        id_prestador.InscricaoMunicipal = emitente.inscricao_municipal

        consulta = servico_consultar_nfse_rps_envio_v03.ConsultarNfseRpsEnvio()
        consulta.IdentificacaoRps = id_rps
        consulta.Prestador = id_prestador

        return consulta.toxml(element_name="ns1:ConsultarNfseRpsEnvio")

    def consultar_nfse(self, emitente, numero=None, inicio=None, fim=None):
        # Prestador
        id_prestador = _tipos.tcIdentificacaoPrestador()
        id_prestador.Cnpj = emitente.cnpj
        id_prestador.InscricaoMunicipal = emitente.inscricao_municipal

        consulta = servico_consultar_nfse_envio_v03.ConsultarNfseEnvio()
        consulta.Prestador = id_prestador
        # Consulta por Numero
        if numero is not None:
            consulta.NumeroNfse = numero
        else:
            # consulta por Data
            consulta.PeriodoEmissao = BIND()
            consulta.PeriodoEmissao.DataInicial = inicio
            consulta.PeriodoEmissao.DataFinal = fim

        return consulta.toxml(element_name="ns1:ConsultarNfseEnvio")

    def consultar_lote(self, emitente, numero):
        # Prestador
        id_prestador = _tipos.tcIdentificacaoPrestador()
        id_prestador.Cnpj = emitente.cnpj
        id_prestador.InscricaoMunicipal = emitente.inscricao_municipal

        consulta = servico_consultar_lote_rps_envio_v03.ConsultarLoteRpsEnvio()
        consulta.Prestador = id_prestador
        consulta.Protocolo = str(numero)

        return consulta.toxml(element_name="ns1:ConsultarLoteRpsEnvio")

    def consultar_situacao_lote(self, emitente, numero):
        "Serializa lote de envio, baseado no servico_consultar_situacao_lote_rps_envio_v03.xsd"
        # Prestador
        id_prestador = _tipos.tcIdentificacaoPrestador()
        id_prestador.Cnpj = emitente.cnpj
        id_prestador.InscricaoMunicipal = emitente.inscricao_municipal

        consulta = servico_consultar_situacao_lote_rps_envio_v03.ConsultarSituacaoLoteRpsEnvio()
        consulta.Prestador = id_prestador
        consulta.Protocolo = str(numero)

        return consulta.toxml(element_name="ns1:ConsultarSituacaoLoteRpsEnvio")

    def serializar_lote_assincrono(self, nfse):
        "Serializa lote de envio, baseado no servico_enviar_lote_rps_envio_v03.xsd"

        servico = _tipos.tcDadosServico()
        valores_servico = _tipos.tcValores()
        valores_servico.ValorServicos = nfse.servico.valor_servico
        # valores_servico.ValorServicos = str(Decimal(
        # nfse.servico.valor_servico.quantize(Decimal('.01'), rounding=ROUND_HALF_UP)))
        valores_servico.IssRetido = nfse.servico.iss_retido
        # Dados opcionais
        if nfse.servico.valor_deducoes:
            valores_servico.ValorDeducoes = nfse.servico.valor_deducoes
        if nfse.servico.valor_pis:
            valores_servico.ValorPis = nfse.servico.valor_pis
        if nfse.servico.valor_confins:
            valores_servico.ValorCofins = nfse.servico.valor_confins
        if nfse.servico.valor_inss:
            valores_servico.ValorInss = nfse.servico.valor_inss
        if nfse.servico.valor_ir:
            valores_servico.ValorIr = nfse.servico.valor_ir
        if nfse.servico.valor_csll:
            valores_servico.ValorCsll = nfse.servico.valor_csll
        if nfse.servico.valor_iss:
            valores_servico.ValorIss = nfse.servico.valor_iss
        if nfse.servico.valor_iss_retido:
            valores_servico.ValorIssRetido = nfse.servico.valor_iss_retido
        if nfse.servico.valor_liquido:
            valores_servico.ValorLiquidoNfse = nfse.servico.valor_liquido
        if nfse.servico.outras_retencoes:
            valores_servico.OutrasRetencoes = nfse.servico.outras_retencoes
        if nfse.servico.base_calculo:
            valores_servico.BaseCalculo = nfse.servico.base_calculo
        if nfse.servico.aliquota:
            valores_servico.Aliquota = nfse.servico.aliquota
        if nfse.servico.desconto_incondicionado:
            valores_servico.DescontoIncondicionado = nfse.servico.desconto_incondicionado
        if nfse.servico.desconto_condicionado:
            valores_servico.DescontoCondicionado = nfse.servico.desconto_condicionado

        servico.Valores = valores_servico
        servico.ItemListaServico = nfse.servico.item_lista
        # opcionais
        if nfse.servico.codigo_cnae:
            servico.CodigoCnae = nfse.servico.codigo_cnae
        if nfse.servico.codigo_tributacao_municipal:
            servico.CodigoTributacaoMunicipio = nfse.servico.codigo_tributacao_municipal
        # obrigatórios
        servico.Discriminacao = nfse.servico.discriminacao
        servico.CodigoMunicipio = nfse.servico.codigo_municipio

        # endereco tomador
        endereco_tomador = _tipos.tcEndereco()
        endereco_tomador.Endereco = nfse.cliente.endereco_logradouro
        if nfse.cliente.endereco_complemento:
            endereco_tomador.Complemento = nfse.cliente.endereco_complemento
        endereco_tomador.Numero = nfse.cliente.endereco_numero
        endereco_tomador.Bairro = nfse.cliente.endereco_bairro
        if nfse.cliente.endereco_cod_municipio:
            endereco_tomador.CodigoMunicipio = nfse.cliente.endereco_cod_municipio
        endereco_tomador.Uf = nfse.cliente.endereco_uf
        endereco_tomador.Cep = nfse.cliente.endereco_cep
        # identificacao Tomador
        id_tomador = _tipos.tcIdentificacaoTomador()
        id_tomador.CpfCnpj = nfse.cliente.numero_documento
        if nfse.cliente.inscricao_municipal:
            id_tomador.InscricaoMunicipal = nfse.cliente.inscricao_municipal
        # Tomador
        tomador = _tipos.tcDadosTomador()
        tomador.IdentificacaoTomador = id_tomador
        tomador.RazaoSocial = nfse.cliente.razao_social
        tomador.Endereco = endereco_tomador
        # opcional
        if nfse.cliente.endereco_telefone or nfse.cliente.email:
            tomador.Contato = _tipos.tcContato()
            if nfse.cliente.endereco_telefone:
                tomador.Contato.Telefone = nfse.cliente.endereco_telefone
            if nfse.cliente.email:
                tomador.Contato.Email = nfse.cliente.email

        # Prestador
        id_prestador = _tipos.tcIdentificacaoPrestador()
        id_prestador.Cnpj = nfse.emitente.cnpj
        id_prestador.InscricaoMunicipal = nfse.emitente.inscricao_municipal

        # identificacao rps
        id_rps = _tipos.tcIdentificacaoRps()
        id_rps.Numero = nfse.numero
        id_rps.Serie = nfse.serie
        id_rps.Tipo = nfse.tipo
        # inf rps
        inf_rps = _tipos.tcInfRps()
        inf_rps.IdentificacaoRps = id_rps
        inf_rps.DataEmissao = nfse.data_emissao.strftime("%Y-%m-%dT%H:%M:%S")
        # Natureza da Operação
        # 1 – Tributação no município
        # 2 - Tributação fora do município
        # 3 - Isenção
        # 4 - Imune
        # 5 –Exigibilidade suspensa por decisão judicial
        # 6 – Exigibilidade suspensa por procedimento administrativo
        inf_rps.NaturezaOperacao = nfse.natureza_operacao
        # Regime Especial de Tributação
        # 1 – Microempresa municipal
        # 2 - Estimativa
        # 3 – Sociedade de profissionais
        # 4 – Cooperativa
        # 5 - Microempresário Individual (MEI)
        # 6 - Microempresário e Empresa de Pequeno Porte (ME EPP)
        if nfse.regime_especial:
            inf_rps.RegimeEspecialTributacao = nfse.regime_especial
        inf_rps.OptanteSimplesNacional = nfse.simples  # 1-sim 2-nao
        inf_rps.IncentivadorCultural = nfse.incentivo  # 1-sim 2-nao
        # Código de status da NFS-e
        # 1-Normal 2-Cancelado (sempre 1, nota não pode ser enviada como cancelada)
        inf_rps.Status = 1
        inf_rps.RpsSubstituido = None  # opcional
        inf_rps.Servico = servico
        inf_rps.Prestador = id_prestador
        inf_rps.Tomador = tomador
        inf_rps.IntermediarioServico = None  # opcional
        inf_rps.ConstrucaoCivil = None  # opcional
        inf_rps.Id = nfse.numero

        rps = _tipos.tcRps()
        rps.InfRps = inf_rps

        lote = _tipos.tcLoteRps()
        lote.NumeroLote = 1
        lote.Id = 1
        lote.Cnpj = nfse.emitente.cnpj
        lote.InscricaoMunicipal = nfse.emitente.inscricao_municipal
        lote.QuantidadeRps = 1
        lote.ListaRps = BIND()
        lote.ListaRps.append(rps)

        enviarLote = servico_enviar_lote_rps_envio_v03.EnviarLoteRpsEnvio()
        enviarLote.LoteRps = lote
        return enviarLote.toxml(element_name="ns1:EnviarLoteRpsEnvio")

    def cancelar(self, nfse, codigo):
        """Retorna string de um XML gerado a partir do
        XML Schema (XSD). Binding gerado pelo modulo PyXB."""
        # id nfse
        id_nfse = _tipos.tcIdentificacaoNfse()
        id_nfse.Numero = nfse.numero
        id_nfse.Cnpj = nfse.emitente.cnpj
        id_nfse.InscricaoMunicipal = nfse.emitente.inscricao_municipal
        id_nfse.CodigoMunicipio = nfse.emitente.endereco_cod_municipio

        # Info Pedido de cancelamento
        info_pedido = _tipos.tcInfPedidoCancelamento()
        info_pedido.Id = "1"
        info_pedido.IdentificacaoNfse = id_nfse
        info_pedido.CodigoCancelamento = codigo

        # Pedido
        pedido = _tipos.tcPedidoCancelamento()
        pedido.InfPedidoCancelamento = info_pedido

        # Cancelamento
        cancelar = servico_cancelar_nfse_envio_v03.CancelarNfseEnvio()
        cancelar.Pedido = pedido

        return cancelar.toxml(element_name="ns1:CancelarNfseEnvio")

    def cancelar_v2(self, nfse):
        # serialização utilizando lxml
        from lxml import etree

        ns1 = "http://www.ginfes.com.br/servico_cancelar_nfse_envio"
        ns2 = "http://www.ginfes.com.br/tipos"
        raiz = etree.Element("{%s}CancelarNfseEnvio" % ns1, nsmap={"ns1": ns1, "ns2": ns2})
        prestador = etree.SubElement(raiz, "{%s}Prestador" % ns1)
        etree.SubElement(prestador, "{%s}Cnpj" % ns2).text = nfse.emitente.cnpj
        etree.SubElement(
            prestador, "{%s}InscricaoMunicipal" % ns2
        ).text = nfse.emitente.inscricao_municipal
        etree.SubElement(raiz, "{%s}NumeroNfse" % ns1).text = nfse.numero
        return etree.tostring(raiz, encoding="unicode")

    def cabecalho(self):
        # info
        cabecalho = cabecalho_v03.cabecalho()
        cabecalho.versao = "3"
        cabecalho.versaoDados = "3"
        return cabecalho.toxml(element_name="ns2:cabecalho")


class SerializacaoNacional(InterfaceAutorizador):
    
    def __init__(self) -> None:
        self._dps_schema: Optional[Any] = None
        self._evento_schema: Optional[Any] = None
    
    def _get_dps_schema(self) -> Any:
        """Get DPS schema with lazy loading and conflict resolution"""
        if self._dps_schema is None:
            self._dps_schema = self._safe_import_dps()
        return self._dps_schema
    
    def _get_evento_schema(self) -> Any:
        """Get evento schema with lazy loading and conflict resolution"""
        if self._evento_schema is None:
            self._evento_schema = self._safe_import_evento()
        return self._evento_schema
    
    def _safe_import_dps(self):
        """Safely import DPS schema handling PyXB conflicts"""
        import pyxb.exceptions_
        import pyxb.namespace
        
        # Strategy 1: Try direct import after basic namespace clearing
        try:
            self._clear_all_pyxb_namespaces()
            from pynfe.utils.nfse.nacional import DPS_v1_00
            return DPS_v1_00
        except (pyxb.exceptions_.NamespaceUniquenessError, ImportError) as e:
            error_msg = str(e)
            if any(conflict in error_msg for conflict in ["TVerNFSe", "CryptoBinary", "NamespaceUniquenessError"]):
                
                # Strategy 2: Try more aggressive cleanup for both NFSe and XMLDSig conflicts
                try:
                    self._force_clear_all_namespaces()
                    from pynfe.utils.nfse.nacional import DPS_v1_00
                    return DPS_v1_00
                except Exception as e2:
                    
                    # Strategy 3: Try importing with progressive module cleanup
                    if "CryptoBinary" in str(e2):
                        # This is the persistent XMLDSig conflict - try multiple approaches
                        for attempt in range(3):
                            try:
                                # Clear everything and try again
                                self._ultra_clear_xmldsig_namespace()
                                module = self._import_module_fresh_isolated('pynfe.utils.nfse.nacional.DPS_v1_00')
                                return module
                            except Exception as e3:
                                if attempt == 2:  # Last attempt
                                    raise ImportError(f"FATAL: Cannot resolve CryptoBinary conflict in DPS module after {attempt+1} attempts. "
                                                    f"This likely indicates the PyXB schemas need to be regenerated. "
                                                    f"Original error: {e}, Final error: {e3}")
                                # Wait a moment and try again with even more aggressive clearing
                                import time
                                time.sleep(0.1)
                                continue
                    else:
                        # Last resort: import from fresh module with full cleanup
                        return self._import_module_fresh_isolated('pynfe.utils.nfse.nacional.DPS_v1_00')
            else:
                raise
    
    def _safe_import_evento(self):
        """Safely import evento schema handling PyXB conflicts"""
        import pyxb.exceptions_
        import pyxb.namespace
        
        try:
            # First, clear any existing namespace conflicts
            self._clear_all_pyxb_namespaces()
            from pynfe.utils.nfse.nacional import pedRegEvento_v1_00
            return pedRegEvento_v1_00
        except (pyxb.exceptions_.NamespaceUniquenessError, ImportError) as e:
            error_msg = str(e)
            if any(conflict in error_msg for conflict in ["TVerNFSe", "CryptoBinary", "NamespaceUniquenessError"]):
                # Try more aggressive cleanup for both NFSe and XMLDSig conflicts
                self._force_clear_all_namespaces()
                try:
                    from pynfe.utils.nfse.nacional import pedRegEvento_v1_00
                    return pedRegEvento_v1_00
                except Exception:
                    # Last resort: import from fresh module with full cleanup
                    return self._import_module_fresh_isolated('pynfe.utils.nfse.nacional.pedRegEvento_v1_00')
            else:
                raise
    def _clear_nacional_modules(self):
        """Clear all nacional schema modules from cache"""
        import sys
        
        modules_to_clear = [
            'pynfe.utils.nfse.nacional.DPS_v1_00',
            'pynfe.utils.nfse.nacional.pedRegEvento_v1_00',
            'pynfe.utils.nfse.nacional.tiposSimples_v1_00',
            'pynfe.utils.nfse.nacional.tiposEventos_v1_00',
            'pynfe.utils.nfse.nacional.tiposComplexos_v1_00',
            'pynfe.utils.nfse.nacional.tiposCnc_v1_00',
            # Also clear XMLDSig related modules that might cause CryptoBinary conflicts
            'pynfe.utils.nfse.nacional._ds'
        ]
        
        for module_name in modules_to_clear:
            if module_name in sys.modules:
                del sys.modules[module_name]
    
    def _clear_all_pyxb_namespaces(self):
        """Clear all problematic PyXB namespaces"""
        import pyxb.namespace
        
        # List of known problematic namespaces
        namespaces_to_clear = [
            "http://www.sped.fazenda.gov.br/nfse",  # NFSe namespace
            "http://www.w3.org/2000/09/xmldsig#"     # XML Digital Signature namespace
        ]
        
        for namespace_uri in namespaces_to_clear:
            try:
                ns = pyxb.namespace.NamespaceForURI(namespace_uri, create_if_missing=False)
                if ns is not None:
                    # Clear conflicting types from the namespace
                    if hasattr(ns, '_categoryMap'):
                        type_bindings = ns._categoryMap.get('typeBinding', {})
                        # Clear known conflicting types
                        conflicting_types = ['TVerNFSe', 'CryptoBinary']
                        for conflict_type in conflicting_types:
                            if conflict_type in type_bindings:
                                del type_bindings[conflict_type]
            except Exception:
                # If namespace clearing fails, continue
                pass
        
        # Also clear module cache
        self._clear_nacional_modules()
    
    def _force_clear_all_namespaces(self):
        """Force clear all PyXB namespaces and reinitialize"""
        import pyxb.namespace
        import sys
        
        # More aggressive namespace clearing for multiple namespace conflicts
        namespaces_to_clear = [
            "http://www.sped.fazenda.gov.br/nfse",
            "http://www.w3.org/2000/09/xmldsig#"
        ]
        
        for namespace_uri in namespaces_to_clear:
            try:
                ns = pyxb.namespace.NamespaceForURI(namespace_uri, create_if_missing=False)
                if ns is not None and hasattr(ns, '_reset'):
                    ns._reset()
            except Exception:
                pass
        
        # Clear all related modules more aggressively
        modules_to_clear = []
        for module_name in list(sys.modules.keys()):
            # Clear nacional modules and any XMLDSig related modules
            if (('nacional' in module_name and 'pynfe' in module_name) or 
                ('_ds' in module_name and 'pynfe' in module_name)):
                modules_to_clear.append(module_name)
        
        for module_name in modules_to_clear:
            del sys.modules[module_name]
    
    def _import_module_fresh_isolated(self, module_name):
        """Import module with ultra-aggressive isolation from existing namespaces"""
        import importlib.util
        import sys
        import pyxb.namespace
        
        # Ultra-aggressive namespace clearing - nuke everything PyXB related
        try:
            # Clear PyXB's internal registry completely
            if hasattr(pyxb.namespace, '_NamespaceForURI'):
                pyxb.namespace._NamespaceForURI.clear()
            if hasattr(pyxb.namespace, '_AvailableForLoad'):
                pyxb.namespace._AvailableForLoad.clear()
            if hasattr(pyxb.namespace, '_NamespaceArchive'):
                pyxb.namespace._NamespaceArchive.clear()
                
            # Nuke specific problematic namespaces completely
            namespaces_to_destroy = [
                "http://www.sped.fazenda.gov.br/nfse",
                "http://www.w3.org/2000/09/xmldsig#",
                "http://www.w3.org/2001/XMLSchema"
            ]
            
            for namespace_uri in namespaces_to_destroy:
                try:
                    ns = pyxb.namespace.NamespaceForURI(namespace_uri, create_if_missing=False)
                    if ns is not None:
                        # Completely destroy all namespace content
                        for attr in ['_categoryMap', '_typeDefinitions', '_elementDeclarations', '_attributeDeclarations']:
                            if hasattr(ns, attr):
                                getattr(ns, attr).clear()
                        
                        # Try different reset methods
                        for reset_method in ['_reset', 'reset', 'clear']:
                            if hasattr(ns, reset_method):
                                try:
                                    getattr(ns, reset_method)()
                                except Exception:
                                    pass
                        
                        # If we can access categoryMap directly, nuke CryptoBinary specifically
                        if hasattr(ns, '_categoryMap') and 'typeBinding' in ns._categoryMap:
                            if 'CryptoBinary' in ns._categoryMap['typeBinding']:
                                del ns._categoryMap['typeBinding']['CryptoBinary']
                            if 'TVerNFSe' in ns._categoryMap['typeBinding']:
                                del ns._categoryMap['typeBinding']['TVerNFSe']
                                
                except Exception:
                    # Even if individual namespace clearing fails, continue
                    pass
                    
        except Exception:
            # If ultra-aggressive clearing fails, continue anyway
            pass
            
        # Also call our standard namespace clearing
        self._force_clear_all_namespaces()
        
        # Nuclear option: Clear ALL modules related to PyXB and schemas
        modules_to_nuke = []
        for mod_name in list(sys.modules.keys()):
            if any(pattern in mod_name.lower() for pattern in [
                'pynfe.utils.nfse.nacional',
                'pynfe.utils.nfse',
                'pyxb',
                '_ds',
                'xmldsig',
                'xml.ds'
            ]):
                modules_to_nuke.append(mod_name)
        
        for mod_name in modules_to_nuke:
            try:
                del sys.modules[mod_name]
            except KeyError:
                pass
        
        # Find the module spec
        spec = importlib.util.find_spec(module_name)
        if spec is None:
            raise ImportError(f"Could not find module {module_name}")
        
        # Create a new module instance
        module = importlib.util.module_from_spec(spec)
        
        # Execute the module in isolation
        try:
            # Execute the module
            spec.loader.exec_module(module)
            return module
            
        except Exception as e:
            # Enhanced error reporting
            error_msg = str(e)
            if "NamespaceUniquenessError" in error_msg:
                if "CryptoBinary" in error_msg:
                    raise ImportError(f"PERSISTENT XMLDSig CryptoBinary conflict in {module_name}. "
                                    f"This indicates multiple schema files are defining CryptoBinary. "
                                    f"You may need to regenerate the PyXB schemas. Error: {e}")
                elif "TVerNFSe" in error_msg:
                    raise ImportError(f"PERSISTENT NFSe TVerNFSe conflict in {module_name}. "
                                    f"Multiple schema files are defining TVerNFSe. Error: {e}")
                else:
                    raise ImportError(f"PERSISTENT PyXB namespace conflict in {module_name}: {e}")
            else:
                raise ImportError(f"Failed to import {module_name} even with ultra-aggressive isolation: {e}")
    
    def _ultra_clear_xmldsig_namespace(self):
        """Ultra-aggressive clearing specifically targeting XMLDSig CryptoBinary conflicts"""
        import pyxb.namespace
        import sys
        
        # Target the XMLDSig namespace specifically
        xmldsig_namespace = "http://www.w3.org/2000/09/xmldsig#"
        
        try:
            ns = pyxb.namespace.NamespaceForURI(xmldsig_namespace, create_if_missing=False)
            if ns is not None:
                # Specifically target CryptoBinary
                if hasattr(ns, '_categoryMap') and 'typeBinding' in ns._categoryMap:
                    typeBinding = ns._categoryMap['typeBinding']
                    
                    # Remove all CryptoBinary variants
                    crypto_keys_to_remove = []
                    for key in typeBinding:
                        if 'CryptoBinary' in str(key) or 'cryptobinary' in str(key).lower():
                            crypto_keys_to_remove.append(key)
                    
                    for key in crypto_keys_to_remove:
                        del typeBinding[key]
                
                # Also clear the entire namespace if we can
                if hasattr(ns, '_categoryMap'):
                    ns._categoryMap.clear()
        except Exception:
            pass
        
        # Clear ALL modules that might contain XMLDSig references
        xmldsig_modules_to_clear = []
        for module_name in list(sys.modules.keys()):
            if any(pattern in module_name.lower() for pattern in [
                '_ds', 'xmldsig', 'xml.ds', 'pynfe.utils', '_common'
            ]):
                xmldsig_modules_to_clear.append(module_name)
        
        for mod_name in xmldsig_modules_to_clear:
            try:
                del sys.modules[mod_name]
            except KeyError:
                pass
    
    def gerar(self, nfse: NotaFiscalServico):
        """Retorna string de um XML gerado a partir do
        XML Schema (XSD). Binding gerado pelo modulo PyXB."""
        # Use safe schema import with autocomplete-friendly casting
        if TYPE_CHECKING:
            # During type checking, provide the proper type for autocomplete
            from pynfe.utils.nfse.nacional import DPS_v1_00 as _DPS
            nfse_nacional_schema = _DPS  # This gives autocomplete
        else:
            # At runtime, use the safe import method
            nfse_nacional_schema = self._get_dps_schema()
        
        tz = datetime.now().astimezone().strftime("%z")
        tz = "{}:{}".format(tz[:-2], tz[-2:])
        infdps = nfse_nacional_schema.TCInfDPS()
        infdps.Id = nfse.identificador_unico_dps
        infdps.tpAmb = nfse.ambiente
        infdps.dhEmi = nfse.data_emissao.strftime("%Y-%m-%dT%H:%M:%S") + tz
        infdps.verAplic = "1.00"
        infdps.serie = nfse.serie
        infdps.nDPS = nfse.numero
        infdps.dCompet = nfse.data_emissao.strftime("%Y-%m-%d")
        infdps.tpEmit = "1"  # 1 - Emissão de NFS-e pelo próprio prestador do serviço
        infdps.cLocEmi = obter_codigo_por_municipio(
            nfse.emitente.endereco_municipio, nfse.emitente.endereco_uf
        )

        prestador = nfse_nacional_schema.TCInfoPrestador()
        prestador.CNPJ = nfse.emitente.cnpj

        if nfse.emitente.inscricao_municipal:
            prestador.IM = nfse.emitente.inscricao_municipal
        if infdps.tpEmit != "1":
            prestador.xNome = nfse.emitente.razao_social
            # Refazer o endereço se for possível o prestador não for o emitente
            if nfse.emitente.endereco_cep:
                prestador_endereco = nfse_nacional_schema.TCEndereco()
                end_nacional = nfse_nacional_schema.TCEnderNac()
                end_nacional.CEP = nfse.emitente.endereco_cep
                end_nacional.cMun = obter_codigo_por_municipio(
                    nfse.emitente.endereco_municipio, nfse.emitente.endereco_uf
                )
                prestador_endereco.endNac = end_nacional
                prestador_endereco.xLgr = nfse.emitente.endereco_logradouro
                prestador_endereco.nro = nfse.emitente.endereco_numero
                if nfse.emitente.endereco_complemento:
                    prestador_endereco.xCpl = nfse.emitente.endereco_complemento
                prestador_endereco.xBairro = nfse.emitente.endereco_bairro
                prestador.end = prestador_endereco

        regime_tributario = nfse_nacional_schema.TCRegTrib()
        regime_tributario.opSimpNac = nfse.simples
        regime_tributario.regEspTrib = "0"  # Verificar se precisa ser passado
        prestador.regTrib = regime_tributario

        infdps.prest = prestador

        if nfse.cliente:
            tomador = nfse_nacional_schema.TCInfoPessoa()
            if nfse.cliente.tipo_documento == "CPF":
                tomador.CPF = nfse.cliente.numero_documento
            else:
                tomador.CNPJ = nfse.cliente.numero_documento
            tomador.xNome = nfse.cliente.razao_social

            if nfse.cliente.inscricao_municipal:
                tomador.IM = nfse.cliente.inscricao_municipal
            if nfse.cliente.endereco_cep:
                tomador_endereco = nfse_nacional_schema.TCEndereco()
                end_nacional = nfse_nacional_schema.TCEnderNac()
                end_nacional.CEP = nfse.cliente.endereco_cep
                end_nacional.cMun = obter_codigo_por_municipio(
                    nfse.cliente.endereco_municipio, nfse.cliente.endereco_uf
                )
                tomador_endereco.endNac = end_nacional
                tomador_endereco.xLgr = nfse.cliente.endereco_logradouro
                tomador_endereco.nro = nfse.cliente.endereco_numero
                if nfse.cliente.endereco_complemento:
                    tomador_endereco.xCpl = nfse.cliente.endereco_complemento
                tomador_endereco.xBairro = nfse.cliente.endereco_bairro
                tomador.end = tomador_endereco

            infdps.toma = tomador

        servico = nfse_nacional_schema.TCServ()

        local_prestacao = nfse_nacional_schema.TCLocPrest()
        local_prestacao.cLocPrestacao = nfse.servico.codigo_municipio
        servico.locPrest = local_prestacao

        codigo_servico = nfse_nacional_schema.TCCServ()
        codigo_servico.cTribNac = nfse.servico.codigo_tributacao_nacional
        codigo_servico.xDescServ = nfse.servico.discriminacao
        if nfse.servico.codigo_tributacao_municipal:
            codigo_servico.cTribMun = nfse.servico.codigo_tributacao_municipal

        servico.cServ = codigo_servico
        infdps.serv = servico

        valores = nfse_nacional_schema.TCInfoValores()
        valor_servico = nfse_nacional_schema.TCVServPrest()
        valor_servico.vServ = "{:.2f}".format(nfse.servico.valor_servico)
        valores.vServPrest = valor_servico

        tributos = nfse_nacional_schema.TCInfoTributacao()
        tributos_municipais = nfse_nacional_schema.TCTribMunicipal()
        tributos_municipais.tribISSQN = "1"
        tributos_municipais.tpRetISSQN = "1"
        tributos.tribMun = tributos_municipais

        tributos_totais = nfse_nacional_schema.TCTribTotal()
        valores_tributos_totais = nfse_nacional_schema.TCTribTotalMonet()
        valores_tributos_totais.vTotTribFed = "{:.2f}".format(nfse.servico.total_tributos_federais)
        valores_tributos_totais.vTotTribEst = "{:.2f}".format(nfse.servico.total_tributos_estaduais)
        valores_tributos_totais.vTotTribMun = "{:.2f}".format(
            nfse.servico.total_tributos_municipais
        )

        tributos_totais.vTotTrib = valores_tributos_totais
        tributos.totTrib = tributos_totais
        valores.trib = tributos

        infdps.valores = valores

        dps = nfse_nacional_schema.TCDPS()
        dps.infDPS = infdps
        dps.versao = "1.00"

        # Gera o XML e remove as tags ns1 do PyXB
        xml_content = dps.toxml(element_name="DPS")
        # Remove prefixos de namespace ns1: das tags de abertura e fechamento
        xml_content = re.sub(r"<ns1:", "<", xml_content)
        xml_content = re.sub(r"</ns1:", "</", xml_content)
        # Remove declarações de namespace desnecessárias
        xml_content = re.sub(r":ns1", "", xml_content)

        return xml_content

    def registrar_evento(self, evento: EventoNFSe):
        """Retorna string de um XML gerado a partir do
        XML Schema (XSD). Binding gerado pelo modulo PyXB."""
        # Use safe schema import with autocomplete-friendly casting
        if TYPE_CHECKING:
            # During type checking, provide the proper type for autocomplete
            from pynfe.utils.nfse.nacional import pedRegEvento_v1_00 as _Evento
            nfse_nacional_evento_schema = _Evento  # This gives autocomplete
        else:
            # At runtime, use the safe import method
            nfse_nacional_evento_schema = self._get_evento_schema()
        
        tz = datetime.now().astimezone().strftime("%z")
        tz = "{}:{}".format(tz[:-2], tz[-2:])

        inf_ped_registro = nfse_nacional_evento_schema.TCInfPedReg()
        inf_ped_registro.Id = evento.identificador
        inf_ped_registro.chNFSe = evento.chave
        inf_ped_registro.CNPJAutor = evento.cnpj
        inf_ped_registro.dhEvento = evento.data_emissao.strftime("%Y-%m-%dT%H:%M:%S") + tz
        inf_ped_registro.tpAmb = evento.ambiente
        inf_ped_registro.verAplic = "1.00"
        inf_ped_registro.nPedRegEvento = str(evento.n_seq_evento)

        if isinstance(evento, EventoNFSeCancelarNota):  # Cancelamento
            cancelamento = nfse_nacional_evento_schema.TE101101()
            cancelamento.xDesc = evento.descricao
            cancelamento.cMotivo = evento.justificativa_codigo
            cancelamento.xMotivo = evento.justificativa
            inf_ped_registro.e101101 = cancelamento

        registro_evento = nfse_nacional_evento_schema.TCPedRegEvt()
        registro_evento.infPedReg = inf_ped_registro
        registro_evento.versao = "1.00"

        # Gera o XML e remove as tags ns1 do PyXB
        xml_content = registro_evento.toxml(element_name="pedRegEvento")
        # Remove prefixos de namespace ns1: das tags de abertura e fechamento
        xml_content = re.sub(r"<ns1:", "<", xml_content)
        xml_content = re.sub(r"</ns1:", "</", xml_content)
        # Remove declarações de namespace desnecessárias
        xml_content = re.sub(r":ns1", "", xml_content)

        return xml_content
