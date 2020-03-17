class Pessoa:
    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p)) # faz o mesmo da linha 10
    print(id(p))
    print(p.cumprimentar()) # faz o mesmo da linha 8

