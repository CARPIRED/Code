"""Simple Flask interface for the MedicalImagingAgent."""

from flask import Flask, render_template, request
from werkzeug.datastructures import FileStorage
from imaging_agent import MedicalImagingAgent

app = Flask(__name__)
agent = MedicalImagingAgent()

@app.route('/', methods=['GET', 'POST'])
def index():
    response = None
    if request.method == 'POST':
        findings = request.form.get('findings', '')
        age = request.form.get('age', '')
        sex = request.form.get('sex', '')
        image: FileStorage | None = request.files.get('image')
        patient_data = {"Edad": age, "Sexo": sex}
        if image and image.filename:
            # In a full implementation, the image would be processed.
            # Here we simply echo the filename for demonstration.
            patient_data["Imagen"] = image.filename
        response = agent.generate_report(findings, patient_data)
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
