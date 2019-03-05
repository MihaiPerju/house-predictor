import pandas as pd
import numpy as np

#Importing the Learning library
from sklearn.tree import DecisionTreeRegressor

train_file = "./train.csv"
train_data = pd.read_csv(train_file)

test_file = "./test.csv"
test_data = pd.read_csv(test_file)

#convert categorical variable into dummy
train_data = pd.get_dummies(train_data)

test_data = pd.get_dummies(test_data)

# Selecting prediction target
y = train_data[["SalePrice"]]
features = [ 'OverallQual', 'YearBuilt', 'TotalBsmtSF', 'GrLivArea']

#Impute the record with the missing "TotalBsmtSF"
train_data['TotalBsmtSF'] = train_data['TotalBsmtSF'].fillna(0)
test_data['TotalBsmtSF'] = test_data['TotalBsmtSF'].fillna(0)


#Selecting the data relevant for prediction
X_train = train_data[features]

#Selecting the test data
X_test = test_data[features]

#Building the model
model = DecisionTreeRegressor(random_state=1)
model.fit(X_train, y)

predictions=model.predict(X_test)
# print(predictions)

# data = pd.DataFrame({'OverallQual': [1,2],'YearBuilt':[19,0],'TotalBsmtSF':[2,2],'GrLivArea':[22,1]});
# print(data[features])
