import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression

#generating sample data
X,y=make_regression(n_samples=1000, n_features=15,noise=0.1,random_state=42)

#splitting the data into training and testing sets
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

#creating and fitting the random forest regression
rf_regressor = RandomForestRegressor(n_estimators=100,random_state=42)
rf_regressor.fit(X_train,y_train)

#maing predictions on the test set
pred=rf_regressor.predict(X_test)

#calculating R^2 score (coefficient of determination)
r2_score=rf_regressor.score(X_test,y_test)
print('R^2 Score: ',r2_score)

#plotting the actual vs predicted values
plt.figure(figsize=(10,6))
plt.scatter(y_test,pred,color='blue',label='Actual vs Prediction')
plt.plot(y_test,y_test,color='red',label='Perfect Prediction')
plt.title('Actual vs Predicted values')
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.legend()
plt.show()