def verificar_arquivo():
    import os as os 
    import json as json
    nomej = [
        {
            "texto": "Olá este é meu arquivo😁"
        }
    ]


    valores_aceitos = ["S", "s", "N", "n"]

    nome_arquivo = str(input("\nInsira o nome do arquivo que deseja proucurar: "))

    if  os.path.exists(nome_arquivo):
        print("\nArquivo encontrado")

    else:
        print("\nArquivo não encontrado, deseja criar um arquivo com este nome? (s/n)")

        resposta = str(input("\nR:"))

        if resposta.lower() == 's':
            print("\nDeseja criar esse arquivo com qual formatação? ")
            print("\n---Formatações possíveis---")
            print("\nJson")
            print("\nPython")
            print("\nHtml")
            print("\nCSV")
            print("\nTXT")
            esolha = str(input("\nR:"))

            if esolha.lower() == 'json':
                nome_arquivo += ".json"
                with open(nome_arquivo, "w", encoding="Utf-8") as f:
                    json.dump( nomej, f, indent=4, ensure_ascii=False)
                    print(f"\nArquivo '{nome_arquivo} criado com sucesso!")

            elif esolha.lower() == 'python':
                nome_arquivo += ".py"
                with open(nome_arquivo, "w", encoding="Utf-8") as f:
                    f.write("\nAqui está seu aruqivo 😁")
                    print(f"\nArquivo '{nome_arquivo} criado com sucesso!")

            elif esolha.lower() == 'html':
                nome_arquivo += ".html"
                with open(nome_arquivo, "w", encoding="Utf-8") as f:
                    f.write("\nAqui está seu aruqivo 😁")
                    print(f"\nArquivo '{nome_arquivo} criado com sucesso!")
            
            elif esolha.lower() == 'csv':
                nome_arquivo += ".csv"
                with open(nome_arquivo, "w", encoding="Utf-8") as f:
                    f.write("\nAqui está seu aruqivo 😁")
                    print(f"\nArquivo '{nome_arquivo} criado com sucesso!")

            elif esolha.lower() == 'txt':
                nome_arquivo += ".txt"
                with open(nome_arquivo, "w", encoding="Utf-8") as f:
                    f.write("\nAqui está seu aruqivo 😁")
                    print(f"\nArquivo '{nome_arquivo} criado com sucesso!")

        else:
            print("\nArquivo não encontrado 😑")



verificar_arquivo()