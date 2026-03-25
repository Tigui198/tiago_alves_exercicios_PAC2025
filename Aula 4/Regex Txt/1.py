import re
from datetime import datetime

with open('dados.txt', 'r', encoding='utf-8') as f:
    conteudo = f.read()
    print("Conteúdo do ficheiro:")
    print(conteudo)

print("Emails encontrados:")
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', conteudo)
for email in emails:
    print(email)

print("Telemóveis encontrados:")
telemoveis = re.findall(r'\b\d{9}\b|\b\d{3}-\d{3}-\d{3}\b|\b\d{3}\s\d{3}\s\d{3}\b', conteudo)
for telemovel in telemoveis:
    print(telemovel)

print("Nomes encontrados:")
nomes = re.findall(r'Nome:\s([^,]+)', conteudo)
for nome in nomes:
    print(nome)

with open('extraidos.txt', 'w', encoding='utf-8') as f:
    linhas = conteudo.strip().split('\n')
    for linha in linhas:
        match = re.match(r'Nome:\s([^,]+),\sEmail:\s([^,]+),\sTelemóvel:\s(.+)', linha)
        if match:
            f.write(f"{match.group(1)} | {match.group(2)} | {match.group(3)}\n")

print("Ficheiro extraidos.txt criado")

print("Emails que terminam em .pt:")
emails_pt = [email for email in emails if email.endswith('.pt')]
for email in emails_pt:
    print(email)

with open('registos.txt', 'r', encoding='utf-8') as f:
    registos = f.read()

print("NIFs encontrados:")
nifs = re.findall(r'NIF:\s(\d{9})', registos)
for nif in nifs:
    print(nif)

print("Datas encontradas:")
datas = re.findall(r'\b(\d{2}/\d{2}/\d{4})\b', registos)
for data in datas:
    print(data)

print("Códigos postais encontrados:")
cps = re.findall(r'\b(\d{4}-\d{3})\b', registos)
for cp in cps:
    print(cp)

print("Domínios dos sites:")
sites = re.findall(r'Site:\s(?:https?://)?(www\.)?([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})', registos)
dominios = [site[1] if site[0] else site[1] for site in sites]
for dominio in dominios:
    print(dominio)

print("Validação de NIFs:")
nifs_validos = 0
for nif in nifs:
    if re.match(r'^[123568]\d{8}$', nif):
        print(f"{nif} - Válido")
        nifs_validos += 1
    else:
        print(f"{nif} - Inválido")
print(f"Total de NIFs válidos: {nifs_validos}/{len(nifs)}")

with open('resumo.txt', 'w', encoding='utf-8') as f:
    linhas_registos = registos.strip().split('\n')
    for linha in linhas_registos:
        nome_match = re.search(r'Nome:\s([^|]+)', linha)
        nif_match = re.search(r'NIF:\s(\d{9})', linha)
        data_match = re.search(r'Data:\s(\d{2}/\d{2}/\d{4})', linha)
        cp_match = re.search(r'Código Postal:\s(\d{4}-\d{3})', linha)
        site_match = re.search(r'Site:\s(?:https?://)?(?:www\.)?([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})', linha)
        
        if nome_match and nif_match and data_match and cp_match and site_match:
            f.write(f"{nome_match.group(1).strip()} | {nif_match.group(1)} | {data_match.group(1)} | {cp_match.group(1)} | {site_match.group(1)}\n")

print("Ficheiro resumo.txt criado")

print("Registos com datas anteriores a 2025:")
linhas_registos = registos.strip().split('\n')
for linha in linhas_registos:
    data_match = re.search(r'Data:\s(\d{2}/\d{2}/\d{4})', linha)
    if data_match:
        data_obj = datetime.strptime(data_match.group(1), '%d/%m/%Y')
        if data_obj.year < 2025:
            print(linha)