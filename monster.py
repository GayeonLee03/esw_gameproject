class Monster:
    def __init__(self, name, image, x, y):
        self.name = name
        self.image = image
        self.x = x
        self.y = y
        self.hp = 100

    def draw(self, screen):
        screen.paste(self.image, (self.x, self.y), self.image)
