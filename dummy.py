# Dependencies:
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
import seaborn as sns
import numpy as np

df = pd.read_csv("risk_factors_cervical_cancer.csv")
df = df.replace('?', np.NaN)
categorical_columns = []

quantitative_columns = []

for column in df.columns:
    # print(column, df[column], pd.api.types.is_float_dtype(df[column]) )
    print(' - ', column, pd.api.types.is_any_real_numeric_dtype(df[column]))
    print(df[column])
    # if pd.api.types.is_float_dtype(df[column]):
    #     quantitative_columns.append(column)
    # else:
    #     categorical_columns.append(column)