# What is this repo ?
A simple script based on Python 3 that allows the native machine webcam to look for trained images. 


# Dependencies: 
- cv2
- face_recognition (Microsoft Visual Studio for C++ might be a prerequisite for this module)
- numpy

# How to install ?

Step 1: Create a separate Python Virtual Environment (preferably Python > 3.6)

Step 2: Install the dependencies using the following command - 
```
pip install -r requirements\requirements.txt
```
# How to run ?

1. Train the model using sample image in the "./src/training_images" folder (make sure to use .jpg image)

2. Make sure you use relevant name for the images. E.g if you put an image  of Barack Obama in the folder make sure you name it "Barack Obama.jpg"

3. Run the script using the following command - 
```
python face-recognition.py
```
