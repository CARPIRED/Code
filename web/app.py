"""Simple Flask interface for the MedicalImagingAgent with PDF export."""

from flask import Flask, render_template, request, send_file
import os
from imaging_agent import MedicalImagingAgent


def create_pdf(text: str, path: str) -> None:
    """Generate a minimal PDF file with the given text."""
    # Adapted from docs/pdfs/generate_sample_pdf.py
    escaped = text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")

    pdf_objects = []
    pdf_objects.append(b"1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n")
    pdf_objects.append(b"2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n")
    pdf_objects.append(
        b"3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>\nendobj\n"
    )

    content_stream = f"BT\n/F1 12 Tf\n50 700 Td\n({escaped}) Tj\nET".encode("ascii")
    pdf_objects.append(
        b"4 0 obj\n<< /Length " + str(len(content_stream)).encode("ascii") + b" >>\nstream\n" + content_stream + b"\nendstream\nendobj\n"
    )

    pdf_objects.append(b"5 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\nendobj\n")

    pdf_header = b"%PDF-1.1\n"

    offsets = []
    current_offset = len(pdf_header)
    for obj in pdf_objects:
        offsets.append(current_offset)
        current_offset += len(obj)

    xref = b"xref\n0 " + str(len(pdf_objects) + 1).encode("ascii") + b"\n0000000000 65535 f \n"
    for off in offsets:
        xref += ("%010d" % off).encode("ascii") + b" 00000 n \n"

    xref += b"trailer\n<< /Root 1 0 R /Size " + str(len(pdf_objects) + 1).encode("ascii") + b" >>\nstartxref\n" + str(current_offset).encode("ascii") + b"\n%%EOF\n"

    with open(path, "wb") as f:
        f.write(pdf_header)
        for obj in pdf_objects:
            f.write(obj)
        f.write(xref)

app = Flask(__name__)
agent = MedicalImagingAgent()

@app.route('/', methods=['GET', 'POST'])
def index():
    response = None
    pdf_available = False
    if request.method == 'POST':
        findings = request.form.get('findings', '')
        image_path = request.form.get('image_path', '')
        age = request.form.get('age', '')
        sex = request.form.get('sex', '')
        task = request.form.get('task', 'report')
        patient_data = {"Edad": age, "Sexo": sex}
        if task == 'classification':
            response = agent.classify_image(image_path, patient_data)
        elif task == 'segmentation':
            response = agent.segment_image(image_path)
        elif task == 'detection':
            response = agent.detect_anomalies(image_path)
        elif task == 'multi':
            response = agent.multi_task_analysis(image_path, findings, patient_data)
            create_pdf(response.get('report', ''), os.path.join(app.root_path, 'report.pdf'))
            pdf_available = True
        else:
            response = agent.generate_report(findings, patient_data)
            create_pdf(response, os.path.join(app.root_path, 'report.pdf'))
            pdf_available = True
    return render_template('index.html', response=response, pdf_available=pdf_available)


@app.route('/download')
def download_pdf():
    """Send the generated PDF to the user."""
    pdf_path = os.path.join(app.root_path, 'report.pdf')
    if os.path.exists(pdf_path):
        return send_file(pdf_path, as_attachment=True)
    return "No PDF generated", 404

if __name__ == '__main__':
    app.run(debug=True)
