#!/usr/bin/env python3


import os
import hashlib
import random

import cv2


folder = 'output'
training_folder = 'training'

for filename in os.listdir(folder):

    path = os.path.join(folder, filename, 'chars')

    for image_filename in os.listdir(path):

        img = cv2.imread(os.path.join(path, image_filename))

        img_hash = hashlib.sha1(img).hexdigest()

        training_image_filename = '{}.tiff'.format(str(img_hash))

        if training_image_filename in os.listdir(training_folder):
            continue

        cv2.imshow('char', img)

        chars = ''
        while True:
            key = cv2.waitKey(0)
            print(key)
            if key == 225:
                continue
            char = chr(key)
            if char == '\n':
                break
            print(char)
            chars += char

        cv2.imwrite(os.path.join(training_folder, training_image_filename), img)


        with open('training_labels', 'a') as f:
            f.write('{}\t{}\n'.format(str(img_hash), chars))
