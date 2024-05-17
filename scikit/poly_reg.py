import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

#generating synthetic dataset
X=np.random.rand(100,1)*10
y=0.5* X**2 - 2*X + np.random.randn(100,1)*5 #Quadratic function

#splitting the dataset into training and testing set
X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.2,random_state=42)

#creating polynomial regression model
degree=2 #degree of the polynomial
poly_reg=make_pipeline(PolynomialFeatures(degree),LinearRegression())

#training the model
poly_reg.fit(X_train,y_train)

#making predictions on the testing set
y_pred=poly_reg.predict(X_test)

#sorting the test values for better visualisation
sorted_zip=sorted(zip(X_test,y_pred))
X_test_sorted,y_pred_sorted=zip(*sorted_zip)

#visualizing the results
plt.scatter(X_test,y_test,color='blue',label='Actual')
plt.plot(X_test_sorted,y_pred_sorted,color='red',label='Predicted')
plt.title(f'Polynomial Regression (Degree {degree})')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()