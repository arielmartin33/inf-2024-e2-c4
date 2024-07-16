#logica para calcular el tiempo total de viaje

#se puede usar la funcion zfill para completar con ceros los minutos y horas (funcion de tipo string)


print("Ingrese los tiempos de viaje de cada tramos, 0 para finalizar")
print()
tiempo_total = 0

while True:
    tiempo_tramo = int(input("ingrese el tiempo del tramo: "))
    if tiempo_tramo == 0:
        break
    else:
        tiempo_total += tiempo_tramo

tiempo_total_horas = str(tiempo_total // 60).zfill(2) #Calculo las horas
tiempo_total_minutos = str(tiempo_total % 60).zfill(2) #calculo los minutos

print(f'El tiempo total del viaje es: {tiempo_total_horas}:{tiempo_total_minutos} hs')