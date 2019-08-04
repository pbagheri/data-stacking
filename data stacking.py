# -*- coding: utf-8 -*-
"""
Henry Tse 
2019-06-18 
Created with the purpose to V2C the data for 2007 Media Village
"""

import pandas as pd
#import numpy as np

# Rename filename as appropriate
df_raw = pd.read_csv('C:/Users/Payam/Dropbox/2007/Tableau data/2007-Media Brand Equity 2019 - Wave 1-Completes - OOF - trimmed for Tableau-data.csv', encoding = "ISO-8859-1")
love_var_names = pd.read_csv('C:/Users/Payam/Dropbox/2007/Tableau data/brand-love-varnames.csv')
general_var_names = pd.read_csv('C:/Users/Payam/Dropbox/2007/Tableau data/general-var-names.csv')
satament_time_varnames = pd.read_csv('C:/Users/Payam/Dropbox/2007/Tableau data/statement_time_varnames.csv')

thrive = satament_time_varnames[['var_name','var_name_with_brand','timing_var','timing_var_with_brand']][0:100]
social = satament_time_varnames[['var_name','var_name_with_brand','timing_var','timing_var_with_brand']][100:200]
culture = satament_time_varnames[['var_name','var_name_with_brand','timing_var','timing_var_with_brand']][200:300]
emotion = satament_time_varnames[['var_name','var_name_with_brand','timing_var','timing_var_with_brand']][300:400]
interest = satament_time_varnames[['var_name','var_name_with_brand','timing_var','timing_var_with_brand']][400:500]
differen = satament_time_varnames[['var_name','var_name_with_brand','timing_var','timing_var_with_brand']][500:600]


love_vars = list(love_var_names.var_name)
love_brands = list(love_var_names.brand_names)
love_name_conversion = dict(zip(love_vars,love_brands))

state_vars = list(satament_time_varnames.var_name)
state_brands = list(satament_time_varnames.var_name_with_brand)
state_name_conversion = dict(zip(state_vars,state_brands))

time_vars = list(satament_time_varnames.timing_var)
time_brands = list(satament_time_varnames.timing_var_with_brand)
time_name_conversion = dict(zip(time_vars,time_brands))

df_raw.rename(columns = love_name_conversion, inplace=True)
df_raw.rename(columns = state_name_conversion, inplace=True)
df_raw.rename(columns = time_name_conversion, inplace=True)


# This can be updated later. Regular non-v2c data.
df_base = df_raw[list(general_var_names.var_name)] 

set_1 = list(love_var_names.brand_names) # Declare more variables based on the set of v2c variables as needed
# The actual stacking
df_1 = df_raw[set_1].stack(dropna=False)
df_1 = pd.Series.to_frame(df_1) # Stacking provides series, so converting series to dataframe
df_1 = df_1.rename(columns={0: 'brand_love'}) # Renaming the v2c label





set_2_1 = list(thrive.var_name_with_brand) # Declare more variables based on the set of v2c variables as needed
# The actual stacking
df_2_1 = df_raw[set_2_1].stack(dropna=True)
df_2_1 = pd.Series.to_frame(df_2_1) # Stacking provides series, so converting series to dataframe
df_2_1 = df_2_1.rename(columns={0: 'response_thrive'}) # Renaming the v2c label

set_2_2 = list(social.var_name_with_brand) # Declare more variables based on the set of v2c variables as needed
# The actual stacking
df_2_2 = df_raw[set_2_2].stack(dropna=True)
df_2_2 = pd.Series.to_frame(df_2_2) # Stacking provides series, so converting series to dataframe
df_2_2 = df_2_2.rename(columns={0: 'response_social'}) # Renaming the v2c label

set_2_3 = list(culture.var_name_with_brand) # Declare more variables based on the set of v2c variables as needed
# The actual stacking
df_2_3 = df_raw[set_2_3].stack(dropna=True)
df_2_3 = pd.Series.to_frame(df_2_3) # Stacking provides series, so converting series to dataframe
df_2_3 = df_2_3.rename(columns={0: 'response_culture'}) # Renaming the v2c label

