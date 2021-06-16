import time, os, shutil
from pathlib import Path

def move_files(i, files):
    try:
        if files == 0:
            pass
        else:
            user_data =  open('user_login.txt','r')
            path = user_data.readlines()[2]
            new_path = list(map(lambda item: f'{path}/{item}', os.listdir(path)))   
            new_path.sort(key=os.path.getmtime, reverse=True)
            destination = f'./{i}/'
            if files == 1:
                shutil.move(new_path[0], destination)
            else:
                for file in new_path[0:files]:
                    shutil.move(file, destination)
    except:pass    

def check_path():
    try:
        for i in range(6):
            os.mkdir('../'.join(str(i)))
    except:
        pass

def check_files():
    files = ['PLANO DE SUBSTITUIÇÃO DAS AULAS PRÁTICAS PRESENCIAIS POR ANP 2021 1.docx.pdf']
    for directory in os.listdir('./'):
        if os.path.isdir('./'.join(str(directory))):
            for file in os.listdir('./'.join(str(directory))):
                files.append(str(file))
    return files


def material_click(index, driver):
    sleep_time = 0.5

    if index == 0:
        files = 0                    
        materia = driver.find_element_by_id("form_acessarTurmaVirtual:turmaVirtual") 
        materia.click()
        for d in range(10):
            for i in range(50):
                try:
                    material = driver.find_element_by_id(f"formAva:j_id_jsp_1220730176_255:{i}:listaMateriais:{d}:idInserirMaterialArquivo")
                    if driver.find_element_by_id(f'formAva:j_id_jsp_1220730176_255:{i}:listaMateriais:{d}:idInserirMaterialArquivo').text in check_files():
                        pass
                    elif driver.find_element_by_id(f'formAva:j_id_jsp_1220730176_255:{i}:listaMateriais:{d}:j_id_jsp_1220730176_513').text in check_files():
                        pass
                    else:
                        files += 1
                        material.click()           
                        time.sleep(sleep_time)         
                except:
                    continue
        if files == 0:
            pass            
        else:
            time.sleep(10)    
            move_files(index, files)
            driver.get('https://sigaa.ifsc.edu.br/sigaa/portais/discente/discente.jsf')
    else:
        files = 0
        materia = driver.find_element_by_id(f"form_acessarTurmaVirtualj_id_{index}:turmaVirtual") 
        materia.click()
        for d in range(10):
            for i in range(10):
                try:
                    material = driver.find_element_by_id(f"formAva:j_id_jsp_1220730176_255:{i}:listaMateriais:{d}:idInserirMaterialArquivo")
                    if driver.find_element_by_id(f'formAva:j_id_jsp_1220730176_255:{i}:listaMateriais:{d}:idInserirMaterialArquivo').text in check_files():
                        pass
                    elif driver.find_element_by_id(f'formAva:j_id_jsp_1220730176_255:{i}:listaMateriais:{d}:j_id_jsp_1220730176_513').text in check_files():
                        pass
                    else:
                        files += 1
                        material.click()
                        time.sleep(sleep_time)
                except:
                    continue
        if files == 0:
            pass            
        else:
            time.sleep(10)    
            move_files(index, files)
            driver.get('https://sigaa.ifsc.edu.br/sigaa/portais/discente/discente.jsf')