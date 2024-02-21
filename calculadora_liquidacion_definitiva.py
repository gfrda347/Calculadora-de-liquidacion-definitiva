def calcular_valores(motivo, salario_basico, fecha_inicio, fecha_ultimas_vacaciones, dias_vacaciones):
    try:
        if motivo == "renuncia":
            indemnizacion = 0
        else:
            indemnizacion = salario_basico / 2

        intereses_cesantias = salario_basico * 0.12 / 12 * 6 
        vacaciones = (salario_basico / 30) * dias_vacaciones
        cesantias = salario_basico / 12 * 6 
        prima = salario_basico / 12 * 2

        total_pagar = indemnizacion + intereses_cesantias + vacaciones + cesantias + prima 

        retencion_fuente = total_pagar * 0.1 

        neto_recibir = total_pagar - retencion_fuente

        return indemnizacion, vacaciones, cesantias, prima, intereses_cesantias, retencion_fuente, total_pagar, neto_recibir

    except ValueError:
        raise ValueError("Error: Ingrese un valor numérico para el salario básico y días de vacaciones.")
    except Exception as e:
        raise Exception(f"Error inesperado: {e}")
