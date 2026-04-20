import numpy as np
import matplotlib.pyplot as plt

# Parâmetros iniciais
m1 = 20
m2 = 20
k1 = 1000
k2 = 2000
b1 = 1
b2 = 5

# Parâmetros da simulação
dt = 0.0001
T = np.arange(0, 100, dt)
n_passos = len(T)  # Número de passos no intervalo

# Inicializar x1, v1, x2, v2 com tamanho compatível
x1 = np.empty(n_passos)
x2 = np.empty(n_passos)
v1 = np.empty(n_passos)
v2 = np.empty(n_passos)

# Condições iniciais
x1[0] = 1
x2[0] = 0
v1[0] = 0.5
v2[0] = -0.5
F = 10

# Função para simular o sistema usando o método de Euler
def euler_metodo(x_1, x_2, v_1, v_2):
    for n in range(n_passos - 1):  # Itera até n_passos - 1
        x1[n + 1] = x1[n] + v1[n] * dt
        x2[n + 1] = x2[n] + v2[n] * dt

        v1[n + 1] = v1[n] + (dt / m1) * (-k1 * x1[n] - k2 * (x1[n] - x2[n]) - b1 * v1[n] - b2 * (v1[n] - v2[n]))
        v2[n + 1] = v2[n] + (dt / m2) * ((-k2 * (x2[n] - x1[n])) - b2 * (v2[n] - v1[n]) + F)

euler_metodo(x1, x2, v1, v2)

# Criação de subplots para exibir os gráficos
fig, axs = plt.subplots(2, 2, figsize=(18, 8))

# Configurar gráficos individuais
axs[0, 0].plot(T, x1, 'magenta')
axs[0, 0].set(xlabel='Tempo (s)', ylabel='Posição x1 (m)', title='Deslocamento x1 x Tempo')
axs[0, 0].grid()

axs[0, 1].plot(T, x2, 'green')
axs[0, 1].set(xlabel='Tempo (s)', ylabel='Posição x2 (m)', title='Deslocamento x2 x Tempo')
axs[0, 1].grid()

axs[1, 0].plot(T, v1, 'blue')
axs[1, 0].set(xlabel='Tempo (s)', ylabel='Velocidade v1 (m/s)', title='Velocidade (v1) x Tempo')
axs[1, 0].grid()

axs[1, 1].plot(T, v2, 'purple')
axs[1, 1].set(xlabel='Tempo (s)', ylabel='Velocidade v2 (m/s)', title='Velocidade (v2) x Tempo')
axs[1, 1].grid()

# Ajuste do espaçamento entre os subplots
plt.subplots_adjust(hspace=0.4, wspace=0.3)

plt.show()

# Diagrama de fase
plt.figure(figsize=(14, 10))

# Criar grade para as setinhas
x1_grade = np.linspace(min(x1), max(x1), 20)
v1_grade = np.linspace(min(v1), max(v1), 20)
X1, V1 = np.meshgrid(x1_grade, v1_grade)

# Calcular as direções das setinhas (neste caso, usando um modelo simples)
U1 = V1
V1_seta = -X1  # Modelo simplificado de oscilador

# Normalizar os vetores
norma_1 = np.sqrt(abs(U1)*2 + abs(V1_seta)*2)
U1_seta = U1/norma_1
V1_seta = V1_seta/norma_1

plt.subplot(2, 2, 3)
plt.quiver(X1, V1, U1_seta, V1_seta, alpha=0.7, color='green')
plt.plot(x1, v1, 'b-', label='Massa 1', linewidth=2)
plt.grid(True, alpha=0.3)
plt.xlabel('Posição do bloco 1 (m)')
plt.ylabel('Velocidade do bloco 1 (m/s)')
plt.title('Diagrama de Fases - Bloco 1 - x1 x v1')

# Criar grade para as setinhas
x2_grade = np.linspace(min(x2), max(x2), 20)
v2_grade = np.linspace(min(v2), max(v2), 20)
X2, V2 = np.meshgrid(x2_grade, v2_grade)

# Calcular as direções das setinhas
U2 = V2
V2_seta = -X2  # Modelo simplificado de oscilador

# Normalizar os vetores
norma_2 = np.sqrt(abs(U2)*2 + abs(V2_seta)*2)
U2_seta = U2/norma_2
V2_seta = V2_seta/norma_2

plt.subplot(2, 2, 4)
plt.quiver(X2, V2, U2_seta, V2_seta, alpha=0.7, color='green')
plt.plot(x2, v2, 'r-', label='Massa 2', linewidth=2)
plt.grid(True, alpha=0.3)
plt.xlabel('Posição do bloco 2 (m)')
plt.ylabel('Velocidade do bloco 2 (m/s)')
plt.title('Diagrama de Fases - Bloco 2 - x2 x v2')

plt.tight_layout()
plt.show()