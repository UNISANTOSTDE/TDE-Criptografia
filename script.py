#Importação das bibliotecas
import random 
from colorama import Fore, Back

#Criando uma chave privada randomica
def random_key():
    string_aleatoria = ''.join(chr(random.randint(33, 126))#Declaração dos caracteres que podem ser utilizados 
                                                            #de acordo com a tabela ASCII
                                                            
                               for _ in range(random.randint(3, 28))) #Definição do tamanho da String, até quantos caracteres ela pode ter
                                                    #(o número 28 representa o número de titulos do Neymar, é nois tamojuntu!)
    return string_aleatoria

#Retornando a chave criptografada
def vigenere(texto, chave, modo):
   
   #Declaração dos caracteres da tabela ASCII
    tabela_ascii = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ "

    #Variável para concatenação
    resultado = ''
    
    #Estrutura de repetição para análise de caracter por caracter do texto digitado
    for i in range(len(texto)):
        
        #Condição para analisar se o caracter se encontra dentro da lista
        if texto[i] in tabela_ascii:
            
            #Contas para encriptar e desencriptar o texto 
            if modo == 'encriptar':
                resultado += tabela_ascii[(ord(texto[i]) +
                                       ord(chave[i % len(chave)]) - 2 * ord('!')) % len(tabela_ascii)]
            elif modo == 'desencriptar':
                resultado += tabela_ascii[(ord(texto[i]) -
                                       ord(chave[i % len(chave)]) + len(tabela_ascii)) % len(tabela_ascii)]
                
    #Retorna o resultado concatenado            
    return resultado

#Printando mensagens
print("TDE - CRIPTOGRAFIA")
print(Fore.WHITE + "------------------------------------------------------")
print("ALUNOS:")
print("Amanda Simões")
print("Caio Vinícius")
print("João Falcão")
print("João Rodrigues")
print("João Evangelista")
print("Vinicius Honorio")
print(Fore.WHITE + "------------------------------------------------------")

print("Pressione ENTER para continuar")

print(Fore.WHITE + "------------------------------------------------------")
input()

texto_original = input('Digite a palavra para ser criptografada: ' + Fore.GREEN)
print(Fore.WHITE + "------------------------------------------------------")

#Chamando a função da chave aleatória e em seguida printando ela
key = random_key()
print(Fore.WHITE + "Chave da criptografia:", Fore.YELLOW + key)
print(Fore.WHITE + "------------------------------------------------------")

#Chamando a função de encriptar e desencriptar com o parametro de encriptamento
texto_criptografado = vigenere(texto_original, key, 'encriptar')
print(Fore.WHITE + 'Texto criptografado:', Fore.RED + texto_criptografado)
print(Fore.WHITE + "------------------------------------------------------")

#Chamando a função de encriptar e desencriptar com o parametro de desencriptamento
texto_descriptografado = vigenere(texto_criptografado, key, 'desencriptar')
print(Fore.WHITE + 'Texto descriptografado:', Fore.GREEN + texto_descriptografado)
print(Fore.WHITE + "------------------------------------------------------")
