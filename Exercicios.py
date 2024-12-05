#Desafio 1: Criar um script que imprima a frase "Olá, mundo Python" na console.
print("Olá, mundo Python!");

#Desafio 2: Para este desafio, quero que você declare duas variáveis: uma chamada 'nome', que deve guardar o seu primeiro nome como uma string, e outra chamada 'idade', que deve guardar a sua idade como um número inteiro. Depois disso, eu quero que você imprima na tela uma frase que diga 'Olá, meu nome é [nome] e eu tenho [idade] anos'. Lembre-se de substituir [nome] e [idade] pelos valores das variáveis que você declarou.
nome = "Mauros Milach Junior";
idade = "25";
#print("Olá, meu nome é " + nome + " e eu tenho " +idade+" anos.")
print("Olá, meu nome é", nome, "e eu tenho", idade, "anos.");

#Desafio 3: Neste desafio, declare duas variáveis: 'num1' que deve guardar o número inteiro 10 e 'num2' que deve guardar o número de ponto flutuante 3,5. Depois disso, realize e imprima na tela o resultado da divisão de 'num1' por 'num2'.
num1 = 10;
num2 = 3.5;
print("Resultado:", num1/num2); 

#Desafio 4: Neste desafio, você deve criar um script que pergunte o nome e a idade do usuário, usando a função input(). Depois disso, o script deve imprimir uma mensagem que diga "Olá, [NOME] você tem [IDADE] anos.".
nome = input("Qual seu nome: ");
idade = int(input("Qual sua idade: "));
#print("Olá, {}! Você tem {} anos.".format(nome, idade));
print(f"Olá, {nome}! Você tem {idade} anos.")