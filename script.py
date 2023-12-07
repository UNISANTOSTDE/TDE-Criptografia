
import random 

def random_key():
    string_aleatoria = ''.join(chr(random.randint(33, 126))
    for _ in range(random.randint(3, 28))) 
    return string_aleatoria


def vigenere(texto, chave, modo):
    tabela_ascii = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ "
    resultado = ''
    for i in range(len(texto)):
        if texto[i] in tabela_ascii:
            if modo == 'encriptar':
                resultado += tabela_ascii[(ord(texto[i]) + ord(chave[i % len(chave)]) - 2 * ord('!')) % len(tabela_ascii)]
            elif modo == 'desencriptar':
                resultado += tabela_ascii[(ord(texto[i]) - ord(chave[i % len(chave)]) + len(tabela_ascii)) % len(tabela_ascii)]          
    return resultado

#Printando mensagens
print("TDE - CRIPTOGRAFIA")
print("------------------------------------------------------")
print("ALUNOS:")
print("Amanda Simões")
print("Caio Vinícius")
print("João Falcão")
print("João Rodrigues")
print("João Evangelista")
print("Vinicius Honorio")
print("------------------------------------------------------")

texto_original = input('Digite a palavra para ser criptografada: ')
print("------------------------------------------------------")

key = random_key()
print("Chave da criptografia: ",key)
print("------------------------------------------------------")


texto_criptografado = vigenere(texto_original, key, 'encriptar')
print('Texto criptografado: ', texto_criptografado)
print("------------------------------------------------------")

texto_descriptografado = vigenere(texto_criptografado, key, 'desencriptar')
print('Texto descriptografado: ', texto_descriptografado)
print("------------------------------------------------------")
