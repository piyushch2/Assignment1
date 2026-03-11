from src.Subtractor import Subtractor

def test_subtract():
    s = Subtractor()
    assert s.subtract(5, 3) == 2
