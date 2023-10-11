import random
from colorama import Fore, Back


def random_key():
    string_aleatoria = ''.join(chr(random.randint(33, 126))
                               for _ in range(random.randint(3, 28))) #numero de titulos do Neymar, é nois tamojuntu!
    return string_aleatoria


def vigenere(texto, chave, modo):
    # alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # alfabeto_minusculo = 'abcdefghijklmnopqrstuvwxyz'
    # numeros = '0123456789'
    tabela_ascii = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ "

    # caracteres_especiais = '!"#$%&\'()*+,-./'
    # caracteres_especiais2 = ':;<=>?@[\\]^_`{|}~'

    resultado = ''
    for i in range(len(texto)):
        if texto[i] in tabela_ascii:
            if modo == 'encriptar':
                resultado += tabela_ascii[(ord(texto[i]) +
                                       ord(chave[i % len(chave)]) - 2 * ord('!')) % len(tabela_ascii)]
            elif modo == 'desencriptar':
                resultado += tabela_ascii[(ord(texto[i]) -
                                       ord(chave[i % len(chave)]) + len(tabela_ascii)) % len(tabela_ascii)]
        
    
        # if texto[i] in alfabeto:
        #     if modo == 'encriptar':
        #         resultado += alfabeto[(ord(texto[i]) +
        #                                ord(chave[i % len(chave)]) - 2 * ord('A')) % 26]
        #     elif modo == 'desencriptar':
        #         resultado += alfabeto[(ord(texto[i]) -
        #                                ord(chave[i % len(chave)]) + 26) % 26]
        # if texto[i] in alfabeto_minusculo:
        #     if modo == 'encriptar':
        #         resultado += alfabeto_minusculo[(ord(texto[i]) +
        #                                          ord(chave[i % len(chave)]) - 2 * ord('a')) % 26]
        #     elif modo == 'desencriptar':
        #         resultado += alfabeto_minusculo[(ord(texto[i]) -
        #                                          ord(chave[i % len(chave)]) + 26) % 26]
        # if texto[i] in numeros:
        #     if modo == 'encriptar':
        #         resultado += numeros[(ord(texto[i]) +
        #                               ord(chave[i % len(chave)]) - 2 * ord('0')) % 10]
        #     elif modo == 'desencriptar':
        #         resultado += numeros[(ord(texto[i]) -
        #                               ord(chave[i % len(chave)]) + 10) % 10]

        # if texto[i] in caracteres_especiais:
        #     if modo == 'encriptar':
        #         resultado += caracteres_especiais[(ord(texto[i]) +
        #                                            ord(chave[i % len(chave)]) - 2 * ord('!')) % 35]
        #     elif modo == 'desencriptar':
        #         resultado += caracteres_especiais[(ord(texto[i]) -
        #                                            ord(chave[i % len(chave)]) + 35) % 35]
    return resultado

print("TDE - CRIPTOGRAFIA")
print(Fore.WHITE + "------------------------------------------------------")
print("ALUNOS:")
print("Amanda")
print("Caio")
print("João Falcão")
print("João Vitor")
print("Vinicius")
print(Fore.WHITE + "------------------------------------------------------")

print("Pressione ENTER para continuar")

print(Fore.WHITE + "------------------------------------------------------")
input()

texto_original = input('Digite a palavra para ser criptografada: ' + Fore.GREEN)
print(Fore.WHITE + "------------------------------------------------------")

key = random_key()
print(Fore.WHITE + "Chave da criptografia:", Fore.YELLOW + key)
print(Fore.WHITE + "------------------------------------------------------")

texto_criptografado = vigenere(texto_original, key, 'encriptar')
print(Fore.WHITE + 'Texto criptografado:', Fore.RED + texto_criptografado)
print(Fore.WHITE + "------------------------------------------------------")
texto_descriptografado = vigenere(texto_criptografado, key, 'desencriptar')
print(Fore.WHITE + 'Texto descriptografado:', Fore.GREEN + texto_descriptografado)
print(Fore.WHITE + "------------------------------------------------------")
