from classes.Protagonist import Protagonist
from loading.load_map import load_map
from loading.load_data import load_data
from classes.Direction import Direction

load_map()
load_data()


def test_locations():
    pass
    # protagonist = Protagonist('Lek', '1')
    #
    # home = Direction(1)
    # wood = Direction(2)
    # edge = Direction(3)
    #
    # assert protagonist.locations.id == 1
    # assert protagonist.locations.name == 'Дом'
    # assert protagonist.locations.description == 'Это дом'
    # protagonist.go(wood)
    # assert protagonist.locations.id == 2
    # assert protagonist.locations.name == 'Лес'
    # assert protagonist.locations.description == 'Это лес'
    #
    # protagonist.go(edge)
    # """Пытаемся идти на опушку, но туда попасть не можем. Значит остаемся на месте"""
    #
    # assert protagonist.locations.id == 2
    # assert protagonist.locations.name == 'Лес'
    # assert protagonist.locations.description == 'Это лес'
    #
    # protagonist.go(home)
    # """Идем домой"""
    # assert protagonist.locations.id == 1
    # assert protagonist.locations.name == 'Дом'
    # assert protagonist.locations.description == 'Это дом'
