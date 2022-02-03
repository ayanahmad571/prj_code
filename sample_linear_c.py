import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import Perceptron
import matplotlib.pyplot as plt

data = pd.read_csv('https://raw.githubusercontent.com/LearnPythonWithRune/MachineLearningWithPython/main/files/weather.csv', parse_dates=True, index_col=0)
print(data.head())
print(data.isnull().sum())

dataset = data[['Humidity3pm', 'Pressure3pm', 'RainTomorrow']].dropna()
X = dataset[['Humidity3pm', 'Pressure3pm']]
y = dataset['RainTomorrow']
y = np.array([0 if value == 'No' else 1 for value in y])
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
clf = Perceptron(random_state=0)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print(accuracy_score(y_test, y_pred))
print(sum(y == 0)/len(y))

fig, ax = plt.subplots()
X_data = X.to_numpy()
y_all = clf.predict(X_data)
ax.scatter(x=X_data[:,0], y=X_data[:,1], c=y_all, alpha=.25)
plt.show()
fig, ax = plt.subplots()
ax.scatter(x=X_data[:,0], y=X_data[:,1], c=y, alpha=.25)
plt.show()