def crear_sala():
    print("\nBIENVENIDO AL SISTEMA DE GESTIÓN DE CINE")
    print("=" * 50)
    
    while True:
        try:
            filas = int(input("Ingresa el número de filas: "))
            columnas = int(input("Ingresa el número de asientos por fila: "))
            
            if filas <= 0 or columnas <= 0:
                print("El número de filas y columnas debe ser mayor a 0.")
                continue
            sala = [["L" for _ in range(columnas)] for _ in range(filas)]
            print(f"Sala creada: {filas} filas x {columnas} asientos")
            return sala
        except ValueError:
            print("❌ Por favor, ingresa números válidos.")

def mostrar_sala(sala):
    if not sala:
        print("❌ Primero debes crear la sala.")
        return
    
    print("\n🎭 SALA DE CINE")
    print("=" * (len(sala[0]) * 3 + 10))

    print("   ", end="")
    for i in range(len(sala[0])):
        print(f"{i+1:2}", end=" ")
    print()

    for i in range(len(sala)):
        print(f"{i+1:2} ", end="")
        for j in range(len(sala[i])):
            if sala[i][j] == "L":
                print("🟩", end="")  
            else:
                print("🟥", end="")  
        print()
    
    print("🟩 = Libre | 🟥 = Ocupado")
    print("=" * (len(sala[0]) * 3 + 10))

def reservar_asiento(sala):
    if not sala:
        print("❌ Primero debes crear la sala.")
        return sala
    
    mostrar_sala(sala)
    try:
        fila = int(input("\nIngresa el número de fila: ")) - 1
        columna = int(input("Ingresa el número de asiento: ")) - 1
        if fila < 0 or fila >= len(sala) or columna < 0 or columna >= len(sala[0]):
            print("❌ Asiento no válido. Verifica los números.")
            return sala

        if sala[fila][columna] == "L":
            sala[fila][columna] = "X"
            print(f"✅ Asiento {fila+1}-{columna+1} reservado exitosamente!")
        else:
            print("❌ Este asiento ya está ocupado.")
            
    except ValueError:
        print("❌ Por favor, ingresa números válidos.")
    return sala

def liberar_asiento(sala):
    if not sala:
        print("❌ Primero debes crear la sala.")
        return sala
    
    mostrar_sala(sala)
    
    try:
        fila = int(input("\nIngresa el número de fila: ")) - 1
        columna = int(input("Ingresa el número de asiento: ")) - 1
        
        if fila < 0 or fila >= len(sala) or columna < 0 or columna >= len(sala[0]):
            print("❌ Asiento no válido. Verifica los números.")
            return sala

        if sala[fila][columna] == "X":
            sala[fila][columna] = "L"
            print(f"✅ Asiento {fila+1}-{columna+1} liberado exitosamente!")
        else:
            print("❌ Este asiento ya está libre.")
            
    except ValueError:
        print("❌ Por favor, ingresa números válidos.")
    
    return sala

def contar_asientos(sala):
    if not sala:
        print("❌ Primero debes crear la sala.")
        return
    
    libres = 0
    ocupados = 0
    total = 0
    
    for fila in sala:
        for asiento in fila:
            if asiento == "L":
                libres += 1
            else:
                ocupados += 1
            total += 1
    
    print("\nESTADÍSTICAS DE LA SALA")
    print("=" * 50)
    print(f"Asientos libres: {libres}")
    print(f"Asientos ocupados: {ocupados}")
    print(f"Total de asientos: {total}")
    
    if total > 0:
        porcentaje_ocupacion = (ocupados / total) * 100
        print(f"Porcentaje de ocupación: {porcentaje_ocupacion:.1f}%")
    
    print("=" * 50)

def main():

    sala = None
    
    while True:
        print("\n" + "=" * 50)
        print("🎬 SISTEMA DE GESTIÓN DE CINE")
        print("=" * 50)
        print("1. Crear sala de cine")
        print("2. Mostrar sala")
        print("3. Reservar asiento")
        print("4. Liberar asiento")
        print("5. Contar asientos ocupados y libres")
        print("6. Salir")
        print("=" * 50)
        
        opcion = input("Selecciona una opción (1-6): ")
        
        if opcion == "1":
            sala = crear_sala()
        elif opcion == "2":
            mostrar_sala(sala)
        elif opcion == "3":
            sala = reservar_asiento(sala)
        elif opcion == "4":
            sala = liberar_asiento(sala)
        elif opcion == "5":
            contar_asientos(sala)
        elif opcion == "6":
            print("🎭 ¡Gracias por usar el sistema de cine! ¡Hasta pronto!")
            break
        else:
            print("❌ Opción no válida. Por favor, selecciona 1-6.")

if __name__ == "__main__":
    main()
    