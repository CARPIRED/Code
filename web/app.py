from flask import Flask, render_template, request
from medical_agent import MedicalAgent

app = Flask(__name__)
agent = MedicalAgent()

@app.route('/', methods=['GET', 'POST'])
def index():
    response = None
    if request.method == 'POST':
        query = request.form.get('query', '')
        response = agent.get_differential_diagnosis(query)
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
