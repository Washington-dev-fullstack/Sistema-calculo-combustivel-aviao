def aviao(escolha):
    return escolha

def combustivel(tempo, queima_horaria):
    return tempo * queima_horaria
    
def calcular_reserva(queima_horaria):
    return queima_horaria * 0.5 #calculo da reserva obrigatória de 30 minutos (0.5h)

def converter_para_libras(kg):
    return kg * 2.2046 #muitos avioes utilizam libras ao inves de quilos
    
def valor_com_virgula(valor):
    return f"{valor:.2f}".replace('.', ',') #vai sair no terminal o valor com virgula

# "catálogo" de aviões para print na linha 39
modelo = {
    1: "Airbus A320",
    2: "Airbus A321 NEO",
    3: "Embraer E195-E2",
    4: "Boeing 737 MAX 8"
}

print("--------Sistema de cálculo de combustível--------\n")

nome_piloto = input("Digite seu nome para um cálculo mais imersivo: ")
print(f"\nSeja bem vindo, piloto \033[1m{nome_piloto}\033[0m") #Texto em negrito

repeticao = "s"
while repeticao == "s":
    while True:
        try:
            print("\n---Para começar, informe o modelo do seu avião de acordo com seu número---")
            print("   1 - Airbus A320")
            print("   2 - Airbus A321 NEO")
            print("   3 - Embraer E195-E2")
            print("   4 - Boeing 737 MAX 8")
            escolha = int(input("Insira o modelo do avião: "))

            if escolha in [1, 2, 3, 4]:
                break
            else:
                print("É nescessário que escolha entre o 1, 2, 3 e 4.\n")
        except ValueError:
            print("É nescessário que digite apenas números.\n")
            
    modelo_escolhido = modelo[escolha]
    print(f"\n\033[1m--- {modelo_escolhido} ---\033[0m") # [1m ativa o negrito | [0m reseta para o padrão
    tempo = float(input("Insira o tempo de voo (horas): "))
    queima_horaria = float(input("Insira o valor da queima de combustivel por hora: "))
    
    resultado_combustivel = combustivel(tempo, queima_horaria)
    reserva = calcular_reserva(queima_horaria)
    total_com_reserva = resultado_combustivel + reserva
    total_lbs = converter_para_libras(total_com_reserva)
    
    if escolha == 1:
        print(f"\nConsiderando apenas o combustível necessário: {valor_com_virgula(resultado_combustivel)} kg")
        print(f"Reserva de segurança (30min): {valor_com_virgula(reserva)} kg")
        print(f"Total necessário para o voo: {valor_com_virgula(total_com_reserva)} kg / {valor_com_virgula(total_lbs)} lbs")
    
    elif escolha == 2:
        print(f"\nConsiderando apenas o combustível necessário: {valor_com_virgula(resultado_combustivel)} kg")
        print(f"Reserva de segurança (30min): {valor_com_virgula(reserva)} kg")
        print(f"Total necessário para o voo: {valor_com_virgula(total_com_reserva)} kg / {valor_com_virgula(total_lbs)} lbs")
    
    elif escolha == 3:
        print(f"\nConsiderando apenas o combustível necessário: {valor_com_virgula(resultado_combustivel)} kg")
        print(f"Reserva de segurança (30min): {valor_com_virgula(reserva)} kg")
        print(f"Total necessário para o voo: {valor_com_virgula(total_com_reserva)} kg / {valor_com_virgula(total_lbs)} lbs")
        
    elif escolha == 4:
        print(f"\nConsiderando apenas o combustível necessário: {valor_com_virgula(resultado_combustivel)} kg")
        print(f"Reserva de segurança (30min): {valor_com_virgula(reserva)} kg")
        print(f"Total necessário para o voo: {valor_com_virgula(total_com_reserva)} kg / {valor_com_virgula(total_lbs)} lbs")
        
    repeticao = input("\nDeseja realizar outro cálculo ? (s/n)\n").lower()
print(f"Então até logo, piloto {nome_piloto}!")