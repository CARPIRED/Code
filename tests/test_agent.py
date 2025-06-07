import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
import imaging_agent


def test_generate_report():
    agent = imaging_agent.MedicalImagingAgent()
    out = agent.generate_report("hallazgo", {"Edad": 50, "Sexo": "M"})
    assert isinstance(out, str)


def test_classification_stub():
    agent = imaging_agent.MedicalImagingAgent()
    result = agent.classify_image("img.png")
    assert "Classified" in result
