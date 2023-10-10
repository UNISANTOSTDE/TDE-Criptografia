
def vigenere(texto, chave, modo):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    texto = texto.upper()
    chave = chave.upper()
    resultado = ''

    for i in range(len(texto)):
        if texto[i] in alfabeto:
            if modo == 'encriptar':
                resultado += alfabeto[(ord(texto[i]) +
                                       ord(chave[i % len(chave)]) - 2 * ord('A')) % 26]
            elif modo == 'desencriptar':
                resultado += alfabeto[(ord(texto[i]) -
                                       ord(chave[i % len(chave)]) + 26) % 26]
        else:
            resultado += texto[i]

    return resultado


texto_original = input('Digite a palavra para ser criptografada: ')
chave = input('Digite a palavra chave: ')

texto_criptografado = vigenere(texto_original, chave, 'encriptar')
print('Texto criptografado:', texto_criptografado)
texto_descriptografado = vigenere(texto_criptografado, chave, 'desencriptar')
print('Texto descriptografado:', texto_descriptografado)
