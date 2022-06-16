"""Programa para calcular la nota final de un estudiante en una materia
por las calificaciones de sus evaluaciones"""



print("--------------------------------")
print("------ NOTAS ESTUDIANTES -------")
print("--------------------------------")
#Input
cod = int(input("Digite el código del estudiante: "))
if cod!=0:
    nota1 = float(input("Digite la de la primera evaluacion: "))
    nota2 = float(input("Digite la de la segunta evaluacion: "))
    nota3 = float(input("Digite la de la tercera evaluacion: "))
    nota4 = float(input("Digite la de la cuarta evaluacion: "))
    nota5 = float(input("Digite la de la quita evaluacion: "))

else:
    print("Fin de los datos de entrada")

#prossecing
reprobados = 0
while cod != 0:
    nota_final = (nota1 + nota2 + nota3 + nota4 + nota5)/5
    print("la nota definitiva de el estudiante con el codigo " + str(cod) + " fue de " + str(nota_final))
    cod = int(input("Digite el codigo del estudiante: "))
    if cod!=0:
            nota1 = float(input("Digite la de la primera evaluacion: "))
            nota2 = float(input("Digite la de la segunta evaluacion: "))
            nota3 = float(input("Digite la de la tercera evaluacion: "))
            nota4 = float(input("Digite la de la cuarta evaluacion: "))
            nota5 = float(input("Digite la de la quita evaluacion: "))
    else:
        print("fin de la entrada")
    if nota_final < 3:
        reprobados = reprobados + 1
#Output
print(str(reprobados) + " reprobaron la materia")
print("Thats all...")