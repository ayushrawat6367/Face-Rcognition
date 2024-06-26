'''
Notes:
1. All of your implementation should be in this file. 
2. Please Read the instructions and do not modify the input and output formats of function detect_faces() and cluster_faces().
3. If you want to show an image for debugging, please use show_image() function in helper.py.
4. Please do NOT save any intermediate files in your final submission.
'''


import cv2
import numpy as np
import os
import sys
import math

import face_recognition

from typing import Dict, List
from utils import show_image

'''
Please do NOT add any imports. The allowed libraries are already imported for you.
'''

def detect_faces(img: np.ndarray) -> List[List[float]]:
    """
    Args:
        img : input image is an np.ndarray represent an input image of shape H x W x 3.
            H is the height of the image, W is the width of the image. 3 is the [R, G, B] channel (NOT [B, G, R]!).

    Returns:
        detection_results: a python nested list. 
            Each element is the detected bounding boxes of the faces (may be more than one faces in one image).
            The format of detected bounding boxes a python list of float with length of 4. It should be formed as 
            [topleft-x, topleft-y, box-width, box-height] in pixels.
    """
    detection_results: List[List[float]] = [] # Please make sure your output follows this data format.

    # Add your code here. Do not modify the return and input arguments.

    face_locations = face_recognition.face_locations(img)
    faces = []
    for (top, right, bottom, left) in face_locations:
        x = float(left)
        w = float(right - x)
        y = float(top) 
        h = float(bottom - y)
        faces.append([x,y,w,h])

    detection_results = faces 
    return detection_results


def cluster_faces(imgs: Dict[str, np.ndarray], K: int) -> List[List[str]]:
    """
    Args:
        imgs : input images. It is a python dictionary
            The keys of the dictionary are image names (without path).
            Each value of the dictionary is an np.ndarray represent an input image of shape H x W x 3.
            H is the height of the image, W is the width of the image. 3 is the [R, G, B] channel (NOT [B, G, R]!).
        K: Number of clusters.
    Returns:
        cluster_results: a python list where each elemnts is a python list.
            Each element of the list a still a python list that represents a cluster.
            The elements of cluster list are python strings, which are image filenames (without path).
            Note that, the final filename should be from the input "imgs". Please do not change the filenames.
    """
    cluster_results: List[List[str]] = [[]] * K # Please make sure your output follows this data format.

    # Add your code here. Do not modify the return and input arguments.
    face_locations = face_recognition.face_locations(imgs)
    print(face_locations)
    faces = []
    for (top, right, bottom, left) in face_locations:
        x = float(left)
        w = float(right - x)
        y = float(top) 
        h = float(bottom - y)
        faces.append([x,y,w,h])
        face_encodings = face_recognition.face_encodings(imgs, faces)
    
    # sorted_faces = []
    # face = imgs[0]
    # sorted_faces.append(face)
    # for i in range(len(face)-1):
    #     closest_faces = faces.loc[[face]].squeeze() # row number, you can find who is it in the row of names
    #     closest_faces=closest_faces.drop(index=sorted_faces,  inplace=False, errors='raise')
    #     closest_faces = closest_faces.sort_values()
    #     similar_face = closest_faces.index[0]
    #     sorted_faces.append(similar_face)
    #     face = similar_face
    #     print(face)
    # cluster_results = sorted_faces
        
    return cluster_results


'''
If your implementation requires multiple functions. Please implement all the functions you design under here.
But remember the above 2 functions are the only functions that will be called by task1.py and task2.py.
'''

# Your functions. (if needed)
