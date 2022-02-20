ValorEscada = int(input("Digite o valor de n"))

for i in range(ValorEscada):
    if i == 0:
        print(" "*(ValorEscada-1) + "*")
    else:
        print(" "*(ValorEscada-(i+1)) + "*"*(i+1))

    
    