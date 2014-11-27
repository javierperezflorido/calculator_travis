from unittest import TestCase
from Calculator import *
from mockito import *
__author__ = 'javier'


class TestCalculator(TestCase):
    def test_suma(self):
        #my_calc = Calculator(2, 4)
        #self.assertEqual(my_calc.suma(), 6)
        my_calc=mock(Calculator)
        when(my_calc).suma().thenReturn(6)
        self.assertEqual(my_calc.suma(),9)
        a=2
