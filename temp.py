# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import h5py
import matplotlib.pyplot as plt
import os
from PIL import Image 

train_imgs = h5py.File('./input_data/train_images.hdf5', 'r')
for i in range(100,300):
    print( "now showing image number " , i)
    
    fig = plt.figure(figsize=[12, 6])
    ax1 , ax2  = fig.subplots(1,2)
    
    ax1.imshow(train_imgs['target_masks'][i][...], origin='upper', cmap='Greys_r')
    ax2.imshow(train_imgs['input_images'][i][...], origin='upper', cmap='Greys_r')
    plt.show()
    
