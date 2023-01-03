import os
import requests
import zipfile
import shutil

import pandas as pd
from sklearn.model_selection import train_test_split

# Setup path to data folder
image_path = "/Users/ducky/Documents/3rd_year_experiment/emotions/datasets"
label_path = "/Users/ducky/Documents/3rd_year_experiment/emotions/Labels"

train_label_path = os.path.join(label_path, "ground_truth_train.csv")
test_label_path = os.path.join(label_path, "ground_truth_test.csv")

# data_path = "../data/emotion_img"
data_path = "/Users/ducky/Documents/3rd_year_experiment/emotions/data"

if os.path.isdir(data_path):
    shutil.rmtree(data_path)
os.makedirs(data_path, exist_ok=True)

train_dataset = os.path.join(data_path, "train")
os.makedirs(train_dataset)
test_dataset = os.path.join(data_path, "test")
os.makedirs(test_dataset)
val_dataset = os.path.join(data_path, "val")
os.makedirs(val_dataset)

# read train label csv file 
train_val_df = pd.read_csv(train_label_path)
test_df = pd.read_csv(test_label_path)

# get label from csv label column
for label in range(1, 8):
    train_df, val_df = train_test_split(train_val_df[train_val_df["label"] == label], 
        shuffle=True, train_size=0.95, random_state=32)

    # Copy image to train dataset dir
    for idx, row in train_df.iterrows():
        print(row['image'])
        train_image_path = os.path.join(image_path, row["image"])
        train_image_folder = row['image'].split('/')[0]
        train_label = str(row["label"])

        train_dataset_dir_path = os.path.join(train_dataset, train_label, train_image_folder)
        if not os.path.isdir(train_dataset_dir_path):
            os.makedirs(train_dataset_dir_path)

        shutil.copy(train_image_path, train_dataset_dir_path)

    # Copy image to validation dataset dir
    for idx, row in val_df.iterrows():
        val_image_path = os.path.join(image_path, row["image"])
        val_image_folder = row['image'].split('/')[0]
        val_label = str(row["label"])

        val_dataset_dir_path = os.path.join(val_dataset, val_label, val_image_folder)
        if not os.path.isdir(val_dataset_dir_path):
            os.makedirs(val_dataset_dir_path)

        shutil.copy(val_image_path, val_dataset_dir_path)

# Copy image to test dataset dir
for idx, row in test_df.iterrows():
    test_image_path = os.path.join(image_path, row["image"])

    shutil.copy(test_image_path, test_dataset)