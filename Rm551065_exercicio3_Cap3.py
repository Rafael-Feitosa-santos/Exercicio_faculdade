
print("\tCalculo da soma das notas e Média\n")

n_pares = 0
n_impares = 0
media_geral = 0.0

for impares in range(1,51,2):
    n_impares +=float(input(f"Inserindo as notas de alunos ÍMPARES.\nInforme a nota do aluno {impares}: "))

for pares in range(2,51,2):
    n_pares += float(input(f"Inserindo as notas de alunos PARES.\nInforme a nota do aluno {pares}: "))

if n_pares > n_impares:
    media_geral = n_pares / 25
    print(f"A média da turma PAR foi {media_geral}. Maior que a impar! ")

elif n_impares > n_pares:
    media_geral = n_impares / 25
    print(f"A média da turma IMPAR foi {media_geral}. Maior que a par! ")

else:
    media_geral = (n_impares + n_pares) / 50
    print(f"A Média da duas turmas foram {media_geral}")
