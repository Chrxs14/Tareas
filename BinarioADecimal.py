numero = input("ingrese el número a convertir: ")
numBinario = []
exponentes = []
binario2 = []
num = 0
res = []
decimal = 0
c=0

for n in numero:
  numBinario.append(int(n))
  exponentes.append(num)
  num += 1

numBinario.reverse()

for n in numBinario:
  if n == 1:
    binario2.append(2)
  else:
    binario2.append(0)

while(c<len(binario2)):
  res.append(binario2[c]**exponentes[c])
  decimal += numBinario[c]*res[c]
  c+=1
print("El valor decimal es: ",decimal)