# Code

Laboratorio experimental para probar funciones de GitHub Copilot Codex con proyectos de automatización médica y educativa. Este repositorio explora la creación de un GPT especializado en tareas médicas.

Para más detalles consulte el documento [docs/medical-gpt-spec.md](docs/medical-gpt-spec.md).

## Web Demo

Se incluye una aplicación Flask sencilla para probar el agente desde un navegador.

### Requisitos
- Python 3.10+
- `flask`
- `openai` (opcional, para usar la API)

### Ejecución
```bash
pip install flask openai
python web/app.py
```
Luego visite `http://localhost:5000` y envíe los síntomas para obtener una respuesta.
