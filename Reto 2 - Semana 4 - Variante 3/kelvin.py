K = float(input("Ingrese los grados Kelvin: "))

def calcular_fahrenheit(grados_kelvin):
    return (grados_kelvin - 273.15) * (9/5) + 32
    
F = calcular_fahrenheit(K)
print("Para una temperatura de ", K, " grados Kelvin, se obtienen ", F, " grados fahrenheit")