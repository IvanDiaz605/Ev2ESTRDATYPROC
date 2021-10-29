#opcion del menú se inicia en 0 para prepararse en un bucle repetitivo
opcion=0

#lista principal de todas las ventas
ventas = []


#función que registrar articulos a la venta
def registrarArticulo():
    venta=[]
    descripcion = input("Escriba la descripción\n")
    precio = float(input("Precio unitario\n"))
    cantidad = int(input("Escriba la cantidad\n"))

    #Una vez que se pide la información Desc, Precio y Cantidad, se almacenan en una lista para posterior almacenarla en uan lista principal (lista anidadad)
    venta.append(descripcion)
    venta.append(precio)
    venta.append(cantidad)
    print("--Articulo agregado---\n")
    return venta

#función para escribirVentas en memoria, en un archivo CSV
def escribirVentas():
    with open('ventas.csv', 'w') as filehandle:
        for listitem in ventas:
            #Crea el archivo CSV con la información de la lista separados por PIPES |
            filehandle.write('%s|' % listitem)

#Empieza ejecución del programa mediante un menú de opciones, se repetirá hasta que digite la opción 4 que es SALIR
while(opcion!=4):
    opcion = int(input("Menu\n1.-Registrar venta\n2.-Consultar Venta\n3.-Reporte de ventas por fecha\n4.-Salir\n"))
    if opcion == 1:
       subopcion = 0
       #Declaramos una lista que almacenara una lista de articulos
       detalles_venta = []
       fecha = input("Escriba la fecha AAAA-MM-DD\n")
       folio = int(input("Escriba el folio\n"))
       subdetalle = []
       #Almacenamos fecha y folio de la venta
       subdetalle.append(fecha)
       subdetalle.append(folio)
       detalles_venta.append(subdetalle)
       total=0
       #se crea un submenú para pedir al usuario si continua agregando articulos a la venta
       while(subopcion!=2):
         subopcion = int(input("1.-Agregar articulo\n2.-Cerrar esta venta\n"))
         if(subopcion==1):
            #Si ingresa 1, el programa invocará a la funciión registrarArticulo() para almacenar dicho articulo a la lista subdetalle
            items=[]
            items=registrarArticulo()
            total = total + (items[1]*items[2])

            detalles_venta.append(items)


         if(subopcion==2):
             #Cierra una venta y la termina agregando a la lista principal Ventas
             ventas.append(detalles_venta)
             print("IVA: ",str( (total*0.16)))
             print("Total a pagar con IVA ",str((total+(total*0.16))))
             print("-----Venta regitrada-----\n")

    if opcion ==2:
        #Consulta venta con el folio
        folio = int(input("Escribe el folio de la venta\n"))

        j=0
        while(j<len(ventas)):
            h = 0
            #Preguntará por cada venta ingresada cual es la que coincide con el folio
            if ventas[j][h][1]==folio:
                #Si la encuentra, recorerrá la lista anidada y sacará la inforamción de los articulos
                print("FOLIO ",str(ventas[j][h][1])," FECHA: ",str(ventas[j][h][0]))
                total=0
                while(h<len(ventas[j])-1):
                    print("Nombre : ",str((ventas[j][h+1][0]))," , Precio U: ",str((ventas[j][h+1][1]))," Cantidad : ",str((ventas[j][h+1][2])))
                    total=total+ventas[j][h + 1][1]*ventas[j][h+1][2]
                    h=h+1
                print("IVA: ", str((total * 0.16)))
                print("Total cobrado con IVA ", str((total + (total * 0.16))))
            j=j+1
    if opcion ==3:

        fecha = input("Fecha de las ventas\n")

        j=0
        while(j<len(ventas)):
            h = 0
            #Al igual que la opción 2 buscará en ciclos anidados la información, pero está pedirá por fecha
            print("::::::::::VENTA:::::::::::")
            if ventas[j][h][0]==fecha:
                print("FOLIO ",str(ventas[j][h][1])," FECHA: ",str(ventas[j][h][0]))
                #Ingresa al detalle a la lista anidada en su interior de ventas
                total=0
                while(h<len(ventas[j])-1):
                    print("Nombre : ",str((ventas[j][h+1][0]))," , Precio U: ",str((ventas[j][h+1][1]))," Cantidad : ",str((ventas[j][h+1][2])))
                    total = total+ventas[j][h+1][1] * ventas[j][h +1][2]
                    h=h+1
                print("IVA: ", str((total * 0.16)))
                print("Total cobrado con IVA ", str((total + (total * 0.16))))
            j=j+1

    if opcion == 4:
        #Una vez que finalizamos el programa, las listas serán almacedas en un archivo CSV
        escribirVentas()
        print("Ventas almacenadas en memoria")
        #Finaliza
        print("Hasta luego")
