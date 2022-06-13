import pygame


class Grid:
    def __init__(self, xGrid, yGrid, type, border, grid_size, top_border, display, spritesDict, width, height):
        self.xGrid = xGrid  # X pos of grid
        self.yGrid = yGrid  # Y pos of grid
        self.clicked = False  # Boolean var to check if the grid has been clicked
        self.mineClicked = False  # Bool var to check if the grid is clicked and its a mine
        self.mineFalse = False  # Bool var to check if the player flagged the wrong grid
        self.flag = False  # Bool var to check if player flagged the grid
        # Create rectObject to handle drawing and collisions
        self.rect = pygame.Rect(border + self.xGrid * grid_size, top_border + self.yGrid * grid_size, grid_size,
                                grid_size)
        self.val = type  # Value of the grid, -1 is mine
        global gameDisplay
        global sprites
        global game_width

        global game_height
        sprites = spritesDict
        gameDisplay = display
        game_width = width
        game_height = height

    def drawGrid(self):
        # Draw the grid according to bool variables and value of grid
        if self.mineFalse:
            gameDisplay.blit(sprites['spr_mineFalse'], self.rect)
        else:
            if self.clicked:
                if self.val == -1:
                    if self.mineClicked:
                        gameDisplay.blit(sprites['spr_mineClicked'], self.rect)
                    else:
                        gameDisplay.blit(sprites['spr_mine'], self.rect)
                else:
                    if self.val == 0:
                        gameDisplay.blit(sprites['spr_emptyGrid'], self.rect)
                    elif self.val == 1:
                        gameDisplay.blit(sprites['spr_grid1'], self.rect)
                    elif self.val == 2:
                        gameDisplay.blit(sprites['spr_grid2'], self.rect)
                    elif self.val == 3:
                        gameDisplay.blit(sprites['spr_grid3'], self.rect)
                    elif self.val == 4:
                        gameDisplay.blit(sprites['spr_grid4'], self.rect)
                    elif self.val == 5:
                        gameDisplay.blit(sprites['spr_grid5'], self.rect)
                    elif self.val == 6:
                        gameDisplay.blit(sprites['spr_grid6'], self.rect)
                    elif self.val == 7:
                        gameDisplay.blit(sprites['spr_grid7'], self.rect)
                    elif self.val == 8:
                        gameDisplay.blit(sprites['spr_grid8'], self.rect)

            else:
                if self.flag:
                    gameDisplay.blit(sprites['spr_flag'], self.rect)
                else:
                    gameDisplay.blit(sprites['spr_grid'], self.rect)

    def revealGrid(self):
        self.clicked = True
        # Auto reveal if it's a 0
        if self.val == 0:
            for x in range(-1, 2):
                if self.xGrid + x >= 0 and self.xGrid + x < game_width:
                    for y in range(-1, 2):
                        if self.yGrid + y >= 0 and self.yGrid + y < game_height:
                            if not grid[self.yGrid + y][self.xGrid + x].clicked:
                                grid[self.yGrid + y][self.xGrid + x].revealGrid()
        elif self.val == -1:
            # Auto reveal all mines if it's a mine
            for m in mines:
                if not grid[m[1]][m[0]].clicked:
                    grid[m[1]][m[0]].revealGrid()

    def updateValue(self):
        # Update the value when all grid is generated
        if self.val != -1:
            for x in range(-1, 2):
                if self.xGrid + x >= 0 and self.xGrid + x < game_width:
                    for y in range(-1, 2):
                        if self.yGrid + y >= 0 and self.yGrid + y < game_height:
                            if grid[self.yGrid + y][self.xGrid + x].val == -1:
                                self.val += 1