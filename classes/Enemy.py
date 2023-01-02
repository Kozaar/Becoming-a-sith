from classes.NPC import NPC
from ORM.Tables import EnemyTable, EnemyPhraseTable


class Enemy(NPC):
    def __init__(self, id: int):
        super().__init__(id)
        self.id = id
        self.name = ''
        """Имя персонажа"""
        self.level = 0
        """Уровень персонажа"""
        self.phrases = self.load_phrases(EnemyPhraseTable, self.id)
        """Список фраз, которые говорит NPC"""

        self.alive = True

        self.load()

    def load(self):
        """Загружает данные из базы данных в объект"""
        enemy = self.load_stats(EnemyTable, self.id)
        self.name = enemy.name
        self.level = enemy.level
        self.location = enemy.location

    def die(self):
        """Убивает персонажа"""
        self.alive = False
        phrases = f'{self.name} убит'
        print(phrases)
        self.session.query(EnemyTable).filter(EnemyTable.id == self.id).delete()
        self.session.commit()
        return phrases

        
