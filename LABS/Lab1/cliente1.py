import socket
import threading

HOST = "127.0.0.1"
PORTA = 12340

def receber_mensagens(sock):
    """Recebe e mostra mensagens do servidor"""
    while True:
        try:
            msg = sock.recv(4096).decode('utf-8')
            if msg:
                print(f"\n{msg}")
                print("> ", end="", flush=True)
        except:
            print("\n[!] Conexao perdida")
            break

def iniciar_cliente():
    """Inicia o cliente"""
    nome = input("Nome: ")
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORTA))
    
    # Envia o nome
    sock.send(nome.encode('utf-8'))
    
    # Thread para receber mensagens
    threading.Thread(target=receber_mensagens, args=(sock,), daemon=True).start()
    
    print("Conectado! Comandos: /users, /sair")
    
    # Loop para enviar mensagens
    while True:
        msg = input("> ")
        if msg == '/sair':
            sock.send(msg.encode('utf-8'))
            break
        try:
            sock.send(msg.encode('utf-8'))
        except:
            break
    
    sock.close()

if __name__ == "__main__":
    iniciar_cliente()