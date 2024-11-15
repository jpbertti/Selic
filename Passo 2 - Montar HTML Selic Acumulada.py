import pandas as pd
import os

# Template HTML com placeholders para os valores
html_template = """
<html>
<head>
<title>SELIC MENSAL ACUMULADA &nbsp; (RFB) - PORTAL DOS ÍNDICES</title>

<link href="http://www.yahii.com.br/BAACEG5T.ico" rel="SHORTCUT ICON" />

</script></b></b></font></td>

<div align="center">
				<table border="0" width="762" cellspacing="0" cellpadding="0">
</td>
					</tr>
					<table width=100% height=25 cellpadding=0 cellspacing=0 border=0 bgcolor="#000059">
<tr align="center" bgcolor=#000059>
<td class=top12 onmouseover="style.borderColor='#666';style.backgroundColor='#990000'" onmouseout="style.borderColor='#FFFFFF';style.backgroundColor='#000059'" style="border-right:solid #FFFFFF 1px;padding-right:10px;padding-left:10px;padding-bottom:0px;"><A HREF="http://www.yahii.com.br" TARGET="_top" CLASS="linha"><font face=verdana size=1 color="#FFFFFF"><b>Home</b></font></a></td>
<td class=top12 onmouseover="style.borderColor='#666';style.backgroundColor='#990000'" onmouseout="style.borderColor='#FFFFFF';style.backgroundColor='#000059'" style="border-right:solid #FFFFFF 1px;padding-right:10px;padding-left:10px;padding-bottom:0px;"><A HREF="http://www.yahii.com.br/Canais.html" TARGET="_top" CLASS="linha"><font face=verdana size=1 color="#FFFFFF"><b>Canais</b></font></a></td>
<td class=top12 onmouseover="style.borderColor='#666';style.backgroundColor='#990000'" onmouseout="style.borderColor='#FFFFFF';style.backgroundColor='#000059'" style="border-right:solid #FFFFFF 1px;padding-right:10px;padding-left:10px;padding-bottom:0px;"><A HREF="http://www.yahii.com.br/Consultas.html" TARGET="_top" CLASS="linha"><font face=verdana size=1 color="#FFFFFF"><b>Consultas</b></font></a></td>
<td class=top12 onmouseover="style.borderColor='#666';style.backgroundColor='#990000'" onmouseout="style.borderColor='#FFFFFF';style.backgroundColor='#000059'" style="border-right:solid #FFFFFF 1px;padding-right:10px;padding-left:10px;padding-bottom:0px;"><A HREF="http://www.yahii.com.br/Downloads.html" TARGET="_top" CLASS="linha"><font face=verdana size=1 color="#FFFFFF"><b>Downloads</b></font></a></td>
<td class=top12 onmouseover="style.borderColor='#666';style.backgroundColor='#990000'" onmouseout="style.borderColor='#FFFFFF';style.backgroundColor='#000059'" style="border-right:solid #FFFFFF 1px;padding-right:10px;padding-left:10px;padding-bottom:0px;"><A HREF="http://www.manager.com.br/index.html" TARGET="_top" CLASS="linha"><font face=verdana size=1 color="#FFFFFF"><b>Empregos</b></font></a></td>
<td class=top12 onmouseover="style.borderColor='#666';style.backgroundColor='#990000'" onmouseout="style.borderColor='#FFFFFF';style.backgroundColor='#000059'" style="border-right:solid #FFFFFF 1px;padding-right:10px;padding-left:10px;padding-bottom:0px;"><A HREF="http://www.yahii.com.br/Diversao.html" TARGET="_top" CLASS="linha"><font face=verdana size=1 color="#FFFFFF"><b>Entretenimento</b></font></a></td>
<td class=top12 onmouseover="style.borderColor='#666';style.backgroundColor='#990000'" onmouseout="style.borderColor='#FFFFFF';style.backgroundColor='#000059'" style="border-right:solid #FFFFFF 1px;padding-right:10px;padding-left:10px;padding-bottom:0px;"><A HREF="http://maps.google.com.br/maps?q=www.yahii.com.br&hl=pt-BR&rlz=1R2PRFB_pt-BRBR456&bav=on.2,or.r_gc.r_pw.,cf.osb&biw=1360&bih=585&wrapid=tlif132254551462510&um=1&ie=UTF-8&ei=h3HUTuDeDsTbtweys8SGAg&sa=X&oi=mode_link&ct=mode&cd=3&ved=0CB0Q_AUoAg" TARGET="_top" CLASS="linha"><font face=verdana size=1 color="#FFFFFF"><b>Nossa Sede</b></font></a></td>
<td class=top12 onmouseover="style.borderColor='#666';style.backgroundColor='#990000'" onmouseout="style.borderColor='#FFFFFF';style.backgroundColor='#000059'" style="border-right:solid #FFFFFF 1px;padding-right:10px;padding-left:10px;padding-bottom:0px;"><A HREF="http://www.yahii.com.br/Servicos.html" TARGET="_top" CLASS="linha"><font face=verdana size=1 color="#FFFFFF"><b>Serviços</b></font></a></td>
</tr></table><BR>


<head>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({
          google_ad_client: "ca-pub-3267321372182803",
          enable_page_level_ads: true
     });
</script>
</head>


  <tr>
  <CENTER><td width="100%" colspan="5" bgcolor="#FFFFFF" align="center" height="20"><font
    color="#000000" size="-3" face="Tahoma"><script language="javascript">

<head>

<table border="0" width="900" cellspacing="0" align="left" height="100">
  <tr>

</script><center></b></b></font></td><BR>

  <tr>
    <td width="900" colspan="5" bgcolor="FFFFFF" align="center" height="15"><font
    color="#141414" size="-3" face="Tahoma"><script language="javascript">

document.write("<font color='#000000' font size='1' font face='verdana'>")
var mydate=new Date()
var year=mydate.getYear()
if (year<2000)
year += (year < 1900) : 0
var day=mydate.getDay()
var month=mydate.getMonth()
var daym=mydate.getDate()
if (daym<10)
daym="0"+daym
var dayarray=new Array("Domingo","Segunda-feira","Terça-feira","Quarta-feira","Quinta-feira","Sexta-feira","Sábado")
var montharray=new Array(" de janeiro de "," de fevereiro de "," de março de ","de abril de ","de maio de ","de junho de","de julho de ","de agosto de ","de setembro de "," de outubro de "," de novembro de "," de dezembro de ")
document.write("   "+dayarray[day]+", "+daym+" "+montharray[month]+year+" ")
document.write("</b></i></font>")
</script>




<SCRIPT LANGUAGE="JAVASCRIPT">
<!--

var now = new Date();
var mName = now.getMonth() +1 ;
var dName = now.getDay() +1;
var dayNr = now.getDate();
var yearNr=now.getYear();
if(dName==1) {Day = "Domingo";}
if(dName==2) {Day = "Segunda-feira";}
if(dName==3) {Day = "Terça-feira";}
if(dName==4) {Day = "Quarta-feira";}
if(dName==5) {Day = "Quinta-feira";}
if(dName==6) {Day = "Sexta-feira";}
if(dName==7) {Day = "Sábado";}
if(mName==1){Month = "janeiro";}
if(mName==2){Month = "fevereiro";}
if(mName==3){Month = "março";}
if(mName==4){Month = "abril";}
if(mName==5){Month = "maio";}
if(mName==6){Month = "junho";}
if(mName==7){Month = "julho";}
if(mName==8){Month = "agosto";}
if(mName==9){Month = "setembro";}
if(mName==10){Month = "outubro";}
if(mName==11){Month = "novembro";}
if(mName==12){Month = "dezembro";}
if(yearNr < 2000) {Year = 1900 + yearNr;}
else {Year = yearNr;}
var todaysDate =(" " + Day + ", " + dayNr + " de " + Month + " de " + Year);

document.write('  '+todaysDate);

//-->
</SCRIPT>

</font></td>
  </tr>
  <tr>



<html>

<head>

<!---DESABILITA BOTAO DIREITO DO MOUSE COMEÇA AQUI---->
<script language="JavaScript1.3"> 

if (window.Event) 
document.captureEvents(Event.MOUSEUP); 

function nocontextmenu() 
{ 
event.cancelBubble = true 
event.returnValue = false; 

return false; 
} 

function norightclick(e) 
{ 
if (window.Event) 
{ 
if (e.which == 2 || e.which == 3) 
return false; 
} 
else 
if (event.button == 2 || event.button == 3) 
{ 
event.cancelBubble = true 
event.returnValue = false; 
return false; 
} 

} 
if (document.layers) { 
document.captureEvents(Event.MOUSEDOWN); 
} 
document.oncontextmenu = nocontextmenu; 
document.onmousedown = norightclick; 
document.onmouseup = norightclick; 
//--> 
</script>
<!---DESABILITA BOTAO DIREITO DO MOUSE TERMINA AQUI----->


<BR>
<BR>


</SCRIPT>
<LINK REL=stylesheet TYPE="text/css" HREF="styles.css">
</HEAD>
<BODY BGCOLOR="#FFFFFF" LINK="#990000" VLINK="#000000" ALINK="#909090" LEFTMARGIN=0 TOPMARGIN=0 MARGINWIDTH=0 MARGINHEIGHT=0>
<TABLE WIDTH="700" BORDER="0" CELLSPACING="0" CELLPADDING="0">
<TR><TD ALIGN="CENTER">



<!-- /AdSpace -->
</TD></TR></table>


<center>
<form>
<select size="1" onChange="location = options[selectedIndex].value">
<option selected>ÍNDICES ECONÔMICOS</option>

<option value="http://www.yahii.com.br/Indices.html">&nbsp</option>
<option value="http://www.yahii.com.br/Indices.html">ÍNDICES DE INFLAÇÃO, CÂMBIO, JUROS, INDEXADORES, POUPANÇA</option>
<option value="http://www.yahii.com.br/AluguelMensal.html">Aluguéis Residenciais &nbsp;&nbsp; (BDI)</option>
<option value="http://www.yahii.com.br/BalancaComercial.html">Balança Comercial &nbsp;&nbsp; (BACEN)</option>
<option value="http://www.yahii.com.br/btn.html">BTN &nbsp;&nbsp; + &nbsp;&nbsp; TR &nbsp;&nbsp; (BDI)</option>
<option value="http://www.yahii.com.br/cetip.html">Certificado de Depósito Intercambiário - CDI &nbsp;&nbsp; (CETIP)</option>
<option value="http://www.yahii.com.br/cormon.html">Correção Monetária &nbsp; - &nbsp; ORTN - OTN - BTN - TR&nbsp; (BACEN)</option>
<option value="http://www.yahii.com.br/cubsp.html">CUB / SP &nbsp; - &nbsp; Desonerado &nbsp;&nbsp; (SINDUCSON)</option>
<option value="http://www.yahii.com.br/cubspSD.html">CUB / SP &nbsp; - &nbsp; Sem Desoneração &nbsp;&nbsp; (SINDUCSON)</option>
<option value="http://www.yahii.com.br/DolarDiario.html">Dólar Comercial Oficial - Índice Diário &nbsp;&nbsp; (BACEN)</option>
<option value="http://www.yahii.com.br/dolar.html">Dólar Comercial Oficial - Índice Mensal &nbsp;&nbsp; (BACEN)</option>
<option value="http://www.yahii.com.br/EuroDiario.html">Euro / R$ Real - Índice Diário &nbsp;&nbsp; (BACEN)</option>
<option value="http://www.yahii.com.br/euro.html">Euro / US$ Dólar PTAX - Índice Mensal &nbsp;&nbsp; (BACEN)</option>
<option value="http://www.yahii.com.br/fgts.html">FGTS &nbsp;&nbsp;&nbsp; (CEF)</option>
<option value="http://www.yahii.com.br/icv.html">ICV &nbsp;&nbsp;&nbsp; (DIEESE)</option>
<option value="http://www.yahii.com.br/igpm.html">Igp-M &nbsp;&nbsp;&nbsp; (FGV)</option>
<option value="http://www.yahii.com.br/igpdi.html">Igp-DI &nbsp;&nbsp;&nbsp; (FGV)</option>
<option value="http://www.yahii.com.br/igp10.html">Igp-10 &nbsp;&nbsp;&nbsp; (FGV)</option>
<option value="http://www.yahii.com.br/irenda.html">Imposto de Renda &nbsp;&nbsp; (SRF)</option>
<option value="http://www.yahii.com.br/incc.html">Incc-DI &nbsp;&nbsp;&nbsp; (FGV)</option>
<option value="http://www.yahii.com.br/inccM.html">Incc-M &nbsp;&nbsp;&nbsp; (FGV)</option>
<option value="http://www.yahii.com.br/iieBR.html">Indicador de Incerteza da Economia - Brasil &nbsp;&nbsp; (FGV)</option>
<option value="http://www.yahii.com.br/inpc.html">Inpc &nbsp;&nbsp; (IBGE)</option>
<option value="http://www.yahii.com.br/ipaDI.html">Ipa-DI &nbsp;&nbsp; (FVG)</option>
<option value="http://www.yahii.com.br/ipaM.html">Ipa-M &nbsp;&nbsp; (FVG)</option>
<option value="http://www.yahii.com.br/ipcfipe.html">Ipc &nbsp;&nbsp; (FIPE)</option>
<option value="http://www.yahii.com.br/ipc.html">Ipc-DI &nbsp;&nbsp; (FGV)</option>
<option value="http://www.yahii.com.br/ipca.html">Ipca &nbsp;&nbsp; (IBGE)</option>
<option value="http://www.yahii.com.br/ipca15.html">Ipca-15 &nbsp;&nbsp; (IBGE)</option>
<option value="http://www.yahii.com.br/ipcaE.html">Ipca-E - Índice Trimestral Acumulado &nbsp;&nbsp; (IBGE)</option>
<option value="http://www.yahii.com.br/ipcaE_Historico.html">Ipca-E - Série Histórica &nbsp;&nbsp; (IBGE)</option>
<option value="http://www.yahii.com.br/ivar.html">IVAR &nbsp;&nbsp; (FGV)</option>
<option value="http://www.yahii.com.br/NovaPoupancaDiaria.html">Nova Poupança - Índice Diário - M.P. nº 567, de 03.05.2012 &nbsp;&nbsp; (BACEN)</option>
<option value="http://www.yahii.com.br/PoupancaDiaria.html">Poupança - Índice Diário &nbsp;&nbsp; (BACEN)</option>
<option value="http://www.yahii.com.br/poupanca.html">Poupança - Índice Mensal &nbsp;&nbsp; (BACEN)</option>
<option value="http://www.yahii.com.br/selic.html">Selic Mensal &nbsp;&nbsp; (SRF)</option>
<option value="http://www.yahii.com.br/SelicAcumulada.html">Selic Mensal Acumulada &nbsp;&nbsp; (SRF)</option>
<option value="http://www.yahii.com.br/TaxasSelic.html">Taxa Selic - R e u n i õ e s &nbsp; d o &nbsp; C O P O M &nbsp;&nbsp; (BACEN)</option>
<option value="http://www.yahii.com.br/tjlp.html">TJLP - Taxa de Juros de Longo Prazo &nbsp;&nbsp; (SRF)</option>
<option value="http://www.yahii.com.br/TJLPTrimestral.html">TJLP - Taxa de Juros de Longo Prazo &nbsp;&nbsp; (BNDES)</option>
<option value="http://www.yahii.com.br/TLP_Fixa.html">TLP - Taxa de Juros Real Fixa &nbsp;&nbsp; (BNDES)</option>
<option value="http://www.yahii.com.br/tbf.html">TBF - Taxa Básica Financeira &nbsp;&nbsp; (BACEN)</option>
<option value="http://www.yahii.com.br/TRIndiceDiario.html">TR - Índice Diário &nbsp;&nbsp; (BACEN)</option>
<option value="http://www.yahii.com.br/tr.html">TR - Índice Mensal &nbsp;&nbsp; (BACEN)</option>
<option value="http://www.yahii.com.br/Ufesp.html">UFESP - Unidade Fiscal do Estado de São Paulo</option>
<option value="http://www.yahii.com.br/Upc.html">UPC - Unidade Padrão de Capital &nbsp;&nbsp; (BACEN)</option>


<option value="http://www.yahii.com.br/Indices.html">&nbsp</option>
<option value="http://www.yahii.com.br/Indices.html">DÉBITOS JUDICIAIS</option>

<option value="http://www.yahii.com.br/debjudSP.html">Tabela para Atualização de Débitos Judiciais do Tribunal de Justiça de São Paulo &nbsp;&nbsp; (TJSP)</option>
<option value="http://www.tjsp.jus.br/Download/Tabelas/Tabela_IPCA-E.pdf">Tabela para Cálculos de Atualização Monetária das Fazendas Públicas - IPCA-E &nbsp;&nbsp; (TJSP)</option>
<option value="http://cgj.tjrj.jus.br/documents/1017893/1616539/correcao-monetaria-2020.pdf/0e6330cb-4bfa-9c37-2bed-0e96f2edb55e?version=1.5">Tabela para Cálculos de Atualização Monetária das Fazendas Públicas &nbsp;&nbsp; (TJRJ)</option>
<option value="http://www.yahii.com.br/jurosdemora.html">Tabela para Cálculo dos Juros de Mora - ICMS/ITCMD &nbsp;&nbsp; (SEFAZ/SP)</option>
<option value="https://www2.jf.jus.br/phpdoc/sicom/tabelaCorMor.php?PHPSESSID=70eku05iojp1d0l489uv5tflb7">Tabela de Correção Monetária do Conselho da Justiça Federal &nbsp;&nbsp; (CJF)</option>
<option value="http://www.yahii.com.br/custasSTF.pdf">Tabela de Custas do Supremo Tribunal Federal &nbsp;&nbsp; (STF)</option>
<option value="http://www.yahii.com.br/custasSTJ.pdf">Tabela de Custas do Superior Tribunal de Justiça &nbsp;&nbsp; (STJ)</option>
<option value="http://www.yahii.com.br/novas-custasRJ-2021.pdf">Tabela de Custas e Taxas Judiciais do Tribunal de Justiça do Rio de Janeiro &nbsp;&nbsp; (TJRJ)</option>
<option value="http://www.yahii.com.br/DespesasTJSP.html">Tabela de Despesas Processuais do Tribunal de Justiça de São Paulo &nbsp;&nbsp; (TJSP)</option>
<option value="http://www.yahii.com.br/custasTST.html">Tabela de Valores para Depósito Recursal do Tribunal Superior do Trabalho (TST)</option>
<option value="http://www.yahii.com.br/TaxasJudiciarias.html">Tabela de Valores das Taxas Judiciárias &nbsp;&nbsp; (TJSP)</option>
<option value="http://www.yahii.com.br/TabelasAnoreg.html">Tabela dos Notários e Registradores do Estado de São Paulo &nbsp;&nbsp; (ANOREG)</option>
<option value="http://www.yahii.com.br/TRF3Regiao.html">Tabelas do Tribunal Regional Federal da 3ª Região &nbsp;&nbsp; (TRF)</option>
<option value="http://www.yahii.com.br/TabelaModulada.html">Tabela para Cálculos da Tabela Modulada - Lei Federal nº 11.960/09 &nbsp;&nbsp; (TJSP)</option>
<option value="http://www.yahii.com.br/TabelaModuladaTJRJ.pdf">Tabela para Cálculos da Tabela Modulada - Lei Federal nº 11.960/09 &nbsp;&nbsp; (TJRJ)</option>
<option value="http://www.yahii.com.br/TabelaUnicaTRT.html">Tabela Única para Atualização de Débitos Trabalhistas &nbsp;&nbsp; (TST)</option>


<option value="http://www.yahii.com.br/Indices.html">&nbsp</option>
<option value="http://www.yahii.com.br/Indices.html">ÍNDICES COM ATUALIZAÇÃO ANUAL</option>
<option value="http://www.yahii.com.br/Salariofa.html">Salário-Família &nbsp;&nbsp; (Ministério da Previdência Social)</option>
<option value="http://www.yahii.com.br/LimiteSFHistorico.html">Salário-Família - Valor limite para direito à cota &nbsp;&nbsp; (Série Histórica)</option>
<option value="http://www.yahii.com.br/Salariomi.html">Salário Mínimo Nacional</option>
<option value="http://www.yahii.com.br/PSRegional.html">Salário Mínimo Regional &nbsp;&nbsp; (Estado de São Paulo)</option>
<option value="http://www.yahii.com.br/sd.html">Seguro Desemprego &nbsp;&nbsp; (Ministério do Trabalho e Emprego)</option>
<option value="http://www.yahii.com.br/SDHistorico.html">Seguro Desemprego - Série Histórica &nbsp;&nbsp; (Ministério do Trabalho e Emprego)</option>


<option value="http://www.yahii.com.br/Indices.html">&nbsp</option>
<option value="http://www.yahii.com.br/Indices.html">PREVIDÊNCIA SOCIAL</option>
<option value="https://sipa.inss.gov.br/SipaINSS/pages/atucadend/atucadendInicio.xhtml">Atualização de Endereço do Segurado &nbsp;&nbsp; (INSS)</option>
<option value="http://www.yahii.com.br/calculoINSS.html">Cálculo de Contribuições Previdenciárias &nbsp;&nbsp; (INSS)</option>
<option value="https://meu.inss.gov.br/central/index.html#/">Carta de Concessão de Benefício &nbsp;&nbsp; (INSS)</option>
<option value="https://www.inss.gov.br/servicos-do-inss/simulacao/">Simulação da Contagem de Tempo de Contribuição &nbsp;&nbsp; (INSS)</option>
<option value="http://www.yahii.com.br/inss.html">Tabela de Contribuições ao INSS</option>
<option value="http://www.yahii.com.br/reajuste.html">Tabela de Reajuste de Benefícios do INSS</option>
<option value="http://www.yahii.com.br/beneficios.html">Tabela de Pagamento de Benefícios do INSS</option>


<option value="http://www.yahii.com.br/Indices.html">&nbsp</option>
<option value="http://www.yahii.com.br/Indices.html">OUTROS ÍNDICES</option>
<option value="http://www.yahii.com.br/Fap1991.html">FAP - Fundo de Atualização Patrimonial &nbsp;&nbsp; (SRF) &nbsp;&nbsp; (Extinto)</option>
<option value="http://www.yahii.com.br/IGMCI.html">IGMI-C - Índice Geral do Mercado Imobiliário - Comércial &nbsp;&nbsp; (FGV) &nbsp;&nbsp; (Extinto)</option>
<option value="http://www.yahii.com.br/IpcIBGE.html">IPC - Índice de Preços ao Consumidor &nbsp;&nbsp; (IBGE) &nbsp;&nbsp; (Extinto)</option>
<option value="http://www.yahii.com.br/HistoricoIpmfCpmf.html">IPMF e CPMF - Histórico das Alterações &nbsp;&nbsp; (BACEN) &nbsp;&nbsp; (Extinto)</option>
<option value="http://www.yahii.com.br/IpcR.html">IPC-R - Índice de Preços ao Consumidor do Real &nbsp;&nbsp; (IBGE) &nbsp;&nbsp; (Extinto)</option>
<option value="http://www.yahii.com.br/MVR.html">MVR - Maior Valor de Referência &nbsp;&nbsp; (Extinto)</option>
<option value="http://www.yahii.com.br/Ufir.html">UFIR - Unidade Fiscal de Referência &nbsp;&nbsp; (Extinto)</option>
<option value="http://www.yahii.com.br/Urv.pdf">URV - Unidade Real de Valor &nbsp; (Medida Provisória nº 482) &nbsp;&nbsp; (Extinto)</option>


<option value="http://www.yahii.com.br/Indices.html">&nbsp</option>
<option value="http://www.yahii.com.br/Indices.html">UTILITÁRIOS FISCAIS E FINANCEIROS</option>
<option value="http://www.yahii.com.br/conversordemoedas.html">Conversor de Moedas &nbsp;&nbsp; (FinanceOne)</option>
<option value="http://www.yahii.com.br/IRhistorico.html">Imposto de Renda - Tabelas Históricas &nbsp;&nbsp; (RFB)</option>
<option value="http://www.yahii.com.br/Moedas.html">Moeda Nacional - Histórico das Alterações &nbsp;&nbsp; (BACEN)</option>
<option value="http://www.yahii.com.br/compe.html">Motivos de Devolução de Cheques e Outros Papéis &nbsp;&nbsp; (BACEN)</option>
<option value="http://www.yahii.com.br/Simples_Nacional.html">Simples Nacional - Tabelas &nbsp;&nbsp; (RFB)</option>
<option value="http://www.yahii.com.br/ConsultasPatrimoniais.html">Sistemas de Consultas Patrimoniais &nbsp;&nbsp; (CNJ e OUTROS)</option>
<option value="http://www.yahii.com.br/TarifasBancarias.html">Tarifas Bancárias &nbsp;&nbsp; (BACEN)</option>
<option value="http://www.yahii.com.br/TaxasSelic.html">Taxa SELIC &nbsp;&nbsp; (COPOM)</option>


<option value="http://www.yahii.com.br/Indices.html">&nbsp</option>
<option value="http://www.yahii.com.br/Indices.html">TABELA DE JUROS</option>
<option value="https://www.debit.com.br/tabelas/juros-simples-e-compostos.php?percentual=0.5">Juros de 0,5% ao mês</option>
<option value="https://www.debit.com.br/tabelas/juros-simples-e-compostos.php?percentual=1">Juros de 1,0% ao mês</option>
<option value="https://www.debit.com.br/tabelas/juros-simples-e-compostos.php?percentual=1.5">Juros de 1,5% ao mês</option>
<option value="https://www.debit.com.br/tabelas/juros-simples-e-compostos.php?percentual=2">Juros de 2,0% ao mês</option>


<option value="http://www.yahii.com.br/Indices.html">&nbsp</option>
<option value="http://www.yahii.com.br/Indices.html">UTILITÁRIOS JURÍDICOS</option>
<option value="http://www.oab.org.br/CodEticaDisciplina.pdf">Código de Ética e Disciplina da O.A.B &nbsp;&nbsp; (pdf)</option>
<option value="http://www.yahii.com.br/fgtsSEFIP.html">FGTS - Códigos de Movimentação SEFIP &nbsp;&nbsp; (CEF)</option>
<option value="http://www.yahii.com.br/lei8906.html">Estatuto da Advocacia - Lei 8.906/94</option>
<option value="http://www.yahii.com.br/DepositoJudicial.pdf">Guia de Depósito Judicial &nbsp;&nbsp; (BANCO DO BRASIL)</option>
<option value="http://www.yahii.com.br/FEDTJ.pdf">Guia de Recolhimento do Fundo Especial de Despesas do TJ de São Paulo &nbsp;&nbsp; (TJSP)</option>
<option value="http://www.yahii.com.br/ITCMD.html">I T C M D &nbsp;&nbsp; (SEFAZ/SP)</option>
<option value="http://www.presidencia.gov.br/legislacao/">Legislação e Publicações da Presidência da República Federativa do Brasil</option>
<option value="http://www.yahii.com.br/Lei11608.html">Lei de Taxas Judiciárias</option>
<option value="https://www.gov.br/planalto/pt-br/conheca-a-presidencia/ministros">Ministérios</option>
<option value="http://www.yahii.com.br/MPEstadual.html">Ministérios Públicos Estaduais</option>
<option value="http://www.yahii.com.br/MPFederal.html">Ministérios Públicos Federais</option>
<option value="http://www.yahii.com.br/PGEstado.html">Procuradorias Gerais do Estado</option>
<option value="http://www.yahii.com.br/SecEstFazendas.html">Secretarias Estaduais da Fazenda</option>
<option value="http://www.yahii.com.br/SumulasSTJ.pdf">Súmulas do S. T. J.</option>
<option value="http://www.yahii.com.br/SumulasSTF.html">Súmulas do S. T. F.</option>
<option value="http://www.yahii.com.br/Honorarios.pdf">Tabela de Honorários Advocatícios</option>
<option value="http://www.yahii.com.br/Tribunais.html">Tribunais</option>
<option value="http://www.yahii.com.br/TREleitoral.html">Tribunais Regionais Eleitorais</option>


<option value="http://www.yahii.com.br/Indices.html">&nbsp</option>
<option value="http://www.yahii.com.br/Indices.html">IR PARA A PÁGINA ÍNDICES ECONÔMICOS</option>
<option value="http://www.yahii.com.br">VOLTAR PARA A PÁGINA PRINCIPAL</option>
</select>
</form>
</center>

&nbsp;
<BR>
<BR>
<BR>
<BR>

</TABLE>
<H2><FONT face=Verdana><center><B>SELIC  &nbsp; MENSAL &nbsp; ACUMULADA<BR></B></FONT></SMALL></H2>


</TABLE>
<H2><SMALL><FONT face=Verdana color=000090 size=4><B>Taxa Referencial do Sistema Especial de Liquidação<br>e de Custódia para Títulos 
Federais</B></FONT></SMALL></H2>



<DIV align=center>
<CENTER>

<TABLE cellSpacing=0  borderColorDark=#ffffff cellPadding=4 
width=720 borderColorLight=#999999 border=0>

              <TR bgColor=#ffffff>
                <TD align=center height=20 colstart="2">
                  <DIV align=justify><FONT 
                  face=verdana color=000000 size=3>

Os juros de mora, incidentes sobre tributos federais, cujos fatos geradores tenham ocorrido
a partir de 1º de janeiro de 1995, devem ser calculados <font color=000090><B>no mês de setembro de 2024</B></FONT>,
nos percentuais abaixo indicados, conforme o mês em que se venceu o prazo legal para pagamento.</TD></TR></TBODY></TABLE></CENTER></DIV></BODY></HTML><P>



</TABLE>
<H2><SMALL><FONT face=Verdana color=990000><B>1995 &nbsp a &nbsp; 2024</B></FONT></SMALL></H2>



<FONT FACE=VERDANA SIZE=1,5 COLOR=004040><CENTER><B><I>Índices Percentuais</B></FONT><P></I></FONT>





<FONT FACE="Arial" SIZE="2"><FONT COLOR="#000090"><B><CENTER>Busca rápida no site</B>


<!-- start of freefind search box html -->
<center><table cellpadding=0 cellspacing=0 border=0 align=center>
<tr>
	<td  style="font-family: Arial, Helvetica, sans-serif; font-size: 7.5pt;">
		<center><table width="90%" cellpadding=0 cellspacing=0 border=0  style="font-family: Arial, Helvetica, sans-serif; font-size: 7.5pt;">
		</table></left>
		<form style="margin:0px; margin-top:4px;" action="http://search.freefind.com/find.html" method="get" accept-charset="utf-8" target="_self">
		<input type="hidden" name="si" value="10010452">
		<input type="hidden" name="pid" value="r">
		<input type="hidden" name="n" value="0">
		<input type="hidden" name="_charset_" value="">
		<input type="hidden" name="bcd" value="&#247;">
		<input type="text" name="query" size="15"> 
		<input type="submit" value="buscar">
		</form>
	</td>
</tr>
<tr>
	<td style="text-align:center; font-family: Arial, Helvetica, sans-serif;	font-size: 7.5pt; padding-top:4px;">
		<a style="text-decoration:none; color:gray;" href="http://www.freefind.com" >search engine</a><a style="text-decoration:none; color:gray;" href="http://www.freefind.com" > by
		<span style="color: #606060;">freefind</span></a>
	</td>
</tr>
</table>

&nbsp;


   <TABLE id="tabela_selic" cellSpacing=0 cellPadding=2 border=1>
      <TBODY>
        <TR>
          <TD width=65 COLSTART="1" bgColor=#e6dbcf><STRONG><FONT face=Verdana size=3><CENTER>A/M</CENTER></FONT></STRONG></TD>
          <TD align=middle width=66 COLSTART="10" bgColor=#e6dbcf><FONT face=Verdana size=3><B>JAN</B></FONT></TD>
          <TD align=middle width=66 COLSTART="10" bgColor=#e6dbcf><FONT face=Verdana size=3><B>FEV</B></FONT></TD>
          <TD align=middle width=66 COLSTART="10" bgColor=#e6dbcf><FONT face=Verdana size=3><B>MAR</B></FONT></TD>
          <TD align=middle width=66 COLSTART="10" bgColor=#e6dbcf><FONT face=Verdana size=3><B>ABR</B></FONT></TD>
          <TD align=middle width=66 COLSTART="10" bgColor=#e6dbcf><FONT face=Verdana size=3><B>MAI</B></FONT></TD>
          <TD align=middle width=66 COLSTART="10" bgColor=#e6dbcf><FONT face=Verdana size=3><B>JUN</B></FONT></TD>
          <TD align=middle width=66 COLSTART="10" bgColor=#e6dbcf><FONT face=Verdana size=3><B>JUL</B></FONT></TD>
          <TD align=middle width=66 COLSTART="10" bgColor=#e6dbcf><FONT face=Verdana size=3><B>AGO</B></FONT></TD>
          <TD align=middle width=66 COLSTART="10" bgColor=#e6dbcf><FONT face=Verdana size=3><B>SET</B></FONT></TD>
          <TD align=middle width=66 COLSTART="10" bgColor=#e6dbcf><FONT face=Verdana size=3><B>OUT</B></FONT></TD>
          <TD align=middle width=66 COLSTART="10" bgColor=#e6dbcf><FONT face=Verdana size=3><B>NOV</B></FONT></TD>
          <TD align=middle width=66 COLSTART="10" bgColor=#e6dbcf><FONT face=Verdana size=3><B>DEZ</B></FONT></TD>
        </TR>
        {table_data}
        <TR>
          <TD width=35 COLSTART="1" bgColor=#e6dbcf><STRONG><FONT face=Verdana size=3><CENTER>A/M</CENTER></FONT></STRONG></TD>
          <TD align=middle width=66 COLSTART="10" bgColor=#e6dbcf><FONT face=Verdana size=3><B>JAN</B></FONT></TD>
          <TD align=middle width=66 COLSTART="10" bgColor=#e6dbcf><FONT face=Verdana size=3><B>FEV</B></FONT></TD>
          <TD align=middle width=66 COLSTART="10" bgColor=#e6dbcf><FONT face=Verdana size=3><B>MAR</B></FONT></TD>
          <TD align=middle width=66 COLSTART="10" bgColor=#e6dbcf><FONT face=Verdana size=3><B>ABR</B></FONT></TD>
          <TD align=middle width=66 COLSTART="10" bgColor=#e6dbcf><FONT face=Verdana size=3><B>MAI</B></FONT></TD>
          <TD align=middle width=66 COLSTART="10" bgColor=#e6dbcf><FONT face=Verdana size=3><B>JUN</B></FONT></TD>
          <TD align=middle width=66 COLSTART="10" bgColor=#e6dbcf><FONT face=Verdana size=3><B>JUL</B></FONT></TD>
          <TD align=middle width=66 COLSTART="10" bgColor=#e6dbcf><FONT face=Verdana size=3><B>AGO</B></FONT></TD>
          <TD align=middle width=66 COLSTART="10" bgColor=#e6dbcf><FONT face=Verdana size=3><B>SET</B></FONT></TD>
          <TD align=middle width=66 COLSTART="10" bgColor=#e6dbcf><FONT face=Verdana size=3><B>OUT</B></FONT></TD>
          <TD align=middle width=66 COLSTART="10" bgColor=#e6dbcf><FONT face=Verdana size=3><B>NOV</B></FONT></TD>
          <TD align=middle width=66 COLSTART="10" bgColor=#e6dbcf><FONT face=Verdana size=3><B>DEZ</B></FONT></TD>
        </TR>
      </TBODY>
    </TABLE></BODY></HTML><BR>



&nbsp;


<DIV align=center>
<CENTER>

<TABLE cellSpacing=0  borderColorDark=#ffffff cellPadding=0 
width=450 borderColorLight=#999999 border=1>

              <TR bgColor=#e6dbcf>
                <TD align=middle height=20 colstart="2">
                  <DIV align=center><FONT 
                  face=verdana color=000000 size=2><B>TAXA DE JUROS SELIC</B></A></B></FONT></TD></TR>

              <TR bgColor=#faf3eb>
                <TD align=middle height=20 colstart="2">
                  <DIV align=center><FONT 
                  face=verdana color=000000 size=2><a href=http://www.yahii.com.br/Selic.html><font color=000000><B>SELIC MENSAL</B></A></TD></TR></TBODY></TABLE></CENTER></DIV></BODY></HTML><BR>


&nbsp;
<BR>



        <TR>

        <TD borderColor=FFFCCC borderColorLight=FFFCCC bgColor=FFFCCC
        borderColorDark=FFFCCC colSpan=3 height=2><FONT face=Verdana 
        size=1 color=000000><CENTER>Fonte:<b><font color=000000><A href="https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/pagamentos-e-parcelamentos/taxa-de-juros-selic#Selicmensalmente">Secretaria da Receita Federal (SRF)</a></b></font>

        <TR>


<p>


</table>
</body></html>

<BR>
<BR>


<script language="Javascript">
function imprimir()
	{
	//if (NS){
	//	self.window.focus();
	//	self.window.print();
		window.print();
	}
	//else{
	//	var WebBrowser = '<OBJECT ID="WebBrowser1" WIDTH=0 HEIGHT=0 CLASSID="CLSID:8856F961-340A-11D0-A96B-00C04FD705A2"></OBJECT>';
	//	document.body.insertAdjacentHTML('beforeEnd', WebBrowser);
	//	WebBrowser1.ExecWB(6, 2);//Use a 1 vs. a 2 for a prompting dialog box    WebBrowser1.outerHTML = "";
	//}
//}


</script>

								<script language="Javascript">
									//var NS = (navigator.appName == "Netscape");
									//var VERSION = parseInt(navigator.appVersion);
									//if (VERSION > 3) {
									//   document.write('<form><input type=button value="Imprimir" name="cmdImprimir" onClick="print()">&nbsp;&nbsp;<input type="button" name="cmdLogin" value="  Voltar  " onClick="javascript:login()"></form>');
									//}
										{
											document.write('<form id=form1 name=form1><input type=button value="Imprimir" name="cmdImprimir" onClick="imprimir()"></form>');
										}
								</script>

&nbsp

</table>
</body></html>

<STYLE>
body    {   font                :   arial;
        font-weight             :   normal;
        font-style              :   normal;
        color                   :   black;
        text-decoration         :   none;
        margin                  :   0.01in; }
a:link  {   font-style          :   normal;
        text-decoration         :   none; }
a.n1:link { color : red; }
a:active{   font-style          :   normal;
        text-decoration         :   none; }
a:visited{  text-decoration     :   none;
        font-style              :   normal; }
a:hover{    text-decoration     :   underline; }
</STYLE>
<SCRIPT LANGUAGE="JavaScript">
<!--
function openAnyWindow(url, name) {
  var l = openAnyWindow.arguments.length;
  var w = "";
  var h = "";
  var features = "";

  for (i=2; i<l; i++) {
    var param = openAnyWindow.arguments[i];
    if ( (parseInt(param) == 0) ||
      (isNaN(parseInt(param))) ) {
      features += param + ',';
    } else {
      (w == "") ? w = "width=" + param + "," :
        h = "height=" + param;
    }
  }

  features += w + h;
  var code = "popupWin = window.open(url, name";
  if (l > 2) code += ", '" + features;
  code += "')";
  eval(code);
}

function fecha()        {
        self.close();
}

//--></SCRIPT>


<div align="center">
				<table border="0" width="900" cellspacing="3" cellpadding="0">
</td>
					</tr>
					<table width=100% height=40 cellpadding=0 cellspacing=3 border=0 bgcolor="#000059">

 
<BR>
<BR> 
<BR>
</body>
</html>

"""

