from ORM.Tables import *
from ORM.ORM import ORM


class NPC(ORM):
    class Types:
        HEALER = 1
        TRADER = 2
        CAPTAIN = 3
    def __init__(self, id: int):

        super().__init__('game.db')
        self.id = id
        self.name = ''
        """Имя персонажа"""
        self.phrases = self.load_phrases(NPCPhraseTable, self.id)
        """Список фраз, которые говорит NPC"""
        self.inventory: dict[str, int] = self.load_inventory(NPCInventoryTable, self.id)
        self.location = 0
        """Список предметов, которые держит NPC"""
        self.load()

    def load(self):
        """Загружает данные из базы данных в объект"""
        npc = self.load_stats(NPCTable, self.id)
        self.name = npc.name
        self.location = npc.location
        print(self.name)
        print(self.phrases)
        print(self.location)

    def receive(self, item):
        """Получает предмет"""
        item_id = self.session.query(InventoryItemsTable).filter(InventoryItemsTable.name == item).first().id
        if item in self.inventory:
            self.session.query(NPCInventoryTable).filter(
                NPCInventoryTable.character_id == self.id).filter(
                NPCInventoryTable.item_id == item_id).update({'count': self.inventory[item] + 1})
        else:
            self.save(NPCInventoryTable, character_id=self.id, item_id=item_id, count=self.inventory[item])
        self.session.commit()
        self.inventory[item] += 1
        print(f'{self.name} получил {item}')
        print(self.inventory)
