from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np

class Image:
    def __init__(self):
        """Initialisation d'une image composee d'un tableau numpy 2D vide
        (pixels) et de 2 dimensions (H = height et W = width) mises a 0
        """
        self.pixels = None
        self.H = 0
        self.W = 0
    

    def set_pixels(self, tab_pixels):
        """ Remplissage du tableau pixels de l'image self avec un tableau 2D (tab_pixels)
        et affectation des dimensions de l'image self avec les dimensions 
        du tableau 2D (tab_pixels) 
        """
        self.pixels = tab_pixels
        self.H, self.W = self.pixels.shape


    def load(self, file_name):
        """ Lecture d'un image a partir d'un fichier de nom "file_name"""
        self.pixels = io.imread(file_name)
        self.H,self.W = self.pixels.shape 
        print("lecture image : " + file_name + " (" + str(self.H) + "x" + str(self.W) + ")")


    def display(self, window_name):
        """Affichage a l'ecran d'une image"""
        fig = plt.figure(window_name)
        if (not (self.pixels is None)):
            io.imshow(self.pixels)
            io.show()
        else:
            print("L'image est vide. Rien à afficher")


    #==============================================================================
    # Methode de binarisation
    # 2 parametres :
    #   self : l'image a binariser
    #   S : le seuil de binarisation
    #   on retourne une nouvelle image binarisee
    #==============================================================================
    def binarisation(self, S):
        im_bin=Image()
        im_bin.set_pixels(np.zeros((self.H, self.W),dtype=np.uint8))
        for l in range (0, self.H):
            for c in range (0, self.W):
                if self.pixels[l][c]>=S:
                    im_bin.pixels[l][c]=255
                else:
                    im_bin.pixels[l][c] =0 
        return im_bin


    #==============================================================================
    # Dans une image binaire contenant une forme noire sur un fond blanc
    # la methode 'localisation' permet de limiter l'image au rectangle englobant
    # la forme noire
    # 1 parametre :
    #   self : l'image binaire que l'on veut recadrer
    #   on retourne une nouvelle image recadree
    #==============================================================================
    def localisation(self):
       c_min = self.W-1
       c_max = 0
       l_min = self.H-1
       l_max = 0
       im_bin2=Image()
       for l in range (0, self.H):
           for c in range (0, self.W):
               if self.pixels[l, c]==0:
                   if c > c_max:
                       c_max = c
                   if c_min > c:
                       c_min = c
                   if l_min > l:
                       l_min = l
                   if l > l_max:
                       l_max = l
                
       im_bin2.set_pixels(self.pixels[l_min:l_max,c_min:c_max])
       return im_bin2
    #==============================================================================
    # Methode de redimensionnement d'image
    #==============================================================================
    def resize(self, new_H, new_W):
        im_bin3=Image()
        Tablo = resize(self.pixels, (new_H,new_W), 0)
        Tablo = np.uint8(Tablo*255)
        im_bin3.set_pixels(Tablo)
        return im_bin3
    #==============================================================================
    # Methode de mesure de similitude entre l'image self et un modele im
    #==============================================================================
    def similitude(self, im):
        result=0
        for l in range (0,self.H):
            for c in range (0, self.W):
                if self.pixels[l, c]==im.pixels[l, c]:
                    result= result + 1
                else :
                    result
        return result/(self.H*self.W)
                
                
        

