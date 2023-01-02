from controller.Controller import Controller
from ORM.Tables import *
from loading.load_data import load_data
from loading.load_map import load_map
from classes.NPC import NPC
from classes.Enemy import Enemy
from classes.Protagonist import Protagonist
from classes.Direction import Direction
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_map()
load_data()
controller = Controller('game.db')

def test_go():
    controller.start_game('130')
    location = controller.get_current_location()
    assert location.id == 1
    assert location.name == 'Entrance'
    assert location.description == 'Entrance to the Jedi Temple'
    assert controller.get_locations_to_go()[0].id == 2

    controller.go(Direction(2))
    location = controller.get_current_location()
    assert location.id == 2
    assert location.name == 'Hallway'
    assert location.description == 'A long hallway, with a door to the left and a door to the right.'
    assert controller.get_locations_to_go()[0].id == 6
    assert controller.get_locations_to_go()[1].id == 1
    assert controller.get_locations_to_go()[2].id == 3
    assert controller.get_locations_to_go()[3].id == 4

    controller.go(Direction(3))
    location = controller.get_current_location()
    assert location.id == 3
    assert location.name == 'Library'
    assert location.description == 'A large library, with many holocrons and books.'
    assert controller.get_locations_to_go()[0].id == 2

    controller.go(Direction(2))
    location = controller.get_current_location()
    assert location.id == 2
    assert location.name == 'Hallway'
    assert location.description == 'A long hallway, with a door to the left and a door to the right.'
    assert controller.get_locations_to_go()[0].id == 6
    assert controller.get_locations_to_go()[1].id == 1
    assert controller.get_locations_to_go()[2].id == 3
    assert controller.get_locations_to_go()[3].id == 4

    controller.go(Direction(4))
    location = controller.get_current_location()
    assert location.id == 4
    assert location.name == 'Dining Room'
    assert location.description == 'A large dining room, with many tables and chairs, spoons and forks, and a large table in the middle.'
    assert controller.get_locations_to_go()[0].id == 5
    assert controller.get_locations_to_go()[1].id == 2

    controller.go(Direction(5))
    location = controller.get_current_location()
    assert location.id == 5
    assert location.name == 'Cellar'
    assert location.description == "A dark cellar, with many barrels and crates, it smells of wine and cheese. It's dark, and you can see nothing."
    assert controller.get_locations_to_go()[0].id == 4

    controller.go(Direction(4))
    location = controller.get_current_location()
    assert location.id == 4

    controller.go(Direction(2))
    location = controller.get_current_location()
    assert location.id == 2

    controller.go(Direction(6))
    location = controller.get_current_location()
    assert location.id == 6
    assert location.name == 'Lift'
    assert location.description == "A lift, with a button to go up and a button to go down."
    assert controller.get_locations_to_go()[0].id == 7
    assert controller.get_locations_to_go()[1].id == 10
    assert controller.get_locations_to_go()[2].id == 2

    controller.go(Direction(7))
    location = controller.get_current_location()
    assert location.id == 7
    assert location.name == 'Down Hallway'
    assert location.description == "A long hallway, with a door forward and a door to the right."
    assert controller.get_locations_to_go()[0].id == 8
    assert controller.get_locations_to_go()[1].id == 6
    assert controller.get_locations_to_go()[2].id == 9

    controller.go(Direction(8))
    location = controller.get_current_location()
    assert location.id == 8
    assert location.name == "Arsenal"
    assert location.description == "A large room, with many weapons and armour."
    assert controller.get_locations_to_go()[0].id == 7

    controller.go(Direction(7))
    location = controller.get_current_location()
    assert location.id == 7

    controller.go(Direction(9))
    location = controller.get_current_location()
    assert location.id == 9
    assert location.name == "Medbay"
    assert location.description == "A large room, with many beds and medical equipment."
    assert controller.get_locations_to_go()[0].id == 7

    controller.go(Direction(7))
    location = controller.get_current_location()
    assert location.id == 7

    controller.go(Direction(6))
    location = controller.get_current_location()
    assert location.id == 6

    controller.go(Direction(10))
    location = controller.get_current_location()
    assert location.id == 10
    assert location.name == "Up Hallway"
    assert location.description == "A long hallway, with a door forward and a door to the right."
    assert controller.get_locations_to_go()[0].id == 11
    assert controller.get_locations_to_go()[1].id == 6
    assert controller.get_locations_to_go()[2].id == 12

    controller.go(Direction(11))
    location = controller.get_current_location()
    assert location.id == 11
    assert location.name == "Training Room"
    assert location.description ==  "A large room, with many training droids and a large training area."
    assert controller.get_locations_to_go()[0].id == 10

    controller.go(Direction(10))
    location = controller.get_current_location()
    assert location.id == 10

    controller.go(Direction(12))
    location = controller.get_current_location()
    assert location.id == 12
    assert location.name == "Council Room"
    assert location.description == "A large room, with a large table in the middle, and a large window."
    assert controller.get_locations_to_go()[0].id == 10

    controller.go(Direction(10))
    location = controller.get_current_location()
    assert location.id == 10

    controller.go(Direction(6))
    location = controller.get_current_location()
    assert location.id == 6

    controller.go(Direction(2))
    location = controller.get_current_location()
    assert location.id == 2

    controller.go(Direction(1))
    location = controller.get_current_location()
    assert location.id == 1
    assert location.name == 'Entrance'
    assert location.description == 'Entrance to the Jedi Temple'
    assert controller.get_locations_to_go()[0].id == 2

