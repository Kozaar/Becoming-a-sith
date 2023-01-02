import sqlite3
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ORM.Tables import Locations

def load_map():
    """Загружает карту из файла"""
    connection = sqlite3.connect('data/game.db')
    sql = create_engine('sqlite:///data/game.db')
    session = sessionmaker(bind=sql)()

    Locations.metadata.create_all(sql)

    with open('data/map.json', 'r', encoding='utf-8') as file:
        locations = json.load(file)['members']
    try:
        for location in locations:
            session.add(Locations(id=location['id'], name=location['name'], description=location['description'],
                                  linkUp=location['linkUp'], linkDown=location['linkDown'], linkLeft=location['linkLeft'],
                                  linkRight=location['linkRight']))
            session.commit()
    except Exception as e:
        session.rollback()
        print(e)

    # print('Карта загружена')
    # print('Количество локаций: ', len(locations))
    # current_location = session.query(Locations).filter(Locations.id == 1).first()
    # print('Текущая локация: ', current_location.name)
    # print('Описание: ', current_location.description)
    # print('Куда я могу пойти:')
    # up_location = session.query(Locations).filter(Locations.id == current_location.linkUp).first()
    # if up_location: print('Вверх: ', up_location.name)
    # down_location = session.query(Locations).filter(Locations.id == current_location.linkDown).first()
    # if down_location: print('Вниз: ', down_location.name)
    # left_location = session.query(Locations).filter(Locations.id == current_location.linkLeft).first()
    # if left_location: print('Влево: ', left_location.name)
    # right_location = session.query(Locations).filter(Locations.id == current_location.linkRight).first()
    # if right_location: print('Вправо: ', right_location.name)
    # print('-----------------------------')
    # print('Я иду вверх')
    # current_location = session.query(Locations).filter(Locations.id == current_location.linkUp).first()
    # print('Текущая локация: ', current_location.name)
    # print('Описание: ', current_location.description)
    # print('Куда я могу пойти:')
    # up_location = session.query(Locations).filter(Locations.id == current_location.linkUp).first()
    # if up_location: print('Вверх: ', up_location.name)
    # down_location = session.query(Locations).filter(Locations.id == current_location.linkDown).first()
    # if down_location: print('Вниз: ', down_location.name)
    # left_location = session.query(Locations).filter(Locations.id == current_location.linkLeft).first()
    # if left_location: print('Влево: ', left_location.name)
    # right_location = session.query(Locations).filter(Locations.id == current_location.linkRight).first()
    # if right_location: print('Вправо: ', right_location.name)
    # print('-----------------------------')
    # print('Я иду обратно вниз')
    # current_location = session.query(Locations).filter(Locations.id == current_location.linkDown).first()
    # print('Текущая локация: ', current_location.name)
    # print('Описание: ', current_location.description)
    # print('Я иду вправо')
    # current_location = session.query(Locations).filter(Locations.id == current_location.linkRight).first()
    # print('Текущая локация: ', current_location.name)
    # print('Описание: ', current_location.description)
    # print('Куда я могу пойти:')
    # up_location = session.query(Locations).filter(Locations.id == current_location.linkUp).first()
    # if up_location: print('Вверх: ', up_location.name)
    # down_location = session.query(Locations).filter(Locations.id == current_location.linkDown).first()
    # if down_location: print('Вниз: ', down_location.name)
    # left_location = session.query(Locations).filter(Locations.id == current_location.linkLeft).first()
    # if left_location: print('Влево: ', left_location.name)
    # right_location = session.query(Locations).filter(Locations.id == current_location.linkRight).first()
    # if right_location: print('Вправо: ', right_location.name)

    session.close()