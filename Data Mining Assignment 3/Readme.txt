This folder contains all files related to Assignment 3 - Questions 1 to 3

The datasets used are within 'datasets'.

Question 1 - EDA : This folder contains the google colab notebook for the Exploratory Data Analysis I have performed on a Zomato dataset.
The dataset consists of numerous restaurants in various countries, along with its address, location, cuisines offered, ratings, average cost for two, has online delivery etc. The detailed explanation of the dataset is available on the colab notebook. In EDA we have visualized the  countries with most restaurants on Zomato, their ratings, how ratings and cost are related, what are the most common cuisines on Zomato and so on.

For EDA I have used various visualization tool such as d3.js(this visual can be viewed only while running the notebook), plotly, matplotlib and seaborn - for different kind of visuals such as interactive visuals, maps, word cloud, bar, pie and donut charts.  

To view the visuals properly, please visit : https://colab.research.google.com/drive/1Qa22R___XVRKtazD2FBwD2ox2PKzgRAh?usp=sharing
(The visuals are not coming up properly on GitHub, especially plotly map - choropleth and D3.js)

Question 2 - Auto EDA : This folder contains the google colab notebooks for my Auto EDA experiments. I have used Pandas profiling and sweetviz for Auto EDA. I have used a dataset which has patient records such as their age, gender, smoking, alcohol, systolic and diastolic pressure and presence and absence of cardiovascular disease. The detailed explanation of the dataset is avalilable in the colab notebook, along with removing outliers and anomalies, some transformations in the dataset(converting age from days to years for readability), and then using Pandas profiling for EDA. 
To try another auto EDA tool, I tried the sweetviz tool, with titanic data set, which contains information of various titanic passengers such as their age, gender etc. and if they survived the titanic crash.

To view the code and the EDA report with visualizations, please visit : 
pandas profiling colab : https://colab.research.google.com/drive/1xJcbKv2gq_9Kp_sgddtq9XGpNPR_hOxv?usp=sharing (This is the mail Auto EDA notebook, with detailed explanation, cleansing and transformations of dataset)
sweetviz colab : https://colab.research.google.com/drive/1Exu81par76e-uiIBQHS8REYw0k-MNb8i?usp=sharing (This is just a basic experiment to try another Auto EDA Tool)

Question 3 - Apache beam : This folder contains the google colab notebook used to work on Apache beam. The dataset consists of shopping data - customers who shop for various IT products such as monitors, keyboards and so on. I have used core transform, pardo transform and composite transform to categorize these customers based on products purchased, and determine the returning and non-returning customers. This information can be further used for marketing and sales promotions. 

To view the code and output(output files are generated locally on colab on execution), please visit:
https://colab.research.google.com/drive/1NlkxX6iumHLJfgEQqQJzx5a1laJSBtAY?usp=sharing




