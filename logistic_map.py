""""
O mapa logístico representado por 

x[n + 1] = r * x[n] * (1 - x[n])

descrito inicialmente por Edward Lorenz, onde x[n] é um número que varia entre zero e um, o que representa a proporção da população existente para a população 
máxima possível. O parâmetro r está sempre limitado no intervalo [0,4]. O mapa varia da seguinte forma com os valores de r:

 - Com r entre 0 e 1, a população acabará morrendo, independente da condição inicial (sem caos)

 - Com r entre 1 e 2, a população se aproximará rapidamente do valor (r - 1)/r, independente da condição inicial (sem caos)

- Com r entre 2 e 3, a população também acabará por se aproximar do mesmo valor (r-1)/r, mas primeiro flutuará em torno desse valor por algum tempo. A taxa de 
convergência é linear, exceto para r = 3, quando é dramaticamente lenta, menor que linear.

- Com r entre 3 e 1 + sqrt(6) (3.44949), a população se aproximará de oscilações permanentes entre dois valores. Esses dois valores são dependentes de r e dados por

x_{+-} = (1/2r) * (r + 1 +- sqrt((r-3)(r+1)))

- Com r entre 3.44949 e 3.54409, de quase todas as condições iniciais, a população se aproximará de oscilações permanentes entre quatro valores.

- Com r maior que 3.54409 para quase todas as condições iniciais a população se aproximará de oscilações entre 8 valores, depois 16, 32, ... Os comprimentos dos 
intervalos de parâmetros que produzem oscilações de um determinado comprimento diminuem rapidamente; a relação entre os comprimentos de dois intervalos sucessivos 
de bifurcação se aproxima da constante de Feigenbaum (4.66920). Esse comportamento é um exempo de cascata de duplicação de período.

"""

import numpy as np 
import matplotlib.pyplot as plt 

def logistic_map(x, r):
    x_next = r * x * (1 - x)
    return x_next

#condição inicial:
x_0 = 0.6

#número de passos:
n = 100

#parãmetro r:
r_values = [2.9, 3.3, 3.5, 3.55]

#para simular x ao longo do tempo

for r in r_values:
    #para criar uma lista dos valores de x
    x_values = np.zeros(n + 1)
    x_values[0] = x_0

    for i in range(n):
        x_next = logistic_map(x_values[i], r)
        x_values[i + 1] = x_next
    
    plt.figure() 
    plt.plot(range(n + 1), x_values, linestyle='-')
    plt.xlabel('n')
    plt.ylabel('x[n]')
    plt.title(f'r = {r}')
    plt.grid(True)

plt.show()




