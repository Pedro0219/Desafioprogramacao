CarEspec = ("!","(",")","@","$","%","^","-","+","*","#", "&")
LetraMaiusculo = 1
LetraMinusculo = 1
Digito = 1
TemCarEspec = 1

senha = input("Digite sua senha:")
characters = list(senha)

for c in characters:
    if c.isalpha() == True and c.isupper() == True:
        LetraMaiusculo = 0
    elif c.isalpha() == True and c.islower() == True:
        LetraMinusculo = 0
    elif c.isdigit() == True:
        Digito = 0
    elif any(item in senha for item in CarEspec):
        TemCarEspec = 0

Faltando = [Digito,TemCarEspec,LetraMinusculo,LetraMaiusculo]

if len(senha) < 6:
    print(6 - len(senha))
else:
    print(sum(Faltando))



