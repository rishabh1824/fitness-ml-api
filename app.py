from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Gym ML API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    weight = float(data["weight"])
    height = float(data["height"]) / 100
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return jsonify({"bmi": round(bmi, 2), "category": category})

# only for local dev; Gunicorn uses `app` directly
if __name__ == "__main__":
    app.run(debug=True)
