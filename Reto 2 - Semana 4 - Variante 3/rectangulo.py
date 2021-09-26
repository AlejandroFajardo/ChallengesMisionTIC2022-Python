b = int(input("Ingrese la base: "))
a = int(input("Ingrese la altura: "))

def calcular_area(base, altura):
    return base * altura
    
def calcular_perimetro(base, altura):
    return (2 * base) + (2 * altura)
    
P = calcular_perimetro(b, a)
A = calcular_area(b, a)
print(A, P)

#Elabore un programa en Python que lea dos datos enteros correspondiente a los lados de un rectángulo e imprima el área y el perímetro.