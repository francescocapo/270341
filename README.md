# Machine Learning project: CUSTOMER SEGMENTATION 
## By Martina Serandrei, Giulia Macis, Francesco Capo

### Introduction
The aim of our project is to analyze the data provided by a very big company about the customers of its Brazilian subsidiary, to be able to build an email campaign based on a customers' clustering.
The clustering is performed following the RFM analysis, where R stands for Recency, F for Rrequency and M for Monetary value.
In order to accomplish our mission, we followed these steps:
- Exploratory Data Analysis (EDA) with the visualization of data.
- Implemented four clustering algorithms, and only after a deep analysis of their performance and outcomes we presented the clusters.

Furthermore, we decided to plot some of the features which might be interesting to correlate:
One of these could be the number of orders derived from each Brazilian federative state with a barplot; so, we counted (with `.size()`) how many order per state by applying the pandas `.groupby()` function. **foto customer state-count** What we can notice is a large majority of orders coming from São Paulo state, which is the most important state by population and this could be a reason for it. 


## Methods
In order to complete in the best way our analisys we choose to use four different algorithms, Kmeans Clustering, Hierarchical clustering, Gaussian Mixture Model and Birch model.
We choose these clustering technique since each of these method provides a different  output and so we will have a different segmentation regarding the customers.

- Our first implementation was the **Kmeans**, this method groups similar kinds of datapoints in form of clusters according to the similarity between them.
 It uses the elbow method technique in order to find the optimal amount of cluster, this will find the right amount of centroids that will determine our clusters
 We chose to use it since it is able to understand, in a pretty efficent way, the different part of the customer segmantation in order to maximize the profits


- Hierarchical clustering groups data based on their similarities, here we need firstly to identify the optiaml amount of clusters, we can do so by plotting a dendrogram, which shows the hierarchical relationship between clusters.
  This method will also first find the best amount of cluster and them is going to segment the data


- The Gaussian Mixture Model works by assuming that all data points are generated from a mixture of a finite number of Gaussian distributions with unknown parameters.
    It is helpful when we represent a smaller population preference, customers, in respect of the overall population preference, total customers.


- Birch model (Balanced Iterative Reducing and Clustering using Hierarchies), is very useful because it helps reducing the computational time by creating a tree structure and assigning each data point to the most relevant cluster. 
  It is very convinient since in most case it requiers only one scan of the database, this will improve our memory and time consumption, but still giving us a good interpretation.


Is worth to note that in order to compute and plot our clusters we needed to import some libraries as:

    pandas as pd
    matplotlib.pyplot as plt
    seaborn as sns
    scipy.cluster.hierarchy as sch

  Furthermore, from this librabry we imported some specif function for instance:
  - from numpy import where, unique | ???
  - from sklearn.preprocessing import StandardScaler | we need it to standarzied our variables
  - from sklearn.cluster import KMeans, AgglomerativeClustering, Birch | we need it to calculate this clusters
  - from sklearn.mixture import GaussianMixture | it was needed to compute the Gaussian Mixture
  - from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score | it computes the metrics results
  - from IPython.display import display | ???

### Experimental design
#### EDA:
In order to deeply understand the dataset before actually working on it, we operated an analysis starting from the visualization of the data and some data exploration.
For example, we firstly printed the shape of the dataset, and then we used the `describe()` function to compute some useful descriptive statistics which summarize the central tendency, dispersion, and shape of a dataset’s distribution, excluding NaN values.
    
Dataset shape:(13801, 26)
We have a quite big dataset with many variables as well, so it might be useful to discard the information we don't need for the clustering.
As a matter of fact we created a new dataframe, called csdv_df_new, excluding _product_category_name_, _product_name_length_ e _product_description_length_.

Successively, we proceeded with the data cleaning:
- We checked for null values and duplicate rows and we deleted them. We found out that the dataset is quite clean since it has only a few duplicate rows and zero null values.

