import sympy as sp

def resolver_integral():
    # Definimos la variable x como símbolo matemático
    x = sp.symbols('x')
    
    print("\n========================================")
    print("   🧮 CALCULADORA INTERACTIVA DE INTEGRALES")
    print("========================================\n")
    
    print("1. Integral Indefinida (obtiene la función + C)")
    print("2. Integral Definida (obtiene el área entre a y b)")
    
    opcion = input("\nSelecciona una opción (1 o 2): ")
    
    try:
        # Entrada de la función
        entrada_f = input("\nIntroduce f(x) [Ejemplo: x**2, sin(x), exp(x), pi*x]: ")
        f = sp.sympify(entrada_f)
        
        if opcion == '1':
            # --- CASO INDEFINIDA ---
            resultado = sp.integrate(f, x)
            print("\n----------------------------------------")
            print(f"Integral Indefinida de: {f}")
            print(f"Resultado: {resultado} + C")
            print("----------------------------------------")
            
        elif opcion == '2':
            # --- CASO DEFINIDA ---
            # Usamos sympify para que acepte 'pi', 'pi/2', 'sqrt(2)', etc.
            lim_a_raw = sp.sympify(input("Límite inferior (a): "))
            lim_b_raw = sp.sympify(input("Límite superior (b): "))
            
            # Convertimos a flotante solo para comparar cuál es mayor
            val_a = float(lim_a_raw.evalf())
            val_b = float(lim_b_raw.evalf())
            
            # Lógica para evitar el error del signo negativo por orden invertido
            if val_a > val_b:
                a, b = lim_b_raw, lim_a_raw
            else:
                a, b = lim_a_raw, lim_b_raw
            
            resultado = sp.integrate(f, (x, a, b))
            
            print("\n----------------------------------------")
            print(f"Integral Definida de {f} en el intervalo [{a}, {b}]")
            # .evalf(4) muestra el resultado con 4 decimales para que sea legible
            print(f"Resultado exacto: {resultado}")
            print(f"Resultado decimal: {resultado.evalf(4)}")
            print("----------------------------------------")
            
        else:
            print("\n❌ Opción no válida. Intenta de nuevo.")

    except Exception as e:
        print(f"\n⚠️ Error: No pude procesar esa expresión. Revisa los paréntesis o símbolos.")
        print(f"Detalle: {e}")

# Ejecutar la función
if __name__ == "__main__":
    resolver_integral()