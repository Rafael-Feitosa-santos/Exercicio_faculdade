minutos = int(input("Digite os minutos atuais: "))
fatorial = 1

for i in range(1, minutos + 1):
    fatorial = fatorial * i

print("A senha para desbloquear é: LIBERDADE{}".format(fatorial))

