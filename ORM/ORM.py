import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ORM.Tables import InventoryItemsTable


class ORM:
    """Класс, который позволяет работать с базой данных через ORM"""
    def __init__(self, db_name: str):
        """Создается подключение к базе данных
        :param db_name: имя базы данных (например, 'npc.db')"""
        self.connection = sqlite3.connect(f'data/{db_name}')
        self.sql = create_engine(f'sqlite:///data/{db_name}')
        self.session = sessionmaker(bind=self.sql)()

    def load_stats(self, ob, id: int):
        """Загружает данные из базы данных в объект
        :param ob: класс, который соответствует таблице в базе данных
        :param id: id объекта в базе данных
        :return: объект, который соответствует строке в базе данных"""
        print('id:', id)
        print(self.session.query(ob).filter_by(id=id))
        return self.session.query(ob).filter_by(id=id).first()

    def update_stats(self, ob, id: int, **kwargs):
        """Обновляет данные в базе данных (для протагониста)
        :param ob: класс, который соответствует таблице в базе данных
        :param id: id объекта в базе данных
        :param kwargs: аргументы, которые нужно обновить
        :return: None"""
        ob.id = id
        ob = self.session.query(ob).filter_by(id=id).first()
        for key, value in kwargs.items():
            setattr(ob, key, value)
        self.session.commit()

    def load_phrases(self, ob, id: int):
        """Загружает фразы из базы данных в объект"""
        phrases = self.session.query(ob).filter_by(character_id=id).all()
        result = []
        for phrase in phrases:
            result.append(phrase.phrase)
        return result

    def load_inventory(self, ob, id: int):
        """Загружает предметы из базы данных в объект"""
        items = self.session.query(ob).filter_by(character_id=id).all()
        inventory = {}
        if items:
            for item in items:
                item_info = self.session.query(InventoryItemsTable).filter_by(id=item.item_id).first()
                inventory.update({item_info.name: item.count})
        return inventory

    def get_protagonist_id(self, ob, telegram_id: str):
        """Возвращает id объекта по его telegram id"""
        protagonist = self.session.query(ob).filter_by(telegram_id=telegram_id).first()
        print('nash:', protagonist)
        if protagonist:
            return protagonist.id
        else:
            return self.session.query(ob).count() + 1

    def save(self, ob, **kwargs):
        """Сохраняет объект в базу данных"""
        self.session.add(ob(**kwargs))
        self.session.commit()