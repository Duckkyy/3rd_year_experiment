import os
import shutil

datasets_fol = 'emotions/datasets'
train_fol = 'emotions/train'
test_fol = 'emotions/test'

train_txt = open("emotions/ground_truth_train.txt", 'r')
test_txt = open('emotions/ground_truth_test.txt', 'r')

train_data = train_txt.readlines()
test_data = test_txt.readlines()

for data in train_data:
    if data[-1] == '\n':
        data = data[:-1]
    
    image_path = data.split()[0]
    image_folder = image_path.split('/')[0]
    class_num = data.split()[1]

    des_path = os.path.join(train_fol, class_num, image_folder)
    os.makedirs(des_path, exist_ok=True)

    image_full_path = os.path.join(datasets_fol, image_path)

    if not os.path.isfile(image_full_path):
        continue

    shutil.copy(image_full_path, des_path)
