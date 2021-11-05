#calculadora simples: Testes em Python

num1=0
num2=0
num3=0
num4=0
resultado=0
operacao=''

while True:

       num1=int(input("Digite o primeiro numero:\n"))
       operacao=input("Digite a operacao:\n")
       num2=int(input("Digite o numero 2:\n"))

       if operacao== '+':
              resultado= num1+num2
       elif operacao =='-':
              resultado= num1-num2
       elif operacao =='/':
              resultado= num1/num2
       elif operacao =='*':
              resultado= num1*num2

       else:
             resultado ='Operação Inválida'

       print(str(num1)+' '+str(operacao)+' '+str(num2)+' = '+str(resultado))
       
