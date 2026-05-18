from cryptography.fernet import Fernet

# Gerar chave e salvar
key = Fernet.generate_key()
with open("chave.key", "wb") as chave_file:
    chave_file.write(key)

# Usar a chave para criptografar
fernet = Fernet(key)
with open("teste.txt", "rb") as file:
    original = file.read()

criptografado = fernet.encrypt(original)

with open("teste.txt.encrypted", "wb") as file:
    file.write(criptografado)
