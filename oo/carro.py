"""
Você deve criar uma classe carro que vai possuir
dosi atributos compostos por outras duas classes:

1) Motor
2) Direção

O mottor terá a responsabilidade de controlar a velocidade.
Ele oferecerá os seguintes atributos:
1) Atributo de dado velocidade;
2) Método a ecelerar, que deverá acrescentar a velocidade de uma unidade
3) Método frear que deverá decrementar a velocidade em duas unidades

A Direção terá a reponsabilidade de controlar a direção. ela oferecerá
os eguintes atributis:
1) valor de direção com valores de possíveis: Norte, Sul, Leste,Oeste.
2) Método girar_a_direita
3) Método girar_a_esquerda

  N
0   L
  s
    Exemplo:
    >>> #testando motor
    >>> motor = motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.acelerar()
    3
    >>> motor.frear()
    >>> motor.acelerar()
    1
    >>> motor.frear()
    >>> motor.acelerar()
    0
    >>> #testando a Direção
    >>> direcao = direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita(
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular direcao()
    >>> 'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_a_direcao()
    >>>'Leste'
    >>> carro.girar_a_esuqerda()
    >>> carro.calcular_a_direcao()
    >>> 'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_a_direcao()
    'Oeste'
"""

NORTE='Norte'
SUL='Sul'
LESTE='Leste'
OESTE='Oeste'

class Direcao:
    rotacao_a_direita_dct={
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
    }

    rotacao_a_esquerda_dct={
        NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL
    }

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_esquerda_dct[self.valor]



class Moto:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 1
        self.velocidade = max(0, self.velocidade)



