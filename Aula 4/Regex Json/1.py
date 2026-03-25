import json
import re

with open('dados.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

print("Validação de emails:")
for pessoa in dados:
    email = pessoa['email']
    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        print(f"{pessoa['nome']}: {email} - Válido")
    else:
        print(f"{pessoa['nome']}: {email} - Inválido")

print("Domínios dos sites:")
for pessoa in dados:
    site = pessoa['site']
    dominio = re.sub(r'https?://(www\.)?', '', site)
    print(f"{pessoa['nome']}: {dominio}")

print("Validação de NIFs:")
for pessoa in dados:
    nif = pessoa['nif']
    if re.match(r'^[123568]\d{8}$', nif):
        print(f"{pessoa['nome']}: {nif} - Válido")
    else:
        print(f"{pessoa['nome']}: {nif} - Inválido")

registos_validos = []
for pessoa in dados:
    email_valido = bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', pessoa['email']))
    nif_valido = bool(re.match(r'^[123568]\d{8}$', pessoa['nif']))
    telemovel_limpo = re.sub(r'[^0-9]', '', pessoa['telemovel'])
    telemovel_valido = len(telemovel_limpo) == 9
    
    if email_valido and nif_valido and telemovel_valido:
        registos_validos.append(pessoa)

with open('validos.json', 'w', encoding='utf-8') as f:
    json.dump(registos_validos, f, indent=2, ensure_ascii=False)

print("Registos válidos guardados em validos.json")

with open('nomes_emails.txt', 'w', encoding='utf-8') as f:
    for pessoa in dados:
        f.write(f"nome: {pessoa['nome']}, email: {pessoa['email']}\n")

print("Ficheiro nomes_emails.txt criado com nome e email")