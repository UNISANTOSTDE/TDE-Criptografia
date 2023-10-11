import random


def random_key():
    string_aleatoria = ''.join(chr(random.randint(33, 126))
                               for _ in range(random.randint(3, 28)))
    return string_aleatoria


def vigenere(texto, chave, modo):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alfabeto_minusculo = 'abcdefghijklmnopqrstuvwxyz'
    numeros = '0123456789'
    # caracteres_especiais = '!"#$%&\'()*+,-./'
    # caracteres_especiais2 = ':;<=>?@[\\]^_`{|}~'

    resultado = ''
    for i in range(len(texto)):
        if texto[i] in alfabeto:
            if modo == 'encriptar':
                resultado += alfabeto[(ord(texto[i]) +
                                       ord(chave[i % len(chave)]) - 2 * ord('A')) % 26]
            elif modo == 'desencriptar':
                resultado += alfabeto[(ord(texto[i]) -
                                       ord(chave[i % len(chave)]) + 26) % 26]
        if texto[i] in alfabeto_minusculo:
            if modo == 'encriptar':
                resultado += alfabeto_minusculo[(ord(texto[i]) +
                                                 ord(chave[i % len(chave)]) - 2 * ord('a')) % 26]
            elif modo == 'desencriptar':
                resultado += alfabeto_minusculo[(ord(texto[i]) -
                                                 ord(chave[i % len(chave)]) + 26) % 26]
        if texto[i] in numeros:
            if modo == 'encriptar':
                resultado += numeros[(ord(texto[i]) +
                                      ord(chave[i % len(chave)]) - 2 * ord('0')) % 10]
            elif modo == 'desencriptar':
                resultado += numeros[(ord(texto[i]) -
                                      ord(chave[i % len(chave)]) + 10) % 10]

        # if texto[i] in caracteres_especiais:
        #     if modo == 'encriptar':
        #         resultado += caracteres_especiais[(ord(texto[i]) +
        #                                            ord(chave[i % len(chave)]) - 2 * ord('!')) % 35]
        #     elif modo == 'desencriptar':
        #         resultado += caracteres_especiais[(ord(texto[i]) -
        #                                            ord(chave[i % len(chave)]) + 35) % 35]
    return resultado


texto_original = input('Digite a palavra para ser criptografada: ')

key = random_key()
print("Chave da criptografia:", key)

texto_criptografado = vigenere(texto_original, key, 'encriptar')
print('Texto criptografado:', texto_criptografado)
texto_descriptografado = vigenere(texto_criptografado, key, 'desencriptar')
print('Texto descriptografado:', texto_descriptografado)
