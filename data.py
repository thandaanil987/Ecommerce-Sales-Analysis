'''Project Title: E-Commerce Sales Data Analysis using Python

Tools Used: Python, Pandas, NumPy, Matplotlib, Seaborn

Objective: To analyze e-commerce sales data to understand business trends, customer behavior, and generate actionable insights.#importing libraries'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#load dataset
data = pd.read_csv('sample_ecommerce_data.csv')
data.head()

#data cleaning
data.info()
data.isnull().sum()

# Convert date column
data['event_time'] = pd.to_datetime(data['event_time'])

#feature engineering
data['hour'] = data['event_time'].dt.hour
data['day'] = data['event_time'].dt.day
data['month'] = data['event_time'].dt.month

#exploratory data analysis

# Most viewed categories
plt.figure(figsize=(10,5))
data['category_code'].value_counts().head(10).plot(kind='bar')
plt.title('Top 10 Categories')
plt.xlabel('Category')
plt.ylabel('Number of Views')
plt.show()

# Hourly Activity
plt.figure(figsize=(10,5))
data['hour'].value_counts().sort_index().plot(kind='line')
plt.title('User Activity by Hour')
plt.xlabel('Hour')
plt.ylabel('Activity Count')
plt.grid(True)
plt.show()