from day_5.vent import Vent

def test_vent_is_diagonal():
    vent1 = Vent(0, 9, 5, 9)
    assert vent1.is_diagonal == False

    vent2 = Vent(6, 4, 2, 0)
    assert vent2.is_diagonal == True


def test_horizontal_vent_can_calculate_its_own_coordinates():
    vent = Vent(0, 9, 5, 9)
    assert vent.calculate_all_coordinates() == [
        "0,9",
        "1,9",
        "2,9",
        "3,9",
        "4,9",
        "5,9",
    ]

    inverse_vent = Vent(5, 9, 0, 9)
    assert inverse_vent.calculate_all_coordinates() == vent.calculate_all_coordinates()


def test_vertical_vent_can_calculate_its_own_coordinates():
    vent = Vent(5, 9, 5, 12)
    assert vent.calculate_all_coordinates() == ["5,9", "5,10", "5,11", "5,12"]

    inverse_vent = Vent(5, 12, 5, 9)
    assert inverse_vent.calculate_all_coordinates() == vent.calculate_all_coordinates()


def test_diagonal_vent_can_calculate_its_own_coordinates():
    vent = Vent(5, 9, 9, 13)
    assert vent.calculate_all_coordinates() == ["5,9", "6,10", "7,11", "8,12", "9,13"]
    inverse_vent = Vent(9, 13, 5, 9)
