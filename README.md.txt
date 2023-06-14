# Programa para inverter posições do arquivo de texto

Este programa lê um arquivo de texto e inverte as posições de determinadas partes das linhas do arquivo. O texto resultante é salvo em um novo arquivo.

## Pré-requisitos

- Python 3.x

## Como usar

1. Certifique-se de ter o Python 3.x instalado em seu sistema.
2. Faça o download do código-fonte para um diretório local.
3. No diretório onde o código-fonte está localizado, crie um arquivo de entrada chamado `input.txt` contendo o texto que deseja processar.
4. Abra um terminal ou prompt de comando e navegue até o diretório onde o código-fonte está localizado.
5. Execute o seguinte comando para iniciar o programa:

```prompt
python nome_do_arquivo.py


6. Siga as instruções exibidas no terminal.
7. O programa exibirá uma barra de progresso indicando o carregamento.
8. Após a conclusão, o texto invertido será salvo em um arquivo de saída chamado output.txt.
9. O programa exibirá uma mensagem informando que o texto foi invertido com sucesso.
10. Pressione Enter para sair do programa.

## Notas adicionais
O programa utiliza a biblioteca time para exibir uma barra de progresso enquanto processa o texto.
As partes específicas das linhas que são invertidas são definidas pela lógica no código-fonte.
Certifique-se de fornecer um arquivo de entrada válido com o nome input.txt no diretório do programa.

## Importânte
Para usar a versão já compilada, basta colocar o executável na mesma pasta que está o arquivo de texto input.txt, assim o programa funcionará.



EXEMPLO DE USO:
Houve demandas onde os clientes enviavam o arquivo CNAB com as posições do sequencial e da chave da nota fiscal invertido, o que gerava um trabalho manual, no exemplo temos um arquivo input.txt que está precisando da inversão do conteúdo que está nas colunas 395 à 400 invertendo com os que estão nas colunas 401 à 444.