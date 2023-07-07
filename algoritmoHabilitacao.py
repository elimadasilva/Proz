# Desenvolva um código que utilize as seguintes características de um veículo:
#- Quantidade de rodas;
#- Peso bruto em quilogramas;
#- Quantidade de pessoas no veículo.

# Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir das condições:
# A: Veículos com duas ou três rodas;
# B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
# C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
# D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas; E: Veículos com quatro rodas ou mais e com mais de 6000 kg.

# Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e compartilhe o link desse projeto no campo ao lado para que outros desenvolvedores possam analisá-lo.

#from pickleshare import print_function
# Variáveis

quantidadeRodas = float(input("Qual a quantidade de rodas do veículo: "))
pesoBrutoKg = float(input(" Qual  o peso do veículo em Kg: "))
quantidadePessoaVeiculo = float(input("Qual o valor máximo de pessoas que o veículo acomoda: "))

#inicio

if (quantidadeRodas == 2) or (quantidadeRodas==3):
  print("Categoria de habilitação para o veículo informado: A")

elif (quantidadeRodas == 4) and (quantidadePessoaVeiculo <= 8) and (pesoBrutoKg <= 3500):
  print("Categoria de habilitação para o veículo informado: B")

elif (quantidadeRodas >=4) and (pesoBrutoKg > 3500.00 and pesoBrutoKg <= 6000.00):
  print("Categoria de habilitação para o veículo informado: C")

elif (quantidadeRodas >=4) and (quantidadePessoaVeiculo > 8):
  print("Categoria de habilitação para o veículo informado: D")

elif (quantidadeRodas >= 4) and (pesoBrutoKg > 6000.00):
  print("Categoria de habilitação para o veículo informado: E")

else:
  print("Dados incorretos!")
#fim