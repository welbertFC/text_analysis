from collections import Counter
from Txt import Txt

class Sum(Txt):

    def __str__(self):
        return self.format_sum()

    def sum_character(self):
        aparicoes = Counter(self.texto.lower())
        return sum(aparicoes.values())


    def sum_character_sem_espaco(self):
        aparicoes = Counter(self.texto.lower())
        del aparicoes [' ']
        return sum(aparicoes.values())

    def sum_palavras(self):
        aparicoes_palavras = self.texto.split()
        return len(aparicoes_palavras)

    def format_sum(self):
        return f'Total de caracteres: {self.sum_character()} \n'\
               f'Total de caracteres sem espaço: {self.sum_character_sem_espaco()}\n' \
               f'Total de palavras: {self.sum_palavras()}\n'




