import math
import time
import matplotlib.pyplot as plt

def calcular_w_min(R, mu_e, g):
    return math.sqrt(g / (R * (1 + mu_e)))

def simular_rotacion(R, w, mu_e, g, duracion):
    w_min = calcular_w_min(R, mu_e, g)
    tiempo_total = 0
    posicion_lata = 0
    tiempos = []
    posiciones = []

    while tiempo_total < duracion:
        tiempo_transcurrido = 0.01
        aceleracion_angular = (mu_e * g) / R
        velocidad_angular_relativa = w - aceleracion_angular / w

        desplazamiento_angular = velocidad_angular_relativa * tiempo_transcurrido
        posicion_lata += desplazamiento_angular * R

        tiempos.append(tiempo_total)
        posiciones.append(posicion_lata)

        if w < w_min:
            print(f"La lata cayó a los {tiempo_total:.2f} segundos.")
            break

        tiempo_total += tiempo_transcurrido
        # time.sleep(0.01)

    if w >= w_min:
        print("La lata no cayó.")

    # Plotear los resultados
    plt.figure(figsize=(8, 6))
    plt.plot(tiempos, posiciones)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Posición de la lata (m)')
    plt.title('Simulación del Gravitrón')
    plt.grid(True)
    plt.show()

# Valores de ejemplo
R = 1.5  # Radio del cilindro en metros
w = 5.0  # Velocidad angular inicial en radianes/segundo
mu_e = 0.3  # Coeficiente de fricción estática
g = 9.81  # Aceleración gravitacional en m/s^2
duracion = 100  # Duración de la simulación en segundos

simular_rotacion(R, w, mu_e, g, duracion)