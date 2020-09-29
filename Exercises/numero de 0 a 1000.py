""""
  a = ['a', 'b', 'c']
  b = [1, 2, 3]
  c = {}
   for key in b:
       for value in a:
           c[key] = value
           a.remove(value)
           break
print(c)

a = ['a', 'b', 'c']
b = [1, 2, 3]
c = {a[i] : b[i] for i in range(len(a))}
print(c)

"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = 0

numero_escritos = ['um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez']

dic = {numeros[i]: numero_escritos[i] for i in range(len(numeros))}
print(dic)

for i in dic:
    a = len(dic[i])
    b += a

print(b)
