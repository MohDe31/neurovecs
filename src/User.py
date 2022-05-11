import random
from tkinter import W
from math import sqrt
import pygame
import numpy as np


class user :

    def __init__(self, velocity, height, width, obs) -> None:
        
        self.height, self.width = height, width
        self.u = pygame.Vector3(random.random() * self.width* 0.5 + 200, random.random() * self.height* 0.5 + 200, 0)
        self.v = velocity
        self.theta = 0
        self.beta = 0
        self.delta_theta = 0.3
        self.delta_t = 100
        self.obs = pygame.Rect(obs[0].x-50, obs[0].y-50, obs[1][0], obs[1][1])
        
        while self.obs.collidepoint(self.u.x, self.u.y) == True :
            self.u = pygame.Vector3(random.random() * self.width* 0.5 + 200, random.random() * self.height* 0.5 + 200, 0)
        
    
    def randomWalk(self, iter) :
    
        if iter % self.delta_t == 0 or self.u.x < 0 or self.u.x > self.width or self.u.y < 0 or self.u.y > self.height \
           or self.obs.collidepoint(self.u.x, self.u.y) == True:
           a = random.randint(0, 360)
           self.theta = a * np.pi / 180

        self.beta = random.uniform(0,1)
        self.delta_theta = 0.3 - 0.6 * self.beta

        self.theta += self.delta_theta

        self.u.x += self.v * np.cos(self.theta) * self.delta_t
        self.u.y += self.v * np.sin(self.theta) * self.delta_t

        

   