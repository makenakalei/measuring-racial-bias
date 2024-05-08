import pandas as pd
import numpy as np
from PIL import Image
from ast import literal_eval  # Used to convert string representation of arrays to actual arrays


data = pd.read_csv('/Users/makenarobison/Desktop/Computer Vision Research/age_gender.csv')


for index, row in data.iterrows():
    img_name = row['img_name']
    pixels_str = row['pixels']
    
    
    pixels_arr = np.array([int(pixel) for pixel in pixels_str.split()])

    
    
    image_size = (48, 48)  
    pixels_arr = pixels_arr.reshape(image_size).astype(np.uint8)
    
    
    image = Image.fromarray(pixels_arr)
    
    
    image.save(f"{img_name}.jpg")  
print("Images saved successfully.")
