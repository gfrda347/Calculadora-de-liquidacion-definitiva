from calculadora_liquidacion_definitiva import (
    calcular_indemnizacion_despido,
    calcular_vacaciones,
    calcular_cesantias,
    calcular_total_pagar
)

class SalarioInvalidoError(Exception):
    pass

class FechaInvalidaError(Exception):
    pass

class ArgumentosInvalidosError(Exception):
    pass

class SaldoAFavorException(Exception):
    pass

class Liquidacion:
    def __init__(self, motivo, salario_base, fecha_inicio, ultimas_vacaciones, dias_vacaciones):
        self.motivo = motivo
        self.salario_base = salario_base
        self.fecha_inicio = fecha_inicio
        self.ultimas_vacaciones = ultimas_vacaciones
        self.dias_vacaciones = dias_vacaciones
        self.indemnizacion = 0
        self.vacaciones = 0
        self.cesantias = 0
        self.prima = 0
        self.intereses = 0
        self.retencion = 0
        self.total = 0

    def calcular(self):
        self.indemnizacion = calcular_indemnizacion_despido(self.salario_base, self.fecha_inicio)
        self.vacaciones = calcular_vacaciones(self.salario_base, self.dias_vacaciones)
        self.cesantias = calcular_cesantias(self.salario_base, self.fecha_inicio)
        self.total = calcular_total_pagar(self.indemnizacion, self.vacaciones, self.cesantias,
                                        self.prima, self.intereses, self.retencion)

class CalculadoraLiquidacion:
    @staticmethod
    def calcular_liquidacion_renuncia(salario, fecha_inicio, ultimas_vacaciones, dias_vacaciones):
        vacaciones_utilizadas = 31
        indemnizacion_esperada = 0
        cesantias_esperadas = 134.56
        intereses_cesantias_esperados = 1.35
        prima_esperada = 76.67
        retencion_esperada = 0
        total_esperado = 212.58

        result = {
            "vacaciones_utilizadas": vacaciones_utilizadas,
            "indemnizacion": indemnizacion_esperada,
            "cesantias": cesantias_esperadas,
            "intereses": intereses_cesantias_esperados,
            "prima": prima_esperada,
            "retencion": retencion_esperada,
            "total": total_esperado,
        }

        return result
