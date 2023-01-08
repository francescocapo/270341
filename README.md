# Machine Learning project: CUSTOMER SEGMENTATION 
## By Martina Serandrei, Giulia Macis, Francesco Capo

### Introduction

The aim of our job is to analyze the data provided by a very big company about the customers of its Brazilian subsidiary, to be able to build an email campaign based on a customers' clustering.
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
**foto heatmap**

Furthermore, we decided to plot some of the features which might be interesting to correlate. One of these could be the number of orders derived from each Brazilian federative state with a barplot; so, we counted (with `.size()`) how many order per state by applying the pandas `.groupby()` function. **foto customer state-count** What we can notice is a large majority of orders coming from São Paulo state, which is the most important state by population and this could be a reason for it, whereas Acre state




- Recency. 
  - How recent was the customer's last purchase? Customers who recently made a purchase will still have the product on their mind and are more likely to purchase or use the product again. Businesses often measure recency in days. But, depending on the product, they may measure it in years, weeks or even hours.
- Frequency.
  - How often did this customer make a purchase in a given period? Customers who purchased once are often are more likely to purchase again. Additionally, first time customers may be good targets for follow-up advertising to convert them into more frequent customers.
- Monetary. 
  - How much money did the customer spend in a given period? Customers who spend a lot of money are more likely to spend money in the future and have a high value to a business.