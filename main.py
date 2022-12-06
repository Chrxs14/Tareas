numero = int(input("ingrese el número a convertir: "))
modulos = []
num_binario = ""
numInicial = numero

while (numero !=0 ):
  modulo = numero % 2
  resultado = numero //2
  numero = resultado
  modulos.append(modulo)

modulos.reverse()
num_binario = ''.join([str(_) for _ in modulos])
print(f"el numero {numInicial} en binario es: {int(num_binario)}")

nombre = input("como se llama? ")
print(f"me alegro de conocerlo {nombre}")