set_2_4 = list(emotion.var_name_with_brand) # Declare more variables based on the set of v2c variables as needed
# The actual stacking
df_2_4 = df_raw[set_2_4].stack(dropna=True)
df_2_4 = pd.Series.to_frame(df_2_4) # Stacking provides series, so converting series to dataframe
df_2_4 = df_2_4.rename(columns={0: 'response_emotion'}) # Renaming the v2c label

set_2_5 = list(interest.var_name_with_brand) # Declare more variables based on the set of v2c variables as needed
# The actual stacking
df_2_5 = df_raw[set_2_5].stack(dropna=True)
df_2_5 = pd.Series.to_frame(df_2_5) # Stacking provides series, so converting series to dataframe
df_2_5 = df_2_5.rename(columns={0: 'response_interest'}) # Renaming the v2c label

set_2_6 = list(differen.var_name_with_brand) # Declare more variables based on the set of v2c variables as needed
# The actual stacking
df_2_6 = df_raw[set_2_6].stack(dropna=True)
df_2_6 = pd.Series.to_frame(df_2_6) # Stacking provides series, so converting series to dataframe
df_2_6 = df_2_6.rename(columns={0: 'response_differentiation'}) # Renaming the v2c label


#***********************************************************
#***********************************************************
set_3_1 = list(thrive.timing_var_with_brand) # Declare more variables based on the set of v2c variables as needed
# The actual stacking
df_3_1 = df_raw[set_3_1].stack(dropna=True)
df_3_1 = pd.Series.to_frame(df_3_1) # Stacking provides series, so converting series to dataframe
df_3_1 = df_3_1.rename(columns={0: 'time_thrive'}) # Renaming the v2c label

set_3_2 = list(social.timing_var_with_brand) # Declare more variables based on the set of v2c variables as needed
# The actual stacking
df_3_2 = df_raw[set_3_2].stack(dropna=True)
df_3_2 = pd.Series.to_frame(df_3_2) # Stacking provides series, so converting series to dataframe
df_3_2 = df_3_2.rename(columns={0: 'time_social'}) # Renaming the v2c label

set_3_3 = list(culture.timing_var_with_brand) # Declare more variables based on the set of v2c variables as needed
# The actual stacking
df_3_3 = df_raw[set_3_3].stack(dropna=True)
df_3_3 = pd.Series.to_frame(df_3_3) # Stacking provides series, so converting series to dataframe
df_3_3 = df_3_3.rename(columns={0: 'time_culture'}) # Renaming the v2c label

set_3_4 = list(emotion.timing_var_with_brand) # Declare more variables based on the set of v2c variables as needed
# The actual stacking
df_3_4 = df_raw[set_3_4].stack(dropna=True)
df_3_4 = pd.Series.to_frame(df_3_4) # Stacking provides series, so converting series to dataframe
df_3_4 = df_3_4.rename(columns={0: 'time_emotion'}) # Renaming the v2c label

set_3_5 = list(interest.timing_var_with_brand) # Declare more variables based on the set of v2c variables as needed
# The actual stacking
df_3_5 = df_raw[set_3_5].stack(dropna=True)
df_3_5 = pd.Series.to_frame(df_3_5) # Stacking provides series, so converting series to dataframe
df_3_5 = df_3_5.rename(columns={0: 'time_interest'}) # Renaming the v2c label

set_3_6 = list(differen.timing_var_with_brand) # Declare more variables based on the set of v2c variables as needed
# The actual stacking
df_3_6 = df_raw[set_3_6].stack(dropna=True)
df_3_6 = pd.Series.to_frame(df_3_6) # Stacking provides series, so converting series to dataframe
df_3_6 = df_3_6.rename(columns={0: 'time_differentiation'}) # Renaming the v2c label


