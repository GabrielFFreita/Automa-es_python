import os as os
import shutil as shutil

caminho_pasta_origem = str(input(r"Informe o caminho da pasta, onde deseja organizar os arquivos por extensão: "))

sub_txt = os.path.join(caminho_pasta_origem, "texto")

sub_png = os.path.join(caminho_pasta_origem, "png")

sub_img = os.path.join(caminho_pasta_origem, "img")

sub_py = os.path.join(caminho_pasta_origem, "py")

sub_jpeg = os.path.join(caminho_pasta_origem, "jpeg")



if not os.path.exists(sub_txt):
     os.makedirs(sub_txt, exist_ok=True)

for nome_arquivo in os.listdir(caminho_pasta_origem):
    if nome_arquivo.endswith(".txt"):
        caminho_completo = os.path.join(caminho_pasta_origem, nome_arquivo)




        if os.path.isfile(caminho_completo) and nome_arquivo.endswith(".txt"):
         shutil.move(caminho_completo, os.path.join(sub_txt, nome_arquivo)) 


if not os.path.exists(sub_py): 
     os.makedirs(sub_py, exist_ok=True)

for nome_arquivo in os.listdir(caminho_pasta_origem):
    if nome_arquivo.endswith(".py"):
        caminho_completo = os.path.join(caminho_pasta_origem, nome_arquivo)




        if os.path.isfile(caminho_completo) and nome_arquivo.endswith(".py"):
         shutil.move(caminho_completo, os.path.join(sub_py, nome_arquivo))




if not os.path.exists(sub_img): 
     os.makedirs(sub_img, exist_ok=True)

for nome_arquivo in os.listdir(caminho_pasta_origem):
    if nome_arquivo.endswith(".img"):
        caminho_completo = os.path.join(caminho_pasta_origem, nome_arquivo)




        if os.path.isfile(caminho_completo) and nome_arquivo.endswith(".img"):
         shutil.move(caminho_completo, os.path.join(sub_img, nome_arquivo)) 




if not os.path.exists(sub_png): 
     os.makedirs(sub_png, exist_ok=True)

for nome_arquivo in os.listdir(caminho_pasta_origem):
    if nome_arquivo.endswith(".png"):
        caminho_completo = os.path.join(caminho_pasta_origem, nome_arquivo)




        if os.path.isfile(caminho_completo) and nome_arquivo.endswith(".png"):
         shutil.move(caminho_completo, os.path.join(sub_png, nome_arquivo)) 



if not os.path.exists(sub_jpeg): 
     os.makedirs(sub_jpeg, exist_ok=True)

for nome_arquivo in os.listdir(caminho_pasta_origem):
    if nome_arquivo.endswith(".jpeg"):
        caminho_completo = os.path.join(caminho_pasta_origem, nome_arquivo)




        if os.path.isfile(caminho_completo) and nome_arquivo.endswith(".jpeg"):
         shutil.move(caminho_completo, os.path.join(sub_jpeg, nome_arquivo)) 




