from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load ML model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    weight = data['weight']
    height = data['height']
    age = data['age']
    activity = data['activity']

    bmi = weight / ((height / 100) ** 2)
    
    # Dummy category (replace with model logic)
    if bmi < 18.5:
        category = "Underweight"
        recommendation = "Eat more, gain strength."
    elif 18.5 <= bmi < 25:
        category = "Normal"
        recommendation = "Maintain your current lifestyle!"
    elif 25 <= bmi < 30:
        category = "Overweight"
        recommendation = "Focus on cardio & low-carb diet."
    else:
        category = "Obese"
        recommendation = "Consult a fitness coach & dietician."

    # If using ML model: prediction = model.predict(...)
    return jsonify({
        'bmi': bmi,
        'category': category,
        'recommendation': recommendation
    })

if __name__ == '__main__':
    app.run(debug=True)