# Caminho para o arquivo CSV
arquivo_csv = r"selic_acumulada.csv"

# Inicializar a variável df
df = None

# Ler o arquivo CSV
try:
    df = pd.read_csv(arquivo_csv, delimiter=';', decimal='.', header=None)
    # Definir nomes das colunas manualmente
    df.columns = ['Ano', 'JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']
    print("Colunas disponíveis:", df.columns.tolist())  # Exibir os nomes das colunas
except Exception as e:
    print(f"Erro ao ler o CSV: {e}")

# Verificar se df foi definido corretamente
if df is not None:
    # Gerar as linhas da tabela
    table_rows = ""
    for index, row in df.iterrows():
        ano = row['Ano']  # Pegar o ano
        # Criar as células da linha para o ano e as porcentagens, aplicando o estilo CSS
        tabela_ano = f"<td align='right' width=66 COLSTART='1' bgColor='#faf3eb'>" \
                   f"<p align='right'><font face='Verdana' size='2'><b>{ano}</b></font></p></td>"
        
        # Verificar e tratar cada valor individualmente para floats e strings
        valores_csv = ''.join([
            f"<td align='right' width=66 COLSTART='10' bgColor='#faf3eb'>"
            f"<p align='right'><font face='Verdana' size='2'>{v if pd.notna(v) else ''}</font></p>"
            f"</td>" for v in row[1:]
        ])
        
        # Montar a linha completa com o ano e as porcentagens
        table_rows += f"<tr>{tabela_ano}{valores_csv}</tr>\n"

    # Substituir o placeholder {table_data} pelas linhas geradas
    arquivo_html = html_template.replace("{table_data}", table_rows)

    # Salvar o novo HTML em um arquivo
    with open("selicacumulada.html", "w", encoding="utf-8") as file:
        file.write(arquivo_html)

    print("HTML gerado com sucesso!")
else:
    print("O DataFrame não foi criado. Verifique a leitura do arquivo CSV.")

arquivo_para_remover = arquivo_csv
arquivo_de_referencia  = "selicacumulada.html"

# Verifica se o arquivo de referência existe
if os.path.exists(arquivo_de_referencia):
    # Verifica se o arquivo a ser removido existe
    if os.path.exists(arquivo_para_remover):
        os.remove(arquivo_para_remover)
        print(f'O arquivo {arquivo_para_remover} foi removido.')
    else:
        print(f'O arquivo {arquivo_para_remover} não existe.')
else:
    print(f'O arquivo de referência {arquivo_de_referencia} não existe.')