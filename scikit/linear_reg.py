import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression

#generating synthetic dataset
X,y=make_regression(n_samples=100,n_features=1,noise=10,random_state=42)

#splitting the dataset into training and testing sets
X_train, X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

#Creating Linear Regression model
linear_regressor = LinearRegression()

#training the model
linear_regressor.fit(X_train,y_train)

#making predictions on the testing set /////// you can only predict y values using x, since y is dependent on x.... and x is independent.
y_pred = linear_regressor.predict(X_test)

#visualising the results
plt.scatter(X_test,y_test, color='blue', label='Actual')
plt.plot(X_test,y_pred,color='red',label='Predicted')
plt.title('Linear Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()