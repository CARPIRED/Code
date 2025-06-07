"""Unit tests for MedicalImagingAgent using pytest."""

import pytest

from imaging_agent import MedicalImagingAgent


@pytest.fixture()
def agent():
    return MedicalImagingAgent()


def test_classify_image_default_normal(agent):
    result = agent.classify_image("scan.png", {"Age": 45})
    assert result == {"label": "normal", "confidence": 0.85}


def test_classify_image_detects_fracture(agent):
    result = agent.classify_image("fracture_scan.png", {"Age": 30})
    assert result["label"] == "fracture"
    assert 0.9 < result["confidence"] <= 1.0


def test_segment_image_returns_mock_mask(agent):
    result = agent.segment_image("scan.png")
    assert "mask" in result
    assert isinstance(result["mask"], list)


def test_detect_anomalies_mock_result(agent):
    result = agent.detect_anomalies("scan.png")
    assert result["boxes"][0]["label"] == "lesion"
