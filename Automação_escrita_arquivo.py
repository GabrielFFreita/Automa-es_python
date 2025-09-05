import os as os 

arq = str(input("\nInforme o nome do seu arquivo: "))
conteudo = str(input("\nInsira o que deseja que seja escrito no seu arquivo: "))

try: 
 if os.path.exists(arq):
    with open(arq, 'w', encoding="Utf-8") as f:
        f.write(conteudo)
except FileNotFoundError:
   print("\nArquivo não encontrado!")