#EXERCÍCIO 1: ex01_tupla.py
semana = ("segunda", "terca", "quarta", "quinta", "sexta")

print("Primeiro dia: ", semana[0])
print("Ùltimo dia: ", semana[-1])
print("Dias: ", len(semana))

#EXERCÍCIO 2: ex02_tupla.py
#notas = (8, 3, 7, 5, 2, 9, 4)
for nota in notas:
    if nota >= 5:
        print(nota)

#EXERCÍCIO 3: ex03_tupla.py
numeros = (4, 7, 2, 9, 1, 5)
print("O número 7 aparece", numeros.count(7), "vez(es)")
print("O número 9 está na posição:", numeros.index(9))

#EXERCÍCIO 4: ex04_tupla.py
temperaturas = (36.5, 37.2, 38.0, 36.8, 39.1)
for temperatura in temperaturas:
    if temperatura < 37.5:
        print(temperatura, "Normal")
    elif temperatura <= 38.5:
        print(temperatura, "Febre moderada")
    elif temperatura > 38.5:
        print(temperatura, "Febre alta")