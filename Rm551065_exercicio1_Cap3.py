faturamento_anual = float(input("Por favor, informe o faturamento anual: "))
tipo_assinatura = input("Informe o tipo de assinatura: Basic - 1, Silver - 2, Gold - 3, Platinum - 4 ")
percentual = 0


if tipo_assinatura == "1":
    percentual = faturamento_anual * 0.30

elif tipo_assinatura == "2":
    percentual = faturamento_anual * 0.20

elif tipo_assinatura == "3":
    percentual = faturamento_anual * 0.10

elif tipo_assinatura == "4":
    percentual = faturamento_anual * 0.05

else:
    print("Tipo de assinatura inválida!!")

print(f"O valor do bonus a receber é R${percentual:.2f}")


