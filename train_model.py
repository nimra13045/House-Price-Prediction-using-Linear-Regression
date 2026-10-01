import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression


# Load dataset
data = pd.read_csv("data/house_data.csv")

# Features
X = data[
    [
        "area_sqft",
        "bedrooms",
        "bathrooms",
        "stories"
    ]
]

# Target
y = data["price_pkr"]


# Create model
model = LinearRegression()

# Train model
model.fit(X, y)


# Save trained model
joblib.dump(model, "model/house_price_model.pkl")

print("Model trained successfully!")
print("Model saved to model/house_price_model.pkl")