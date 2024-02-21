def calcular_indemnizacion_despido(salario_mensual, dias_trabajados, tiempo_servicio):
    factor_indemnizacion = min(max(tiempo_servicio, 1), 20)
    indemnizacion = (salario_mensual * dias_trabajados / 360) + factor_indemnizacion
    return indemnizacion

def calcular_indemnizacion_por_renuncia(salario_mensual, dias_trabajados, meses_contrato):
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
    retencion_fuente = base_gravable * 0.1  # una retención del 10%
    return retencion_fuente

def calcular_total_pagar(indemnizacion, vacaciones, cesantias, intereses_cesantias, primas, retencion_fuente):
    total_pagar = indemnizacion + vacaciones + cesantias + intereses_cesantias + primas - retencion_fuente
    return total_pagar

# Entrada de datos por parte del usuario
salario_mensual = float(input("Ingrese el salario mensual: "))
dias_trabajados = int(input("Ingrese la cantidad de días trabajados: "))
tiempo_servicio = int(input("Ingrese el tiempo de servicio en años: "))
meses_contrato = int(input("Ingrese la cantidad de meses del contrato: "))
dias_trabajados_semestre = int(input("Ingrese la cantidad de días trabajados en el semestre: "))

indemnizacion = calcular_indemnizacion_despido(salario_mensual, dias_trabajados, tiempo_servicio)
indemnizacion_terminacion = calcular_indemnizacion_por_renuncia(salario_mensual, dias_trabajados, meses_contrato)
vacaciones = calcular_vacaciones(salario_mensual, tiempo_servicio)
cesantias = calcular_cesantias(salario_mensual, dias_trabajados)
intereses_cesantias = calcular_intereses_cesantias(cesantias, dias_trabajados)
primas = calcular_primas(salario_mensual, dias_trabajados_semestre)

base_gravable = salario_mensual  # Ajusta la base gravable según tus necesidades
retencion_fuente = calcular_retencion_fuente(base_gravable)

total_pagar = calcular_total_pagar(indemnizacion, vacaciones, cesantias, intereses_cesantias, primas, retencion_fuente)

# Imprimir resultados
print(f"Indemnización por despido: {indemnizacion}")
print(f"Indemnización por terminación de contrato: {indemnizacion_terminacion}")
print(f"Vacaciones: {vacaciones}")
print(f"Cesantías: {cesantias}")
print(f"Intereses de cesantías: {intereses_cesantias}")
print(f"Primas: {primas}")
print(f"Retención en la fuente: {retencion_fuente}")
print(f"Total a pagar: {total_pagar}")
