import streamlit as st 


#Titulo
st.write("""
# Mi proyecto de tecnología

En este proyecto realizaré una propuesta de herramienta para calcular las probabilidades de un evento
Realizado por 

***Salome Mahecha Cortés***

**Septimo grado del colegio Liceo Garden High school**
""")

st.write("""
# Calculadora de probabilidad básica
	
Una calculadora de probabilidad básica es una herramienta que permite a los usuarios calcular la probabilidad de un evento único. 
La probabilidad de un evento se puede definir como la medida de la posibilidad de que ese evento ocurra. 
La fórmula para calcular la probabilidad de un evento único es: 

**P(E) = n(E)/n(S)**
	
donde:

-**P(E)** es la probabilidad de que el evento **E** ocurra.

-**n(E)** es el número de resultados favorables al evento **E**.

-**n(S)** es el número total de resultados posibles.

# Ejemplo:

Si hay 8 caramelos en un frasco, de los cuales 3 son caramelos de coco y 5 caramelos de chocolate. ¿Cuál es la probabilidad de que se recoja un caramelo de coco?

Solución:

Paso 1: Calcularemos la probabilidad de caramelos de coco. Entonces,

n (E) = 3

n (S) = 8

Paso 2: Usemos la formula para calcular la probabilidad.

P (E) = n (E) / n (S)

P (E) = 3/8

P (E) = 0,375 o 37,5%  

# Calculadora


""")

st.subheader('A continuación seleccione el número de resultados favorables al evento n(E):')
E = st.slider('número de resultados favorables al evento:', min_value=1, max_value=20, value=2, step=1)

	
st.subheader('A continuación seleccione el número total de resultados posibles n(S):')
S = st.slider('número total de resultados posibles:', min_value=1, max_value=20, value=2, step=1)

PE = (int(E) / int (S))*100

st.subheader(f"Probabilidad: {round(PE,1)}%")

st.markdown("😎")



