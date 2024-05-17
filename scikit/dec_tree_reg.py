import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.datasets import make_regression

#generating synthetic dataset
X,y=make_regression(n_samples=100,n_features=1,noise=10, random_state=42)

#splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2,random_state=42)

#creating decision tree regressor model
decision_tree_regressor=DecisionTreeRegressor(random_state=42)

#training the model
decision_tree_regressor.fit(X_train,y_train)

y_pred = decision_tree_regressor.predict(X_test)

plt.scatter(X_test,y_test,color='blue',label='Actual')
plt.scatter(X_test,y_pred,color='red',label='Predicted')
plt.title('Decision tree regression')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()