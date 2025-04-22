import os
import pandas as pd

# match dataset with csv
dataset_path="./Aerial_Landscapes" # path to the dataset folder
categories=[d for d in os.listdir(dataset_path) if os.path.isdir(os.path.join(dataset_path, d))] # because original dataset already split imgs into folders with specific names, so use it as label
image_paths = []
image_labels = []

for category in categories:
    category_path = os.path.join(dataset_path, category)
    for image_name in os.listdir(category_path):
        image_path = os.path.join(category_path, image_name)
        image_paths.append(os.path.abspath(image_path).replace('\\','/')) # use absolute path
        image_labels.append(category)

dataframe = pd.DataFrame({
    'image_path': image_paths,
    'label': image_labels
})


print(f'Dataframe shape: {dataframe.shape}')

# save to csv
dataframe.to_csv('index.csv', index=False)

# test show
print(dataframe.head(5))

# THEN RUN dataSpliter.py