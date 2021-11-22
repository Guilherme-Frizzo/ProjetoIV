import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sql_FUT import criarJogador

def extrair_inteiro(texto):
	try:
		i = texto.find(' ')
		sem_unidade = texto[:i]

		sem_virgula = sem_unidade.replace(',', '.')

		return float(sem_virgula) * 1000000
	except:
		return 0

driver = webdriver.Chrome()
driver.get('https://www.transfermarkt.com.br/campeonato-brasileiro-serie-a/marktwerte/wettbewerb/BRA1/pos//detailpos/0/altersklasse/alle/plus/1')

iframe = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#sp_message_iframe_575849"))
)
driver.switch_to.frame(iframe)

time.sleep(2)

aceitar = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.sp_choice_type_ACCEPT_ALL"))
)
aceitar.click()
driver.switch_to.default_content()

time.sleep(2)

dados = []

for i in range(4):
	linhas = WebDriverWait(driver, 20).until(
		EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'table.items > tbody > tr'))
	)

	for linha in linhas:
		colunas = linha.find_elements_by_tag_name('td')

		links = linha.find_elements_by_tag_name('a')
		nome = links[0].text

		img = links[1].find_element_by_css_selector("img")
		clube = img.get_attribute('alt')
		valormercado = colunas[10].text.strip()

		dados.append({
			'nome': nome,
			'clube': clube,
			'valormercado': extrair_inteiro(valormercado)
		})

	if i < 3:
		driver.get('https://www.transfermarkt.com.br/campeonato-brasileiro-serie-a/marktwerte/wettbewerb/BRA1/pos//detailpos/0/altersklasse/alle/plus/1/page/' + str(i + 2) )
		#link_botao = WebDriverWait(driver, 20).until(
		#	EC.element_to_be_clickable((By.CSS_SELECTOR, "li.tm-pagination__list-item.tm-pagination__list-item--icon-next-page > a"))
		#)
		#link_botao.click()
		time.sleep(3)

print(dados)

for jogador in dados:
	criarJogador(jogador['nome'], jogador['clube'], jogador['valormercado'])

driver.close()
