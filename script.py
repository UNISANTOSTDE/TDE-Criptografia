def criptografia(palavra):
    mensagem = " "

    for i in palavra:
        mensagem = mensagem + chr(ord(i) + 5)
    return mensagem


def descriptografar(mensagem):
    frase = " "

    for i in mensagem:
        frase = frase + chr(ord(i) - 5)

    return frase


print("TESTE DE CRIPTOGRAFIA")

palavra = criptografia(" vaESTE")
print("Criptografado: " + palavra)

palavra_descriptografada = descriptografar(palavra)

print("Descriptografado: " + palavra_descriptografada)
