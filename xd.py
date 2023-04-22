while True:
    print(" Bienvenido al restaurante medranuel")
    
    print("MENU DE OPCIONES:")
    
    print("1.Pollo a la brasa $4.00")
    
    print("2.Mostrito $5.00")
    
    print("3.Lomo saltado $6.00")
    
    print("4.chaufita $2.00")
    
    respuesta=input("Elige una opcion:").upper()
    
    if    respuesta=="1":
        print("Pollo a la brasa")
    elif  respuesta=="2":
        print("Mostrito")
    elif  respuesta=="3":
        print("Lomo saltado")
    elif  respuesta=="4":
        print("chaufita")

    else:
        print("error: elegiste una opcion no valida")
print("Gracias por su preferencia")
    
