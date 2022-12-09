from math import factorial as fact

def exp(a,b,n): #de
    return sum( [ fact(n)/(fact(k)*fact(n-k))*a**(n-k)*b**n for k in range(n+1)] )



def expand(entrada):
    a = int(entrada[1])
    x = entrada[2]
    b = int(entrada[4])
    n = int(entrada[7])

    if '-' in entrada: #si hay un menos, el coeficiente de b es negativo
        b = -int(entrada[3])
    
    else: #si no, lo dejamos
        pass

    return sum([ '{0}{1}^{2}'.format(fact(n)/(fact(k)*fact(n-k))*a**(n-k)*b**n) , x , n-k ] for k in range(n+1) )

if __name__ == '__main__':
    entrada = input('Introduce un polinomio de la forma (ax+b)^n: ') #cadena de texto
    print(expand(entrada))
