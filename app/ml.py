import pandas as pd
from sklearn.tree import DecisionTreeClassifier


def train_demand_model():
    data = pd.DataFrame([
        {"location": "Jurong", "food_type": "Rice", "requests": 15, "demand": "High"},
        {"location": "Jurong", "food_type": "Bread", "requests": 10, "demand": "Medium"},
        {"location": "Woodlands", "food_type": "Rice", "requests": 7, "demand": "Medium"},
        {"location": "Woodlands", "food_type": "Canned Food", "requests": 3, "demand": "Low"},
        {"location": "Tampines", "food_type": "Rice", "requests": 12, "demand": "High"},
        {"location": "Tampines", "food_type": "Bread", "requests": 5, "demand": "Low"},
        {"location": "Bedok", "food_type": "Instant Noodles", "requests": 8, "demand": "Medium"},
        {"location": "Bedok", "food_type": "Canned Food", "requests": 4, "demand": "Low"},
        {"location": "Yishun", "food_type": "Rice", "requests": 13, "demand": "High"},
        {"location": "Yishun", "food_type": "Bread", "requests": 6, "demand": "Medium"},
    ])

    X = pd.get_dummies(data[["location", "food_type", "requests"]], columns=["location", "food_type"])
    y = data["demand"]

    model = DecisionTreeClassifier(random_state=42)
    model.fit(X, y)

    return model, X.columns


model, feature_columns = train_demand_model()


def predict_demand(location: str, food_type: str, requests: int):
    input_df = pd.DataFrame([{
        "location": location,
        "food_type": food_type,
        "requests": requests
    }])

    input_encoded = pd.get_dummies(input_df, columns=["location", "food_type"])

    for col in feature_columns:
        if col not in input_encoded:
            input_encoded[col] = 0

    input_encoded = input_encoded[feature_columns]

    prediction = model.predict(input_encoded)[0]
    return prediction