"""Simple Flask interface for the MedicalImagingAgent."""

from flask import Flask, render_template, request
from imaging_agent import MedicalImagingAgent

app = Flask(__name__)
agent = MedicalImagingAgent()

@app.route('/', methods=['GET', 'POST'])
def index():
    response = None
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
        else:
            response = agent.generate_report(findings, patient_data)
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
