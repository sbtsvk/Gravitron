import math
import matplotlib.pyplot as plt

# Función para calcular la fuerza centrípeta
def fuerza_centrípeta(m, R, w):
    return m * R * w**2

# Obtener los datos del usuario
R = float(input("Ingrese el radio del cilindro en metros: "))
m = float(input("Ingrese la masa de la persona (lata de aluminio) en kg: "))
g = 9.81  # Aceleración debido a la gravedad en m/s^2
w = float(input("Ingrese la velocidad angular del cilindro en rad/s: "))

# Definir coeficientes de fricción estática para diferentes superficies
mu_e_metal = 0.3  # Coeficiente de fricción estática para superficie de metal
mu_e_plastico = 0.5  # Coeficiente de fricción estática para superficie de plástico
# Calcular las fuerzas centrípetas para cada tipo de superficie
Fc_metal = fuerza_centrípeta(m, R, w)
Fc_plastico = fuerza_centrípeta(m, R, w)

# Graficar las fuerzas en función de la velocidad angular
w_values = [i / 10 for i in range(int(w * 10), int(2 * w * 10) + 1)]  # Rango de velocidades angulares para la gráfica

# Graficar fuerza centrípeta para superficie de metal
Fc_metal_values = [fuerza_centrípeta(m, R, w) for w in w_values]
plt.plot(w_values, Fc_metal_values, label="Fuerza Centrípeta (Metal)")

# Graficar fuerza centrípeta para superficie de plástico
Fc_plastico_values = [fuerza_centrípeta(m, R, w) for w in w_values]
plt.plot(w_values, Fc_plastico_values, label="Fuerza Centrípeta (Plástico)")
# Configuración de la gráfica
plt.title("Comparación de Fuerza Centrípeta para Diferentes Superficies")
plt.xlabel("Velocidad Angular (rad/s)")
plt.ylabel("Fuerza Centrípeta (N)")
plt.legend()
plt.grid(True)
plt.show()
