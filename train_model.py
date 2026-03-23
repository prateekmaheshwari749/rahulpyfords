import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# Load dataset
df = pd.read_csv("mobile_addiction_dataset.csv")

X = df.drop("AddictionLevel", axis=1)
y = df["AddictionLevel"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("addiction_model.pkl", "wb"))

print("Model Trained & Saved!")