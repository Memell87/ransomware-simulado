from cryptography.fernet import Fernet

# Ler chave existente
with open("chave.key", "rb") as chave_file:
    key = chave_file.read()

fernet = Fernet(key)

# Ler arquivo criptografado
with open("teste.txt.encrypted", "rb") as file:
    criptografado = file.read()

# Descriptografar
descriptografado = fernet.decrypt(criptografado)

with open("teste_recuperado.txt", "wb") as file:
    file.write(descriptografado)
