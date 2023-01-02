from ORM.Tables import *
from ORM.ORM import ORM
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ORM.Tables import Locations


class Direction(ORM):
    def __init__(self, id) -> None:
        super().__init__('game.db')
        self.link = []
        """Ссылки на локации"""

        self.id = id
        self.current_location = self.session.query(
            Locations).filter(Locations.id == self.id).first()
        """id локации"""
        self.name = self.current_location.name
        """Имя локации"""
        self.description = self.current_location.description
        """Описание локации"""

    def check(self):
        # print(f'Я иду в')
        self.link = []
        n = self.session.query(Locations).all()
        for i in n:
            if int(self.id) == i.id:
                self.name = i.name
                self.description = i.description
                self.link.append(i.linkUp)
                self.link.append(i.linkDown)
                self.link.append(i.linkLeft)
                self.link.append(i.linkRight)
                break
    def get_description(self):
        return self.current_location.description

