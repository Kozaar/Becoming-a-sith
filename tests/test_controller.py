from ORM.Tables import *
from loading.load_data import load_data
from loading.load_map import load_map
from controller.Controller import Controller

load_map()
load_data()
controller = Controller('game.db')


def test_get_location():
    location = controller.get_location(ProtagonistTable, id=1)
    assert location.id == 1
    assert location.name == 'Entrance'
    assert location.description == 'Entrance to the Jedi Temple'


def test_get_npc():
    npc = controller.get_npc(id=1)
    assert npc.id == 1
    assert npc.name == 'Stormtrooper'
    assert npc.location == 1


def test_get_enemy():
    enemy = controller.get_enemy(id=1)
    assert enemy.id == 1
    assert enemy.name == 'Younling Kim'
    assert enemy.level == 1
    assert enemy.location == 2


def test_get_inventory_item():
    item = controller.get_inventory_item(id=1)
    assert item.id == 1
    assert item.name == 'Камень'
    assert item.description == 'Камень, который можно поднять'
    assert item.type == 'Вспомогательный предмет'


def test_get_npc_phrases():
    phrases = controller.get_npc_phrases(id=1)
    assert len(phrases) == 125

def test_get_enemy_phrases():
    phrases = controller.get_enemy_phrases(id=1)
    assert len(phrases) == 125


def test_get_protagonist_inventory():
    item = controller.get_protagonist_inventory(id=1)
    assert item.id == 1
    assert item.item_id == 1
    assert item.character_id == 1
    assert item.count == 1

def test_get_npc_in_location():
    npc: list = controller.get_npc_in_location(location_id=1)
    assert len(npc) == 6
    assert npc[0].id == 1
    assert npc[0].name == 'Stormtrooper'
    assert npc[0].location == 1

def test_get_enemy_in_location():
    enemy: list = controller.get_enemy_in_location(location_id=2)
    assert len(enemy) == 2
    assert enemy[0].id == 1
    assert enemy[0].name == 'Younling Kim'
    assert enemy[0].level == 1
    assert enemy[0].location == 2

def test_multiple_controllers():
    controller1 = Controller('game.db')
    controller2 = Controller('game.db')
    controller3 = Controller('game.db')
    controller4 = Controller('game.db')
    controller5 = Controller('game.db')

    controller1.start_game('123')
    controller2.start_game('124')
    controller3.start_game('125')
    controller4.start_game('126')
    controller5.start_game('127')

    controller2.session.query(ProtagonistTable).filter(ProtagonistTable.telegram_id == '124').delete()
    controller2.session.commit()
    controller3.session.query(ProtagonistTable).filter(ProtagonistTable.telegram_id == '125').delete()
    controller3.session.commit()
    controller4.session.query(ProtagonistTable).filter(ProtagonistTable.telegram_id == '126').delete()
    controller4.session.commit()

    controller5.protagonist.name = 'new_name'

    controller5.protagonist.update_protagonist()
    assert controller5.protagonist.name == 'new_name'

def test_save_controller():
    controller5 = Controller('game.db')
    controller5.start_game('127')

    controller5.session.query(ProtagonistTable).filter(ProtagonistTable.telegram_id == '127').delete()
    controller5.session.commit()

def test_get_locations_to_go():
    controller10 = Controller('game.db')
    controller10.start_game('128')
    locations = controller10.get_locations_to_go()
    assert len(locations) == 1
    assert locations[0].id == 2
