def calificar_respuestas(respuestas_candidato, respuestas_correctas, puntos_por_pregunta=5, puntaje_minimo=80):
    """
    Compara las respuestas del candidato con las respuestas oficiales.

    :param respuestas_candidato: Lista de letras seleccionadas por el candidato. Ej: ['B', 'C', 'B', ...]
    :param respuestas_correctas: Lista de letras correctas según la plantilla. Ej: ['B', 'B', 'B', ...]
    :param puntos_por_pregunta: Cuántos puntos vale cada respuesta correcta.
    :param puntaje_minimo: Puntaje necesario para aprobar.
    :return: Un diccionario con resultado, puntaje y respuestas detalladas.
    """
    respuestas_evaluadas = []
    total_puntaje = 0

    for i, (marcada, correcta) in enumerate(zip(respuestas_candidato, respuestas_correctas), start=1):
        es_correcta = marcada == correcta
        if es_correcta:
            total_puntaje += puntos_por_pregunta

        respuestas_evaluadas.append({
            "numero_pregunta": i,
            "respuesta_marcada": marcada,
            "respuesta_correcta": correcta,
            "es_correcta": es_correcta
        })

    aprobado = total_puntaje >= puntaje_minimo

    return {
        "puntaje": total_puntaje,
        "aprobado": aprobado,
        "respuestas": respuestas_evaluadas
    }
