import pandas as pd
import numpy as np
df = pd.read_csv('./advertising.csv')

data = df.to_numpy()

sales_data = data[:, 3]
max_idx = np.argmax(sales_data)
sales_max = data[max_idx, 3]

print(sales_max, max_idx)  # 27.0 175

tvs_data = data[:, 0]
average_value = np.average(tvs_data)

print(average_value)  # 147.0425

sales_counter = np.sum(sales_data >= 20)

print(sales_counter)  # 40

sales_cond = sales_data >= 15
radio_data = data[:, 1]
radio_cond = radio_data * sales_cond
radio_mean = np.sum(radio_cond) / np.sum(sales_cond)
print(radio_mean)  # 26.2


newspaper_data = data[:, 2]
newspaper_mean = newspaper_data.mean()
newspaper_cond = newspaper_data > newspaper_mean
sales_cond = sales_data * newspaper_cond
sales_sum = np.sum(sales_cond)
print(sales_sum)  # 1405.1

sales_mean = sales_data.mean()
score_sales = np.where(
    sales_data > sales_mean,
    "Good",
    np.where(sales_data < sales_mean, "Bad", "Average")
)
print(score_sales[7:10])  # ['Bad' 'Bad' 'Good']

sub_abs = abs(sales_data - sales_mean)
average_idx = np.argmin(sub_abs)
sales_average = sales_data[average_idx]
score_sales = np.where(
    sales_data > sales_average,
    "Good",
    np.where(sales_data < sales_average, "Bad", "Average")
)

print(score_sales[7:10])  # ['Bad' 'Bad' 'Good']
