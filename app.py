import streamlit as st
import sympy as sp

# 1. Configuración de la interfaz
st.set_page_config(page_title="Calculadora Integral Pro", page_icon="📐")

st.title("🧮 Solucionador de Integrales Académico")
st.markdown("Esta aplicación resuelve integrales utilizando cálculo simbólico.")

# 2. Barra lateral para opciones
with st.sidebar:
    st.header("Configuración")
    opcion = st.radio("Tipo de Integral:", ["Indefinida", "Definida"])
    st.info("Usa 'pi' para π y '**' para potencias.")

# 3. Entrada de la función
x = sp.symbols('x')
entrada_f = st.text_input("Introduce la función f(x):", value="x**2")

try:
    # Convertimos el texto a una expresión matemática
    f = sp.sympify(entrada_f)
    
    # Mostramos la función en formato LaTeX (bonito)
    st.latex(f"f(x) = {sp.latex(f)}")

    if opcion == "Indefinida":
        if st.button("Resolver"):
            resultado = sp.integrate(f, x)
            st.success("Resultado obtenido:")
            st.latex(r"\int " + sp.latex(f) + r" \, dx = " + sp.latex(resultado) + r" + C")

    else:
        # Caso Definida: Entradas para los límites
        col1, col2 = st.columns(2)
        with col1:
            a_raw = st.text_input("Límite a:", value="0")
        with col2:
            b_raw = st.text_input("Límite b:", value="pi")

        if st.button("Calcular Área"):
            # Procesamos límites con la lógica de orden que ya perfeccionamos
            lim_a = sp.sympify(a_raw)
            lim_b = sp.sympify(b_raw)
            
            v_a = float(lim_a.evalf())
            v_b = float(lim_b.evalf())
            
            # Ordenamos para que siempre dé positivo (el área)
            a, b = (lim_a, lim_b) if v_a <= v_b else (lim_b, lim_a)
            
            resultado = sp.integrate(f, (x, a, b))
            
            st.success(f"Área en el intervalo [{a}, {b}]")
            st.latex(r"\int_{" + sp.latex(a) + r"}^{" + sp.latex(b) + r"} " + sp.latex(f) + r" \, dx = " + sp.latex(resultado))
            st.write(f"**Valor decimal aproximado:** {resultado.evalf():,.2f}")
            

except Exception as e:


    st.error(f"Error en la expresión: {e}")