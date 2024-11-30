from flask import Flask, render_template
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ekf')
def ekf():
    return render_template('ekf_simulation.html')

@app.route('/ukf')
def ukf():
    return render_template('ukf_simulation.html')




if __name__ == '__main__':
    app.run(debug=True)