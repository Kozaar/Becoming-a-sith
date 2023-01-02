import sqlite3
from sqlalchemy.orm import sessionmaker
from ORM.Tables import *

def init_tables():
    """Инициализация таблиц
    Создание объектов в бд"""
    connection = sqlite3.connect('data/game.db')
    sql = create_engine('sqlite:///data/game.db')
    session = sessionmaker(bind=sql)()

    # NPCPhraseTable.metadata.create_all(sql)
    NPCTable.metadata.create_all(sql)

    try:
        npc = NPCTable(id=1, name='Bob')
        session.add(npc)
        session.commit()
    except Exception as e:
        session.rollback()
        # print(e)

    try:
        npc_phrase = NPCPhraseTable(id=1, character_id=1, phrase='Hello')
        session.add(npc_phrase)
        session.commit()
        npc_phrase = NPCPhraseTable(id=2, character_id=1, phrase='How are you?')
        session.add(npc_phrase)
        session.commit()
    except Exception as e:
        session.rollback()
        # print(e)

    try:
        enemy = EnemyTable(id=1, name='Enemy', level=5)
        session.add(enemy)
        session.commit()
    except Exception as e:
        session.rollback()
        # print(e)

    try:
        enemy_phrase = EnemyPhraseTable(id=1, character_id=1, phrase='DIE')
        session.add(enemy_phrase)
        session.commit()
        enemy_phrase = EnemyPhraseTable(id=2, character_id=1, phrase='Yowai mo')
        session.add(enemy_phrase)
        session.commit()
    except Exception as e:
        session.rollback()
        # print(e)

    try:
        inventory_item = InventoryItemsTable(id=1, name='Sword', description='A sword')
        session.add(inventory_item)
        session.commit()
    except Exception as e:
        session.rollback()
        # print(e)

    try:
        protagonist_item = ProtagonistInventoryTable(id=1, item_id=1, character_id=0, count=1)
        session.add(protagonist_item)
        session.commit()
    except Exception as e:
        session.rollback()
        # print(e)

    try:
        npc_item = NPCInventoryTable(id=1, item_id=1, character_id=1, count=1)
        session.add(npc_item)
        session.commit()
    except Exception as e:
        session.rollback()
        # print(e)
    # 
    try:
        direction = DirectionTable(id=1, name='Лес', description = 'Это лес')
        session.add(direction)
        session.commit()
        print("Done")
    except Exception as e:
        session.rollback()
        print(e)


