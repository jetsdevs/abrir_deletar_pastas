import os
import shutil
from datetime import datetime


# Abrir Paras
def abrir_pasta(caminho_pasta):
    try:
        # Verifica se o diretório existe
        if os.path.exists(caminho_pasta):
            # Abrindo a pasta
            os.startfile(caminho_pasta)
            print(f"A pasta {caminho_pasta} foi aberta.")
        else:
            print(f"O diretório {caminho_pasta} não existe.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


# Deletar Pasta
def deletar_pasta(caminho_pasta):
    try:
        # Verifica se o diretório existe
        if os.path.exists(caminho_pasta):
            # Deleta a pasta
            shutil.rmtree(caminho_pasta)
            print(f"A pasta {caminho_pasta} foi deletada.")
        else:
            print(f"O diretório {caminho_pasta} não existe.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


while True:
    agora = datetime.now()
    data_hora_formatada = agora.strftime("%d-%m-%Y %H:%M:%S")

    opcao = int(
        input(
            f""" 
                                        {data_hora_formatada}

                            Seja bem vindo!\n
                      Qual função deseja realizar:\n
                        ######## Opções ########

                            [1] Abrir Pasta
                            [2] Deletar Pasta
                            [0] Encerrar
                                             
                          ====== FIM ======                    

                      """
        )
    )

    if opcao == 0:
        break
    elif opcao != [1, 2]:
        print("Opção Inválida, tente novamente!")

    if opcao == 1:
        caminho_da_pasta = input(
            "Digite o caminho da pasta que deseja abrir:\nExemplo: C:\\pasta:\n"
        )
        abrir_pasta(caminho_da_pasta)

    if opcao == 2:
        caminho_da_pasta = input("Digite o caminho da pasta que deseja apagar:\n")
        deletar_pasta(caminho_da_pasta)

    outra_pasta = input("Deseja realizar outra operação? (S|N): ").upper()
    if outra_pasta != "S":
        break
print("Tenha um bom descanso!")
