import pytest
import math
from root_finding.root_finding import bisection_method, check_root_exist


class TestMethods:
    def test_check_root_exist(self):
        assert check_root_exist(math.sin, 2, 4) == True

    def test_check_root_exist_2(self):
        assert check_root_exist(math.sin, 3.9, 4) == False