# Dataframe df_1 Is multiindexed, so we need to define labels to ensure they can be matched together
df_1.index.levels[0].name = 'Index' 
df_2_1.index.levels[0].name = 'Index'
df_2_2.index.levels[0].name = 'Index'
df_2_3.index.levels[0].name = 'Index'
df_2_4.index.levels[0].name = 'Index'
df_2_5.index.levels[0].name = 'Index'
df_2_6.index.levels[0].name = 'Index'
df_3_1.index.levels[0].name = 'Index'
df_3_2.index.levels[0].name = 'Index'
df_3_3.index.levels[0].name = 'Index'
df_3_4.index.levels[0].name = 'Index'
df_3_5.index.levels[0].name = 'Index'
df_3_6.index.levels[0].name = 'Index'
df_base.index.name = 'Index'

df_2_1['ind'] = df_2_1.index
df_2_1['brandname'] = df_2_1['ind'].apply(lambda x: x[1][17:])
df_2_1.drop(['ind'], axis=1, inplace=True)
df_2_2['ind'] = df_2_2.index
df_2_2['brandname'] = df_2_2['ind'].apply(lambda x: x[1][21:])
df_2_2.drop(['ind'], axis=1, inplace=True)
df_2_3['ind'] = df_2_3.index
df_2_3['brandname'] = df_2_3['ind'].apply(lambda x: x[1][19:])
df_2_3.drop(['ind'], axis=1, inplace=True)
df_2_4['ind'] = df_2_4.index
df_2_4['brandname'] = df_2_4['ind'].apply(lambda x: x[1][20:])
df_2_4.drop(['ind'], axis=1, inplace=True)
df_2_5['ind'] = df_2_5.index
df_2_5['brandname'] = df_2_5['ind'].apply(lambda x: x[1][22:])
df_2_5.drop(['ind'], axis=1, inplace=True)
df_2_6['ind'] = df_2_6.index
df_2_6['brandname'] = df_2_6['ind'].apply(lambda x: x[1][15:])
df_2_6.drop(['ind'], axis=1, inplace=True)


df_3_1['ind'] = df_3_1.index
df_3_1['brandname'] = df_3_1['ind'].apply(lambda x: x[1][24:])
df_3_1.drop(['ind'], axis=1, inplace=True)
df_3_2['ind'] = df_3_2.index
df_3_2['brandname'] = df_3_2['ind'].apply(lambda x: x[1][28:])
df_3_2.drop(['ind'], axis=1, inplace=True)
df_3_3['ind'] = df_3_3.index
df_3_3['brandname'] = df_3_3['ind'].apply(lambda x: x[1][26:])
df_3_3.drop(['ind'], axis=1, inplace=True)
df_3_4['ind'] = df_3_4.index
df_3_4['brandname'] = df_3_4['ind'].apply(lambda x: x[1][27:])
df_3_4.drop(['ind'], axis=1, inplace=True)
df_3_5['ind'] = df_3_5.index
df_3_5['brandname'] = df_3_5['ind'].apply(lambda x: x[1][29:])
df_3_5.drop(['ind'], axis=1, inplace=True)
df_3_6['ind'] = df_3_6.index
df_3_6['brandname'] = df_3_6['ind'].apply(lambda x: x[1][22:])
df_3_6.drop(['ind'], axis=1, inplace=True)

