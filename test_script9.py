import script9 as s

class TestEq:
    def test_10_5(self):
        assert s.div(10, 5) == 2
    def test_5_0(self):
        assert s.div(5, 0) == 0
    def test_10_4(self):
        assert s.div(10, 4) == 2
    
class TestReverse:
    def test_baa(self):
        assert s.reverse("baa") == "aa"
    def test_aaabc(self):
        assert s.reverse("aaabc") == "cb"
    def test_bc(self):
        assert s.reverse("bc") == "cb"
    def test_d(self):
        assert s.reverse("d") == "d"