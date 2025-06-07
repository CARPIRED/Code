"""Simple Flask interface for the MedicalImagingAgent with upload support."""

from flask import (
    Flask,
    render_template,
    request,
    send_from_directory,
    url_for,
)
from werkzeug.utils import secure_filename
import os
from imaging_agent import MedicalImagingAgent

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
agent = MedicalImagingAgent()


@app.route("/uploads/<filename>")
def uploaded_file(filename: str):
    """Serve uploaded files."""
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

@app.route('/', methods=['GET', 'POST'])
def index():
    response = None
    image_url = None
    if request.method == 'POST':
        findings = request.form.get('findings', '')
        age = request.form.get('age', '')
        sex = request.form.get('sex', '')
        task = request.form.get('task', 'report')

        # Handle uploaded file
        image_file = request.files.get('image_file')
        image_path = request.form.get('image_path', '')
        if image_file and image_file.filename:
            filename = secure_filename(image_file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image_file.save(file_path)
            image_path = file_path
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                image_url = url_for('uploaded_file', filename=filename)

        patient_data = {"Edad": age, "Sexo": sex}
        if task == 'classification':
            response = agent.classify_image(image_path, patient_data)
        elif task == 'segmentation':
            response = agent.segment_image(image_path)
        elif task == 'detection':
            response = agent.detect_anomalies(image_path)
        elif task == 'multi':
            response = agent.multi_task_analysis(image_path, findings, patient_data)
        else:
            response = agent.generate_report(findings, patient_data)
    return render_template('index.html', response=response, image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)
