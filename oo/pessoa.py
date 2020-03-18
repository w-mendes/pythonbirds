class Pessoa:
    olhos = 2 # Atributo de classe

    def __init__(self, *filhos, nome=None, idade=44): # Atributos de Instância, nome, idade e filhos
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod # Método de classe "
    def metodo_estatico():
        return 42

    @classmethod # Método de classe
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

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
    Ewerton.olhos = 1
    del Ewerton.olhos
    print(Ewerton.__dict__) # Atributos de instancia ficam presentes no atributo especia '__dict__'
    print(Brian.__dict__)
    print(Bernardo.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(Ewerton.olhos)
    print(Brian.olhos)
    print(Bernardo.olhos)
    print(id(Pessoa.olhos), id(Ewerton.olhos), id(Brian.olhos), id(Bernardo.olhos))
    print(Pessoa.metodo_estatico(), Ewerton.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), Ewerton.nome_e_atributos_de_classe())





