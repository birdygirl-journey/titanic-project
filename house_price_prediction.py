import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset
df = pd.read_csv('house_prices.csv')
print(df.head())

# Split data into features (X) and target (y)
X = df[['Area (sqft)', 'Bedrooms', 'Bathrooms', 'Stories', 'Parking']]
y = df['Price ($)']

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate model
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Try a sample prediction
new_house = [[2500, 3, 2, 2, 1]]
predicted_price = model.predict(new_house)
print(f"Predicted price for new house: ${predicted_price[0]:.2f}")
