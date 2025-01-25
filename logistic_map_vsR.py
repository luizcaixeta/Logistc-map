import numpy as np 
import matplotlib.pyplot as plt 

def logistic_map(x, r):
    return r * x * (1 - x)

#condição inicial:
x_0 = 0.6

#valores de r:
r_values = np.linspace(0., 4., 10000) # Se o x_n está no intervalo [0,1] então r está no intervalo [0,4]

#número de passos:
n = 1000

#lista para armazenar os valores de x para cada valor de r
x_values = np.zeros((len(r_values), n+1))

#iterar sobre os valores de r e calcular os valores de x
for i, r in enumerate(r_values):
    x = x_0
    x_values[i, 0] = x_0
    for j in range(1, n+1):
        x = logistic_map(x, r)
        x_values[i, j] = x

#plotar x por r
plt.figure(figsize=(10, 6))
for i in range(len(r_values)):
    plt.plot(r_values[i] * np.ones_like(x_values[i]), x_values[i], marker=',', color='black', markersize=0.1, linestyle='') # np.ones_like gera uma matriz do tamanho de r_values totalmente preenchida pelo número 1

plt.xlabel('r')
plt.ylabel('x')
plt.title('Bifurcação')
plt.show()

