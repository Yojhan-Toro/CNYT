import LibComplejos as lc
import unittest

class TestDivisionComplejos(unittest.TestCase):
    
    def test_Division(self):
        self.assertEqual(lc.division((3,2.8), (1.5,-2)), (-0.176, 1.632))     
        self.assertEqual(lc.division((1,2), (2,1)), (0.8, 0.6))

    def test_Multiplicacion(self):
        self.assertEqual(lc.multiplicacion((-2,1), (1,2)), (-4,-3))
        self.assertEqual(lc.multiplicacion((1,1), (1,1)), (0,2))

    def test_SumayResta(self):
        self.assertEqual(lc.suma((2,2), (1,-5)), (3, -3)) 
        self.assertEqual(lc.suma((1,1), (1,-1)), (2, 0))     
        
    def test_Conjugado(self):
        self.assertEqual(lc.conjugado((-2, -1)), (-2, 1))
        self.assertEqual(lc.conjugado((2, 5)), (2, -5))
        
    def test_Modulo(self):
        self.assertAlmostEqual(lc.modulo((-2, -1)), 2.23606797)
        self.assertAlmostEqual(lc.modulo((2, 5)), 5.3851648)

    def test_Fase(self):
        self.assertAlmostEqual(lc.fase((-2, -1)), 0.4636476)
        self.assertAlmostEqual(lc.fase((2, 5)), 1.1902899)

    def test_PolarCartesianas(self):
        self.assertEqual(lc.polarCar(2.23606797, 0.4636476), (-2, -1))
        self.assertEqual(lc.polarCar(5.3851648, 1.1902899), (2, 5))

           
if __name__ == '__main__':
    unittest.main()

