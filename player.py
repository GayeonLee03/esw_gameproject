class Player:
    def __init__(self, image):
        self.image = image
        self.x = 104
        self.y = 130

    def draw(self, screen):
        screen.paste(self.image, (self.x, self.y), self.image)
    def move(self, command):
        if command['up_pressed']:
            self.y -= 5

        if command['down_pressed']:
            self.y += 5

        if command['left_pressed']:
            self.x -= 5

        if command['right_pressed']:
            self.x += 5