Then we started analyzing the variables of the dataset by plotting the correlation among the numerical variables through a **correlation heatmap**, which is useful to understand which variables are related to each other and the strength of their relationship. In the cells of the heatmap, the strength of the relationship is indicated with positive values if there is a positive correlation, and negative values if a negative correlation is present.
In our case we saw that basically our numeric variables are the ones related to the payments or the orders; in particular, we can see that there is a high correlation between _payment_value_ and the _price_, while we have  a negative correlation, with _order_item_id_ and the _price_ since _order_item_id_ stands for the number of items for each order, and the _price_ means the price of each item. 
It is easily understandable from the description that the number of items that we place in an order cannot influence in any way the price of an item. We can make the same reasoning for the relationship between _order_item_id_ and _freight_value_.
**foto heatmap**

Furthermore, we decided to plot some of the features which might be interesting to correlate. One of these could be the number of orders derived from each Brazilian federative state with a barplot; so, we counted (with `.size()`) how many order per state by applying the pandas `.groupby()` function. **foto customer state-count** What we can notice is a large majority of orders coming from São Paulo state, which is the most important state by population and this could be a reason for it, whereas Acre state

The clustering has been performed following the RFM analysis.
Moreover, to seek accuracy we implemented four clustering algorithms, and only after a deep analysis of their performance and outcomes we presented the clusters.
Throughout the code we used python built-in functions, so we needed to import the packages used.
In order to deeply understand the dataset before actually working on it, we operated an analysis starting from the visualization of the data and some data exploration.
For example, we firstly printed the shape of the dataset, and then we used the `describe()` function to compute some useful descriptive statistics which summarize the central tendency, dispersion, and shape of a dataset’s distribution, excluding NaN values.

Dataset shape:(13801, 26)
We have a quite big dataset with many variables as well, so it might be useful to discard the information we don't need for the clustering.
As a matter of fact we created a new dataframe, called csdv_df_new, excluding _product_category_name_, _product_name_length_ e _product_description_length_.

Successively, we proceeded with the data cleaning:
- We checked for null values and duplicate rows and we deleted them. We found out that the dataset is quite clean since it has only a few duplicate rows and zero null values.

Then we started analyzing the variables of the dataset by plotting the correlation among the numerical variables through a **correlation heatmap**, which is useful to understand which variables are related to each other and the strength of their relationship. In the cells of the heatmap, the strength of the relationship is indicated with positive values if there is a positive correlation, and negative values if a negative correlation is present.
In our case we saw that basically our numeric variables are the ones related to the payments or the orders; in particular, we can see that there is a high correlation between _payment_value_ and the _price_, while we have  a negative correlation, with _order_item_id_ and the _price_ since _order_item_id_ stands for the number of items for each order, and the _price_ means the price of each item. 
It is easily understandable from the description that the number of items that we place in an order cannot influence in any way the price of an item. We can make the same reasoning for the relationship between _order_item_id_ and _freight_value_.
![heatmap.png](images%2Fheatmap.png)

Furthermore, we decided to plot some of the features which might be interesting to correlate. One of these could be the number of orders derived from each Brazilian federative state with a barplot; so, we counted (with `.size()`) how many order per state by applying the pandas `.groupby()` function. ![customer_state_count.png](images%2Fcustomer_state_count.png) What we can notice is a large majority of orders coming from São Paulo state, which is the most important state by population and this could be a reason for it.
Another intriguing relationship to investigate was the how many orders are paid using a certain payment type per state. And as we can see from the graph the most used payment type in general is the credit card and then boleto is the second most used method to pay. ![barplot_payment.png](images%2Fbarplot_payment.png)
The last aspect we wanted to look into was the number of order made in each month. The result revealed that from April to August the subsidiary got a lot of orders with a peak in May, whereas in the rest of the months they were very few; in September, October and November there were no orders at all. This information helped us a lot during the analysis because(?)

A fundamental step for the initial analysis was studying and visualizing the ouliers to understand if they needed to be removed from the dataset or they could bring a relevant importance to the customers' segmentation. We decided to handle the question by using a pairplot, thanks to which we could detect them in _payment_value_ most of all, but seeingt them, made us realize that if even they could have unusual characteristics, they remained customers to be considered because maybe they could have been included in the email campaign.
Finally, before diving deeply into the data manipulation, we performed an encoding for categorical variable into quantitative variables, so that they could be taken into consideration in the analysis. We smply used the pandas function `.get_dummies()`.

