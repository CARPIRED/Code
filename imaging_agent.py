"""Advanced medical imaging agent placeholder."""

from typing import Any, Dict

from medical_agent import MedicalAgent


class MedicalImagingAgent(MedicalAgent):
    """Agent specialized in clinical imaging tasks."""

    REPORT_PROMPT = (
        "Eres un radiólogo clínico con 20 años de experiencia. "
        "A continuación recibirás hallazgos radiológicos y datos del paciente. "
        "Tu tarea es generar un informe médico estructurado y profesional. "
        "Utiliza un lenguaje clínico preciso y evita interpretaciones no sustentadas."
    )

    def generate_report(self, findings: str, patient_data: Dict[str, Any]) -> str:
        """Generate a structured radiology report."""
        details = ", ".join(f"{k}: {v}" for k, v in patient_data.items())
        prompt = f"{self.REPORT_PROMPT}\n\nHallazgos: {findings}. Datos del paciente: {details}."
        return self._chat(prompt)
