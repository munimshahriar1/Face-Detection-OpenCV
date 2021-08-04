#!/usr/bin/env python
# coding: utf-8

# In[1]:


import face_recognition
import cv2
import numpy as np
import os
import glob
import sys


# In[2]:


faces_encodings = []
faces_names = []
cur_dir = os.getcwd()
path = os.path.join(cur_dir, 'src\\training_images\\')


# In[3]:


list_of_files = [f for f in glob.glob(path+'*.jpg')]
names = list_of_files.copy()


# In[4]:


for i in range(len(list_of_files)):
    globals()[f'image_{i}'] = face_recognition.load_image_file(list_of_files[i])
    globals()[f'image_encoding_{i}'] = face_recognition.face_encodings(globals()[f'image_{i}'])[0]
    faces_encodings.append(globals()[f'image_encoding_{i}'])
# Create array of known names
    names[i] = names[i].replace(cur_dir, "")  
    faces_names.append(names[i])


# In[5]:


face_locations = []
face_encodings = []
face_names = []
process_this_frame = True


# In[6]:


video_capture = cv2.VideoCapture(0)
while True:
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    if process_this_frame:
        face_locations = face_recognition.face_locations( rgb_small_frame)
        face_encodings = face_recognition.face_encodings( rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces (faces_encodings, face_encoding)
            name = "Unknown"
            face_distances = face_recognition.face_distance( faces_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = faces_names[best_match_index]
            face_names.append(name)
    process_this_frame = not process_this_frame
    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        # Draw a rectangle around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        # Input text label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        # print("Name :", name)
        name_2= name.split("\\")[-1].replace(".jpg", "")
        cv2.putText(frame, name_2, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        # print("Name_2 :", name_2)
    # Display the resulting image
    cv2.imshow('Video', frame)
    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:
