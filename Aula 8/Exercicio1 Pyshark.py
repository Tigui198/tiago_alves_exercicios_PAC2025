import pyshark

PLACA = "eth1"
ALVO = "192.168.1.0/24"

def processa_pacote(pacote):
    try:
        camada = pacote.highest_layer
        if hasattr(pacote, 'ip'):
            end_origem = pacote.ip.src
            end_destino = pacote.ip.dst
        else:
            end_origem = "Desconhecido"
            end_destino = "Desconhecido"
            
        print(f"[{camada}] {end_origem} >> {end_destino}")
    except AttributeError:
        pass

def captura_trafego(interface, limite):
    print(f"\n>>> Escutando em {interface} ({limite} pacotes) <<<")
    
    captura = pyshark.LiveCapture(interface=interface)
    
    try:
        for i, pacote in enumerate(captura.sniff_continuously(packet_count=limite)):
            processa_pacote(pacote)
    finally:
        captura.close()

if __name__ == "__main__":
    print(f"Alvo da varredura: {ALVO}")
    try:
        captura_trafego(PLACA, 50)
    except KeyboardInterrupt:
        print("\nParada pelo usuario.")
    except Exception as e:
        print(f"Falha: {e}")