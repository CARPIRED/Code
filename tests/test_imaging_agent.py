"""Unit tests for MedicalImagingAgent using the built-in unittest framework."""

import unittest

from imaging_agent import MedicalImagingAgent


class TestMedicalImagingAgent(unittest.TestCase):
    """Tests covering core imaging agent functionality."""

    def setUp(self) -> None:
        self.agent = MedicalImagingAgent()

    def test_classify_image_default_normal(self) -> None:
        result = self.agent.classify_image("scan.png", {"Age": 45})
        self.assertEqual(result, {"label": "normal", "confidence": 0.85})


    def test_classify_image_detects_fracture(self) -> None:
        result = self.agent.classify_image("fracture_scan.png", {"Age": 30})
        self.assertEqual(result["label"], "fracture")
        self.assertTrue(0.9 < result["confidence"] <= 1.0)


    def test_segment_image_returns_mock_mask(self) -> None:
        result = self.agent.segment_image("scan.png")
        self.assertIn("mask", result)
        self.assertIsInstance(result["mask"], list)


    def test_detect_anomalies_mock_result(self) -> None:
        result = self.agent.detect_anomalies("scan.png")
        self.assertEqual(result["boxes"][0]["label"], "lesion")


if __name__ == "__main__":
    unittest.main()