# Merging the new v2c variable with the other variables you need
df_1 = df_1.merge(df_base,how='left', left_index = True, right_index = True)
df_2_1 = df_base.merge(df_2_1,how='left', left_index = True, right_index = True)
df_2_2 = df_base.merge(df_2_2,how='left', left_index = True, right_index = True)
df_2_3 = df_base.merge(df_2_3,how='left', left_index = True, right_index = True)
df_2_4 = df_base.merge(df_2_4,how='left', left_index = True, right_index = True)
df_2_5 = df_base.merge(df_2_5,how='left', left_index = True, right_index = True)
df_2_6 = df_base.merge(df_2_6,how='left', left_index = True, right_index = True)
df_3_1 = df_base.merge(df_3_1,how='left', left_index = True, right_index = True)
df_3_2 = df_base.merge(df_3_2,how='left', left_index = True, right_index = True)
df_3_3 = df_base.merge(df_3_3,how='left', left_index = True, right_index = True)
df_3_4 = df_base.merge(df_3_4,how='left', left_index = True, right_index = True)
df_3_5 = df_base.merge(df_3_5,how='left', left_index = True, right_index = True)
df_3_6 = df_base.merge(df_3_6,how='left', left_index = True, right_index = True)

df_2_1['unique_respid'] = df_2_1[['respid','brandname']].apply(lambda x: ''.join(x), axis=1)
df_2_2['unique_respid'] = df_2_2[['respid','brandname']].apply(lambda x: ''.join(x), axis=1)
df_2_3['unique_respid'] = df_2_3[['respid','brandname']].apply(lambda x: ''.join(x), axis=1)
df_2_4['unique_respid'] = df_2_4[['respid','brandname']].apply(lambda x: ''.join(x), axis=1)
df_2_5['unique_respid'] = df_2_5[['respid','brandname']].apply(lambda x: ''.join(x), axis=1)
df_2_6['unique_respid'] = df_2_6[['respid','brandname']].apply(lambda x: ''.join(x), axis=1)

df_3_1['unique_respid'] = df_3_1[['respid','brandname']].apply(lambda x: ''.join(x), axis=1)
df_3_2['unique_respid'] = df_3_2[['respid','brandname']].apply(lambda x: ''.join(x), axis=1)
df_3_3['unique_respid'] = df_3_3[['respid','brandname']].apply(lambda x: ''.join(x), axis=1)
df_3_4['unique_respid'] = df_3_4[['respid','brandname']].apply(lambda x: ''.join(x), axis=1)
df_3_5['unique_respid'] = df_3_5[['respid','brandname']].apply(lambda x: ''.join(x), axis=1)
df_3_6['unique_respid'] = df_3_6[['respid','brandname']].apply(lambda x: ''.join(x), axis=1)

cols_to_drop = ['brandname']
cols_to_drop.extend(list(general_var_names.var_name))

df_2_2.drop(cols_to_drop, axis=1, inplace=True)
df_2_3.drop(cols_to_drop, axis=1, inplace=True)
df_2_4.drop(cols_to_drop, axis=1, inplace=True)
df_2_5.drop(cols_to_drop, axis=1, inplace=True)
df_2_6.drop(cols_to_drop, axis=1, inplace=True)
df_3_1.drop(cols_to_drop, axis=1, inplace=True)
df_3_2.drop(cols_to_drop, axis=1, inplace=True)
df_3_3.drop(cols_to_drop, axis=1, inplace=True)
df_3_4.drop(cols_to_drop, axis=1, inplace=True)
df_3_5.drop(cols_to_drop, axis=1, inplace=True)
df_3_6.drop(cols_to_drop, axis=1, inplace=True)



df_fin = df_2_1.merge(df_2_2,how='left', on='unique_respid')
df_fin = df_fin.merge(df_2_3,how='left', on='unique_respid')
df_fin = df_fin.merge(df_2_4,how='left', on='unique_respid')
df_fin = df_fin.merge(df_2_5,how='left', on='unique_respid')
df_fin = df_fin.merge(df_2_6,how='left', on='unique_respid')
df_fin = df_fin.merge(df_3_1,how='left', on='unique_respid')
df_fin = df_fin.merge(df_3_2,how='left', on='unique_respid')
df_fin = df_fin.merge(df_3_3,how='left', on='unique_respid')
df_fin = df_fin.merge(df_3_4,how='left', on='unique_respid')
df_fin = df_fin.merge(df_3_5,how='left', on='unique_respid')
df_fin = df_fin.merge(df_3_6,how='left', on='unique_respid')

