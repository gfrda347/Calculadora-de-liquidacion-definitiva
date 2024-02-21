import unittest
from calculadora_liquidacion_definitiva import calcular_indemnizacion_despido, calcular_indemnizacion_por_renuncia, calcular_vacaciones, calcular_cesantias, calcular_intereses_cesantias, calcular_primas, calcular_retencion_fuente, calcular_total_pagar

class TestCalculos(unittest.TestCase):

    def test_calcular_indemnizacion_despido(self):
        self.assertEqual(calcular_indemnizacion_despido(1000000, 90, 5), 2020202.08)

    def test_calcular_indemnizacion_por_renuncia(self):
        self.assertEqual(calcular_indemnizacion_por_renuncia(1000000, 90, 5), 1010101.04)

    def test_calcular_vacaciones(self):
        self.assertEqual(calcular_vacaciones(1000000, 5), 75000)

    def test_calcular_cesantias(self):
        self.assertEqual(calcular_cesantias(1000000, 90), 250000)

    def test_calcular_intereses_cesantias(self):
        self.assertEqual(calcular_intereses_cesantias(250000, 90), 22500)

    def test_calcular_primas(self):
        self.assertEqual(calcular_primas(1000000, 180), 500000)

    def test_calcular_retencion_fuente(self):
        self.assertEqual(calcular_retencion_fuente(1000000), 100000)

    def test_calcular_total_pagar(self):
        indemnizacion = calcular_indemnizacion_despido(1000000, 90, 5)
        vacaciones = calcular_vacaciones(1000000, 5)
        cesantias = calcular_cesantias(1000000, 90)
        intereses_cesantias = calcular_intereses_cesantias(cesantias, 90)
        primas = calcular_primas(1000000, 180)
        base_gravable = 1000000
        retencion_fuente = calcular_retencion_fuente(base_gravable)
        total_pagar = calcular_total_pagar(indemnizacion, vacaciones, cesantias, intereses_cesantias, primas, retencion_fuente)
        self.assertEqual(total_pagar, 1827502.04)

if __name__ == '__main__':
    unittest.main()