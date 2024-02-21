import unittest

from calculadora_liquidacion_definitiva import calcular_valores
class TestCalculos(unittest.TestCase):
    def test_caso_de_prueba_estandar(self):
        resultado = calcular_valores("Despido", 300000, "01/01/2020", "01/01/2023", 15)
        
        self.assertEqual(resultado[0], 150000.0)  # Valor de Indemnización
        self.assertEqual(resultado[1], 1500)   # Valor de Vacaciones
        self.assertEqual(resultado[2], 9990)   # Valor de Cesantías
        self.assertEqual(resultado[3], 999.90) # Valor de Prima
        self.assertEqual(resultado[4], 99.90)  # Valor de Intereses de Cesantías
        self.assertEqual(resultado[5], 2159.90)  # Retención de Fuente
        self.assertEqual(resultado[6], 21599.01) # Total a Pagar
        self.assertEqual(resultado[7], 19439.11) # Neto a Recibir

    def test_caso_sin_dias_de_vacaciones(self):
        resultado = calcular_valores("Renuncia", 2500, "15/06/2021", "15/12/2022", 0)
        
        self.assertEqual(resultado[0], 5000)     # Valor de Indemnización
        self.assertEqual(resultado[1], 0)        # Valor de Vacaciones
        self.assertEqual(resultado[2], 3112.5)   # Valor de Cesantías
        self.assertEqual(resultado[3], 416.25)   # Valor de Prima
        self.assertEqual(resultado[4], 31.125)   # Valor de Intereses de Cesantías
        self.assertEqual(resultado[5], 814.25)   # Retención de Fuente
        self.assertEqual(resultado[6], 9374.875) # Total a Pagar
        self.assertEqual(resultado[7], 8556.625) # Neto a Recibir

    def test_caso_con_vacaciones_utilizadas(self):
        resultado = calcular_valores("Despido", 4500, "01/03/2019", "01/03/2022", 20)
        
        self.assertEqual(resultado[0], 19440)    # Valor de Indemnización
        self.assertEqual(resultado[1], 0)        # Valor de Vacaciones
        self.assertEqual(resultado[2], 17608.50) # Valor de Cesantías
        self.assertEqual(resultado[3], 1873.92)  # Valor de Prima
        self.assertEqual(resultado[4], 176.09)   # Valor de Intereses de Cesantías
        self.assertEqual(resultado[5], 4594.35)  # Retención de Fuente
        self.assertEqual(resultado[6], 34504.16) # Total a Pagar
        self.assertEqual(resultado[7], 29909.81) # Neto a Recibir
    
    def test_caso_con_salario_alto(self):
        resultado = calcular_valores("Renuncia", 7000, "01/07/2018", "01/07/2021", 10)
        
        self.assertEqual(resultado[0], 28000)    # Valor de Indemnización
        self.assertEqual(resultado[1], 0)        # Valor de Vacaciones
        self.assertEqual(resultado[2], 23143.50) # Valor de Cesantías
        self.assertEqual(resultado[3], 1833.92)  # Valor de Prima
        self.assertEqual(resultado[4], 230.44)   # Valor de Intereses de Cesantías
        self.assertEqual(resultado[5], 5620.89)  # Retención de Fuente
        self.assertEqual(resultado[6], 48587.97) # Total a Pagar
        self.assertEqual(resultado[7], 42967.08) # Neto a Recibir
    
    def test_caso_con_salario_minimo(self):
        resultado = calcular_valores("Despido", 877, "01/01/2022", "01/01/2024", 8)
        
        self.assertEqual(resultado[0], 1794)      # Valor de Indemnización
        self.assertEqual(resultado[1], 0)         # Valor de Vacaciones
        self.assertEqual(resultado[2], 153.27)    # Valor de Cesantías
        self.assertEqual(resultado[3], 72.92)     # Valor de Prima
        self.assertEqual(resultado[4], 1.53)      # Valor de Intereses de Cesantías
        self.assertEqual(resultado[5], 203.46)    # Retención de Fuente
        self.assertEqual(resultado[6], 1818.26)   # Total a Pagar
        self.assertEqual(resultado[7], 1614.80)   # Neto a Recibir

    def test_caso_fecha_reciente(self):
        resultado = calcular_valores("Renuncia voluntaria", 3200, "15/12/2023", "15/06/2024", 5)
        
        self.assertEqual(resultado[0], 0)         # Valor de Indemnización
        self.assertEqual(resultado[1], 0)         # Valor de Vacaciones
        self.assertEqual(resultado[2], 107.20)    # Valor de Cesantías
        self.assertEqual(resultado[3], 26.67)     # Valor de Prima
        self.assertEqual(resultado[4], 1.07)      # Valor de Intereses de Cesantías
        self.assertEqual(resultado[5], 13.19)     # Retención de Fuente
        self.assertEqual(resultado[6], 122.75)    # Total a Pagar
        self.assertEqual(resultado[7], 109.56)    # Neto a Recibir
if __name__ == '__main__':
    unittest.main()