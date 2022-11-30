a) Frequent pattern mining using Apriori algorithm :

   https://colab.research.google.com/drive/1_-XCfA-0Nx1SoYFAvDrfHMqnkEjmkA03?usp=sharing
   
   Implementing the Apriori algorithm, using market basket optimization csv dataset which contains a list of transactions with the grocery items which are purchased together. After performing the necessary transformations, the algorithm is trained using the transactions in the dataset. Then the rules are generated from the list based on the values of confidence, support, and lift. Hence we are able to get the top 10 rules from the dataset generated using apriori algorithm.

   Frequent pattern mining using FP Growth algorithm :

   https://colab.research.google.com/drive/1J9HJ-Usu_PBV92sco-QXtShbmENJCW1b?usp=sharing
   
   Implementing the FP growth algorithm, using the market basket optimization csv dataset which contains a list of transactions with the grocery items which are purchased together. The necessary transformations and EDA are performed on the dataset. The most frequent items are chosen from the dataset and FP growth algorithm is applied on it, and association rules are created. This shows the values of confidence, lift and support of the list of items in the rules. Hence we are able to obtain the most frequent association of items.
   

b) Databricks to demonstrate frequent pattern mining :

   https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/2469856715563369/4118559153341084/7971224237730433/latest.html
   
   In this databricks notebook, I have performed matket basket analysis using the Apriori algorithm and FP growth. Data is obtained from different sources, and are merged together. Then the necessary transformations are done on the datset. EDA is performed on the dataset to understand and visualize the data. I have tried using python and apriori algorithm for creating the association rules. A basket is created with 100 most frequently ordered items, and hence a subset of the data is used to create association rules using apriori algorithm. Thus we obtain the top association rules. I've tried generating top association rules with FP growth algorithm using SQL and Scala.
    
   

