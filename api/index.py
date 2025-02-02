from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Enable CORS

# Load student marks from a JSON file
def load_marks():
    with open("students.json", "r") as file:
        return json.load(file)

@app.route('/api', methods=['GET'])
def get_marks():
    students_marks = load_marks()  # Load data dynamically
    names = request.args.getlist('name')  # Get names from query parameters
    marks = [students_marks.get(name, None) for name in names]  # Get marks or None if not found
    return jsonify({"marks": marks})

if __name__ == "__main__":
    app.run(debug=True)
