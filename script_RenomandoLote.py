# Script de Renomeação de arquivos em Lotes
# Esse script serve para remover ou Adicionar Sufixos de Diversos arquivos 

# Bibilotecas Necessarias para Rodar o Arquivo
import os
import glob

# Adicione o Diretorio da Pasta ao qual você quer renomear
diretorio = "Path//"

#
extensao = ".mp3"

# Adicionar Prefixo que deseja Remover / Adicionar
prefixo = "SUFIXO AQUI"

def rmvSufixo(nome):
    novoNome = nome.replace(prefixo,"")
    return novoNome
    
def addSufixo(nome):
    novoNome = prefixo + nome
    return novoNome

if __name__ == "__main__":
    #Selecionando todos os Arquivos com aquela extensão
    arquivos = glob.glob(os.path.join(diretorio, '*{}'.format(extensao)))

    for arquivos_old in arquivos:
        nome_arquivo = os.path.basename(arquivos_old);    
        
        #Remove o Sufixo especificado        
        novo_nome = rmvSufixo(nome_arquivo)

        # #Adiciona o Sufixo especificado
        # novo_nome = addSufixo(nome_arquivo)

        #Renomeando
        novo_dir = os.path.join(diretorio, novo_nome)
        print(novo_dir)
        os.rename(arquivos_old,novo_dir)


