# Matheus de Souza Magalhães

# Calculadora de Entropia 

# Basta colocar as probabilidades no vetor pk

import math
pk = 0.55,0.35,0.1
h = 0
lenght  = len(pk)

for x in range(0,lenght):
    pb = pk[x]*math.log2(1/pk[x])
    h = h + pb
print(h)

