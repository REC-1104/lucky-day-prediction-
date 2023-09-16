import time
print("""

🔮 LUCKY DAY PREDICTION MODEL 🔮

Welcome, fellow adventurer, to the realm of the unknown! Prepare yourself to uncover the secrets of your fortunate days with our cutting-edge Lucky Day Prediction Model. Powered by AI and sprinkled with a dash of magic, this model is designed to decipher the cosmic patterns and unveil the days when luck will be on your side.

""");time.sleep(10)
"""

IMPORTING LIBRARIES

"""

# Importing required libraries.

print('Importing libraries.....\n')
import numpy as np
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.feature_selection import SelectKBest,f_regression
import plotly.express as px
import warnings
warnings.simplefilter("ignore")
print('Imported libraries successfully.....program starting.......\n')

"""### LOADING THE DATASET"""

# Loading the dataset obtained by mystical sources.

df = pd.read_csv('lib\luckyDay.csv')
print(df.head());time.sleep(5)
print()
print('Loaded data successfully\n');time.sleep(1)

print('Applying some modifications to the dataset....\n');time.sleep(2)

# Converting the ['Birthdate'] dtype into int.

df['Birthdate'] = df['Birthdate'].str.replace('-', '').astype('int')

# Converting ['Zodiac Sign'] dtype into int.

print('Mapping the zodiac signs\n');time.sleep(2)
zodiac_mapping = {zodiac: index for index, zodiac in enumerate(df['Zodiac Sign'].unique())}
df['Zodiac Sign'] = df['Zodiac Sign'].map(zodiac_mapping).astype(int)+1;
for zodiac, number in zodiac_mapping.items():
    print(zodiac,":",number+1);time.sleep(1);
print()

# Converting ['Lucky Charms','Rituals Followed'] dtypes into int.

YN_mapping = {YN: index for index, YN in enumerate(df['Lucky Charms'].unique())}

df['Lucky Charms'] = df['Lucky Charms'].map(YN_mapping).astype(int)+1

df['Rituals Followed'] = df['Rituals Followed'].map(YN_mapping).astype(int)+1

# Yes :2
# No : 1

print('Data after modifications\n');time.sleep(1)
print(df.head());time.sleep(5)
print()

print('EDA of the dataset...\n');time.sleep(2)
"""### EDA"""

# Shape of the dataset.

print('Shape of dataset is',df.shape,'\n');time.sleep(1)

# Info about the dataset.

print('Info about dataset\n');time.sleep(1)
print(df.info());time.sleep(5)
print()
nan = df.isnull().sum().sum()
print('Number of NaN is',nan,'\n');time.sleep(1)

# Central tendency and dispersion of the dataset.

print('Central tendency and dispersion can be infer from\n');time.sleep(1)
print(df.describe());time.sleep(5)
print()

"""

### DATA VISUALIZATION

"""

# cols = ['Zodiac Sign', 'Lucky Number', 'Lucky Charms', 'Rituals Followed']
# print("REDIRECTING TO NEW PAGE");time.sleep(2)
# sn.pairplot(df[cols]) 

# """The above graph gives me relationships between every two columns in the dataset."""

# print("REDIRECTING TO NEW PAGE....");time.sleep(2)
# fig = px.scatter_3d(df, x='Lucky Number', y='Zodiac Sign', z='Lucky Day (%)', color='Lucky Charms')
# fig.update_layout(title='Scatter Plot', autosize=False , width=800, height=600)
# fig.update_traces(marker_size = 4)
# fig.show()


# """The above 3d plot shows data distribution based on ['Zodiac Sign','Lucky Number','Lucky Day (%)','Lucky Charms']."""

# print("REDIRECTING TO NEW PAGE....");time.sleep(2)
# colors = LinearSegmentedColormap.from_list('blackg',["black", "g"], N=256)
# fig, ax = plt.subplots(figsize=(10,5))
# sn.heatmap(df.corr(), annot=True, cmap = colors, fmt=".1g", cbar=True);
# plt.title('Correlation Matrix')
# plt.show()

print("""
      
To see the data visualisation of dataset, please refer to the images in 'lib' directory

From the graphs obtained we can get following observations :
- Rituals followed and zodiac are two variables which have maximum co linearity.
- The frequency of people in dataset having lucky charm is more than that of people not having it.

""");time.sleep(10)

"""APPLYING THE MULTIPLE LINEAR REGRESSION MODEL"""

# Segrigating the required variables and target feature.

print("Splitting the dataset....\n");time.sleep(2)
required_features=[]
target = "Lucky Day (%)"
for feature in df.columns :
    if feature != target :
         required_features.append(feature)
required_features

"""

Selecting variables which are highly relevant for our model to reduce overfitting. SelectKBest by Sci-Kit learn is the algorithm for the purpose.

"""
"""

Also splitting the datset into test and train.

"""
print('Selecting best variables for the model....\n');time.sleep(2)
X=df[required_features]
y=df[target]
k=4
X_new = SelectKBest(f_regression, k=k).fit_transform(X, y)
selected_features = X.columns[SelectKBest(f_regression, k=k).fit(X, y).get_support()]
print('Selected best features are',selected_features,'\n');time.sleep(3)
train_X, test_X, train_y, test_y = train_test_split(X_new, y,test_size=0.3,random_state=47)

"""

Using Multiple LinearRegression on the training data.

"""
print('Training the data on the model....\n');time.sleep(2)
reg = linear_model.LinearRegression()
reg.fit(train_X,train_y)

"""

Slopes of optimum 4 dimensional curve.

"""

print('Slopes obtained are',reg.coef_,'\n');time.sleep(1.5)

"""

Intercept of optimum 4 dimensional curve.

"""

print("Intercept obtained is",reg.intercept_,'\n');time.sleep(1)

"""

Predicting the %age of lucky days for testing data using the Multiple Linear Regression model.

"""

print("Predicting output of testing data....\n");time.sleep(2)
predicted_y = reg.predict(test_X)
print("Predicted output of testing data",predicted_y,'\n');time.sleep(1.5)

"""

### CALCULATING ERROR

"""

print('Mean Absolute Error:', metrics.mean_absolute_error(test_y,predicted_y),'\n');time.sleep(1)
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(test_y,predicted_y)),'\n');time.sleep(1)

"""### CALCULATING R^2"""

print("The value of R^2 is",reg.score(test_X,test_y),'\n');time.sleep(1)

print(""">The amount of GOOD LUCK coming your way depends on your WILLINGNESS TO ACT.<

GOOD LUCK 😊

You can find the web-app made to lucky day prediction using the information obtained from the above analysis at https://lucky-day-prediction.vercel.app/
""")

