import pandas as pd
from sklearn.model_selection import train_test_split

# RUN IT AFTER indexGenerate.py

# split dataset into training, validation, and test sets

# read the csv file
dataframe = pd.read_csv('index.csv')

# split the dataframe into training 70%, validation 15%, and test 15%
# include shuffle in train_test_split
train_df, temp_df = train_test_split(dataframe, test_size=0.3, random_state=42, stratify=dataframe['label'])
val_df, test_df = train_test_split(temp_df, test_size=0.5, random_state=42, stratify=temp_df['label'])
# IT WILL OVERWRITE THE OLD CSV FILES, SO BE CAREFUL

# test show
print(f'Train shape: {train_df.shape}')
print(f'Validation shape: {val_df.shape}')
print(f'Test shape: {test_df.shape}')

# save
train_df.to_csv('train.csv', index=False)
val_df.to_csv('val.csv', index=False)
test_df.to_csv('test.csv', index=False)

# df here is origin, not enforced (not change csv, only edit img) or unbalanced (remove some img,so num reduce)