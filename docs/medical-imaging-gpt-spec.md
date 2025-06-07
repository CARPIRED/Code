# Medical Imaging GPT Specification

This document outlines the goal and design of a specialized GPT agent focused on advanced clinical imaging. The project centers around processing radiological studies and associated metadata to assist clinicians in diagnosis and reporting.

## Purpose

Develop an AI model capable of interpreting medical images (X-ray, CT, MRI, Ultrasound) with support for complex pattern recognition, segmentation, and structured report generation. The agent integrates clinical metadata to provide reproducible and explainable results.

## Core Tasks

- **Classification** of clinically relevant findings such as fractures, nodules, or effusions.
- **Segmentation** of anatomical structures or lesions.
- **Detection** of anomalies in 2D/3D studies.
- **Report Generation** with professional clinical language.
- **Multi‑task** workflows combining the above capabilities.

## Input Format

Images may be supplied as DICOM, NIfTI, or PNG/JPEG files. Metadata is provided in CSV, JSON, or FHIR format and can include `Age`, `Sex`, `Modality`, `Diagnosis`, and other clinical markers. Manual annotations are supported via NIfTI masks or JSON bounding boxes.

## Model Configuration

The agent can be configured with architectures such as `resnet50`, `densenet121`, `unet3d`, `swin_unetr`, or `r2gen_gpt`. Input size, channel count, normalization method, data augmentation, loss function, optimizer, and evaluation metrics are all customizable.

Example preprocessing sequence using MONAI:

```
[
  "LoadImaged",
  "AddChanneld",
  "Spacingd",
  "Orientationd",
  "NormalizeIntensityd",
  "CropForegroundd"
]
```

## Prompt Template for Report Generation

```
Eres un radiólogo clínico con 20 años de experiencia. A continuación recibirás hallazgos radiológicos y datos del paciente. Tu tarea es generar un informe médico estructurado y profesional. Utiliza un lenguaje clínico preciso y evita interpretaciones no sustentadas.
```

The expected output is a JSON object containing key findings and a succinct impression.

## Implementation Notes

- Validate consistency between image resolution and selected architecture.
- Include explainability tools (Grad-CAM, SHAP, LIME).
- Ensure compliance with HIPAA, GDPR, and local privacy regulations.
- Provide confidence scores and saliency masks when applicable.