As we said before our segmentation follows the RFM analysis:
It is a behavior-based technique used to segment customers by examining their transaction history focusing on the following:
o	Recency: how recently a customer has purchased.
It is expressed in days,  meaning that high recency corresponds to orders made a long time ago. 
o	Frequency: how often they purchase 
o	Monetary value: how much the customer spends 
It is the most suitable technique since it helps to identify customers who are more likely to respond to promotions, which is the ultimate goal of the target email campaign.
For example, Customers who recently made a purchase will still have the product on their minds, so they are more likely to buy again especially if they are pulled by the marketing campaign.
Additionally, first-time customers, with a low frequency may be good targets for the marketing campaign to convert them into more frequent customers.
To carry out the techniques we first computed all the metrics and then we stored them in a dataframe called score_dataframe.
Since the scales of the 3 variables are substantially different We considered it necessary to standardize the results in order to work with uniform values.
At this point having all the data we needed we started implementing the clustering methods.

![elbowmethod.png](images%2Felbowmethod.png)

### Results 
After implementing all the clustering methods we carried out an overall analysis of the outcomes obtained and of the performance of the algorithms.

We visualized the clusters through 3D scatter plots but we also computed empirical results about the characteristics of the clusters obtained.
Comparing both we can describe the clusters:
For example we notice that the ones obtained with kmeans, hierarchical and birch algorithm  are quite similar to each other (despite the order of their lebels)
For example the clusters obtained in the birch model and k means model are very similar to each others. 
The first one represents inactive customers that have made a few purchases typically a long time ago.
The second one represents active customers that have made purchases many times, also recently, and have spent a fair amount on their purchases.
The third cluster represents new customers that have purchased very recently (they have in fact the lowest recency value) and have not spent much, because they haven’t made frequent transactions yet.
Finally, the fourth cluster represents usual/ loyal customers, they shop really frequently and spend a large amount of money on their orders (they have the highest monetary value). 
The hierarchical clusters are pretty similar to the kmeans and birch clusters as well, The slight differences are that:
In the hierarchical clusters the inactive customers have a lower recency and a lower frequency, 
the active/usual customers  have a lower monetary value and higher recency and 
the new customers have a higher recency and lower frequency.

The Gaussian method instead returns different clusters,
As a matter of fact cluster 4 corresponds to the union of the kmeans clusters number 4 and two , meaning that there is no distinction between Active/ medium- spender customers and loyal/high-spender customers. Additionally Three really similar clusters are created, all three contains customers with a high recency, low frequency low monetary value making them not useful for our ultimate goal.

The inappropriateness of this method can be proven by the scores that quantify the performance of the algorithms.

We decided to calculate 3 of these scores:
1. The silhouette score: 

    It measures how similar a value is to its own cluster (cohesion) compared to other clusters (separation). The score ranges from −1 to +1, where a high value indicates that the datapoint is well matched to its own cluster and a low value indicates poorly matched to its cluster.
![silhouette.png](images%2Fsilhouette.png)
2. Calinski and Harabasz score:

   It measures the sum of between-cluster dispersion and of within-cluster dispersion.
   The higher the value the better the clusters.
   ![calinski harabasz.png](images%2Fcalinski%20harabasz.png)
3. Davies-Bouldin score.

    The measure is the average similarity measure of each cluster with its most similar cluster, where similarity is the ratio of within-cluster distances to between-cluster distances.This means that, clusters which are farther apart and less dispersed will result in a better score.
The meaning value is zero, so the lower the score the better the clusters.
From the scores it emerges that the best algorithm is k means and the worst is gaussian mixture model, as we already deduced by the visual representations of the clusters.
      ![davis bouldin.png](images%2Fdavis%20bouldin.png)

### Conclusion
After the detailed analysis we concluded that the best model is the k means algorithm, therefore the segments obtained are the following four:
-inactive customers
-active customers
-new customers
-loyal customers