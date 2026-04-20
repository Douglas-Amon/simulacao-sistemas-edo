# 📊 Simulação de Sistemas Dinâmicos com EDOs

Projeto desenvolvido para a Unidade 3 da disciplina **ECT-33401 - Computação Numérica (UFRN)**.

O objetivo é modelar e simular sistemas dinâmicos utilizando **Equações Diferenciais Ordinárias (EDOs)** resolvidas numericamente pelo método de Euler.

---

## 🚀 Sistemas simulados

* ⚙️ Sistema Massa-Mola-Amortecedor em cascata
* 🐇 Sistema Predador-Presa (Lotka-Volterra modificado)
* 🎯 Pêndulo Amortecido

---

## 🧠 Metodologia

Todos os sistemas foram resolvidos utilizando o **método de Euler**, uma técnica numérica para aproximar soluções de EDOs:

$$
x_{n+1} = x_n + f(x_n, t_n),\Delta t
$$

---

## 📌 1. Sistema Massa-Mola-Amortecedor

Sistema com duas massas acopladas por molas e amortecedores.

Segundo a modelagem (baseada na 2ª Lei de Newton), temos:

$$
m_1 \ddot{x}_1 = -k_1 x_1 - k_2(x_1 - x_2) - b_1 \dot{x}_1 - b_2(\dot{x}_1 - \dot{x}_2)
$$

$$
m_2 \ddot{x}_2 = -k_2(x_2 - x_1) - b_2(\dot{x}_2 - \dot{x}_1) + F
$$

📊 Resultados:

* Oscilações amortecidas ao longo do tempo
* Sistema converge para o equilíbrio

📌 Observação: conforme mostrado nos gráficos, o aumento da massa reduz a amplitude e aumenta o período, enquanto maior amortecimento reduz as oscilações. 

---

## 📌 2. Sistema Predador-Presa

Modelo baseado em Lotka-Volterra modificado:

$$
x' = x(a - cx - dy)
$$

$$
y' = -y(b - ex) - h
$$

📊 Resultados:

* Oscilações iniciais com estabilização ao longo do tempo
* Dependência forte das condições iniciais

📌 Conforme observado nos gráficos, as populações tendem ao equilíbrio após oscilações iniciais. 

---

## 📌 3. Pêndulo Amortecido

Sistema oscilatório com dissipação de energia:

* Perda gradual de energia
* Oscilações decrescentes
* Convergência ao equilíbrio

📊 O diagrama de fase mostra uma espiral convergente típica de sistemas amortecidos.

---

## 📂 Estrutura do Projeto

```bash
📁 simulacao-sistemas-edo
 ├── main.py
 ├── massa_mola.py
 ├── predador_presa.py
 ├── pendulo_amortecido.py
 ├── imagens/
 └── README.md
```

---

## ▶️ Como executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/simulacao-sistemas-edo.git
cd simulacao-sistemas-edo
```

2. Execute:

```bash
python main.py
```

---

## 📊 Resultados

* Sistemas físicos convergem para equilíbrio devido ao amortecimento
* Modelos ecológicos apresentam comportamento oscilatório
* Método de Euler foi eficaz para simulações numéricas

---

## 📌 Tecnologias utilizadas

* Python 3
* NumPy
* Matplotlib

---

## 👨‍💻 Autor

Douglas Amon -
Universidade Federal do Rio Grande do Norte (UFRN)

---

## ⭐ Possíveis melhorias

* Implementar Runge-Kutta (RK4)
* Interface gráfica interativa
* Análise de estabilidade automática
* Animações dos sistemas

---
