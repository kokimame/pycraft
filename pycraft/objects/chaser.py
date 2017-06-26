import random

from pycraft.objects.enemy import Enemy
from .textures import tex_coords

class Chaser(Enemy):

    def __init__(self, config):
        super(Chaser, self).__init__(config)
        self.texture = tex_coords((2, 1), (2, 1), (2, 1))

    def update(self, dt, objects, pad=0.25):
        if random.randint(1, 301) % 300 == 0: self.jump()
        else: self.strafe_forward()
        super(Chaser, self).update(dt, objects, pad)

    def draw(self):
        pass