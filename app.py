from flask import Flask, render_template, request
import pandas as pd
import joblib


app = Flask(__name__)


# Load trained model
model = joblib.load("model/house_price_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Get values from HTML form
    area = float(request.form["area"])
    bedrooms = int(request.form["bedrooms"])
    bathrooms = int(request.form["bathrooms"])
    stories = int(request.form["stories"])

    # Create DataFrame
    new_house = pd.DataFrame({
        "area_sqft": [area],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "stories": [stories]
    })

    # Predict price
    predicted_price = model.predict(new_house)[0]

    return render_template(
        "index.html",
        prediction=f"{predicted_price:,.0f}"
    )


if __name__ == "__main__":
    app.run(debug=True)