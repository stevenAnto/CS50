def funcionDecoradora(funcionParametro):
    def funcionInterior():
        #Acciones adicionales que decoran
        print("Vamos a realizar un calculo")
        funcionParametro()
        #Acciones adicionales que decoran
        print("Hemos terminado el calculo")
    return funcionInterior

@funcionDecoradora
def suma():
    print(15+20)

def resta():
    print(30-10)

suma()



