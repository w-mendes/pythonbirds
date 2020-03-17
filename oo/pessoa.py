class Pessoa:
    def __init__(self, nome=None, idade=35):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Brian')
    print(Pessoa.cumprimentar(p)) # faz o mesmo da linha 10
    print(id(p))
    print(p.cumprimentar()) # faz o mesmo da linha 8
    p.nome = 'Ewerton'
    print(p.nome)
    print(p.idade)

