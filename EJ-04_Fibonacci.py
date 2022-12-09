'''
EJERCICIO: calcular el n-ésimo número de la serie de Fibonacci
'''
def Fibo_list(k): #sucesión de Fibonacci hasta el número k
    a,b=0,1
    sucesion=[a] #creamos una lista con la sucesión, empezando por el 0
    
    while b<k:
        sucesion.append(b) #añadimos b a la sucesion
        a,b=b,a+b

    return sucesion


def fibonacci(n): 
    '''Funcion que dado un numero n, devuelve el n-ésimo número de la serie de Fibonacci'''
    k = 0
    while len(Fibo_list(k)) < n:
        k += 1
    return Fibo_list(k)[-1]

def ejercicio_4():
    n = input('Introduce un número de la serie d Fibonacci que deseas conocer: ')
    try:
        n = int(n)
    except:
        print('El número introducido no es válido.')
        return
    
    print( fibonacci(n) )


# ---------- PROGRAMA PRINCIPAL ----------
if __name__=='__main__':
    ejercicio_4()
