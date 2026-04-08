import socket
import threading
import re
from datetime import datetime
import os

# Configuracao basica
HOST = "127.0.0.1"
PORTA = 12340
clientes = {}  # socket -> nome

# Criar pasta de logs
if not os.path.exists("logs"):
    os.makedirs("logs")

# Padroes para detetar dados pessoais
def contem_dados_pessoais(texto):
    """Verifica se a mensagem contem dados pessoais"""
    padroes = [
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',  # email
        r'\b\d{9}\b',  # telefone (9 digitos)
        r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b',  # IP
        r'\b\d{2}[/-]\d{2}[/-]\d{4}\b',  # data nascimento
        r'\b\d{16}\b',  # cartao credito
    ]
    for padrao in padroes:
        if re.search(padrao, texto):
            return True
    return False

# Detetar engenharia social (palavras suspeitas)
def contem_engenharia_social(texto):
    """Verifica se a mensagem contem tentativas de engenharia social"""
    palavras_suspeitas = ['urgente', 'gratis', 'oferta', 'clica', 'ganhaste', 'promocao', 'confia']
    texto_lower = texto.lower()
    for palavra in palavras_suspeitas:
        if palavra in texto_lower:
            return True
    return False

def transmitir_para_todos(mensagem, remetente=None):
    """Envia mensagem para todos os clientes exceto o remetente"""
    for sock in list(clientes.keys()):
        if sock != remetente:
            try:
                sock.send(mensagem.encode('utf-8'))
            except:
                pass

def remover_cliente(sock):
    """Remove cliente da lista"""
    if sock in clientes:
        nome = clientes[sock]
        del clientes[sock]
        print(f"[-] {nome} saiu")
        transmitir_para_todos(f"[SISTEMA] {nome} saiu do chat", None)
        sock.close()

def lidar_cliente(sock, endereco):
    """Gerencia um cliente individualmente"""
    # Recebe o nome do cliente
    nome = sock.recv(1024).decode('utf-8')
    clientes[sock] = nome
    print(f"[+] {nome} conectado de {endereco[0]}")
    transmitir_para_todos(f"[SISTEMA] {nome} entrou no chat", None)
    
    # Loop para receber mensagens
    while True:
        try:
            msg = sock.recv(4096).decode('utf-8')
            if not msg:
                break
            
            # Verifica se e comando
            if msg == '/sair':
                break
            elif msg == '/users':
                lista = ", ".join(clientes.values())
                sock.send(f"[SISTEMA] Utilizadores: {lista}".encode('utf-8'))
                continue
            
            # Verifica dados pessoais
            if contem_dados_pessoais(msg):
                alerta = "[SISTEMA] ALERTA: Mensagem bloqueada (contem dados pessoais)"
                sock.send(alerta.encode('utf-8'))
                # Registar no log
                with open("logs/gdpr.txt", "a") as f:
                    f.write(f"{datetime.now()} | {nome} | {msg}\n")
                continue
            
            # Verifica engenharia social
            if contem_engenharia_social(msg):
                with open("logs/eng_social.txt", "a") as f:
                    f.write(f"{datetime.now()} | {nome} | {msg}\n")
            
            # Mensagem aprovada - enviar para todos
            transmitir_para_todos(f"{nome}: {msg}", sock)
            
        except:
            break
    
    remover_cliente(sock)

def iniciar_servidor():
    """Inicia o servidor"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORTA))
    server.listen()
    print(f"Servidor a correr em {HOST}:{PORTA}")
    
    while True:
        sock, endereco = server.accept()
        thread = threading.Thread(target=lidar_cliente, args=(sock, endereco))
        thread.start()

if __name__ == "__main__":
    iniciar_servidor()