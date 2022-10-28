from PIL import Image
import os, sys

#defined paths
folder_path = '/Users/chrislee/Documents/Bionic Hand/Neural Network/Training Images/'
folder_dirs = os.listdir(folder_path)
rock_path = '/Users/chrislee/Documents/Bionic Hand/Neural Network/Training Images/Rock Training Images'
rock_dirs = os.listdir(rock_path)
paper_path = '/Users/chrislee/Documents/Bionic Hand/Neural Network/Training Images/Paper Training Images'
paper_dirs = os.listdir(paper_path)
scissor_path = '/Users/chrislee/Documents/Bionic Hand/Neural Network/Training Images/Scissor Training Images'
scissor_dirs = os.listdir(scissor_path)

#functions
def resize(path, dirs):
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((320,320), Image.Resampling.LANCZOS)
            imResize.save(f + '.png', 'PNG', quality=90)

def load_training_images():
    training_data_array=[]

    for item in rock_dirs:
        if os.path.isfile(rock_path + item):
            im = Image.open(rock_path + item)
            training_data_array.append((im, "rock"))

    for item in paper_dirs:
        if os.path.isfile(paper_path + item):
            im = Image.open(paper_path + item)
            training_data_array.append((im, "paper"))

    for item in scissor_dirs:
        if os.path.isfile(scissor_path + item):
            im = Image.open(scissor_path + item)
            training_data_array.append((im, "scissor"))

    return training_data_array

#process all images
resize(rock_path, rock_dirs)
resize(paper_path, paper_dirs)
resize(scissor_path, scissor_dirs)

training_array = load_training_images()

#print out all elements of processed image array
for element in training_array:
    element[0].show()
    print(element[1])

