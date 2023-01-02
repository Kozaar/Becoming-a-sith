from controller.Controller import Controller
from ORM.Tables import *
from loading.load_data import load_data
from loading.load_map import load_map
from classes.NPC import NPC
from classes.Enemy import Enemy
from classes.Protagonist import Protagonist
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_map()
load_data()


controller = Controller('game.db')
engine = create_engine('sqlite:///data/game.db')
session = sessionmaker(bind=engine)()

def test_create_protagonist():
    protagonist = Protagonist('Lich', '512')
    assert protagonist.name == 'Lich'
    assert protagonist.hp == 10
    assert protagonist.location == 1
    assert protagonist.level == 1
    protagonist.level = 4
    protagonist.take_hit(4)
    assert protagonist.hp == 6
    protagonist.update_protagonist()

def test_update_protagonist():
    protagonist = Protagonist('Lich', '512')
    assert protagonist.level == 4
    protagonist.session.query(ProtagonistTable).filter(ProtagonistTable.telegram_id == '512').delete()
    protagonist.session.commit()

def test_create_npc():
    npc = NPC(1)
    assert npc.name == 'Stormtrooper'
    assert npc.location == 1
    assert npc.id == 1

def test_create_enemy():
    enemy = Enemy(1)
    assert enemy.name == 'Younling Kim'
    assert enemy.location == 2
    assert enemy.id == 1