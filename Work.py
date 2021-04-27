import pyodbc
import SystemInformation as sys
import Financial as finance
#información necesario para la conexion. BD alojada en Azure
server = 'sqlmarioc.database.windows.net'
database = 'Proyecto'
username = 'adminsql'
password = 'Admin123'   
driver= '{ODBC Driver 17 for SQL Server}'

def MainMenu():
    fin = False
    Menu()
    while fin==False:
      
        opcion = input(">: ")
        if opcion == "testconaz":
            AzureDatabaseSelect("Usuarios")
        elif opcion == "sysinfo":
            sys.SystemInformation()
        elif opcion == "finance":
            finance.Menu()
        elif opcion == "menu":
            Menu()
        elif opcion.startswith("echo"):
            echo(opcion)
        elif opcion == "help" or opcion == "/?":
            print("Comandos: menu, testconaz, sysinfo, finance, echo, scan, exit/99")
        elif opcion == "exit" or opcion == "99":
            fin = True
            exit()
        elif opcion == "scan":
            print("insertar escaneo aquí")
        elif input == "":
            print("No se ha encontrado ninguna orden")
        else:
            print("Comando no reconocido. Ejecute help o /? para ver los comandos disponibles")

def Menu():
    print("seleccione su opción: ")
    print("\ntestconaz:Comprobar conexion a base de datos en Azure")
    print("\nsysinfo:Mostrar datos del sistema")
    print("\nfinance:Abrir menu financiero")
    print("\n99: Salir")

def AzureDatabaseSelect(tabla):
    print("Conectandose a la BBDD de Azure")
    with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM dbo."+ tabla)
            row = cursor.fetchone()
            print("IdTransacn, id")
            while row:
                print (str(row[0]) + "         " + str(row[1]))
                row = cursor.fetchone()
    print("Conexion a Azure satisfactoria")            

def InsertarDoctor():
    print("Insertando Doctor en la tabla")

def echo(texto):
    cadena = texto.replace("echo ","")
    cadena = cadena.replace("\"","")
    print(cadena)