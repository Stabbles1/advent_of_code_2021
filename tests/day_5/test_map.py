from day_5.vent import Vent
from day_5.map import Map

def test_map_plots_vents_correctly():
    vent1 = Vent(1,1,1,2)
    vent2 = Vent(0,1,3,1)
    map = Map()
    map.advent(vent1)
    map.advent(vent2)
    assert map.vent_locations == {'0,1': 1, '1,1': 2, '1,2': 1, '2,1': 1, '3,1': 1}

def test_dangerous_coordinates():
    vent1 = Vent(1,1,1,2)
    vent2 = Vent(0,1,3,1)
    map = Map()
    map.advent(vent1)
    map.advent(vent2)
    assert map.dangerous_coordinates(2) == ['1,1']
    assert map.dangerous_coordinates(1) == ['1,1', '1,2', '0,1', '2,1', '3,1']