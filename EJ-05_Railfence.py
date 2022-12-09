
def rellenar_con_letra_o_con_X(matriz, col, fil, cadena):
    if col <= len(cadena): #si tenemos letras en la cadena
        matriz[fil][col] = cadena[col] #rellenamos con las letras
    else: #si se nos acaben rellenamos con Xs
        matriz[fil][col] = 'X'

def codificar(cadena, rieles):
    cadena = input('Introduce una cadena de texto: ')
    rieles = input('Introduce el número de rieles que deseas que haya: ')
    try: #nos aseguramos de que es un numero entero
        rieles = int(rieles)
    except:
        print('Debe ser un número entero')
        return #error, salimos de la funcion

    #creamos la matriz donde vamos a cifrar el codigo
    matriz = [ [' ' for c in range(19)] for f in range(rieles) ] # filas: nº rieles, columnas: 19

    #numero de casillas que tenemos que rellenar de Xs
    num_X = 19-len(cadena)

    #rellenamos la matriz
    contador=0 #numero de casillas que hemos rellenado
    for col in range(19): # recorremos las columnas
        for fil in range(rieles): #y las filas
            #mientras no hayamos rellenado todas las casillas
            while contador <= 19: 
                contador += 1 #actualizamos el contador

                
                
            
