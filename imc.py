#Trabalho de Python - Cálculo do IMC
#Aluno: Kaique Beserra Pina
#Gestão de TI 
#Uma mensagem de bem vindo a calculadora
print ("Bem vindo a calculadora de IMC")
#Entrada de dados - peso
peso = float(input("Digite seu peso em kg: "))
#Entrada de dados - altura
altura = float(input("Digite sua altura em metros: "))
#Cálculo do IMC
imc = peso / (altura * altura)
#Saída de dados
print("Seu IMC é:", imc)
#classificação do IMC
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("Classificação: Peso normal")
elif 25 <= imc < 29.9:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")
#agregando uma mensagem final
print("Obrigado por usar a calculadora de IMC!")
#Fim do programa
#adicionar um comentário para o git commit
#git commit -m “início do projeto de cálculo de massa corporal"
#fim    