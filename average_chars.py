#!/usr/bin/env python3

import os
from collections import defaultdict

import numpy as np
import cv2

char_dict = defaultdict(list)

with open('training_labels') as f:
    for line in map(str.strip, f):
        try:
            image_hash, chars = line.split('\t')
        except ValueError:
            continue

        char_dict[chars].append(image_hash)


for chars, images in char_dict.items():
    if not chars == 'e':
        continue
    print(chars)
    print(len(images))

    average_img = np.zeros((100,100,))
    for image in images:
        filename = '{}.tiff'.format(image)
        print(image)
        img = cv2.imread(os.path.join('training', filename))
        cv2.imshow('img', img)
        cv2.waitKey(0)

        #average_img = average_img + np.pad(img, (100, 100, 3), mode='minimum')

        cv2.imshow('average', average_img)


