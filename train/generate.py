from gan_model_train import Generator

import numpy as np 

import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision.utils import save_image

import cv2
from PIL import Image

class GAN_generator():
    def __init__(self):    
        # loading the Pretrained Generator
        self.model = Generator()
        self.model.load_state_dict(torch.load('./models/caMoufLage_1.pt'))
        self.model.eval()

        if torch.cuda.is_available():
            self.Tensor = torch.cuda.FloatTensor
            self.model.cuda()
        else:
            self.Tensor = torch.FloatTensor
    
    def predictIMG(self, array= None):
        # Now, we will use some autogenerated latent spaces to produce some new image
        img2 = self.model(self.Tensor([[0.3, 1, 1, 1, -1, 1, 5, 1, 1, -1]])) #[[1,2,-0.2,1,-3,0.3,0.2,0.1,0.2,0.5]])) 
        #img2 = self.model(self.Tensor([array]))
        save_image(img2.data[0], 'output/generated_IMG2.png' , nrow= 1, normalize= True)
        self.resizeIMG()
    
    def resizeIMG(self, file= './output/generated_IMG2.png'):
        """Resize the given image
        """
        im = Image.open(file)
        im = im.resize((int(im.size[0]*10), int(im.size[1]*10)), Image.NEAREST)
        im.save('./output/new.png')
        
    def generateIMG(self, array):
        """Generates an Image from given array And returns it
        """
        img = self.model(self.Tensor([array]))
        return img

model = GAN_generator()
model.predictIMG()