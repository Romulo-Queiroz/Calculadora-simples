num1 = 0
num2 = 0
resultado = 0
operacao = ''

nome_do_usuario=input("Digite seu nome:")
print()
print(f"Bem vindo:{nome_do_usuario}")
print()


while True:

       num1=int(input("Digite o primeiro número:\n"))
       operacao=input("Digite a operacao:\n")
       num2=int(input("Digite o segundo número 2:\n"))

       if operacao == '+':
              resultado = num1+num2
       elif operacao == '-':
              resultado = num1-num2
       elif operacao == '/':
              resultado= num1/num2
       elif operacao == '*':
              resultado= num1*num2
       else:
             resultado = 'Operação Inválida'

       print (str(num1)+' '+str(operacao)+' '+str(num2)+' = '+str(resultado))
