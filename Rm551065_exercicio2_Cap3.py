
print("\tVotação da live:\n ")
segunda = int(input("1 - segunda-feira "))
terca = int(input("2 - terça-feira "))
quarta = int(input("3 - quarta-feira "))
quinta = int(input("4 - quinta-feira "))
sexta = int(input("5 - sexta-feira "))

d_votado = 0
d_escolhido = 0

if segunda > d_votado:
    d_votado = segunda
    d_escolhido = "SEGUNDA-FEIRA"

if terca > d_votado:
    d_votado = terca
    d_escolhido = "TERÇA-FEIRA"

if quarta > d_votado:
    d_votado = quarta
    d_escolhido = "Quarta-feira"

if quinta > d_votado:
    d_votado = quinta
    d_escolhido = "Quinta-feira"

if sexta > d_votado:
    d_votado = sexta
    d_escolhido = "SEXTA-FEIRA"

if d_escolhido == 0:
    print("Voto Invalido")

percentual = d_votado/(segunda + terca + quarta + quinta + sexta) * 100
print(f"O dia mais votado da semana foi {d_escolhido} com o total de {d_votado} votos e o percentual de {percentual:.0f}%")