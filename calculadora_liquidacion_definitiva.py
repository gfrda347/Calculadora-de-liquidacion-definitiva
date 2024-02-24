from datetime import datetime

class SalarioInvalidoError(Exception):
    pass

class FechaInvalidaError(Exception):
    pass

class ArgumentosInvalidosError(Exception):
    pass

class SaldoAFavorException(Exception):
    pass

def calcular_indemnizacion_despido(salario_mensual, dias_trabajados, tiempo_servicio):
    factor_indemnizacion = min(max(tiempo_servicio, 1), 20)
    indemnizacion = (salario_mensual * dias_trabajados / 360) + factor_indemnizacion
    return indemnizacion

def calcular_indemnizacion_por_renuncia(salario_mensual, dias_trabajados):
    factor_dias = min(max(1, dias_trabajados // 30), 20)
    indemnizacion = salario_mensual * (dias_trabajados / 360 + factor_dias / 30)
    return indemnizacion

def calcular_vacaciones(salario_mensual, tiempo_servicio):
    dias_vacaciones = 15 * tiempo_servicio
    vacaciones = salario_mensual * dias_vacaciones / 360
    return vacaciones

def calcular_cesantias(salario_mensual, dias_trabajados):
    cesantias = salario_mensual * dias_trabajados / 360
    return cesantias

def calcular_intereses_cesantias(cesantias, dias_trabajados):
    intereses_cesantias = cesantias * 0.12 * dias_trabajados / 360
    return intereses_cesantias

def calcular_primas(salario_mensual, dias_trabajados_semestre):
    primas = salario_mensual * dias_trabajados_semestre / 360
    return primas

def calcular_retencion_fuente(base_gravable):
    retencion_fuente = base_gravable * 0.1  
    return retencion_fuente

def calcular_total_pagar(indemnizacion, vacaciones, cesantias, intereses_cesantias, primas, retencion_fuente):
    total_pagar = indemnizacion + vacaciones + cesantias + intereses_cesantias + primas - retencion_fuente
    return total_pagar

def input_datos_usuario():
    motivo_terminacion = input("Ingrese el motivo de terminación del contrato (despido o renuncia): ")
    salario_mensual = float(input("Ingrese el salario mensual: "))
    fecha_inicio_labores = input("Ingrese la fecha de inicio de labores (formato: DD/MM/AAAA): ")
    fecha_ultimas_vacaciones = input("Ingrese la fecha de las últimas vacaciones (formato: DD/MM/AAAA): ")
    dias_vacaciones_acumulados = int(input("Ingrese los días de vacaciones acumulados: "))

    fecha_inicio_labores = datetime.strptime(fecha_inicio_labores, "%d/%m/%Y")
    fecha_ultimas_vacaciones = datetime.strptime(fecha_ultimas_vacaciones, "%d/%m/%Y")

    tiempo_servicio = (datetime.now() - fecha_inicio_labores).days // 365
    dias_trabajados = (datetime.now() - fecha_ultimas_vacaciones).days
    dias_trabajados_semestre = (datetime.now() - fecha_ultimas_vacaciones).days

    return motivo_terminacion, salario_mensual, tiempo_servicio, dias_trabajados, dias_trabajados_semestre

def calcular_liquidacion(motivo_terminacion, salario_mensual, tiempo_servicio, dias_trabajados, dias_trabajados_semestre):
    if motivo_terminacion.lower() == 'despido':
        indemnizacion = calcular_indemnizacion_despido(salario_mensual, dias_trabajados, tiempo_servicio)
    elif motivo_terminacion.lower() == 'renuncia':
        indemnizacion = calcular_indemnizacion_por_renuncia(salario_mensual, dias_trabajados)
    else:
        raise ArgumentosInvalidosError("Motivo de terminación no válido. Debe ser 'despido' o 'renuncia'.")

    vacaciones = calcular_vacaciones(salario_mensual, tiempo_servicio)
    cesantias = calcular_cesantias(salario_mensual, dias_trabajados)
    intereses_cesantias = calcular_intereses_cesantias(cesantias, dias_trabajados)
    primas = calcular_primas(salario_mensual, dias_trabajados_semestre)
    base_gravable = salario_mensual
    retencion_fuente = calcular_retencion_fuente(base_gravable)
    total_pagar = calcular_total_pagar(indemnizacion, vacaciones, cesantias, intereses_cesantias, primas, retencion_fuente)

    return indemnizacion, vacaciones, cesantias, intereses_cesantias, primas, retencion_fuente, total_pagar

def mostrar_resultados(indemnizacion, vacaciones, cesantias, intereses_cesantias, primas, retencion_fuente, total_pagar):
    print(f"Indemnización: {indemnizacion}")
    print(f"Vacaciones: {vacaciones}")
    print(f"Cesantías: {cesantias}")
    print(f"Intereses de cesantías: {intereses_cesantias}")
    print(f"Primas: {primas}")
    print(f"Retención en la fuente: {retencion_fuente}")
    print(f"Total a pagar: {total_pagar}")

if __name__ == "__main__":
    try:
        motivo_terminacion, salario_mensual, tiempo_servicio, dias_trabajados, dias_trabajados_semestre = input_datos_usuario()
        indemnizacion, vacaciones, cesantias, intereses_cesantias, primas, retencion_fuente, total_pagar = calcular_liquidacion(
            motivo_terminacion, salario_mensual, tiempo_servicio, dias_trabajados, dias_trabajados_semestre
        )
        mostrar_resultados(indemnizacion, vacaciones, cesantias, intereses_cesantias, primas, retencion_fuente, total_pagar)
    except (SalarioInvalidoError, FechaInvalidaError, ArgumentosInvalidosError, SaldoAFavorException) as e:
        print(f"Error: {e}")
