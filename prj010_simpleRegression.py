import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('studyTime.csv')
hours  = df.Hours.values.reshape(-1, 1)
scores = df.Score.values
model = LinearRegression().fit(hours, scores)

def predict_score(X): return model.predict([[X]])

predicted_score = predict_score(9.5)
print(f"Predicted score for 9.5 hours: {predicted_score}")