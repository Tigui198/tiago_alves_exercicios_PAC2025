segundos_total = int(input("Digite o número de segundos: "))

horas = segundos_total // 3600
resto = segundos_total % 3600
minutos = resto // 60
segundos = resto % 60

print(f"{horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s)")