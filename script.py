# def criptografia(palavra):
#     mensagem = " "

#     for i in palavra:
#         mensagem = mensagem + chr(ord(i) + 5)
#     return mensagem


# def descriptografar(mensagem):
#     frase = " "

#     for i in mensagem:
#         frase = frase + chr(ord(i) - 5)

#     return frase


# print("TESTE DE CRIPTOGRAFIA")

# palavra = criptografia(" vaESTE")
# print("Criptografado: " + palavra)

# palavra_descriptografada = descriptografar(palavra)

# print("Descriptografado: " + palavra_descriptografada)

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
                print(ord(chave[i % len(chave)]))
                print(resultado)
            elif modo == 'desencriptar':
                resultado += alfabeto[(ord(texto[i]) -
                                       ord(chave[i % len(chave)]) + 26) % 26]
        else:
            resultado += texto[i]

    print(resultado)
    return resultado


teste = vigenere('teste', 'key', 'encriptar')
vigenere(teste, 'key', 'desencriptar')
