#Cores
RED  = "\033[1;31m"
RESET = "\033[0;0m" 

listaNumero = []

#Função para dar espaçamento
def linhas():
    print("-"*35)

for x in range(2):
    numero=int(input("Informe um número " +RED+ "INTEIRO"+RESET+":")) 
    listaNumero.append(numero)
linhas()

def verificaNumero(lista,x):
    copy = list(lista)
    for i in range(len(lista)):
        if x<0:
            lista[i+x] = copy[i]
        else:
            lista[i] = copy[i-x]
 
verificaNumero(listaNumero, -1)
print (listaNumero)
              




