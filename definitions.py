import time, os, shutil
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import filedialog as fd


class SigaaAutomation ():
    
        
    def __init__(self):
        self.driver = webdriver.Edge()
        self.downloads = []
        self.ext = ['.zip','.pdf']

    def check_files_download(self):
        user_data =  open('user_login.txt','r')
        path = user_data.readlines()[2].replace('\n','')
        downloads = self.downloads   

        counter = 0
        while counter < len(downloads):
            downloaded = os.listdir(path)
            print(f"Downloads:{downloads} Downloaded:{downloaded}")
            for file in downloads:            
                if downloaded.count(file) == 0:
                    counter = 0
                    break
                else:
                    counter += 1
            time.sleep(1)
            print(counter)
        self.downloads = []
        return True

    def move_files(self, i, files):
        try:
            if files == 0:
                pass
            else:
                user_data =  open('user_login.txt','r')
                path = user_data.readlines()[2].replace('\n','')
                new_path = list(map(lambda item: f'{path}/{item}', os.listdir(path)))   
                new_path.sort(key=os.path.getmtime, reverse=True)
                destination = f'./{i}/'
                if files == 1:
                    shutil.move(new_path[0], destination)
                else:
                    for file in new_path[0:files]:
                        shutil.move(file, destination)

                
                user_data.close()
        except Exception as e:print(e)    

    def check_path(self):
        for i in range(6):
            try:
                os.mkdir('../'.join(str(i)))
            except Exception as e:print(e)


    def check_files(self):
        files = ['PLANO DE SUBSTITUIÇÃO DAS AULAS PRÁTICAS PRESENCIAIS POR ANP 2021 1.docx.pdf']
        for directory in os.listdir('./'):
            if os.path.isdir('./'.join(str(directory))):
                for file in os.listdir('./'.join(str(directory))):
                    files.append(str(file))
        return files

    def percorrer(self):

        materias =  int(open('user_login.txt','r').readlines()[3])
        for index in range(0,materias):
            self.material_click(index)

    def material_click(self, index):
        sleep_time = 0.5

        if index == 0:
            try:
                files = 0                    
                materia = self.driver.find_element_by_id("form_acessarTurmaVirtual:turmaVirtual") 
                materia.click()
                for d in range(10):
                    for i in range(30):
                        try:
                            material = self.driver.find_element_by_id(f"formAva:j_id_jsp_1220730176_255:{i}:listaMateriais:{d}:idInserirMaterialArquivo")
                            if self.driver.find_element_by_id(f'formAva:j_id_jsp_1220730176_255:{i}:listaMateriais:{d}:idInserirMaterialArquivo').text in self.check_files():
                                pass
                            elif self.driver.find_element_by_id(f'formAva:j_id_jsp_1220730176_255:{i}:listaMateriais:{d}:j_id_jsp_1220730176_513').text in self.check_files():
                                pass
                            else:

                                for e in self.ext:
                                    if e in self.driver.find_element_by_id(f'formAva:j_id_jsp_1220730176_255:{i}:listaMateriais:{d}:idInserirMaterialArquivo').text:
                                        self.downloads.append(
                                            self.driver.find_element_by_id(f'formAva:j_id_jsp_1220730176_255:{i}:listaMateriais:{d}:idInserirMaterialArquivo').text)
                                        material.click()
                                        files += 1
                                    else:pass        
                                for e in self.ext:
                                    if e in self.driver.find_element_by_id(f'formAva:j_id_jsp_1220730176_255:{i}:listaMateriais:{d}:j_id_jsp_1220730176_513').text:    
                                        self.downloads.append(
                                            self.driver.find_element_by_id(f'formAva:j_id_jsp_1220730176_255:{i}:listaMateriais:{d}:j_id_jsp_1220730176_513').text)
                                        material.click()
                                        files += 1
                                    else:pass         
                                time.sleep(sleep_time)         
                        except:pass
                            
                if files == 0:
                    self.driver.get('https://sigaa.ifsc.edu.br/sigaa/portais/discente/discente.jsf')            
                else:
                    while not self.check_files_download():
                        time.sleep(1)                    
                    self.move_files(index, files)
                    self.driver.get('https://sigaa.ifsc.edu.br/sigaa/portais/discente/discente.jsf')
            except:pass
        else:
            try:
                files = 0
                materia = self.driver.find_element_by_id(f"form_acessarTurmaVirtualj_id_{index}:turmaVirtual") 
                materia.click()
                for d in range(10):
                    for i in range(30):
                        try:
                            material = self.driver.find_element_by_id(f"formAva:j_id_jsp_1220730176_255:{i}:listaMateriais:{d}:idInserirMaterialArquivo")
                            if self.driver.find_element_by_id(f'formAva:j_id_jsp_1220730176_255:{i}:listaMateriais:{d}:idInserirMaterialArquivo').text in self.check_files():
                                pass
                            elif self.driver.find_element_by_id(f'formAva:j_id_jsp_1220730176_255:{i}:listaMateriais:{d}:j_id_jsp_1220730176_513').text in self.check_files():
                                pass
                            else:                                                            
                                for e in self.ext:
                                    if e in self.driver.find_element_by_id(f'formAva:j_id_jsp_1220730176_255:{i}:listaMateriais:{d}:idInserirMaterialArquivo').text:
                                        self.downloads.append(
                                            self.driver.find_element_by_id(f'formAva:j_id_jsp_1220730176_255:{i}:listaMateriais:{d}:idInserirMaterialArquivo').text)
                                        material.click()
                                        files += 1
                                    else:pass
                                for e in self.ext:
                                    if e in self.driver.find_element_by_id(f'formAva:j_id_jsp_1220730176_255:{i}:listaMateriais:{d}:j_id_jsp_1220730176_513').text:    
                                        self.downloads.append(
                                            self.driver.find_element_by_id(f'formAva:j_id_jsp_1220730176_255:{i}:listaMateriais:{d}:j_id_jsp_1220730176_513').text)
                                        material.click()
                                        files += 1
                                    else:pass
                                  
                                time.sleep(sleep_time)
                        except:pass
                if files == 0:
                    self.driver.get('https://sigaa.ifsc.edu.br/sigaa/portais/discente/discente.jsf')            
                else:
                    while not self.check_files_download():
                        time.sleep(1)   
                    self.move_files(index, files)
                    self.driver.get('https://sigaa.ifsc.edu.br/sigaa/portais/discente/discente.jsf')
            except:pass
    
    def user_creation(self):
        if not os.path.exists('./user_login.txt'):
            login = input('Digite seu login:\n>')
            senha = input('Digite sua senha:\n>')
            materias = input ("Quantas matérias você tem?\n")
            path = fd.askdirectory()
            with open('user_login.txt', 'w+') as user_login:
                user_login.write(f"{login}")
                user_login.write("\n")        
                user_login.write(f"{senha}")
                user_login.write("\n")  
                user_login.write(f"{path}")
                user_login.write("\n")
                user_login.write(f"{materias}")    

    def sigaa_enter(self):
        user_data = open('user_login.txt','r').readlines()
        login, senha = user_data[0], user_data[1]

        self.driver.get("https://sigaa.ifsc.edu.br/sigaa/verTelaLogin.do")
        assert "SIGAA - Sistema Integrado de Gestão de Atividades Acadêmica" in self.driver.title
        elem = self.driver.find_element_by_name("user.login")
        elem.clear()
        elem.send_keys(login.replace('\n',''))
        elem = self.driver.find_element_by_name('user.senha')
        elem.clear()
        elem.send_keys(senha.replace('\n',''))
        elem.send_keys(Keys.RETURN)
