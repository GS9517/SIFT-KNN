
#read csv as dataframe
import pandas as pd
from sklearn.model_selection import train_test_split


#read train.csv as dataframe
train_df = pd.read_csv('train.csv')
#read val.csv as dataframe
#val_df = pd.read_csv('val.csv')
#read test.csv as dataframe
test_df = pd.read_csv('test.csv')

print("Train label counts:\n", train_df['label'].value_counts())
#print("Validation label counts:\n", val_df['label'].value_counts())
print("Test label counts:\n", test_df['label'].value_counts())