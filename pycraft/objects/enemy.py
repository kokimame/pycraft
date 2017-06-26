from pycraft.objects.character import Character


class Enemy(Character):
    """ Class to hold common logic among enemies. """
    def __init__(self, config):
        super(Enemy, self).__init__(config)

    def draw(self):
        pass