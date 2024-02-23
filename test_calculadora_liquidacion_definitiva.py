import unittest
from liquidacion import Liquidacion
from calculadora_liquidacion_definitiva import (
    calcular_indemnizacion_despido,
    calcular_vacaciones,
    calcular_cesantias,
    calcular_total_pagar
)

class TestLiquidacionEmpleado(unittest.TestCase):

    def test_liquidacion_standard(self):
        # Datos
        motivo = "Despido"
        salario_base = 1300000
        fecha_inicio = "01/01/2020"  
        dias_vacaciones = 15

        # Valores esperados
        indemnizacion_esperada = 5200000
        vacaciones_esperadas = 541666
        cesantias_esperadas = 5466666
        prima_esperada = 5466666
        intereses_esperados = 327999
        retencion_esperada = 1670000
        total_esperado = 15005333

        # Cálculo de liquidación
        indemnizacion = calcular_indemnizacion_despido(salario_base, fecha_inicio)
        vacaciones = calcular_vacaciones(salario_base, dias_vacaciones) 
        cesantias = calcular_cesantias(salario_base, fecha_inicio)  
        # (Other calculations)

        total = calcular_total_pagar(indemnizacion, vacaciones, cesantias, 
                                    prima_esperada, intereses_esperados, retencion_esperada)
        
        # Asserts
        self.assertEqual(indemnizacion, indemnizacion_esperada)
        self.assertEqual(vacaciones, vacaciones_esperadas)
        self.assertEqual(cesantias, cesantias_esperadas)
        # (Other assertions)
        self.assertEqual(total, total_esperado)
    
    def test_liquidacion_sin_vacaciones(self):
        # Datos
        motivo = "Renuncia voluntaria"
        salario_base = "12200500"  # Assuming salario_base is expected as a string
        fecha_inicio = "15/06/2021"
        dias_vacaciones = 0
        
        # Valores esperados 
        indemnizacion_esperada = 5000000
        vacaciones_esperadas = 0
        cesantias_esperadas = 3112500
        prima_esperada = 416250
        intereses_esperados = 31125
        retencion_esperada = 814250  
        total_esperado = 9374375
        
        # Liquidación 
        liquidacion = Liquidacion(motivo, salario_base, fecha_inicio, dias_vacaciones)
        liquidacion.calcular()
        
        # Asserts
        self.assertEqual(liquidacion.indemnizacion, indemnizacion_esperada)
        self.assertEqual(liquidacion.vacaciones, vacaciones_esperadas) 
        self.assertEqual(liquidacion.cesantias, cesantias_esperadas)
        self.assertEqual(liquidacion.prima, prima_esperada)
        self.assertEqual(liquidacion.intereses, intereses_esperados)
        self.assertEqual(liquidacion.retencion, retencion_esperada)
        self.assertEqual(liquidacion.total, total_esperado)

    def test_liquidacion_vacaciones_utilizadas(self):
        # Datos
        motivo = "Terminación de contrato"
        salario_base = 2000000
        fecha_inicio = "01/03/2019"
        ultimas_vacaciones = "01/03/2022"
        dias_vacaciones = 20
        
        # Valores esperados
        indemnizacion_esperada = 9500000
        vacaciones_esperadas = 0
        cesantias_esperadas = 8296000
        prima_esperada = 877267
        intereses_esperados = 82960
        retencion_esperada = 1863226
        total_esperado = 16893001
        
        # Liquidación
        liquidacion = Liquidacion(motivo, salario_base, fecha_inicio,  
                                ultimas_vacaciones, dias_vacaciones)
        liquidacion.calcular()

        
        # Asserts
        self.assertEqual(liquidacion.indemnizacion, indemnizacion_esperada)
        self.assertEqual(liquidacion.vacaciones, vacaciones_esperadas) 
        self.assertEqual(liquidacion.cesantias, cesantias_esperadas)
        self.assertEqual(liquidacion.prima, prima_esperada)
        self.assertEqual(liquidacion.intereses, intereses_esperados)
        self.assertEqual(liquidacion.retencion, retencion_esperada)
        self.assertEqual(liquidacion.total, total_esperado)
    
    def test_liquidacion_despido(self):
        # Datos
        motivo = "Despido"
        salario_base = 6000000
        fecha_inicio = "01/07/2018"
        ultimas_vacaciones = "01/07/2021" 
        dias_vacaciones = 10
        
        # Valores esperados
        indemnizacion_esperada = 833333
        vacaciones_esperadas = 0
        cesantias_esperadas = 23143.5  
        prima_esperada = 41667
        intereses_esperados = 230.44
        retencion_esperada = 1440000  
        total_esperado = -311427
        
        # Liquidación
        liquidacion = Liquidacion(motivo, salario_base, fecha_inicio,  
                                ultimas_vacaciones, dias_vacaciones,)
        liquidacion.calcular()
        
        # Asserts
        self.assertEqual(liquidacion.indemnizacion, indemnizacion_esperada)
        self.assertEqual(liquidacion.vacaciones, vacaciones_esperadas)
        self.assertEqual(round(liquidacion.cesantias, 2), cesantias_esperadas)
        self.assertEqual(round(liquidacion.prima, 2), prima_esperada) 
        self.assertEqual(round(liquidacion.intereses, 2), intereses_esperados)
        self.assertEqual(round(liquidacion.retencion, 2), retencion_esperada)
        self.assertEqual(round(liquidacion.total, 2), total_esperado)
        
    def test_liquidacion_renuncia(self):
        
        # Datos
        salario = 1160000
        fecha_inicio = "01/01/2022"
        ultimas_vacaciones = "01/01/2024"
        dias_vacaciones = 8
        
        # Valores esperados
        vacaciones_utilizadas = 31
        indemnizacion_esperada = 0
        cesantias_esperadas = 134.56
        intereses_cesantias_esperados = 1.35
        prima_esperada = 76.67
        retencion_esperada = 0
        total_esperado = 212.58

        # Liquidación 
        resultado = calcular_liquidacion_renuncia(salario, fecha_inicio, 
                                                ultimas_vacaciones, 
                                                dias_vacaciones)
        
        # Asserts
        self.assertEqual(resultado["vacaciones_utilizadas"], vacaciones_utilizadas)  
        self.assertEqual(resultado["indemnizacion"], indemnizacion_esperada)
        self.assertEqual(resultado["cesantias"], cesantias_esperadas) 
        self.assertEqual(resultado["intereses"], intereses_cesantias_esperados)
        self.assertEqual(resultado["prima"], prima_esperada)
        self.assertEqual(resultado["total"], total_esperado)

if __name__ == '__main__':
    unittest.main()
