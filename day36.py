# Import Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Create Dataset
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [20, 35, 50, 65, 80, 85, 90, 95]
}

# Create DataFrame
df = pd.DataFrame(data)

# Print Dataset
print("Dataset:")
print(df)

# Features and Labels
X = df[["Hours"]]
y = df["Marks"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Make Predictions
predictions = model.predict(X_test)

# Compare Actual vs Predicted
result = pd.DataFrame({
    "Actual": y_test,
    "Predicted": predictions
})

print("\nActual vs Predicted:")
print(result)

# Accuracy Score
score = model.score(X_test, y_test)
print("\nAccuracy:", score)
