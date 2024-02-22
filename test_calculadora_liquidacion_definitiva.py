import unittest
from calculadora_liquidacion_definitiva import calcular_indemnizacion_despido, calcular_indemnizacion_por_renuncia, calcular_vacaciones, calcular_cesantias, calcular_intereses_cesantias, calcular_primas, calcular_retencion_fuente, calcular_total_pagar

class PruebasLiquidacion(unittest.TestCase):

    def test_calcular_indemnizacion_despido(self):
        salario = 1300000
        dias = 1096
        tiempo = 1096
        resultado = calcular_indemnizacion_despido(salario, dias, tiempo)
        self.assertEqual(resultado, 15005333)


if __name__ == '__main__':
    unittest.main()