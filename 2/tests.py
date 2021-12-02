from submarine import Submarine


def test_with_sample_data():
    sample_data = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
    sub = Submarine("yellow")
    for movement in sample_data:
        direction, magnitude = movement.split(" ")
        sub.move(direction=direction, magnitude=int(magnitude))
    assert sub.distance == 15
    assert sub.depth == 60
