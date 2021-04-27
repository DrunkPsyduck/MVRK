def Menu():
    print("Menu financiero")
    fin = False
    while fin==False:
        print("seleccione su opción: ")
        print("\n1: Pecio Actual BTC")
        print("\n99: Salir")
        opcion = input(">: ")
        if opcion == "1":
            GetBtcCurrentPrice();
        elif opcion == "2":
            print("")
        elif opcion == "3":
            finance.Menu()
        elif opcion == "99":
            fin = True
        elif input == "":
            print("No se ha encontrado ninguna orden")
            
        input("Pulse cualquier tecla para continuar... ")


def GetBtcCurrentPrice():
    print("2")