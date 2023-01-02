from classes.NPC import NPC
from classes.Enemy import Enemy
from classes.Protagonist import Protagonist
from ORM.Tables import ProtagonistInventoryTable, NPCInventoryTable, EnemyTable

from loading.load_data import load_data
from loading.load_map import load_map

load_map()
load_data()
def test_protagonist():
    protagonist = Protagonist('Герой', "123")
    assert protagonist.name == 'Герой'
    assert protagonist.hp == 10
    assert protagonist.inventory.get('Камень') == 1


def test_protagonist_interactions():
    protagonist = Protagonist('Герой', "123")
    enemy = Enemy(1)
    protagonist.attack(enemy)
    assert True
    if enemy.alive:
        assert protagonist.hp == 9
    else:
        assert protagonist.hp == 10

    npc = NPC(1)
    protagonist.talk_to(npc)
    print(protagonist.id)
    assert True
    protagonist.give(npc, 'Камень')
    assert protagonist.inventory.get('Камень') is None
    assert protagonist.session.query(ProtagonistInventoryTable).filter(ProtagonistInventoryTable.character_id == protagonist.id).first() is None
    assert npc.inventory.get('Камень') == 2
    assert npc.session.query(NPCInventoryTable).filter(NPCInventoryTable.character_id == npc.id).first().count == 2