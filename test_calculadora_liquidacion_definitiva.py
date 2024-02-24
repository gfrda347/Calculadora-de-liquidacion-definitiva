import unittest, datetime
from liquidacion import Liquidacion, calcular_liquidacion_renuncia
from calculadora_liquidacion_definitiva import (calcular_indemnizacion_despido, calcular_vacaciones, calcular_cesantias, calcular_total_pagar, SalarioInvalidoError, SaldoAFavorException, FechaInvalidaError, ArgumentosInvalidosError)

class TestLiquidacionEmpleado(unittest.TestCase):

    def test_liquidacion_standard(self):
        motivo, salario_base, fecha_inicio, dias_vacaciones = "Despido", 1300000, "01/01/2020", "01/01/2023", 15
        # Valores esperados
        indemnizacion_esperada, vacaciones_esperadas, cesantias_esperadas, prima_esperada, intereses_esperados, retencion_esperada, total_esperado = 5310590, 622917, 546666, 731000, 327999, 167000, 7706173
        # Cálculo de liquidación
        indemnizacion, vacaciones, cesantias = calcular_indemnizacion_despido(salario_base, fecha_inicio), calcular_vacaciones(salario_base, dias_vacaciones), calcular_cesantias(salario_base, fecha_inicio)
        total = calcular_total_pagar(indemnizacion, vacaciones, cesantias, prima_esperada, intereses_esperados, retencion_esperada)
        self.assertEqual(indemnizacion, indemnizacion_esperada)
        self.assertEqual(vacaciones, vacaciones_esperadas)
        self.assertEqual(cesantias, cesantias_esperadas)
        self.assertEqual(total, total_esperado)

    def test_liquidacion_sin_vacaciones(self):
        motivo, salario_base, fecha_inicio, dias_vacaciones = "Renuncia voluntaria", "12200500", "15/06/2021", 0
    # Valores esperados
        indemnizacion_esperada, vacaciones_esperadas, cesantias_esperadas, prima_esperada, intereses_esperados, retencion_esperada, total_esperado = 5000000, 0, 3112500, 416250, 31125, 814250, 9374375
        liquidacion = Liquidacion(motivo, salario_base, fecha_inicio, dias_vacaciones)
        liquidacion.calcular()
        self.assertEqual(liquidacion.indemnizacion, indemnizacion_esperada)
        self.assertEqual(liquidacion.vacaciones, vacaciones_esperadas)
        self.assertEqual(liquidacion.cesantias, cesantias_esperadas)
        self.assertEqual(liquidacion.prima, prima_esperada)
        self.assertEqual(liquidacion.intereses, intereses_esperados)
        self.assertEqual(liquidacion.retencion, retencion_esperada)
        self.assertEqual(liquidacion.total, total_esperado)

    def test_liquidacion_vacaciones_utilizadas(self):
        motivo, salario_base, fecha_inicio, ultimas_vacaciones, dias_vacaciones = "Terminación de contrato", 2000000, "01/03/2019", "01/03/2022", 20
    # Valores esperados
        indemnizacion_esperada, vacaciones_esperadas, cesantias_esperadas, prima_esperada, intereses_esperados, retencion_esperada, total_esperado = 9500000, 0, 8296000, 877267, 82960, 1863226, 16893001
    # Liquidación
        liquidacion = Liquidacion(motivo, salario_base, fecha_inicio, ultimas_vacaciones, dias_vacaciones)
        liquidacion.calcular()
        self.assertEqual(liquidacion.indemnizacion, indemnizacion_esperada)
        self.assertEqual(liquidacion.vacaciones, vacaciones_esperadas)
        self.assertEqual(liquidacion.cesantias, cesantias_esperadas)
        self.assertEqual(liquidacion.prima, prima_esperada)
        self.assertEqual(liquidacion.intereses, intereses_esperados)
        self.assertEqual(liquidacion.retencion, retencion_esperada)
        self.assertEqual(liquidacion.total, total_esperado)

    def test_liquidacion_despido(self):
        motivo, salario_base, fecha_inicio, ultimas_vacaciones, dias_vacaciones = "Despido", 6000000, "01/07/2018", "01/07/2021", 10
    # Valores esperados
        indemnizacion_esperada, vacaciones_esperadas, cesantias_esperadas, prima_esperada, intereses_esperados, retencion_esperada, total_esperado = 833333, 0, 23143.5, 41667, 230.44, 1440000, -311427
    # Liquidación
        liquidacion = Liquidacion(motivo, salario_base, fecha_inicio, ultimas_vacaciones, dias_vacaciones)
        liquidacion.calcular()
        self.assertEqual(liquidacion.indemnizacion, indemnizacion_esperada)
        self.assertEqual(liquidacion.vacaciones, vacaciones_esperadas)
        self.assertEqual(round(liquidacion.cesantias, 2), cesantias_esperadas)
        self.assertEqual(round(liquidacion.prima, 2), prima_esperada)
        self.assertEqual(round(liquidacion.intereses, 2), intereses_esperados)
        self.assertEqual(round(liquidacion.retencion, 2), retencion_esperada)
        self.assertEqual(round(liquidacion.total, 2), total_esperado)

    def test_liquidacion_renuncia_reciente(self):
        motivo, salario, fecha_inicio, ultimas_vacaciones, dias_vacaciones = "Renuncia voluntaria", 2000000, "15/12/2023", "15/06/2024", 5
    # Valores esperados
        vacaciones_utilizadas, indemnizacion_esperada, cesantias_esperadas, prima_esperada, intereses_cesantias_esperados, retencion_esperada, total_esperado = 6, 0, 107200, 26670, 1070, 13490, 122450
    # Liquidación
        resultado = calcular_liquidacion_renuncia(salario, fecha_inicio, ultimas_vacaciones, dias_vacaciones)
        self.assertEqual(resultado["vacaciones_utilizadas"], vacaciones_utilizadas)
        self.assertEqual(resultado["indemnizacion"], indemnizacion_esperada)
        self.assertEqual(round(resultado["cesantias"], 2), cesantias_esperadas)
        self.assertEqual(round(resultado["prima"], 2), prima_esperada)
        self.assertEqual(round(resultado["intereses"], 2), intereses_cesantias_esperados)
        self.assertEqual(round(resultado["retencion"], 2), retencion_esperada)
        self.assertEqual(round(resultado["total"], 2), total_esperado)

    def test_liquidacion_antiguedad_significativa(self):
        motivo, salario, fecha_inicio, ultimas_vacaciones, dias_vacaciones = "Renuncia", 5000000, "01/01/2010", "01/01/2013", 30
    # Valores esperados
        vacaciones_utilizadas, indemnizacion_esperada, vacaciones_esperadas, cesantias_esperadas, prima_esperada, intereses_cesantias_esperados, retencion_esperada, total_esperado = 12, 71825000, 27500000, 69512500, 57584800, 695125, 19754745, 222363180
    # Liquidación
        resultado = calcular_liquidacion_renuncia(salario, fecha_inicio, ultimas_vacaciones, dias_vacaciones)
        self.assertEqual(resultado["vacaciones_utilizadas"], vacaciones_utilizadas)
        self.assertTrue(resultado["antiguedad_ajustada"] > 0)  # Ajustar según la implementación real
        self.assertEqual(resultado["indemnizacion"], indemnizacion_esperada)
        self.assertEqual(resultado["vacaciones"], vacaciones_esperadas)
        self.assertEqual(resultado["cesantias"], cesantias_esperadas)
        self.assertEqual(resultado["prima"], prima_esperada)
        self.assertEqual(resultado["intereses"], intereses_cesantias_esperados)
        self.assertEqual(resultado["retencion"], retencion_esperada)
        self.assertEqual(resultado["total"], total_esperado)

    def test_liquidacion_despido_injustificado(self):
        motivo, salario, fecha_inicio, ultimas_vacaciones, dias_vacaciones = "Despido injustificado", 3500000, "01/06/2018", "01/06/2021", 20
    # Valores esperados
        vacaciones_utilizadas, antiguedad_ajustada, indemnizacion_esperada, vacaciones_esperadas, cesantias_esperadas, prima_esperada, intereses_cesantias_esperados, retencion_esperada, total_esperado = 36, 6, 21000000, 5833333, 17640000, 21960000, 1764000, 6819733, 61377600
    # Liquidación
        resultado = calcular_liquidacion_renuncia(motivo, salario, fecha_inicio, ultimas_vacaciones, dias_vacaciones)
        self.assertEqual(resultado["vacaciones_utilizadas"], vacaciones_utilizadas)
        self.assertEqual(resultado["antiguedad_ajustada"], antiguedad_ajustada)
        self.assertEqual(resultado["indemnizacion"], indemnizacion_esperada)
        self.assertEqual(resultado["vacaciones"], vacaciones_esperadas)
        self.assertEqual(resultado["cesantias"], cesantias_esperadas)
        self.assertEqual(resultado["prima"], prima_esperada)
        self.assertEqual(resultado["intereses"], intereses_cesantias_esperados)
        self.assertEqual(resultado["retencion"], retencion_esperada)
        self.assertEqual(resultado["total"], total_esperado)

    # excepciones
    def test_salario_invalido(self):
    # Datos
        motivo, salario, fecha_inicio, ultimas_vacaciones, dias_vacaciones = "Despido", -2000, "01/01/2021", "01/01/2023", 12
        try:
            calcular_liquidacion_renuncia(motivo, salario, fecha_inicio, ultimas_vacaciones, dias_vacaciones)
        # El código llega aquí si no se lanza excepción
            self.fail("No se lanzó la excepción SalarioInvalidoError")
        except SalarioInvalidoError as error:
        # Verificar mensaje de error
            self.assertEqual(str(error), "El salario no puede ser negativo")

    def test_fecha_inicio_invalida(self):
    # Datos
        motivo, salario, fecha_inicio, ultimas_vacaciones, dias_vacaciones = "Renuncia", 2500000, "01/01/2025", "01/06/2023", 8
        try:
            calcular_liquidacion_renuncia(motivo, salario, fecha_inicio, ultimas_vacaciones, dias_vacaciones)
            self.fail("No se lanzó la excepción FechaInvalidaError")
        except FechaInvalidaError as error:
            fecha_actual = datetime.date.today().strftime("%d/%m/%Y")
            mensaje_esperado = f"La fecha de inicio {fecha_inicio} es inválida. La fecha no puede ser posterior a la actual ({fecha_actual})"
            self.assertEqual(str(error), mensaje_esperado)

    def test_argumentos_faltantes(self):
        # Se omiten datos requeridos por la función
        try:
            calcular_liquidacion_renuncia("", "", '01/01/2022', "01/06/2022")
            self.fail("No se lanzo ArgumentosInvalidosError")
        except ArgumentosInvalidosError as error:
            self.assertEqual(
                str(error), "Faltan argumentos obligatorios")

    def test_ningun_argumento(self):
        # No se envían argumentos
        try:
            calcular_liquidacion_renuncia()
            self.fail("No se lanzo ArgumentosInvalidosError")
        except ArgumentosInvalidosError as error:
            self.assertEqual(
                str(error), "Faltan argumentos obligatorios")

    def test_saldo_a_favor(self):
    # Datos
        motivo, salario, fecha_inicio, ultimas_vacaciones, dias_vacaciones = "Despido justificado", 900000, "01/03/2021", "01/06/2023", 5
        try:
            calcular_liquidacion_renuncia(motivo, salario, fecha_inicio, ultimas_vacaciones, dias_vacaciones)
            self.fail("No se lanzó la excepción SaldoAFavorException")
        except SaldoAFavorException as error:
            mensaje_esperado = "El total de la liquidación presenta saldo a favor del empleado"
            self.assertEqual(str(error), mensaje_esperado)
if __name__ == '__main__':
    unittest.main()
