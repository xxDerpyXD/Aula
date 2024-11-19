nome = (input("qual seria seu nome?"))
nota1 = int(input("qual foi sua nota no 1 bimestre:"))
nota2 = int(input("qual foi sua nota no 2 bimestre:"))
nota3 = int(input("qual foi sua nota no 3 bimestre:"))
nota4 = int(input("qual foi sua nota no 4 bimestre:"))
total = (nota1+nota2+nota3+nota4) / 4 

print (f"Olá, {nome}! Sua média é: {total} pontos")