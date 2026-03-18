# Importing required modules
from flask import Flask, render_template
from your_blueprint import your_blueprint

# Create the Flask app
app = Flask(__name__)

# Registering blueprints
app.register_blueprint(your_blueprint)

# Template rendering route
@app.route('/')
def index():
    return render_template('index.html')