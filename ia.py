# -*- coding: utf-8 -*-
from multiprocessing.pool import ThreadPool
import time
from itertools import permutations
from random import randint
from palavra import Palavra

dicionario = []
dicionario_ordenado = []
tabuleiro = []
pacote = []
turno_atual = 0
jogador = []

# Troca elementos da mão da IA aleatoriamente
def trocar_mao_ia():
    global jogador
    troca = ""
    for i in jogador.getMao():
        if (randint(0, 1) == 0) or (i == '#'):
            troca += i
    return troca

def permutacao(necessaria):
    global dicionario_ordenado, jogador
    validas = []
    if (necessaria != '*'):
        jogador.getMao().append(necessaria)
    for i in range(len(jogador.getMao())):
        if (i+1 >= 3) and (i+1 <= 8):
            for test_word in permutations(jogador.getMao(), i+1):
                aux = (''.join(test_word)) 
                if (aux in dicionario_ordenado) and (dicionario_ordenado[aux] not in validas) and ((necessaria in aux) or (necessaria == '*')):
                    validas.append(dicionario_ordenado[aux])            
    if (necessaria != '*'):
        jogador.getMao().remove(necessaria)
    return validas

def procura_tabuleiro():
    global tabuleiro, pacote, jogador
    start_time = time.time() # Temporizador para marcar o tempo maximo da jogada da IA
    usadas = []
    while (True):
        if (time.time() - start_time > 10): # Timeout
            return False
        i, j = tabuleiro.getPreenchido()[0]
        necessaria = tabuleiro.getElemento(i, j)[1]
        resultados = permutacao(necessaria)
        if (len(resultados) != 0): # Encontrou algum resultado
            resultados.reverse() # Inverte os resultados para tentar encontrar primeiro as palavras maiores
            indexes = []
            if (necessaria == '*'):
                for count in range(len(resultados)):
                    indexes.append(0)
            else:
                indexes = encontra_fixador(resultados, tabuleiro.getElemento(i, j)[1], i, j)
            resultado_final = encaixa_palavra(resultados, indexes, i, j)
            if resultado_final != False:
                return resultado_final

# Fixador é a letra que ja está no tabuleiro
def encontra_fixador(resultados, fixador, i, j): 
    indexes = []
    for letras in resultados:
        for count in range(len(letras)):
            if letras[count] == fixador:
                indexes.append(count)
                break
    return indexes

def encaixa_palavra(resultados, indexes, i, j):
    global jogador, tabuleiro, dicionario, turno_atual
    for count in range(len(resultados)):
        # Horizontal
        palavra = Palavra(resultados[count], (i, j - indexes[count]), jogador, 'H', tabuleiro, dicionario, '')
        boolean = palavra.checaPalavra(turno_atual)
        if (boolean == True):
            return (resultados[count], (i, j - indexes[count]), 'H', '')
        # Vertical
        palavra = Palavra(resultados[count], (i - indexes[count], j), jogador, 'V', tabuleiro, dicionario, '')
        boolean = palavra.checaPalavra(turno_atual)
        if (boolean == True):
            return (resultados[count], (i - indexes[count], j), 'V', '')
    return False

def jogada_ia(xjogador, xtabuleiro, xpacote, xturno_atual, xdicionario, xdicionario_ordenado):
    global jogador, tabuleiro, pacote, turno_atual, dicionario, dicionario_ordenado
    jogador = xjogador
    tabuleiro = xtabuleiro
    pacote = xpacote
    turno_atual = xturno_atual
    dicionario = xdicionario
    dicionario_ordenado = xdicionario_ordenado

    devolver = False
    if ('#' in jogador.getMao()):
        jogador.getMao().remove('#')
        devolver = True

    resultado = procura_tabuleiro()
    if resultado == False: # Se não conseguiu achar nenhuma palavra valida
        if devolver == True:
            jogador.getMao().append('#')
        if (pacote.tamanho() != 0): # Troca Mão
            return (2, '', '', '', '')
        else: # Não é possivel trocar mao, entao passa o turno
            return (3, '', '', '', '')
    else:
        if devolver == True:
            jogador.getMao().append('#')
        return (1, resultado[0], resultado[1], resultado[2], resultado[3])