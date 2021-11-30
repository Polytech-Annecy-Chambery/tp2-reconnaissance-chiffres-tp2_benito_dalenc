from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    image_bin = image.binarisation(S)
    image_loc=image_bin.localisation()
    Sim_max=0
    Sim_ind=0

    for u in range (0, len(liste_modeles)):
        im_bin4 = image_loc.resize( liste_modeles[u].H, liste_modeles[u].W )
        Sim_im = im_bin4.similitude(liste_modeles[u])
        if Sim_im > Sim_max:
            Sim_max = Sim_im  
            Sim_ind = u
    
    return Sim_ind     