#create a pygame window and draw a circle
import pygame
import random

#initialize pygame
#wrtie main function
def main():
    pygame.init()

    #create the screen
    screen = pygame.display.set_mode((800, 600))

    #title and icon
    pygame.display.set_caption("Circle")
    icon = pygame.image.load("C:/Users/Dhanasree Vijay Sai/OneDrive/Pictures/firetruck_policecar.png")
    pygame.display.set_icon(icon)

    #draw a circle on the screen
    #color, position, radius, width
    pygame.draw.circle(screen, (255, 0, 0), (400, 300), 100, 0)
    
    background = pygame.image.load("C:/Users/Dhanasree Vijay Sai/OneDrive/Pictures/firetruck_policecar.png")

    #call the draw_circle function
    pygame.draw.circle(screen, (255, 0, 0), (50, 50), 100)
    pygame.draw.rect(screen, (255, 255, 0), (90, 90, 100, 100))
    
    val = input("Enter a number: ")
#call the main function
main()

    
