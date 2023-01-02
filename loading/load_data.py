import sqlite3
from sqlalchemy.orm import sessionmaker
from ORM.Tables import *
import json
def load_data():
    """Инициализация таблиц
    Создание объектов в бд"""
    connection = sqlite3.connect('data/game.db')
    sql = create_engine('sqlite:///data/game.db')
    session = sessionmaker(bind=sql)()

    NPCTable.metadata.create_all(sql)

    try:
        # Создание персонажа
        session.add(ProtagonistTable(id=1, name='Герой', telegram_id='123', hp=10, location=1, level=1, xp=0))
        session.commit()
        print('Персонаж создан')
    except Exception as e:
        session.rollback()
        print(e)

    # try:
        # npc = NPCTable(id=1, name='Bob', location=1)
        # for i in NPCTable:
        #     print
    with open('data/npc.json', 'r', encoding='utf-8') as file:
        npcs = json.load(file)['members']

        for npc in npcs:
            try:
                session.add(NPCTable(id=npc['id'], name=npc['name'], location=npc['location'], npc_type=npc['npc_type']))
                session.commit()
            except Exception as e:
                session.rollback()
                print(e)
            # print(npc)



    # except Exception as e:
    #     session.rollback()
    #     print(e)
        
    #     session.add(npc)
    #     session.commit()
    # except Exception as e:
    #     session.rollback()
        # print(e)

    try:
        npc_phrases = ['Hi', 'Hello','How are you', 
        'You are awesome', 'Will you be my friend?', 'Youre evil?', 'No need to kill them','Are you good?', 'Lets be friends', 'Do not want to talk', 'Get out of here',
        'You are not loved', 'Hi', 'Youre evil? ', 'Please do not kill me', 'Get on the path of goodness', 'Youre evil?', 'Why do you do evil ', 'Please do not kill me ', 'You are not loved ', 'Do not want to talk ', 'Why do you do evil', 'Do not want to talk', 'cool sword', 'Lets not fight ', 'cool sword ', 'Lets not fight', 'Hi', 'Get on the path of goodness', 'Please do not kill me ', 'Che cavo', 'Please do not kill me']
        for j in range(1, 26):
            for i in range(1, 26):
                npc_phrase = NPCPhraseTable(character_id=j, phrase=npc_phrases[i])
                session.add(npc_phrase)
                session.commit()

        npc_phrase = NPCPhraseTable(character_id=26, phrase='Yes I am the door')
        session.add(npc_phrase)
        session.commit()

        npc_phrase = NPCPhraseTable(character_id=26, phrase='You wont go further')
        session.add(npc_phrase)
        session.commit()

        npc_phrase = NPCPhraseTable(character_id=26, phrase='I wont let you')
        session.add(npc_phrase)
        session.commit()

        npc_phrase = NPCPhraseTable(character_id=26, phrase='Get out from here')
        session.add(npc_phrase)
        session.commit()
            
        # npc_phrase = NPCPhraseTable(id=2, character_id=1, phrase='How are you?')
        # session.add(npc_phrase)
        # session.commit()
    except Exception as e:
        session.rollback()
        # print(e)

    with open('data/enemies.json', 'r', encoding='utf-8') as file:
        enemies = json.load(file)['members']
    for enemy in enemies:
        try:
            session.add(EnemyTable(id=enemy['id'], name=enemy['name'], location=enemy['location'], level=enemy['level']))
            session.commit()
        except Exception as e:
            session.rollback()
            print(e)


    try:

        enemy_phrases = ['DIE', 'Even if you hit a person by accident, it still hurts','What am I doing? I kill the monster', 
        'How about dying?', 'You are too weak', 'I will crush you', 'Strength is with me','again and in the eye', 'tooth for tooth', 'You are a piece of shit', 'Come on grandma bitch',
        'НЫЫЫЫЫЫАААААААААА', 'I will destroy you', 'VZZZZZZZ', 'KIIIIYYYYYY', 'НЫЫЫЫЫЫАААААААААА', 'I will destroy you', 'AXAXAXAX', 'Вжух', 'You cant win', 'KIIIIYYYYYY', 'You are too weak', 'You are weaker than me', 'I am small but strong', 'You cant win', 'You are too weak', 'I am small but strong', 'You cant win ', 'You are weaker than me', 'You cant win ', 'You are too weak', 'You cant win']
        for j in range(1, 26):
            for i in range(1, 26):
                enemy_phrase = EnemyPhraseTable(character_id=j, phrase=enemy_phrases[i])
                session.add(enemy_phrase)
                session.commit()
            
        enemy_phrase = EnemyPhraseTable(character_id=26, phrase='Why did you kill those kids')
        session.add(enemy_phrase)
        session.commit()

        enemy_phrase = EnemyPhraseTable(character_id=26, phrase='This was my family')
        session.add(enemy_phrase)
        session.commit()

        enemy_phrase = EnemyPhraseTable(character_id=26, phrase='You are evil')
        session.add(enemy_phrase)
        session.commit()

        enemy_phrase = EnemyPhraseTable(character_id=26, phrase='I will stop you')
        session.add(enemy_phrase)
        session.commit()

        # number = 489
        # for j in range(24, 27):
        # for i in range(25, 27):
        #     enemy_phrase = EnemyPhraseTable(id=i, character_id=j, phrase=enemy_phrases[i])
        #     session.add(enemy_phrase)
        #     session.commit()
                # number +=1
        #         print(number)
        # print(number)

    except Exception as e:
        session.rollback()
        # print(e)

    try:
        inventory_item = InventoryItemsTable(id=1, name='Камень', description='Камень, который можно поднять', type='Вспомогательный предмет')
        session.add(inventory_item)
        session.commit()
    except Exception as e:
        session.rollback()
        # print(e)

    try:
        protagonist_item = ProtagonistInventoryTable(id=1, item_id=1, character_id=1, count=1)
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

    session.close()


