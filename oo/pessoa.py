class Pessoa:
    def __init__(self, *filhos, nome=None, idade=44): # Atributos de Instância, nome, idade e filhos
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    Brian = Pessoa(nome='Brian')
    Bernardo = Pessoa(nome='Bernador')
    Ewerton = Pessoa(Brian, Bernardo, nome='Ewerton')
    print(Pessoa.cumprimentar(Ewerton)) # faz o mesmo da linha 10
    print(id(Ewerton))
    print(Ewerton.cumprimentar()) # faz o mesmo da linha 8
    print(Ewerton.nome)
    print(Ewerton.idade)
    for filho in Ewerton.filhos:
        print(filho.nome)
    Ewerton.sobrenome = 'Mendes' # Adicionando atributo 'sobrenome'
    del Ewerton.filhos # Removendo um atributo
    print(Ewerton.sobrenome)
    print(Ewerton.__dict__)
    print(Brian.__dict__)
    print(Bernardo.__dict__)


