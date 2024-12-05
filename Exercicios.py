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

#Desafio 5: Neste desafio, você crie um script que solicite ao usuário dois números. Em seguida, seu script deve imprimir a soma, a subtração, a multiplicação, a divisão (resultado decimal) e a exponenciação (primeiro número ao segundo número) desses dois números.
num1 = float(input("Digite um número: "));
num2 = float(input("Digite outro número: "));
print("Soma:", num1+num2);
print("Subtração:", num1-num2);
print("Multiplicação:", num1*num2);
print("Divisão:", num1/num2);
print("Exponenciação:", num1**num2);

#Desafio 6: Neste desafio, você deve criar uma lista chamada 'frutas' que contenha os seguintes itens: "Maçã", "Banana", "Manga" e "Uva". Depois disso, imprimir esta lista na tela.
frutas = ["maçã", "banana", "manga", "uva"];
print(frutas);

#Desafio 7: Para este desafio, use a lista 'frutas' do desafio anterior. Seu desafio é imprimir o primeiro e o último elemento da lista.
frutas = ["maçã", "banana", "manga", "uva"];
print(f"Primeiro elemento: {frutas[0]}");
print(f"Ultimo elemento: {frutas[-1]}");

#Desafio 8: Para este desafio, comece a lista 'frutas' do desafio anterior. Primeiro, seu desafio é alterar o segundo elemento da lista (índice 1)  de "banana" para "morango". Depois disso, adicione a fruta "abacaxi" ao final da lista. Por fim, imprima a lista modificada na tela.
frutas = ["maçã", "banana", "manga", "uva"];
frutas[1] = "morango";
frutas.append("abacaxi");
print(frutas);

#Desafio 9: Para este desafio, comece com a lista 'frutas' do desafio anterior. Primeiro remover a "manga" da lista usando o método remove(). Depois disso, remova o último item da lista usando o comando del(). Por fim, imprima a lista modificada na tela.
frutas = ["Maçã", "Morango", "Manga", "Uva", "Abacaxi"];
frutas.remove("Manga");
del frutas[-1];
print(frutas);

#Desafio 10: Para este desafio, comece a lista 'frutas' do desafio anterior. Use um "for loop" para percorrer a lista e imprima cada fruta precedida pelo texto "Eu gosto de";
frutas = ['Maçã', 'Morango', 'Uva'];
for fruta in frutas:
    print(f"Eu gosto de {fruta}");