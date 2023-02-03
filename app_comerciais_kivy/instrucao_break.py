"""
INSTRUÇÃO BREAK

É a instrução que interrompe a execução do laço
de repetição a qual está contida
"""

"""

for i in range(10):
    if(True):
        break

i = 10
while(i<100):
    i = i + 1
    if(True):
        break
"""

"""
print("Antes de entrar no laço")

for item in range(10):
    print(item)
    if(item == 6):
        break

print("depois de entrar no laço")
"""

"""
INSTRUÇÃO CONTINUE

É a instrução que interrompe a execução de 
apenas um único ciclo

"""

"""
for i in range (10):
    if (True):
        continue

i = 10
while(i<10):
    i += 1
    if(True):
        continue
"""

print()
print('inicio')
i = 0

while(i<10):
    i += 1
    if(i%2==0):
        continue
    if(i>5):
        break
    print(i)
else:
    print('else')

print('fim')
print()









































