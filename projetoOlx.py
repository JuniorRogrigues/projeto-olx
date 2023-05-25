from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
from time import sleep


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=800,600', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver


driver = iniciar_driver()
# Navegar até o site
driver.get('https://www.olx.com.br/estado-ba/grande-salvador?q=monitor')
driver.maximize_window()
sleep(10)

# Carregar todos os elementos da página
driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
sleep(2)
# Encontrar os títulos
titulos = driver.find_elements(By.XPATH, "//div[@class='sc-12rk7z2-7 kDVQFY']//h2")
# Encontrar os preços
precos = driver.find_elements(By.XPATH, "//span[@class='m7nrfa-0 eJCbzj sc-ifAKCX jViSDP']")
# Encontrar os links
links = driver.find_elements(By.XPATH, "//a[@data-ds-component='DS-Link']")
# Guardar isso em um arquivo .csv
for titulo, preco, link in zip(titulos, precos, links):
    with open('precos.csv', 'a', encoding='utf-8', newline='') as arquivo:
        link_processado = link.get_attribute('href')
        arquivo.write(f'{titulo.text};{preco.text};{link_processado}{os.linesep}')

input('')
driver.close()
