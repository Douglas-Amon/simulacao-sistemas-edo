import numpy as np
import matplotlib.pyplot as plt
import math

# Considere os seguintes parâmetros no ecossistema:

a = 1
b = 0.25
c = 0.01
d = 0.02
e = 0.02
h = 0

# Parâmetros da simulação
dt = 0.01  # Passo dt (seconds)
T = 100   # tempo total de simulação (seconds)
num_passos = int(T / dt)

# Inicialização dos parâmetros a serem simulados
t = np.linspace(0, T, num_passos)
x = np.zeros(num_passos)  # quantidade de presas
y = np.zeros(num_passos) # quantidade de predadores

# Condições iniciais
x[0] = 30 # número de presas
y[0] = 15 # número de predadores

# Método de Euler
for n in range(num_passos - 1):
    # Calcula a derivada de x e y
    dx_dt = x[n] * (a - c*x[n] - d*y[n])
    dy_dt = -y[n] * (b - e*x[n]) - h

    # Equações de Euler
    x[n + 1] = x[n] + dx_dt * dt

    y[n + 1] = y[n] + dy_dt * dt

# Resultados obtidos
plt.figure(figsize=(14, 4))

plt.plot(t, x, 'g')
plt.title('Evolução da quantidade de presas em função do tempo')
plt.xlabel('Tempo (s)')
plt.ylabel('Quantidade de presas')
plt.grid()

plt.show()

plt.figure(figsize=(14, 4))
plt.plot(t, y, 'r')
plt.title('Evolução da quantidade de predadores em função do tempo')
plt.xlabel('Tempo (s)')
plt.ylabel('Quantidade de predadores')
plt.grid()
plt.show()

# Diagrama de fase
# Cria uma grade para o campo direcional
grade_x, grade_y = np.meshgrid(np.linspace(0, 40, 20), np.linspace(15, 75, 20))

# Calcula o campo direcional
dx_grade = grade_x * (a - c*grade_x - d*grade_y)
dy_grade = -grade_y * (b - e*grade_x - h)

# Normaliza os vetores direcionais para uma melhor visualização
magnitude_grade = np.sqrt(dx_grade**2 + dy_grade**2)
magnitude_grade[magnitude_grade == 0] = 1  # Para evitar divisão por zero
dx_grade /= magnitude_grade
dy_grade /= magnitude_grade

# Fator de escala para o comprimento dos vetores
fator_escala = 1.5

# Plotando o campo direcional e os diagramas de fase
plt.figure(figsize=(12, 6))

# Campo direcional
plt.quiver(grade_x, grade_y, dx_grade * fator_escala, dy_grade * fator_escala,
           angles='xy', scale_units='xy', scale=1, color='purple', alpha=0.7,
           headlength=3, headwidth=2)

# Trajetória
plt.plot(x, y, color='blue', label='Trajetória / evolução do ecossistema')

# Configurações do gráfico
plt.title('Campo Direcional e Diagrama de Fase: Predador-Presa')
plt.xlabel('Quantidade de Presas (x)')
plt.ylabel('Quantidade de Predadores (y)')
plt.legend()
plt.grid()
plt.show()

