from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import filedialog as fd
import os, time
from definitions import material_click, check_path

check_path()


if not os.path.exists('./user_login.txt'):
    login = input('Digite seu login:\n>')
    senha = input('Digite sua senha:\n>')
    path = fd.askdirectory()
    with open('user_login.txt', 'w+') as user_login:
        user_login.write(f"{login}")
        user_login.write("\n")        
        user_login.write(f"{senha}")
        user_login.write("\n")  
        user_login.write(f"{path}")

user_data = open('user_login.txt','r').readlines()
login, senha = user_data[0], user_data[1]

    
driver = webdriver.Edge()
driver.get("https://sigaa.ifsc.edu.br/sigaa/verTelaLogin.do")
assert "SIGAA - Sistema Integrado de Gestão de Atividades Acadêmica" in driver.title
elem = driver.find_element_by_name("user.login")
elem.clear()
elem.send_keys(login.replace('\n',''))
elem = driver.find_element_by_name('user.senha')
elem.clear()
elem.send_keys(senha.replace('\n',''))
elem.send_keys(Keys.RETURN)


for i in range(7):
    
    material_click(i, driver)



