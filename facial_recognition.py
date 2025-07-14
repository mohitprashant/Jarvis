# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 02:50:56 2025

@author: 18moh
"""
from imutils import paths
import face_recognition as fr
import pickle
import cv2
import os


class FacialRecogition():
    def __init__(self):
       self.mod_loc = 'Internal Data/Modules/facial recognition/'
       self.friend_names, self.friend_faces = self.load_freq_faces()
       
        
        
    def load_freq_faces(self):
        directory_path = self.mod_loc
        file_paths = []
        encodings = []
        names = []
        
        for filename in os.listdir(directory_path):
            full_path = os.path.join(directory_path, filename)
            if os.path.isfile(full_path):
                if filename.endswith('.enc'):
                    file_paths.append(full_path)
                    names.append(filename[:-4])
                    
                    with open(full_path, 'rb') as file:
                        loaded_variable = pickle.load(file)
                        encodings.append(loaded_variable)
                    
        return names, encodings
    
    
    def add_new(self, encoding, name):
        file_path = os.path.join(self.mod_loc, name+'.enc')
        with open(file_path, 'wb') as f:
            pickle.dump(encoding, f)
    
    
    
    def encode_face(self, img):
        face_locations = fr.face_locations(img)
        face_encodings = fr.face_encodings(img, face_locations)
        return face_encodings, face_locations
        
        
    
    def identify(self, img):
        pass
    
    
    
    def run_web_cam(self):
        pass
    
    
    def take_a_picture(self):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: Could not open webcam.")
            exit()
            
        grabbed, frame = cap.read()
        rgb_small_frame = None
        if grabbed:
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1]
            rgb_small_frame = cv2.cvtColor(rgb_small_frame , cv2.COLOR_BGR2RGB)
            
            # cv2.imwrite("captured_image.jpg", rgb_small_frame)
            
            print("Image captured.")
        else:
            print("Error: Could not read frame from webcam.")
    
        cap.release()
        cv2.destroyAllWindows()
        return rgb_small_frame
        
        
if __name__ == '__maind__':
    f = FacialRecogition()
    img = f.take_a_picture()
    face, loc = f.encode_face(img)
    
    for i in range(len(face)):
        f.add_new(face[i], str(i))
    

        
        
if __name__ == '__main__':
    # default webcam
    stream = cv2.VideoCapture(0)
    f = FacialRecogition()
    known_faces, known_names = f.friend_faces, f.friend_names
    
    face_locations = []
    face_encodings = []
    face_names = []
    
    while(True):
        grabbed, frame = stream.read()
        
        
        frame_count = 0
        if(frame_count%4 == 0):
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1]
            rgb_small_frame = cv2.cvtColor(rgb_small_frame , cv2.COLOR_BGR2RGB)
            
            #===============ENCODE FACE=============
            
            face_locations = fr.face_locations(rgb_small_frame)
            face_encodings = fr.face_encodings(rgb_small_frame, face_locations)
                
            #===============ENCODE FACE=============
            
            #===============IDENTIFYING FACE=============
            
            for x in face_encodings:
                matches = fr.compare_faces(known_faces, x)
                name = 'unknown'
                
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_names[first_match_index]
                    
                face_names.append(name)
                
            #===============IDENTIFYING FACE=============
            
            #===============DISPLAY FACE=============
            
        for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    
            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            
            #===============DISPLAY FACE=============

        
        frame_count += 1
        frame_count %= 4
        cv2.imshow("Image", frame)
        key = cv2.waitKey(1)
        if key == ord("q"):    # Press q to break out of the loop
            break
    
    # Cleanup
    stream.release()
    cv2.waitKey(1)
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    
    
    
    
    
    
    
    
    
    