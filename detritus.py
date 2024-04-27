import pygame
import glob
import random
import sys
import os

seconds_between_images = 2 * 1000  # The desired seconds should be multiplied by 1000

def main():

    images_directory = "/home/pi/detritus/media" # Replace this directory with the directory where you save the images 

    # Initialize pygame
    pygame.init()

    # Set up the screen
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("detritus")

    # Hide the cursor
    pygame.mouse.set_visible(False)

    # Get the list of image files in the specified directory
    image_files = glob.glob(os.path.join(images_directory, "*.jpg")) 
    random.shuffle(image_files) 

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    running = False

        if not image_files:
            image_files = glob.glob(os.path.join(images_directory, "*.jpg"))
            random.shuffle(image_files)

        # Load and resize the image to fit the screen
        if image_files:
            image_path = image_files.pop()  
            image = pygame.image.load(image_path)
            image = pygame.transform.scale(image, (screen.get_width(), screen.get_height()))

            # Display the image on the screen
            screen.blit(image, (0, 0))
            pygame.display.flip()

            # Wait seconds_between_images milliseconds before switching to the next image
            pygame.time.wait(seconds_between_images)

            # Clear the screen
            screen.fill((0, 0, 0))

        # Update the screen
        pygame.display.update()

        clock.tick(60)

        # Check if 'q' has been pressed and exit immediately
        if pygame.key.get_pressed()[pygame.K_q]:
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()
