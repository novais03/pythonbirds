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
    >>> direcao.
"""