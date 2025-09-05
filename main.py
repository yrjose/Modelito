import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Título da aplicação
st.title("Visualizador de Polinômio de Grau 3")

# Sliders para escolher os coeficientes
a = st.slider("Coeficiente a (x³)", -10.0, 10.0, 1.0)
b = st.slider("Coeficiente b (x²)", -10.0, 10.0, 0.0)
c = st.slider("Coeficiente c (x)", -10.0, 10.0, 0.0)
d = st.slider("Coeficiente d (termo independente)", -10.0, 10.0, 0.0)

#comentario massa 17:10 05/09/25
#comentario muito massa 17:28 05/09/25
# Intervalo de x
x = np.linspace(-10, 10, 400)
y = a*x**3 + b*x**2 + c*x + d

# Cria gráfico
fig, ax = plt.subplots()
ax.plot(x, y, label=f"{a:.1f}x³ + {b:.1f}x² + {c:.1f}x + {d:.1f}")
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
ax.set_title("Gráfico do Polinômio")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.grid(True)
ax.legend()

# Mostra gráfico no app
st.pyplot(fig)

#streamlit run app.py
