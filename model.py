from os import listdir
from os.path import isfile, join
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

class Antialiasing:
    def __init__(self, path, method):
        self.path = path
        self.method = method
        self.files = self.get_files()
        
    def get_directors(self):
        return self.files
    
    def get_files(self):
        aux = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        result = []
        for i in range(len(aux)):
            
            isJpeg =  aux[i].find(".jpeg") != -1
            isPng =  aux[i].find(".png") != -1

            if(isJpeg | isPng):
                result.append(aux[i])
                
                return result
            
    def convert(self):
        for index in range(len(self.files)):
                file_name = self.files[index];
                image_path = f'{self.path}/{file_name}'
                img = Image.open(image_path)
                plt.figure(f'{self.method},{file_name}')   
                plt.imshow(img, interpolation=self.method, cmap='RdBu_r')
                #plt.title()
                plt.figure(f'no interpolation, (file_name)')
                plt.imshow(img, cmap = 'RdBu_r')
            
        plt.show()