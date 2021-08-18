# What is this repo ?
A simple script based on Python 3 that allows the native machine webcam to look for trained images. 

# How to install ?

Step 1: Create a separate Python Virtual Environment (preferably Python > 3.6)

Step 2: Install the dependencies using the following command - 
'''
pip install -r requirements\requirements.txt
'''


# Dependencies: 
- cv2
- face_recognition (Microsoft Visual Studio for C++ might be a prerequisite for this module)
- numpy

# How to use ?
You can train your particular image by placing the relevant image inside the "./src/training_images" folder.
- Run the .py file to use the script.
- Use the .bat file to run the script on Windows Powershell directly. (Note: You might need to change the Python Path and the source code path)
- Use 'q' or 'Q' to terminate the script.

# Important:
- Make sure you use .jpg image file type in the the "./src/training_images" folder.
- Make sure you use relevant name for the image file.


