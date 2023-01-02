from classes.NPC import NPC
from classes.Enemy import Enemy
from classes.Protagonist import Protagonist
from ORM.Tables import ProtagonistInventoryTable, NPCInventoryTable, EnemyTable

from loading.load_data import load_data
from loading.load_map import load_map

def test_npc():
    npc = NPC(1)
    assert npc.id == 1
    assert npc.name == "Stormtrooper"
    assert npc.location == 1    
    
    npc = NPC(2)
    assert npc.id == 2
    assert npc.name == "Simple clone Adam"
    assert npc.location == 1   

    npc = NPC(3)
    assert npc.id == 3
    assert npc.name == "Simple clone Bob"
    assert npc.location == 2

    npc = NPC(4)
    assert npc.id == 4
    assert npc.name == "Simple clone Charlie"
    assert npc.location == 2

    npc = NPC(5)
    assert npc.id == 5
    assert npc.name == "Simple clone David"
    assert npc.location == 2

    npc = NPC(6)
    assert npc.id == 6
    assert npc.name == "Simple clone Eve"
    assert npc.location == 2

    npc = NPC(7)
    assert npc.id == 7
    assert npc.name == "Simple clone Frank"
    assert npc.location == 2


    npc = NPC(8)
    assert npc.id == 8
    assert npc.name == "Simple clone George"
    assert npc.location == 1

    npc = NPC(9)
    assert npc.id == 9
    assert npc.name == "Simple clone Henry"
    assert npc.location == 6

    npc = NPC(10)
    assert npc.id == 10
    assert npc.name == "Simple clone Ida"
    assert npc.location == 6

    npc = NPC(11)
    assert npc.id == 11
    assert npc.name == "Simple clone John"
    assert npc.location == 8

    npc = NPC(12)
    assert npc.id == 12
    assert npc.name == "Simple clone Kate"
    assert npc.location == 8

    npc = NPC(13)
    assert npc.id == 13
    assert npc.name == "Simple clone Larry"
    assert npc.location == 9

    npc = NPC(14)
    assert npc.id == 14
    assert npc.name == "Simple clone Mary"
    assert npc.location == 9


    npc = NPC(15)
    assert npc.id == 15
    assert npc.name == "Simple clone Nancy"
    assert npc.location == 11

    npc = NPC(16)
    assert npc.id == 16
    assert npc.name == "Simple clone Oscar"
    assert npc.location == 11

    npc = NPC(17)
    assert npc.id == 17
    assert npc.name == "Simple clone Peter"
    assert npc.location == 11

    npc = NPC(18)
    assert npc.id == 18
    assert npc.name == "Simple clone Quin"
    assert npc.location == 10

    npc = NPC(19)
    assert npc.id == 19
    assert npc.name == "Simple clone Robert"
    assert npc.location == 5

    npc = NPC(20)
    assert npc.id == 20
    assert npc.name == "Simple clone Susan"
    assert npc.location == 7

    npc = NPC(21)
    assert npc.id == 21
    assert npc.name == "Simple clone Tom"
    assert npc.location == 2

    npc = NPC(22)
    assert npc.id == 22
    assert npc.name == "Intendant Huskar"
    assert npc.location == 1

    npc = NPC(23)
    assert npc.id == 23
    assert npc.name == "Medic Hilka"
    assert npc.location == 1

    npc = NPC(24)
    assert npc.id == 24
    assert npc.name == "Captain Kain"
    assert npc.location == 1 

    npc2 = NPC(25)
    assert npc2.id == 25
    assert npc2.name == "Lost pilot X-10"
    assert npc2.location == 9

    npc2 = NPC(26)
    assert npc2.id == 26
    assert npc2.name == "Door to 5"
    assert npc2.location == 4

    # npc = NPC(26)
    # assert npc.id == 26
    # assert npc.name == "Door to 5"
    # assert npc.location == 4
