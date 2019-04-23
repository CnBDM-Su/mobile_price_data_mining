# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 12:10:12 2019

@author: suyu
"""
import pandas as pd
df = pd.read_csv('C:/Users/64161/Desktop/master.csv',error_bad_lines=False)
data = df.groupby('country')['suicides/100k pop'].mean()

new = pd.Series.to_frame(data)
sort = new.sort_values(by=['suicides/100k pop'])
print(sort)
