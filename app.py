from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('web.html')

@app.route('/run-python-code', methods=['POST'])
def run_python_code():
    subprocess.run(["python", "i192178_minahil.py"])
    return "Script executed successfully!"

if __name__ == '__main__':
    app.run(debug=True)
