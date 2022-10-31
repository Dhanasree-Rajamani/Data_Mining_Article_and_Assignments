Question 1:

I) Normalization and Data Portability Techniques

II) Feature Subset Selection

Google colab notebook URL for I and II(Normalization, Data Portability and Feature Subset selection):
https://colab.research.google.com/drive/1uH046NxiK0DZRnBWlyT1mOYgfjFAWaO8#scrollTo=dS51kh3A0MBp&uniqifier=2

I) For normalization, The dataset used is a cardio dataset, in which target variable is presence or absence of cardiovascular disease in a patient based on various attributes such as age, weight, smoking, alcohol, cholesterol etc.(more features explained in colab). The techniques I've tried for normalization are Scaling, Z-score and Feature Clipping. 

I) For data portability I have tried various techniques such as Label encoding, One-hot encoding, Quantile bucketing - equi width, equi depth.
Here I have used multiple datasets such as 
 - Diabetes dataset - (for women), which contains information such as number of pregnancies, glucose, BMI, Insulin, blood pressure, skin thickness, age, diabetes predigree function and the target variable is whether or not the person has diabetes.
 - Car price prediction dataset - which contains various information such as car name, fuel type, door number, drive wheel, engine size, city mpg, etc.(Described more within the colab) and the price of the car is the target variable.
 - Cardio dataset mentioned above

II) For feature subset selection I have used various techniques such as Feature selection by removing constant values(Filter method), Forward selection and Backward elimination (Wrapper method) 
The datasets used here are:
 - Starbucks customer dataset - which has various information about the customer such as - gender, age, status, visit no, etc.  and the target label is whether the customer is loyal or not loyal.
 - Diabetes dataset mentioned above
 - Car price prediction dataset mentioned above


III) MICE for data imputation

I have used MICE for data imputation, for 2 datasets here.
First one is a sample datset with age, experience and salary. Missing values here are imputed using MICE.
Second one is a proper dataset, containing Age, height, weight and BMI. Missing values in all columns are imputed using MICE.

Google colab notebook URL:
https://colab.research.google.com/drive/1x3TgTGmyoCGVwNyt3U3TXMOz0IGb9x9A#scrollTo=dofO54K1XWx-

IV) PCA and SVD

PCA:

I have tried 2 implementation techniques for PCA for dimensionality reduction. The dataset I have taken consists of feature such as diameter, weight, green, blue and red. The target variable is determining if the given fruit is a Grapefruit or Orange. I have implemented various steps in PCA, and done dimensionality reduction and the target label is determined with the features given by PCA.

Google colab notebook URL:
https://colab.research.google.com/drive/1UJWMs26_XX2G-lCCqozOmTnRbn9K76u3#scrollTo=7DRrElbpQ5OV

SVD:

I have used SVD for dimensionality reduction in the fruit recognition dataset. The dataset consists of 5 features which are reduced to 2 which then helps to identify the label - Orange/Grapefruit. I have implemented various steps in SVD in the google colab notebook.

Google colab notebook URL:
https://colab.research.google.com/drive/1E5pBUX_ZASvMqbeE-XLaaNLw2dUhvygi#scrollTo=EnPJv-wEIUD0

Question 2:

I have used FeatureWiz and Auto ViML(which uses SULOV, XGBoost) here.

I have used FeatureWiz on a diabetes dataset(for women), which consists of features such as number of pregnancies, glucoed, blood pressure, skin thickness, insulin, BMI, diabetes pedigree function, age. Featurewiz does feature engineering and reduces the features required to determine diabets(target) from 8 to 2.

Google colab notebook URL:
https://colab.research.google.com/drive/1XnefAkzV-0UvccIfa_3F97qdOLqTY2a7#scrollTo=Y_24FLi0C7q2

I have tried AutoViML with 2 datsets(classification and regression).

The regression dataset, is a car price prediction dataset which consists of car_ID, symboling, CarName, fueltype, enginelocation, wheelbase, carlength, carwidth, carheight, enginetype, cylindernumber, enginesize, fuelsystem, citympg, price, etc.(more features are explained in the colab). Here SULOV has been used to remove highly corelated features and XGBoost is used for feature selection and model training. Suitable models are evaluated to finalize the best model for the datset, the regression metrics are caluclated and important features to determine the target variable are identified. 

Google colab notebook URL:
https://colab.research.google.com/drive/1c-KfOSuklisXC8oIvu85gIDZ82FK7sXb#scrollTo=Z05Q2FJfFkoh

The second is a cardio dataset, in which target variable is presence or absence of cardiovascular disease in a patient based on various attributes such as age, weight, smoking, alcohol, cholesterol etc.(more features explained in colab). Auto ViML evaluated suitable models and identifies the best model for the dataset. It also calculates model accuracy, precision, fetaure importance etc.

Google colab notebook URL:
https://colab.research.google.com/drive/1cvefKl68BUyza1hxoIysXFZtGyvWmSfK#scrollTo=aveHX2513LvG


Question 3:

This link contains an end-to-end ML example. I have tried various ML models such as Random Forest, Decision tree and Logistic regression and the best model has been evaluated. The dataset with which the ML model is used is a diabetes dataset(for women), which contains information such as number of pregnancies, glucose, BMI, Insulin, blood pressure, skin thickness, age, diabetes predigree function and the target variable is whether or not the person has diabetes. I have also explored the data to understand the data, check for nulls and missing values. And data preparation has been done to fit the data in the format required for the logistic regression algorithm.

Databricks Notebook URL:
https://community.cloud.databricks.com/?o=2469856715563369#notebook/4099372178060647/command/1947713007899086

I have also added a copy of all these files in the github folder here.
