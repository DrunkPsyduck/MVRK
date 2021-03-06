import pyodbc
import SystemInformation as sys
import Financial as finance
import platform
import os
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
      
        opcion = input(":> ")
        if opcion == "testconaz":
            AzureDatabaseSelect("Usuarios")
        elif opcion == "sysinfo":
            sys.SystemInformation()
        elif opcion == "finance":
            finance.Menu()
        elif opcion.startswith("echo"):
            echo(opcion)
        elif opcion == "help" or opcion == "/?":
            print("Comandos disponibles:\n  testconaz, sysinfo, finance, echo, scan, cls/clear, exit/99")
        elif opcion == "exit" or opcion == "99":
            fin = True
            exit()
        elif opcion == "scan":
            print("Llamada a scan aquí")
        elif input == "":
            print("No se ha encontrado ninguna orden")
        elif opcion == "cls" or opcion=="clear":
            if platform.system() == "Windows":
                os.system("cls")
            else:
                os.system("clear")
        else:
            print("Comando no reconocido. Ejecute help o /? para ver los comandos disponibles")

def Menu():
    print("Para ver una lista de los comandos disponibles utilice 'help' o '/?'")

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
