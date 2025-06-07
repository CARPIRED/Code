# Code

Laboratorio experimental para explorar el desarrollo de un GPT especializado en imagenología médica avanzada. El objetivo es implementar un asistente capaz de procesar estudios radiológicos, integrar metadatos clínicos y generar reportes estructurados.

Para más detalles consulte el documento [docs/medical-imaging-gpt-spec.md](docs/medical-imaging-gpt-spec.md).
El codigo incluye la clase `MedicalImagingAgent` (ver `imaging_agent.py`), que permite generar informes radiologicos a partir de hallazgos y metadatos.

## Preprocesamiento de imágenes

Para preparar un estudio antes del análisis se puede utilizar el módulo
`preprocessing.py`, que sigue la secuencia indicada en la especificación.

```python
from preprocessing import load_image, normalize, crop_foreground

data = load_image("imagen.png")
data = normalize(data)
data = crop_foreground(data)
```

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

## Configuración del API key

`MedicalAgent` puede conectarse opcionalmente con la API de OpenAI. Si no se
proporciona la clave al crear la instancia, la clase buscará las variables de
entorno `MEDICAL_AGENT_API_KEY` o `OPENAI_API_KEY`.

### Entorno local

Defina la variable antes de ejecutar la aplicación o colóquela en un archivo
`.env` que su gestor de entorno cargue automáticamente:

```bash
export OPENAI_API_KEY=sk-...
python web/app.py
```

### Entorno de producción

Durante el despliegue configure la variable `MEDICAL_AGENT_API_KEY` (o
`OPENAI_API_KEY`) en el sistema o proporcione un archivo de configuración solo
accesible para el servicio. De esta manera se evita exponer la clave en el
código fuente.
