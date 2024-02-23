from datetime import datetime

def calcular_indemnizacion_despido(salario_mensual, dias_trabajados, tiempo_servicio):
    factor_indemnizacion = min(max(tiempo_servicio, 1), 20)
    indemnizacion = (salario_mensual * dias_trabajados / 360) + factor_indemnizacion
    return indemnizacion

def calcular_indemnizacion_por_renuncia(salario_mensual, dias_trabajados,):
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

# Entrada de datos
motivo_terminacion = input("Ingrese el motivo de terminación del contrato (despido o renuncia): ")
salario_mensual = float(input("Ingrese el salario mensual: "))
fecha_inicio_labores = input("Ingrese la fecha de inicio de labores (formato: DD/MM/AAAA): ")
fecha_ultimas_vacaciones = input("Ingrese la fecha de las últimas vacaciones (formato: DD/MM/AAAA): ")
dias_vacaciones_acumulados = int(input("Ingrese los días de vacaciones acumulados: "))

# Convertir las fechas ingresadas a objetos datetime
fecha_inicio_labores = datetime.strptime(fecha_inicio_labores, "%d/%m/%Y")
fecha_ultimas_vacaciones = datetime.strptime(fecha_ultimas_vacaciones, "%d/%m/%Y")

# Calcula tiempo de servicio en años
tiempo_servicio = (datetime.now() - fecha_inicio_labores).days // 365

# Calcula días trabajados desde la última fecha de vacaciones
dias_trabajados = (datetime.now() - fecha_ultimas_vacaciones).days

# Calcular días trabajados en el semestre (suponiendo que las vacaciones fueron en el semestre actual)
dias_trabajados_semestre = (datetime.now() - fecha_ultimas_vacaciones).days

if motivo_terminacion.lower() == 'despido':
    indemnizacion = calcular_indemnizacion_despido(salario_mensual, dias_trabajados, tiempo_servicio)
elif motivo_terminacion.lower() == 'renuncia':
    indemnizacion = calcular_indemnizacion_por_renuncia(salario_mensual, dias_trabajados, tiempo_servicio)
else:
    print("Motivo de terminación no válido. Debe ser 'despido' o 'renuncia'.")
    exit()

vacaciones = calcular_vacaciones(salario_mensual, tiempo_servicio)
cesantias = calcular_cesantias(salario_mensual, dias_trabajados)
intereses_cesantias = calcular_intereses_cesantias(cesantias, dias_trabajados)
primas = calcular_primas(salario_mensual, dias_trabajados_semestre)

base_gravable = salario_mensual  
retencion_fuente = calcular_retencion_fuente(base_gravable)

total_pagar = calcular_total_pagar(indemnizacion, vacaciones, cesantias, intereses_cesantias, primas, retencion_fuente)

print(f"Indemnización: {indemnizacion}")
print(f"Vacaciones: {vacaciones}")
print(f"Cesantías: {cesantias}")
print(f"Intereses de cesantías: {intereses_cesantias}")
print(f"Primas: {primas}")
print(f"Retención en la fuente: {retencion_fuente}")
print(f"Total a pagar: {total_pagar}")

