# Scrabble_Game
Jogo de palavras cruzadas em Python. Player vs Player ou Player vs Computer

Instituto Federal de Educação, Ciência e Tecnologia de Minas Gerais, IFMG - Campus Formiga Ciência da Computação

Jogo Scrabble para a disciplina Projeto e Analise de Algoritmos.

Autores: Luiz Eduardo Pereira, Rafaela Martins Vieira.

Objetivo:
O objetivo deste trabalho era criar o classico jogo Scrabble de palavras cruzadas, disponibilizando a opção de jogar contra o computador.

Execução:
python3 run.py config.txt saida.csv

run.py executa 100 simulações consecutivas armazenando os resultados em um arquivo de extensão CSV. config.txt possui todos os parametros de entrada do programa, como tempo de simulação, número de funcionarios e distribuições de chegada de pacientes / tempo de atendimento.

Para analisar resultados entre duas amostras:

Rscript output-analysis-script.r Arquivos necessarios: amostra1.csv, amostra2.csv

Código cedido pelo Prof. Me. Diego Mello da Silva

Referencia para as distribuições utilizadas: Silva, L. P. “Análise de Cenários em um Sistema de Pronto Socorro Atendimento Utilizando Simulação Discreta”. https://bit.ly/2JelTs7
