class MonsterBall:
    def __init__(self, image):
        self.image = image
        self.count = 5

    def draw(self, screen):
        screen.paste(self.image, (184, 209), self.image)