cols = df_fin.columns.tolist()
new_cols = cols[0:4]
new_cols.append(cols[6])
new_cols.append(cols[5])
new_cols.append(cols[4])
for i in range(7,len(cols)):
    new_cols.append(cols[i])
    
df_fin=df_fin[new_cols]

df_fin['brandname'] = df_fin['brandname'].apply(lambda x: x[1:])

df_1['ind'] = df_1.index
df_1['brandname'] = df_1['ind'].apply(lambda x: x[1])
df_1.drop(['ind'], axis=1, inplace=True)

cols = df_1.columns.tolist()
new_cols = cols[1:]
new_cols.append(cols[0])
df_1 = df_1[new_cols]
df_1['brand'] = df_1['brandname'].apply(lambda x: '_'+x)

df_1['unique_respid'] = df_1['respid'] + df_1['brand']

df_fin.drop(list(general_var_names.var_name), axis=1, inplace=True)

df_1['brand_name'] = df_1['brandname']
df_1.drop(['brandname'], axis=1, inplace=True)
df_fin = df_1.merge(df_fin,how='left', on='unique_respid')

new_cols = list(general_var_names.var_name)
add_cols = ['unique_respid',
       'brand_name', 'brand_love', 'response_thrive', 'response_social', 'response_culture',
       'response_emotion', 'response_interest', 'response_differentiation',
       'time_thrive', 'time_social', 'time_culture', 'time_emotion',
       'time_interest', 'time_differentiation']

new_cols.extend(add_cols)

df_fin = df_fin[new_cols]

#df_3 = df_3.merge(df_2,how='left', on = 'respid')

#df_1.to_csv('C:/Users/Payam/Dropbox/2007/Tableau data/2007-Tableau-love.csv',encoding='utf-8',index=False)
#df_2_1.to_csv('C:/Users/Payam/Dropbox/2007/Tableau data/2007-Tableau-statement_1.csv',encoding='utf-8')
#df_2_2.to_csv('C:/Users/Payam/Dropbox/2007/Tableau data/2007-Tableau-statement_2.csv',encoding='utf-8')
#df_2_3.to_csv('C:/Users/Payam/Dropbox/2007/Tableau data/2007-Tableau-statement_3.csv',encoding='utf-8')
#df_2_4.to_csv('C:/Users/Payam/Dropbox/2007/Tableau data/2007-Tableau-statement_4.csv',encoding='utf-8')
#df_2_5.to_csv('C:/Users/Payam/Dropbox/2007/Tableau data/2007-Tableau-statement_5.csv',encoding='utf-8')
#df_2_6.to_csv('C:/Users/Payam/Dropbox/2007/Tableau data/2007-Tableau-statement_6.csv',encoding='utf-8')
#df_3_1.to_csv('C:/Users/Payam/Dropbox/2007/Tableau data/2007-Tableau-timing_1.csv',encoding='utf-8')
#df_3_2.to_csv('C:/Users/Payam/Dropbox/2007/Tableau data/2007-Tableau-timing_2.csv',encoding='utf-8')
#df_3_3.to_csv('C:/Users/Payam/Dropbox/2007/Tableau data/2007-Tableau-timing_3.csv',encoding='utf-8')
#df_3_4.to_csv('C:/Users/Payam/Dropbox/2007/Tableau data/2007-Tableau-timing_4.csv',encoding='utf-8')
#df_3_5.to_csv('C:/Users/Payam/Dropbox/2007/Tableau data/2007-Tableau-timing_5.csv',encoding='utf-8')
#df_3_6.to_csv('C:/Users/Payam/Dropbox/2007/Tableau data/2007-Tableau-timing_6.csv',encoding='utf-8')
df_fin.to_csv('C:/Users/Payam/Dropbox/2007/Tableau data/2007-Tableau-data.csv',encoding='utf-8',index=False)
