# Code

Laboratorio experimental para explorar el desarrollo de un GPT especializado en imagenología médica avanzada. El objetivo es implementar un asistente capaz de procesar estudios radiológicos, integrar metadatos clínicos y generar reportes estructurados.

El proyecto se guía por el [Prompt Maestro](docs/prompt-maestro.md), que describe las tareas de clasificación, segmentación y generación de informes.
La clase principal es `MedicalImagingAgent` (ver `imaging_agent.py`), utilizada desde la aplicación web.
La especificación detallada se encuentra en [docs/medical-imaging-gpt-spec.md](docs/medical-imaging-gpt-spec.md).

## Web Demo

Se incluye una aplicación Flask sencilla para probar el agente desde un navegador.
La interfaz permite ingresar los hallazgos radiológicos y los datos básicos del paciente
para generar un informe estructurado utilizando `MedicalImagingAgent`.

### Requisitos
- Python 3.10+
- Dependencias listadas en `requirements.txt`

### Ejecución
```bash
pip install -r requirements.txt
python web/app.py
```
Luego visite `http://localhost:5000` e introduzca los datos solicitados para obtener
un informe radiológico de ejemplo. Configure la variable de entorno `OPENAI_API_KEY`
si desea usar la API de OpenAI.

Las pruebas unitarias se encuentran en `tests/` y se ejecutan con `pytest`.
