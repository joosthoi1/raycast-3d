import tkinter as tk
import math
import time
import gridcreation as gc


class main(tk.Frame):
    screenWidth = 65
    screenHeight = 40

    playerX = 3.5
    playerY = 3.5
    playerA = 0.0

    game_map = [
        "########",
        "#.#....#",
        "#....#.#",
        "#....#.#",
        "#......#",
        "#...####",
        "##.....#",
        "########",
    ]

    print(game_map)
    mapHeight = len(game_map)
    mapWidth = len(game_map[0])

    FOV = math.pi / 4
    depth = mapWidth

    def __init__(self, root = None):
        tk.Frame.__init__(self, root)
        self.grid()
        self.grid = gc.grid(self.screenWidth, self.screenHeight, parent=self)
        self.grid.grid()
        self.bind_all("<Return>", self.close)
        self.bind_all("<Left>", self.left)
        self.bind_all("<Right>", self.right)
        self.bind_all("w", self.forward)
        self.bind_all("s", self.backward)
        self.bind_all("a", self.strave_left)
        self.bind_all("d", self.strave_right)
        self.after(1000, self.ray_cast)
        self.mainloop()

    def ray_cast(self):
        self.floorCeilingmap = []
        for x in range(self.screenWidth):
            rayAngle = (self.playerA - self.FOV / 2) + (x / self.screenWidth) * self.FOV
#            print(rayAngle)
            distance = 0.0
            hitWall = False

            eyeX = math.cos(rayAngle)
            eyeY = math.sin(rayAngle)
#            print(eyeX, eyeY)
            while not hitWall and distance < self.depth:
                distance += 0.1
#                print(math.floor(self.playerX + eyeX * distance))
#                print(math.floor(self.playerY + eyeY * distance))

                testX = math.floor(self.playerX + eyeX * distance)
                testY = math.floor(self.playerY + eyeY * distance)
                if testX < 0 or testX >= self.mapWidth or testY < 0 or testY >= self.mapHeight:
                    distance = self.depth
                    hitWall = True
#                print(self.game_map[testY][testX])
                if self.game_map[testY][testX] == "#":
                    hitWall = True
            #print(distance)
            ceilingHeight = self.screenHeight / 2 - self.screenHeight / distance
            floorHeight = self.screenHeight - ceilingHeight

            if distance <= self.depth:
                shade = math.floor(255/((self.depth/2)/distance))
                if shade > 255:
                    shade = 255
                shade = '#%02x%02x%02x' % (shade, shade, shade)
            else: shade = "white"
            for y in range(self.screenHeight):
                if y < ceilingHeight:
                    self.grid.boxlist[y*self.screenWidth+x].config(bg="white")
                elif y > ceilingHeight and y <= floorHeight:
                    self.grid.boxlist[y*self.screenWidth+x].config(bg=shade)
                else:
                    self.grid.boxlist[y*self.screenWidth+x].config(bg="white")



        #self.playerA -= 0.1
        #self.render()
        self.after(1, self.ray_cast)

    def forward(self, event=None):
        self.playerX += math.cos(self.playerA)*0.1
        self.playerY += math.sin(self.playerA)*0.1
        print(self.playerX, self.playerY, self.playerA)
    def backward(self, event=None):
        self.playerX -= math.cos(self.playerA)*0.1
        self.playerY -= math.sin(self.playerA)*0.1
        print(self.playerX, self.playerY, self.playerA)

    def strave_left(self, event=None):
        self.playerX -= math.sin(self.playerA)*0.1
        self.playerY -= math.cos(self.playerA)*0.1
        print(self.playerX, self.playerY, self.playerA)

    def strave_right(self, event=None):
        self.playerX += math.sin(self.playerA)*0.1
        self.playerY += math.cos(self.playerA)*0.1
        print(self.playerX, self.playerY, self.playerA)

    def left(self, event= None):
        self.playerA -= 0.08
        print(self.playerA)

    def right(self, event = None):
        self.playerA += 0.08
        print(self.playerA)

    def close(self, event=None):
        quit()

    def render(self):
        pass
#        y = -1
#        for x, i in enumerate(self.grid.boxlist):
#            if x % 40 == 1:
#                y += 1
#            if self.floorCeilingmap[y][0] <= x % 40 or self.floorCeilingmap[y][1] >= x % 40:
#                i.configure(bg='white')
#            else:
#                i.configure(bg='black')


root = tk.Tk()
main(root)
