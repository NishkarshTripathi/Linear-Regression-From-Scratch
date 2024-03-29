# Importing dependencies
import matplotlib.pyplot as plt 
import pandas as pd
from sklearn import preprocessing

# Loading dataset
dataset = pd.read_csv('/PATH/Salary_Data.csv')
X = dataset[['YearsExperience']].values
y = dataset['Salary'].values

costcheck = []
p1 = 0
p2 = 0
learning_rate = 0.03
epochs = 500

# Calculate Hypothesis h(x)
def hypothesis(x):
  hx = p1 + (p2 * x)
  return hx

# Calculate Cost
def cost_function():
  squared_diff = 0
  for i in range(len(X)):
    squared_diff = squared_diff + (hypothesis(X[i]) - y[i])
    
  cost = (1 / (2 * len(X))) * (squared_diff**2)
  return cost

# Applying Gradient Descent
def gradient_descent():
  global p1, p2, costcheck
  for i in range(epochs):
    temp0 = p1 - learning_rate * derivative_1()
    temp1 = p2 - learning_rate * derivative_2()
    p1 = temp0
    p2 = temp1
    costcheck.append(cost_function())
    
    
# Calculating Derivatives
def derivative_1():
  d1 = 0
  for i in range(len(X)):
    d1 = d1 + (hypothesis(X[i]) - y[i])
    
  d1 = (1 / len(X)) * d1
  return d1

def derivative_2():
  d2 = 0
  for i in range(len(X)):
    d2 = d2 + ((hypothesis(X[i]) - y[i]) * X[i])
    
  d2 = (1 / len(X)) * d2
  return d2

gradient_descent()

# Plotting the cost
xaxis = []
for i in range(500):
  xaxis.append(i) 
plt.plot(xaxis, costcheck)
#plt.show

# Plotting the best fit line with data
kkk = []
for i in range(len(dataset[['YearsExperience']].values)):
  kkk.append(hypothesis(dataset[['YearsExperience']].values[i]))

plt.scatter(dataset[['YearsExperience']].values, dataset[['Salary']].values, color='blue')  
plt.scatter(dataset[['YearsExperience']].values, kkk, color='red')
#plt.show()
