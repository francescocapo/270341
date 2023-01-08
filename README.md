# Machine Learning project: CUSTOMER SEGMENTATION 
## By Martina Serandrei, Giulia Macis, Francesco Capo

### Introduction

The aim of our job is to analyze the data provided by a very big company about the customers of its Brazilian subsidiary, to be able to build an email campaign based on a customers' clustering.
The clustering have been performed following the RFM analysis.
Moreover to seek accuracy we implemented four clustering algorithms, and only after a deep analysis of their performance and outcomes we presented the clusters.
Throughout the code we used python built-in functions, so we needed to import the packages used.
We started our analysis with the visualization of the data and some data exploration, in order to deeply understand the dataset we were provided with before actually working on it.
For example, we firstly printed the shape of the dataset and them we used the describe() function to compute some useful descriptive statistics which summarize the central tendency, dispersion, and shape of a dataset’s distribution, excluding NaN values.
Dataset shape:(13801, 26)
We have a quite big dataset with many variables as well, so it might be useful to discard the information we don't need for the clustering.
As a matter of fact we created a new dataframe, called csdv_df_new, excluding product_category_name, product_name_length e product_description_length.
We proceeded with the data cleaning:
Checking for null values and duplicate rows and deleting them. We find out that the dataset is quite clean since it has only a few duplicate rows and zero null values.

Then we started analyzing the variables of the dataset, 



- Recency. 
  - How recent was the customer's last purchase? Customers who recently made a purchase will still have the product on their mind and are more likely to purchase or use the product again. Businesses often measure recency in days. But, depending on the product, they may measure it in years, weeks or even hours.
- Frequency.
  - How often did this customer make a purchase in a given period? Customers who purchased once are often are more likely to purchase again. Additionally, first time customers may be good targets for follow-up advertising to convert them into more frequent customers.
- Monetary. 
  - How much money did the customer spend in a given period? Customers who spend a lot of money are more likely to spend money in the future and have a high value to a business.