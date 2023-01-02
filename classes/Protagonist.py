import random

from classes.NPC import NPC
from classes.Enemy import Enemy
from classes.Direction import Direction
from ORM.ORM import ORM
from internal.roll_dice import roll_dice
from ORM.Tables import ProtagonistTable, ProtagonistInventoryTable


class Protagonist(ORM):  # you may decide to add some parent class here, e.g. ORM Model
    def __init__(self, name: str, id: str):  # add more parameters if you need
        super().__init__('game.db')
        self.telegram_id = id
        self.id: int = 0  # a unique identifier of a current player
        self.name: str = name
        self.hp: int = 10
        self.xp: int = 0

        self.level: int = 1
        # name and count, modify starting inventory at your wish
        self.locations = Direction(1)
        """"Задаем начальную локацию персонажу"""
        self.inventory: dict[str, int] = {}
        self.location = 1
        """Задаем начальную локацию персонажу"""
        self.load()

        self.level_caps = [0, 5, 9, 15, 21, 27, 35, 44, 51, 55, 60]

    def load(self):
        stats = self.session.query(ProtagonistTable).filter(ProtagonistTable.telegram_id == self.telegram_id).first()
        if stats:
            self.id = stats.id
            self.name = stats.name
            self.hp = stats.hp
            self.level = stats.level
            self.location = stats.location
            self.inventory = self.load_inventory(ProtagonistInventoryTable, self.id)
            self.xp = stats.xp
        else:
            self.id = self.session.query(ProtagonistTable).count() + 1
            self.save_protagonist()

    def update_protagonist(self):
        self.session.query(ProtagonistTable).filter(ProtagonistTable.telegram_id == self.telegram_id).update(
            {'name': self.name, 'hp': self.hp, 'level': self.level, 'location': self.location, 'xp': self.xp})
        self.session.commit()

    def save_protagonist(self):
        print(self.id, self.name, self.hp, self.level, self.location)
        self.save(ProtagonistTable, name=self.name, hp=self.hp, level=self.level, location=self.location,
                  telegram_id=self.telegram_id, xp=self.xp)

    def talk_to(self, npc: NPC):
        npc = NPC(npc.id)
        return random.choice(npc.phrases) if len(npc.phrases) > 0 else 'Мне нечего сказать'

    def attack(self, enemy: Enemy):
        phrases = []
        hit = roll_dice() + self.level
        enemy_hit = roll_dice() + enemy.level
        phrases.append(f"You attack {enemy.name} with your roll: {hit}")
        print(phrases[-1])
        phrases.append(f"{enemy.name} attacks you with his roll: {enemy_hit}")
        print(phrases[-1])
        if hit > enemy_hit:
            phrases.append(enemy.die())
            enemy.die()
            self.xp += enemy.level
            phrases += self.level_up()
            return 1, phrases
        else:
            self.take_hit()
            phrases.append(f"Enemy says: {random.choice(enemy.phrases)}")
            print(phrases[-1])
            phrases.append(f"You have {self.hp} hp left")
            print(phrases[-1])
            return 0, phrases

    def level_up(self):
        phrases = []
        if self.level < 10:
            if self.xp >= self.level_caps[self.level]:
                self.advance_level()
                phrases.append('You leveled up!')
                print("You leveled up!")
        print(f"Your level is {self.level}")
        phrases.append(f"Your level is {self.level}")
        return phrases

    def take_hit(self, value=1):
        self.hp -= value
        self.update_protagonist()
        if self.hp <= 0:
            raise Exception("You died")

    def heal(self):
        self.hp = 10
        self.update_protagonist()

    def advance_level(self, value: int = 1):
        self.level += value
        self.update_protagonist()

    def go(self, direction: Direction):
        print("Вы идете")
        direction.check()
        if int(self.locations.id) not in direction.link:
            """Если локация игрока не содержит ссылку на следущую локацию"""
            print('Нет дружок туда ты идти не можешь')
        else:

            """Идем в эту лакацию"""
            print(f'Вы пришли в {direction.name} \n')
            self.locations = direction

    def whereami(self):
        phrases = [self.locations.name, self.locations.description]
        print('Текущая локация: ', self.locations.name)
        print(f'Описание: {self.locations.description} \n')
        return phrases

    def take(self, item: str):
        item_id = self.session.query(ProtagonistInventoryTable).filter(
            ProtagonistInventoryTable.protagonist_id == self.id).filter(
            ProtagonistInventoryTable.item_name == item).first()
        if item in self.inventory:
            self.session.query(ProtagonistInventoryTable).filter(
                ProtagonistInventoryTable.character_id == self.id).filter(
                ProtagonistInventoryTable.item_id == item_id).update({'count': self.inventory[item] + 1})
        else:
            self.save(ProtagonistInventoryTable, character_id=self.id, item_id=item_id, count=self.inventory[item])
        self.session.commit()
        self.inventory[item] += 1
        print(f"You take {item}")
        print(f"Your inventory: {self.inventory}")

    def give(self, npc: NPC, item: str):
        if item in self.inventory:
            self.inventory[item] -= 1
            if self.inventory[item] == 0:
                del self.inventory[item]
                self.session.query(ProtagonistInventoryTable).filter(
                    ProtagonistInventoryTable.character_id == self.id).delete()
            else:
                self.session.query(ProtagonistInventoryTable).filter(
                    ProtagonistInventoryTable.character_id == self.id).filter(
                    ProtagonistInventoryTable.item_name == item).update({'count': self.inventory[item]})
            self.session.commit()
            npc.receive(item)
            print(f"You give {item} to {npc.name}")
            print(f"Your inventory: {self.inventory}")

