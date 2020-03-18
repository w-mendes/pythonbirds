"""
Devemos criar uma classe 'carro' que vai possuir dois atributos compostos por outras duas classes:
1) Motor
2) Direção

O Motor terá a responsabilidade de controlar a velocidade. Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Método acelerar, que deverá incrementar a velocidade de uma unidade
3) Método frear que deverá decrementar a velocidade em duas unidades

A direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes atributos:
1) Valor de direção com valores possíveis: Norte, Sul, Leste e Oeste.
2) Método girar _a_direita
3) Método girar_a_esquerda

       N
    O     L
       S

       Exemplo:
       # Testando Motor
       >>> motor = Motor()
       >>> motor.velocidade
       0
       >>> motor.acelerar()
       >>> motor.velocidade
       1
       >>> motor.acelerar()
       >>> motor.velocidade
       2
       >>> motor.acelerar()
       >>> motor.velocidade
       3
       >>> motor.frear()
       >>> motor.velocidade
       1
       >>> motor.frear()
       >>> motor.velocidade
       0
       >>> # Testando Direção
       >>> direcao = Direcao()
       >>> direcao.valor
       'Norte'
       >>> direcao.girar_a_direita()
       >>> direcao.valor
       'Leste'
       >>> direcao.girar_a_direita()
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
       >>> carro = Carro(direcao, motor)
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
       >>> carro.calcular_direção()
       >>> 'Norte'
       >>> carro.girar_a_direita()
       >>> carro.calcular_direção()
       >>> 'Leste'
       >>> carro.girar_a_esquerda()
       >>> carro.calcular_direção()
       >>> 'Norte'
       >>> carro.girar_a_esquerda()
       >>> carro.calcular_direção()
       >>> 'Oeste'
"""
NORTE='Norte'
SUL = 'Sul'
LESTE = "Leste"
OESTE = 'Oeste'

class Direcao:
    rotacao_a_direita_dct = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    rotação_a_esquerda_dct = {NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL}

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]
        #if self.valor == NORTE:
        #    self.valor = LESTE
        #elif self.valor == LESTE:
        #    self.valor = SUL
        #elif self.valor == SUL:
        #    self.valor = OESTE
        #elif self.valor == OESTE:
        #    self.valor = NORTE
    def girar_a_esquerda(self):
        self.valor = self.rotação_a_esquerda_dct[self.valor]

class Motor:                                        # Classe Motor
    def __init__(self):
        self.velocidade = 0                         # Atributo de velocidade da Classe Motor

    def acelerar(self):                             # Método acelerar da Classe Motor
        self.velocidade += 1

    def frear(self):                                # Método frear da Classe Motor
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)

