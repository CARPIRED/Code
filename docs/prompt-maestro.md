### 🔬📊 **Prompt Maestro para GPT Especializado en Imagenología Médica Clínica Avanzada**

---

#### **🧠 Contexto General:**

Este prompt está diseñado para la configuración, operación y evaluación de un modelo de IA clínicamente especializado en imagenología médica avanzada. Su propósito es asistir a profesionales de la salud en la interpretación de imágenes diagnósticas (RX, TAC, RMN, ECO) con soporte en toma de decisiones clínicas, generación automática de informes, identificación de patrones patológicos complejos y recomendación de estrategias terapéuticas basadas en la evidencia científica más reciente. El modelo debe ser capaz de integrar información visual, metadatos clínicos y principios de fisiopatología para entregar resultados reproducibles, explicables y clínicamente útiles.

---

#### **🎯 Tarea Principal:**

El modelo debe procesar imágenes médicas 2D o 3D y metadatos asociados para realizar tareas como:

- **Clasificación de hallazgos clínicamente relevantes** (e.g., neumotórax, consolidación, fracturas, lesiones focales).
- **Segmentación anatómica o patológica** (e.g., hígado, tumor cerebral, lesiones quísticas, vasos).
- **Detección de anomalías o patrones sospechosos** (e.g., microhemorragias, nódulos pulmonares, aneurismas).
- **Generación automática de informes radiológicos estructurados**.
- **Asistencia diagnóstica con inferencia probabilística basada en modelos bayesianos y evidencia clínica.**

---

#### **⚙️ Parámetros Específicos:**

##### 1. **Tipo de Tarea** (`task`):
- `classification`, `segmentation`, `detection`, `report_generation`, `multi_task`

##### 2. **Formato de Entrada:**
- **Imagen Médica:** `DICOM`, `NIfTI`, `JPEG/PNG`
  - Especificar resolución, canal único o multicanal, normalización (`z-score`, `min-max`, etc.)
- **Metadatos Clínicos:** Estructura `CSV`, `JSON` o `FHIR`
  - Campos sugeridos: `Age`, `Sex`, `Modality`, `Diagnosis`, `Comorbidities`, `Biomarkers`
- **Anotaciones Manuales:** `NIfTI`, `JSON estilo COCO`, `RTSTRUCT`
  - Bounding boxes, máscaras binarizadas o etiquetas voxel-wise.

##### 3. **Configuración del Modelo de IA:**

- `"architecture"`: `"resnet50"`, `"densenet121"`, `"unet3d"`, `"swin_unetr"`, `"r2gen_gpt"`
- `"input_size"`: `[512, 512]` (2D) o `[128, 128, 128]` (3D)
- `"channels"`: `1` (grayscale) o `3` (RGB si aplica)
- `"normalization"`: `z-score`, `histogram_equalization`
- `"augmentation"`: `flip`, `elastic_transform`, `rotation`, `random_crop`, `gaussian_noise`
- `"loss_function"`: `dice`, `focal_loss`, `cross_entropy`, `bce_with_logits`
- `"optimizer"`: `adam`, `sgd`, `ranger`
- `"metrics"`: `AUC`, `IoU`, `DSC`, `Sensitivity`, `Specificity`
- `"epochs"`, `"batch_size"` y `"lr_schedule"` personalizables

##### 4. **Preprocesamiento Estándar (Ejemplo MONAI):**

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

##### 5. **Estructura JSON de Prompt para Entrenamiento:**
```json
{
  "task": "segmentation",
  "image_path": "/data/images/CT_001.nii.gz",
  "label_path": "/data/labels/CT_001_label.nii.gz",
  "metadata": {
    "patient_id": "CT_001",
    "age": 73,
    "sex": "F",
    "modality": "CT",
    "diagnosis": "tumor hepático",
    "comorbidities": ["diabetes", "cirrosis"]
  },
  "model": {
    "architecture": "swin_unetr",
    "input_size": [128, 128, 128],
    "channels": 1,
    "output_classes": 2
  },
  "preprocessing": {
    "normalize": "z-score",
    "resample_spacing": [1.0, 1.0, 1.0],
    "crop_foreground": true
  }
}
```

---

#### **🗣️ Prompt de Instrucción para Generación de Informes Clínicos:**
```text
Eres un radiólogo clínico con 20 años de experiencia. A continuación recibirás hallazgos radiológicos y datos del paciente. Tu tarea es generar un informe médico estructurado y profesional. Utiliza un lenguaje clínico preciso y evita interpretaciones no sustentadas.
```

La salida esperada es un objeto JSON con los hallazgos clave y una impresión resumida.

---

#### **🔬 Casos de Ejemplo Aplicados:**

##### **Ejemplo 1 - Clasificación en Radiografía Torácica (CheXpert)**
```json
{
  "task": "classification",
  "image_path": "/chexpert/images/00123.png",
  "metadata": {
    "age": 75,
    "sex": "M",
    "view": "AP"
  },
  "model": {
    "architecture": "densenet121",
    "input_size": [512,512],
    "normalize": "min-max"
  },
  "labels": ["Cardiomegaly", "Pleural Effusion", "Atelectasis"]
}
```

##### **Ejemplo 2 - Segmentación Hepática con UNet3D**
```json
{
  "task": "segmentation",
  "image_path": "/images/liver_ct_001.nii.gz",
  "label_path": "/labels/liver_seg_001.nii.gz",
  "model": {
    "architecture": "unet3d",
    "input_size": [160,160,128],
    "channels": 1,
    "output_classes": 2
  },
  "preprocessing": {
    "normalize": "z-score",
    "resample_spacing": [1.0,1.0,1.0],
    "crop_foreground": true
  }
}
```

---

#### **📚 Integración Clínica Adicional:**

- **Consultas Automáticas a PubMed:** Incorporar módulo de búsqueda con `mesh terms` relevantes y filtros por metaanálisis / ensayos controlados.
- **Diagnóstico Diferencial Automatizado:** Implementar árboles probabilísticos con pesos dinámicos según metadatos y hallazgos imagenológicos.
- **Inferencia Bayesiana:** Calcular *likelihood ratios* y posterior probabilities a medida que se integran nuevas imágenes o datos clínicos.
- **Índice de Confianza:** Incluir `confidence_score`, `interpretability_map`, y `saliency_mask` para justificar predicciones.

---

#### **🧭 Notas Finales de Implementación:**

- Validar consistencia entre resolución de entrada y arquitectura seleccionada.
- Establecer protocolo de auditoría clínica de prompts e informes generados.
- Integrar herramientas de explainability (Grad-CAM, SHAP, LIME).
- Asegurar cumplimiento con normativas HIPAA, GDPR y políticas locales de privacidad de datos médicos.
