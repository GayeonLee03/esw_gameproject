class EquippedMonster:
    def __init__(self, name, image):
        self.name = name
        self.image = image
        self.hp = 100

    def draw(self, screen):
        screen.paste(self.image, (8, 205), self.image)
