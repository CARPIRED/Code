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
        age = request.form.get('age', '')
        sex = request.form.get('sex', '')
        patient_data = {"Edad": age, "Sexo": sex}
        response = agent.generate_report(findings, patient_data)
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
