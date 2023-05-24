import os
import shutil
import csv

csv_file_path = './subrat/Data/HAM_Data/archive/HAM10000_metadata.csv'
image_folder_path = './subrat/Data/HAM_Data/archive/HAM10000_images_part_1'


class_folders = {}

# class_folder = "/subrat/Data/HAM_Data/modified_HAM"
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header row if present
    for row in csv_reader:
        image_id = row[1]  # Assuming the image name is in the first column
        dx = row[2]  # Assuming the class label is in the second column
    # print(image_id)
    # exit()
        # Create a folder for the class if it doesn't exist
        if dx not in class_folders:
            class_folder = os.path.join(image_folder_path, dx)
            if not os.path.exists(class_folder):
                os.makedirs(class_folder)
            class_folders[dx] = class_folder

        # Move the image to the corresponding class folder
        src = os.path.join(image_folder_path, image_id + '.jpg')
        dst = os.path.join(class_folders[dx], image_id + '.jpg')
        shutil.move(src, dst)
