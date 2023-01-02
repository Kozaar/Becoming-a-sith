from classes.NPC import NPC
from classes.Enemy import Enemy
from classes.Protagonist import Protagonist
from ORM.Tables import ProtagonistInventoryTable, NPCInventoryTable, EnemyTable
from classes.Enemy import Enemy

def test_enemy():
    enemy_name = [' ','Kim', 'Katrin', 'Robert', 'Dane', 'Qian', 'Zhen', 'Chao', 'Bao', 'Li', 'Zhang', 'Wang',
    'Chen', 'Liu', 'Huang', 'Zhao', 'Wu', 'Liang', 'Yang', 'Zhou', 'Xie', 'Sun', 'Wang']
    enemy_level = [0,1,1,1,1,1,1,1,3,3,1, 4,1,1, 5,1,1,1,7,8,4,4,5]
    enemy_location = [0, 2, 2,3,5,5,5,5,4,7,7,8,8,8,9,9,9,9,10,11,11,11,11]
    # enemy = Enemy(1)
    # assert enemy.id == 1
    # assert enemy.name == "Younling Kim"
    # assert enemy.location == 2
    # assert enemy.level == 1    

    # enemy = Enemy(2)
    # assert enemy.id == 1
    # assert enemy.name == "Younling Katrin"
    # assert enemy.location == 2
    # assert enemy.level == 1    

    for i in range(1, 22):
        enemy = Enemy(i)
        assert enemy.id == i
        assert enemy.name == f'Younling {enemy_name[i]}'
        assert enemy.level == enemy_level[i]
        assert enemy.location == enemy_location[i]
    
    enemy = Enemy(26)
    assert enemy.id == 26
    assert enemy.name == "Jedi knight Keevan"
    assert enemy.location == 12
    assert enemy.level == 10   

    enemy = Enemy(24)
    assert enemy.id == 24
    assert enemy.name == "Younling Zora"
    assert enemy.location == 12
    assert enemy.level == 1

    enemy = Enemy(25)
    assert enemy.id == 25
    assert enemy.name == "Younling Tia"
    assert enemy.location == 12
    assert enemy.level == 1

    enemy = Enemy(23)
    assert enemy.id == 23
    assert enemy.name == "Younling Kira"
    assert enemy.location == 12
    assert enemy.level == 2