for (x in 0:num) {
  cat(x, "\n")
  
}
vet = c(4,5,6)

2+1/1

if(condição){
 ##Bloco de comandos a serem executados caso
 ## a condição seja verdadeira
  
}
val_1 = 2
val_2 = 5

if(val_1 < val_2){
  cat('O primeiro valor é menor que o segundo');
}

if(val_2 < val_1){
  cat('O segundo valor é menor que o primeiro');
} else{
  cat('o primeiro valor é menor que o segundo');
}

while(condição){
  ##Bloco de comandos a serem executados caso
  ##a condição seja  verdadeira
}
#exemplo de while
val_1 = 0
while (val_1 < 10) {
  cat('Essa mensagem será repetida 10 vezes')
  val_1 = val_1 + 1
}
for(variável in vetor_números){
 ## Bloco de comandos a serem executados
 ## caso a condição seja verdadeira.
}
for (val_1 in 1:10) {
 ## Bloco de comandos a serem executados dez vezes
}

notas = c(5, 6, 7, 2, 3, 9, 10, 8, 6, 9)##nessa linha o programador constrói o vetor de notas
n = lentgh(notas) ##nessa linha o
##programador obtém o tamanho do vetor de notas, ou seja, a quantidade de elementos dentro do vetor.
##Abaixo o programador implementa a estrutura for, de modo que para cada elemento i dentro da sequência
#que vai de 1 até n ele executará p bloco de comandos

for (i in 1:n) {
  soma = soma + notas[i]
  ## esse comando faz com que seja armazenado a adição dos elementos do vetor notas à variável soma.
}
media = soma/n ## Calcula-se a média nessa linha.
cat("A média é igual a ", media) ##Retorna para o usuário o valor da média calculada.
  