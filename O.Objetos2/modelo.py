class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome


    @nome.setter
    def nome(self, nome):
        self._nome = nome.title

    def __str__(self):
       return f'Nome: {self._nome} - {self.ano}, Likes: {self._likes}.'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min, Likes: {self._likes}.'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
       return f'{self._nome} - {self.ano} - {self.temporadas} Temporadas, Likes: {self._likes}.'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)




vingadores = Filme ("vingadores - guerra infinita", 2018, 160)
atlanta = Serie ("atlanta", 2018, 2)
tmep = Filme ('todo mundo em panico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, tmep, demolidor]
playlist_FDS = Playlist('FDS', filmes_e_series)

print(f'Tamanho da playlist:{len(playlist_FDS)}')




for programa in playlist_FDS:
    print(programa)



