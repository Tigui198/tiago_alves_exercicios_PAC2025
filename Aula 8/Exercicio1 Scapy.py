from scapy.all import ARP, Ether, srp, sniff

INTERFACE = "eth1" 
REDE = "192.168.1.0/24"

def analisa(pacote_recebido):
    print(pacote_recebido.summary())

print(f"Scan da Rede: {REDE}")
requisicao_arp = ARP(pdst=REDE)
broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
pacote_envio = broadcast/requisicao_arp
respostas_recebidas = srp(pacote_envio, timeout=2, verbose=0)[0]

print("IP\t\tMAC")
for pacote_enviado, pacote_recebido in respostas_recebidas:
    print(f"{pacote_recebido.psrc}\t{pacote_recebido.hwsrc}")

print("Monitorizando")
sniff(iface=INTERFACE, count=50, prn=analisa)