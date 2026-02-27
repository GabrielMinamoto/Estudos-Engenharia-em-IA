#começando a Aula de Python
print(5)
#sempre usar aspas para escrever
print('Olá pessoal')
#-----------------------------
#só posso juntar texto com texto, ou número com número
print(6+9)
#-----------------------------
#variavel
produto1 = 5
print(produto1)
produto2 = 2000
produto3 = 1
print(produto1 + produto2 + produto3)
#-----------------------------
#nomes de variaveis
nomeProduto1 = "Macarrão"
nomeProduto2 = "Celular"
nomeProduto3 = "bala"
#-----------------------------
#nomes colados
print( nomeProduto1 + nomeProduto2 + nomeProduto3)
#-----------------------------
#separando os nomes
print( nomeProduto1 + " " + nomeProduto2 + " " +nomeProduto3)
#-----------------------------
#soma de variaveis
amigos = 5
aluguel = 1000
supermercado = 500
carro = 400
total = ( aluguel + supermercado + carro)
print(total)
#-----------------------------
#subtração de variaveis
aluguel = aluguel - 100
print(aluguel)
total = ( aluguel + supermercado + carro)
print(total)
#-----------------------------
#multiplicação de variaveis
amigos = 6
aluguel = 1000
supermercado = 500
carro = 400
print(carro * 2)
total_de_carros = carro * 2
print(total_de_carros)
total = aluguel + supermercado + total_de_carros
print(total)
#-----------------------------
#divisão de variaveis
total_por_pessoa = total / amigos
print(total_por_pessoa)
#-----------------------------
#REGRAS DE NOMENCLATURA
#1- Não pode começar com número
#2- Não pode conter espaços
#3- Não pode conter caracteres especiais
#4- Não pode ser o nome de um comando do Python
#-----------------------------
#TIPOS DE DADOS
#para descobrir tipo de dado -->
type(aluguel)
#tipos -->
#int - números inteiros
#float - números decimais
#str - texto
#bool - verdadeiro ou falso
#-----------------------------
#MANIPULAÇÃO DE STRINGS
# exemplo:
#inicial ="     Fabricio CARRaro da alura "
#final = "FABRICIO CARRARO DA ALURA"
texto ="     Fabricio CARRaro  da alura "
print(texto)
print(texto.lower())
print(texto.upper())
print(texto.strip())#remove os espaços em branco do início e do fim
print(texto.replace("  ", " "))#substitui os dois espaços por um espaço
#A variavel texto não é alterada, para alterar a variável texto, preciso atribuir o resultado da manipulação a ela
texto = texto.upper().strip().replace("  ", " ")
print(texto)
#-----------------------------
#ENTRADA DE DADOS - INPUT
nome = input("Digite seu nome: ")
print(nome)
idade = input("Digite seu idade: ")
print(idade)
#o input sempre retorna uma string, para converter para inteiro, uso a função int() 
idade = int(idade)
print("A pessoa se chama " + nome + " e tem " + str(idade) + " anos")#salva temporariamente a idade como string para concatenar com o texto
print(f"A pessoa se chama {nome} e tem {idade} anos")#Jeito mais facil e moderno