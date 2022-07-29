# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 08:36:05 2022

@author: knian
"""

class Addition:
    
    def __init__(self, nombres):
        self.nombres = nombres
        self.valide()
        
    def n_somme(self):
        self.somme = sum(self.nombres)
        return self.somme
        
    def n_affiche(self):
        print(f"La somme des nombres {self.nombres} est egal à {self.somme}")
        
    def valide(self):
        self.validate = True
        for nombre in self.nombres:
            if not isinstance(nombre, (float, int)):
                self.validate = False
                raise ValueError("Veillez entrer que des nombres")
                
n_nombre = Addition([2,4,8])
somme = n_nombre.n_somme()
n_nombre.n_affiche()