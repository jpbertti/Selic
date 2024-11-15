from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Função para extrair dados da tabela HTML
def extrair_data(table):
    """Extrai dados de uma tabela HTML para listas de meses, anos e valores."""
    headers = [th.get_text(strip=True) for th in table.find_all('tr')[0].find_all('td') + table.find_all('tr')[0].find_all('th')]
    anos = headers[1:]
    meses = []
    data = {ano: [] for ano in anos}

    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        if not cols:
            continue
        mes = cols[0].get_text(strip=True)
        meses.append(mes)
        for i, col in enumerate(cols[1:]):
            value = col.get_text(strip=True)
            data[anos[i]].append(value)

    return meses, anos, data

def print_table_data(anos, data, file=None):
    """Imprime os dados extraídos de uma tabela e opcionalmente salva em um arquivo, organizando os anos de forma decrescente."""
    # Ordenar anos de forma decrescente
    anos_organizados = sorted(anos, reverse=True)
    
    output = []
    for ano in anos_organizados:
        output.append(f"{ano}; {'; '.join(data[ano])}")

    resultado = '\n'.join(output)


    if file:
        with open(file, 'a', encoding='utf-8') as f:
            f.write(resultado + '\n')
    else:
        print(resultado)

# Configurações do Selenium
chrome_options = Options()
chrome_options.add_argument('--headless')  # Opcional: para rodar o Chrome em modo headless
chrome_options.add_argument('--ignore-certificate-errors')  # Ignora erros de certificado

# Inicializa o driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Acessa a página
    driver.get('https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/pagamentos-e-parcelamentos/taxa-de-juros-selic#Selicmensalmente')

    # Aguarda a página carregar completamente
    time.sleep(10)  # Ajuste o tempo conforme necessário

    # Obtém o conteúdo HTML da página
    html = driver.page_source

finally:
    # Encerra o driver
    driver.quit()

# Analisar o HTML
soup = BeautifulSoup(html, 'lxml')

# Encontrar todas as tabelas
tabelas = soup.find_all('table')
print(f"Total de tabelas encontradas: {len(tabelas)}")

# Arquivo para tabelas 1 a 5
file_acumulada = 'selic_mensal.csv'

# Código para processar a Tabela 2
try:
    tabela = tabelas[1]  # A Tabela 2 está no índice 1
    meses, anos, data = extrair_data(tabela)
    print_table_data(anos, data, file=file_acumulada)
except IndexError:
    print("Tabela 2 não encontrada ou índice incorreto.")

# Código para processar a Tabela 3
try:
    tabela = tabelas[2]  # A Tabela 3 está no índice 2
    meses, anos, data = extrair_data(tabela)
    print_table_data(anos, data, file=file_acumulada)
except IndexError:
    print("Tabela 3 não encontrada ou índice incorreto.")

# Código para processar a Tabela 4
try:
    tabela = tabelas[3]  # A Tabela 4 está no índice 3
    meses, anos, data = extrair_data(tabela)
    print_table_data(anos, data, file=file_acumulada)
except IndexError:
    print("Tabela 4 não encontrada ou índice incorreto.")

# Código para processar a Tabela 5
try:
    tabela = tabelas[4]  # A Tabela 5 está no índice 4
    meses, anos, data = extrair_data(tabela)
    print_table_data(anos, data, file=file_acumulada)
except IndexError:
    print("Tabela 5 não encontrada ou índice incorreto.")

# Arquivo para tabelas 6 a 11
file_mensal = 'selic_acumulada.csv'

# Código para processar a Tabela 6
try:
    tabela = tabelas[5]  # A Tabela 6 está no índice 5
    meses, anos, data = extrair_data(tabela)
    print_table_data(anos, data, file=file_mensal)
except IndexError:
    print("Tabela 6 não encontrada ou índice incorreto.")

# Código para processar a Tabela 7
try:
    tabela = tabelas[6]  # A Tabela 7 está no índice 6
    meses, anos, data = extrair_data(tabela)
    print_table_data(anos, data, file=file_mensal)
except IndexError:
    print("Tabela 7 não encontrada ou índice incorreto.")

# Código para processar a Tabela 8
try:
    tabela = tabelas[7]  # A Tabela 8 está no índice 7
    meses, anos, data = extrair_data(tabela)
    print_table_data(anos, data, file=file_mensal)
except IndexError:
    print("Tabela 8 não encontrada ou índice incorreto.")

# Código para processar a Tabela 9
try:
    tabela = tabelas[8]  # A Tabela 9 está no índice 8
    meses, anos, data = extrair_data(tabela)
    print_table_data(anos, data, file=file_mensal)
except IndexError:
    print("Tabela 9 não encontrada ou índice incorreto.")

# Código para processar a Tabela 10
try:
    tabela = tabelas[9]  # A Tabela 10 está no índice 9
    meses, anos, data = extrair_data(tabela)
    print_table_data(anos, data, file=file_mensal)
except IndexError:
    print("Tabela 10 não encontrada ou índice incorreto.")

# Código para processar a Tabela 11
try:
    tabela = tabelas[10]  # A Tabela 11 está no índice 10
    meses, anos, data = extrair_data(tabela)
    print_table_data(anos, data, file=file_mensal)
except IndexError:
    print("Tabela 11 não encontrada ou índice incorreto.")


    
