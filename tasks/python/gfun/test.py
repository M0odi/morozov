from FunRandomName import *

def test():
    gfun = FunRandomName()
    
    gfun.reset_adjectives()
    gfun.reset_nouns()
    assert gfun.get_random_name() == "Тайный посетитель"

    gfun.add_adjective("Беспокойный")
    gfun.add_noun("транзистор")
    assert gfun.get_random_name() == "Беспокойный транзистор"

    gfun.reset_adjectives()
    gfun.reset_nouns()
    gfun.add_adjective("Мощный")
    gfun.add_noun("трактор")
    assert gfun.get_random_name() == "Мощный трактор"

test()