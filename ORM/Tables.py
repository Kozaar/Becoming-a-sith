from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class NPCTable(Base):
    """NPC Table"""
    __tablename__ = 'npc'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(Integer, ForeignKey('locations.id'))
    npc_type = Column(Integer)

    def __repr__(self):
        return f"NPCTable(id={self.id}, name={self.name})"


class NPCPhraseTable(Base):
    """NPC Phrase Table"""
    __tablename__ = 'npc_phrases'

    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('npc.id'))
    phrase = Column(String)

    def __repr__(self):
        return f'NPCPhraseTable(id={self.id}, npc_id={self.character_id}, phrase={self.phrase})'


class EnemyTable(Base):
    """Enemy Table"""
    __tablename__ = 'enemy'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    level = Column(Integer)
    location = Column(Integer, ForeignKey('locations.id'))

    def __repr__(self):
        return f'EnemyTable(id={self.id}, name={self.name}, level={self.level}'

class EnemyPhraseTable(Base):
    """Enemy Phrase Table"""
    __tablename__ = 'enemy_phrases'

    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('enemy.id'))
    phrase = Column(String)

    def __repr__(self):
        return f'EnemyPhraseTable(id={self.id}, enemy_id={self.character_id}, phrase={self.phrase})'


class InventoryItemsTable(Base):
    """Inventory Items Table"""
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    type = Column(String)
    weight = Column(Integer)
    price = Column(Integer)

    def __repr__(self):
        return f'InventoryTable(id={self.id}, name={self.name}, description={self.description}, type={self.type}, weight={self.weight}, price={self.price})'


class NPCInventoryTable(Base):
    """NPC Inventory Table"""
    __tablename__ = 'npc_inventory'

    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('npc.id'))
    item_id = Column(Integer, ForeignKey('inventory.id'))
    count = Column(Integer)

    def __repr__(self):
        return f'NPCInventoryTable(id={self.id}, npc_id={self.npc_id}, item_id={self.item_id}, count={self.count})'


class ProtagonistTable(Base):
    """Protagonist Table"""
    __tablename__ = 'protagonist'

    id = Column(Integer, primary_key=True)
    telegram_id = Column(String)
    name = Column(String)
    location = Column(Integer, ForeignKey('locations.id'))
    level = Column(Integer)
    hp = Column(Integer)
    xp = Column(Integer)

    def __repr__(self):
        return f'ProtagonistTable(id={self.id}, name={self.name}, location={self.location})'

class ProtagonistInventoryTable(Base):
    """Protagonist Inventory Table"""
    __tablename__ = 'protagonist_inventory'

    id = Column(Integer, primary_key=True)
    character_id = Column(Integer)
    item_id = Column(Integer, ForeignKey('inventory.id'))
    count = Column(Integer)

    def __repr__(self):
        return f'ProtagonistInventoryTable(id={self.id}, character_id={self.character_id}, item_id={self.item_id}, count={self.count})'


class Locations(Base):
    """Locations Table"""
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    linkUp = Column(Integer, ForeignKey('locations.id'))
    linkDown = Column(Integer, ForeignKey('locations.id'))
    linkLeft = Column(Integer, ForeignKey('locations.id'))
    linkRight = Column(Integer, ForeignKey('locations.id'))

    def __repr__(self):
        return f"DirectionTable(id={self.id}, name={self.name}, description= {self.description})"
