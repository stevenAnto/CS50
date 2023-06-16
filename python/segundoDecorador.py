def funcion_decorador(functionPa):
    def funcionInterior(*args,**kwar):
        print("Vamos a realizar un calculao")
        functionPa(*args,**kwar)
        print("vamos a terminar")
    return funcionInterior


@funcion_decorador
def suma(num1,num2):
    print(num1+num2)

suma(5,4)

@funcion_decorador
def potencia(base,exponenete):
    print(pow(base,exponenete))

potencia(exponenete=3,base=5)
