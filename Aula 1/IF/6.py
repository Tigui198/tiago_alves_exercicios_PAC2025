status = input("Status do servidor (ok/erro): ").lower()
tempo = int(input("Tempo de resposta (ms): "))

servidor = {"status": status, "tempo_resposta": tempo}

match servidor:
    case {"status": "ok", "tempo_resposta": t} if t > 200:
        print("Servidor lento")
    case {"status": "ok"}:
        print("Servidor ativo")
    case {"status": "erro"}:
        print("Servidor indisponível")
    case _:
        print("Estado desconhecido")