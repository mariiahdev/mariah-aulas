#EXERCÍCIO 1: 
alunos = ["emanuel", "mariah", "nicholas", "stephany", "giovanna"]
print(alunos[0])
print(alunos[-1])

#EXERCÍCIO 2: 
lista = [7, 4, 9, 6, 3]
lista.append(8)
lista.pop(1)
print(lista)
print(len(lista))

#EXERCÍCIO 3:
lista = [8, 3, 7, 5, 2, 9, 4]
for i in lista: 
  if i < 5:
    print(i)

#EXERCÍCIO 4:
pares = []
for i in range(1, 21):
  if i % 2 == 0:
    pares.append(i)
  print(pares)
  print(len(pares))