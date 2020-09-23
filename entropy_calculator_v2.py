import math

print("Sistemas de Comunicacao III")
print("Calculadora de entropia")
print("By: Matheus de Souza Magalhães")
print("*******************************")
n = 3
pk = 0.55,0.35,0.1
s = '00','01','111'
print("Os símbolos são: ", s)
print("As probabilidades de símbolo são: ", pk)



def entropia():
    h = 0
    lenght  = len(pk)
    for x in range(0,lenght):
        pb = pk[x]*math.log2(1/pk[x])
        h = h + pb
    print("H(S) = %.3f" %h)
   
    l = 0 
    for i in range(0,n):
        l += len(s[i])*pk[i]
    print("L = %.2f" %l)
    
    ef = h/l 
    print("Eficiencia = %.4f" % ef)

entropia()