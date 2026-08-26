from vehiculo import Vehiculo # Importa la clase Vehiculo desde el archivo local vehiculo.py

vehiculo1 = Vehiculo("AB1234", 2018) # Instancia el primer objeto Vehiculo pasándole su patente y año
vehiculo2 = Vehiculo("CD5678", 2020) # Instancia el segundo objeto Vehiculo pasándole su patente y año
vehiculo3 = Vehiculo("EF9012", 2023) # Instancia el tercer objeto Vehiculo pasándole su patente y año

print(vehiculo1.ingresar()) # Ejecuta ingresar() del primer vehículo y muestra el texto retornado en consola
print(vehiculo2.ingresar()) # Ejecuta ingresar() del segundo vehículo y muestra el texto retornado en consola
print(vehiculo3.ingresar()) # Ejecuta ingresar() del tercer vehículo y muestra el texto retornado en consola

print(f"Tarifa por hora del primer vehículo: ${vehiculo1.tarifa_hora()}") # Concatena e imprime la tarifa retornada por el primer vehículo
print(f"Tarifa por hora del segundo vehículo: ${vehiculo2.tarifa_hora()}") # Concatena e imprime la tarifa retornada por el segundo vehículo
print(f"Tarifa por hora del tercer vehículo: ${vehiculo3.tarifa_hora()}") # Concatena e imprime la tarifa retornada por el tercer vehículo
