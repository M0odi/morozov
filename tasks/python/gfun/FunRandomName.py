# GoogleDocs имеет забавную фичу: когда пользователь просматривает
# документ по ссылке без авторизации, он помечается забавным именем,
# например «Волосатый жук», «Ворчливая бобриха», «Сонный мухомор»
# и т. п. Попробуйте представить себя в роли разработчика Google.
# Реализуйте класс FunRandomName, содержащий 2 приватных
# атрибута (набор прилагательных и имен) и несколько методов
# (подумайте над тем сколько их может Вам понадобится) для генерации
# забавного имени и добавления новых имен, либо прилагательных
# соответственно. Если метод является вспомогательным для другого
# метода, не забудьте сделать его приватным (название начинается с __,
# например __get_size_atrr). Метод который возвращает забавное имя
# должен иметь например следующую сигнатуру: def get_name(self,
# *args, **kwargs)-> str: ... . Придумайте также простейшие тесты (юнит
# тесты). Подумайте где можно использовать функции map(), filter() или
# reduce() в данном задании. Проявите творчество и смекалку. Не
# забывайте, что пара «прилагательное имя» всегда создается случайно

import random
from functools import reduce

class FunRandomName:

    def __init__(self):
        self.__adjectives = ["Тотальный", "Беспокойный", "Злющий", 'Мохнатый']
        self.__nouns = ["кракен", "тарантул", "бегемот", 'овен']
    
    def get_random_name(self) -> str:
        
        if self.__adjectives.__len__() == 0 or self.__nouns.__len__() == 0:
            return "Тайный посетитель"
        
        adjective = random.choice(self.__adjectives)
        noun = random.choice(self.__nouns)
        return f"{adjective} {noun}"
    
    def add_adjective(self, adjective: str):
        self.__adjectives.append(adjective)
    
    def add_noun(self, noun: str):
        self.__nouns.append(noun)

    def reset_adjectives(self):
        self.__adjectives.clear()
    
    def reset_nouns(self):
        self.__nouns.clear()