# ransomware-simulado
# 🔐 Projeto de Criptografia em Python


Este projeto é **educacional** e simula o funcionamento de um ransomware de forma **segura e acadêmica**, utilizando a biblioteca `cryptography` em Python.  
O objetivo é aprender sobre **criptografia simétrica**, praticar versionamento com GitHub e desenvolver documentação técnica.

---

## 📚 Conceito: Criptografia com Fernet

O módulo `Fernet` da biblioteca `cryptography` implementa **criptografia simétrica** baseada em AES (Advanced Encryption Standard) no modo CBC, com chave de 128 bits.  
Isso significa que a mesma chave é usada tanto para **criptografar** quanto para **descriptografar** os dados.

### 🔑 Geração da chave
```python
from cryptography.fernet import Fernet

key = Fernet.generate_key()

🔒 Criptografia

fernet = Fernet(key)
criptografado = fernet.encrypt(dados)

🔓 Descriptografia
descriptografado = fernet.decrypt(criptografado)

📂 Estrutura do Projeto
ransomware-simulado/
│── encrypter.py          # Script para gerar chave e criptografar
│── decrypter.py          # Script para descriptografar
│── teste.txt             # Arquivo original
│── chave.key             # Chave gerada automaticamente
│── teste.txt.encrypted   # Arquivo criptografado
│── teste_recuperado.txt  # Arquivo recuperado
└── venv/                 # Ambiente virtual Python

▶️ Como executar
nano teste.txt
python encrypter.py
python decrypter.py

🎯 Objetivos de Aprendizagem
Criptografia simétrica

Uso da biblioteca cryptography
Versionamento no GitHub
Documentação técnica

🚨 Nota Importante
Este projeto é apenas para fins educacionais.
Um ransomware real é ilegal e prejudicial. Aqui você está apenas simulando o processo de criptografia e descriptografia em um ambiente controlado para aprendizado.
