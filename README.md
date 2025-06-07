# Code

Laboratorio experimental para explorar el desarrollo de un GPT especializado en imagenología médica avanzada. El objetivo es implementar un asistente capaz de procesar estudios radiológicos, integrar metadatos clínicos y generar reportes estructurados.

Para más detalles consulte el documento [docs/medical-imaging-gpt-spec.md](docs/medical-imaging-gpt-spec.md).
El codigo incluye la clase `MedicalImagingAgent` (ver `imaging_agent.py`), que permite generar informes radiologicos a partir de hallazgos y metadatos.

## Web Demo

Se incluye una aplicación Flask sencilla para probar el agente desde un navegador.
La interfaz permite ingresar un estudio de imagen, seleccionar la tarea deseada
(clasificación, segmentación, detección, multi‑task o generación de reporte) y
proporcionar datos básicos del paciente.

### Requisitos
- Python 3.10+
- `flask`
- `openai` (opcional, para usar la API)

### Ejecución
```bash
pip install flask openai
python web/app.py
```
Luego visite `http://localhost:5000` e introduzca los datos solicitados para obtener
resultados de ejemplo en la tarea seleccionada.
