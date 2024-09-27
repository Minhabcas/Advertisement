import pandas as pd
import numpy as np
import math

#1
data = pd.read_csv('Advertising.csv')
print(data.head())

#2
tv_data = data['TV']
sales_data = data['sales']
newspaper_data = data['newspaper']
radio_data = data['radio']

#3
#Hiệu Phương sai
covariance = tv_data.cov(sales_data)
covariance = newspaper_data.cov(radio_data)
print(f"Hiệp Phương sai giữa Newspaper và Radio:{covariance}")
print(f"Hiệp phương sai giữa TV và Sales: {covariance}")

#Phương sai
variance_tv = tv_data.var()
variance_sales = sales_data.var()
variance_newspaper = newspaper_data.var()
variance_radio = radio_data.var()
print(f"Phương sai của TV: {variance_tv}")
print(f"Phương sai của Sales: {variance_sales}")
print(f"Phương sai của Newspaper: {variance_newspaper}")
print(f"Phương sai của Radio: {variance_radio}")

#Hệ số tương quan Pearson
pearson_correlation = tv_data.corr(sales_data)
print(f"Hệ số tương quan Pearson giữa TV và Sales: {pearson_correlation}")
pearson_correlation = newspaper_data.corr(radio_data)
print(f"Hệ số tương quan Pearson giữa Newspaper và Radio: {pearson_correlation}")

#Góc 00
theta_radians_TV = np.arccos(pearson_correlation)
theta_degrees = np.degrees(theta_radians_TV)
print(f"Góc giữa TV và Sales (radians): {theta_radians_TV}")
print(f"Góc giữa TV và Sales (degrees): {theta_degrees}")




 