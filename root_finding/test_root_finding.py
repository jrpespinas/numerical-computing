import pytest
import math
from root_finding.root_finding import bisection_method, check_root_exist


class TestMethods:
    def test_check_root_exist(self):
        assert check_root_exist(math.sin, 2, 4) == True

    def test_check_root_exist_2(self):
        assert check_root_exist(math.sin, 3.9, 4) == False

    def test_bisection_method(self):
        assert bisection_method(math.sin, 2, 4) >= 3.14

    def test_bisection_method_2(self):
        assert bisection_method(math.sin, 3, 4) >= 3.14
