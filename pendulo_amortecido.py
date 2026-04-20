import numpy as np
import matplotlib.pyplot as plt

# Parâmetros iniciais
L = 2
L0 = 1
k = 40
m = 1
g = 9.81
theta = np.pi * 3/4

# Parâmetros da simulação
dt = 0.001  # Passo dt (seconds)
T = 30.0   # tempo total de simulação (seconds)
num_passos = int(T / dt)

# Iniciação dos parâmetros a serem simulados
t = np.linspace(0, T, num_passos)
x1 = np.zeros(num_passos)
x2 = np.zeros(num_passos)

# Condições iniciais
x1[0] = 0
x2[0] = 0

# Utilizando o método de Euler
for n in range(num_passos - 1):
  dx1_dt = -(g*np.sin(theta) + 2*x1[n]*x2[n])/L
  dx2_dt = ((m*L*x1[n]**2) - (k*(L-L0)) + (m*g*(np.cos(theta))))/m

  # Equações de Euler para iterar
  x1[n+1] = x1[n] + dx1_dt * dt
  x2[n+1] = x2[n] + dx2_dt * dt

# Resultados obtidos
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, x1)
plt.title('Velocidade em função do tempo')
plt.xlabel('Tempo (s)')
plt.ylabel('x1')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(t, x2)
plt.title('Posição em função do tempo')
plt.xlabel('Tempo (s)')
plt.ylabel('x2')
plt.grid()

plt.tight_layout()
plt.show()


# Diagrama de fase
# Cria uma grade para o campo direcional
grade_x, grade_y = np.meshgrid(np.linspace(-12.5, 0, 20), np.linspace(-15, 15, 20))

# Calcula o campo direcional
dx_grade = (-1/L) * (g*np.sin(theta) + 2*grade_x*grade_y)
dy_grade = (1/m) * ((m*L*grade_x**2) - (k*(L-L0)) + (m*g*(np.cos(theta))))

# Normaliza os vetores direcionais para uma melhor visualização
magnitude_grade = np.sqrt(dx_grade**2 + dy_grade**2)
magnitude_grade[magnitude_grade == 0] = 1  # Para evitar divisão por zero
dx_grade /= magnitude_grade
dy_grade /= magnitude_grade

# Fator de escala para o comprimento dos vetores
fator_escala = 0.5

# Plotando o campo direcional e os diagramas de fase
plt.figure(figsize=(12, 10))

# Campo direcional
plt.quiver(grade_x, grade_y, dx_grade * fator_escala, dy_grade * fator_escala,
           angles='xy', scale_units='xy', scale=1, color='purple', alpha=0.8,
           headlength=3, headwidth=2)

# Trajetória
plt.plot(x1, x2, color='blue', label='Trajetória / evolução do pêndulo amortecido \n com o passar do tempo')

# Configurações do gráfico
plt.title('Diagrama de Fase e Campo Direcional: Pêndulo amortecido')
plt.xlabel('Posição')
plt.ylabel('Velocidade')
plt.legend()
plt.grid()
plt.show()