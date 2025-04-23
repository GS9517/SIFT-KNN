import pandas as pd
from sklearn.model_selection import train_test_split

# RUN IT AFTER indexGenerate.py

# split dataset into training, validation, and test sets

# read the csv file
dataframe = pd.read_csv('index.csv')

# split the dataframe into training 80%, validation 10%, and test 10%
# include shuffle in train_test_split

train_df, test_df = train_test_split(dataframe, test_size=0.2, random_state=42, stratify=dataframe['label'])

# split the dataframe into training 70%, validation 15%, and test 15%
# include shuffle in train_test_split
# IT WILL OVERWRITE THE OLD CSV FILES, SO BE CAREFUL

# test show
print(f'Train shape: {train_df.shape}')
#print(f'Validation shape: {val_df.shape}')
print(f'Test shape: {test_df.shape}')

# save
train_df.to_csv('train.csv', index=False)
test_df.to_csv('test.csv', index=False)


