#!/usr/bin/python3
import cv2
import numpy as np
import subprocess
import os
from pathlib import Path
def main():
    try:
        music_player = subprocess.run('playerctl status --format "{{ uc(status) }}"',shell=True,stdout=subprocess.PIPE, text=True).stdout
        if(music_player == ''):
            return
        
        directory = str(Path.home()) + "/.cache/eww/music_player"

        # Verify if title is equal to the data
        name_track = subprocess.run("playerctl metadata --format '{{title}}'",shell=True,stdout=subprocess.PIPE, text=True).stdout
        image_track = subprocess.run("playerctl metadata --format '{{mpris:artUrl}}'",shell=True,stdout=subprocess.PIPE, text=True).stdout.strip()

        if(os.path.isfile(directory + "/song_name")):
            file = open(directory + "/song_name", "r")
            content = file.read()

        if content == name_track:
            return

        # Read the image path

        w_download = f"wget --adjust-extension {image_track} -O {directory}/image"

        print(w_download)
        subprocess.run(w_download, shell=True)

        name, extension = os.path.splitext(directory + "/image")
        print("Name: ", name)
        print("File Extension: ", extension)
        path_image = f"{directory}/image" 
        image = cv2.imread(path_image, cv2.IMREAD_COLOR)

        #Display image

        cv2.imshow('Image', image)
        cv2.destroyAllWindows()

        # Extracting Image Parameters

        height, width, channels = image.shape[:3]

        # Reshaping Image Data
        data = np.reshape(image, (height * width, channels)).astype(np.float32)

        num_clusters = 3

        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

        flags = cv2.KMEANS_RANDOM_CENTERS
        compactness, labels, centers = cv2.kmeans(data, num_clusters, None, criteria, 10, flags)

        # Displaying Dominant Colors

        colors = []

        for color in centers:
            colors.append(str(color[2]) + ',' + str(color[1]) + "," + str(color[0]))
        
        # Select the darkest color for the background
        
        def calculate_luminosity(color):
            r, g, b = map(float, color.split(','))
            luminosity = 0.2126*r + 0.7152*g + 0.0722*b
            return luminosity

        darkest_color = None
        darkest_color_position = None
        darkest_luminosity = float('inf')

        for x, color in enumerate(colors):
            luminosity = calculate_luminosity(color)
            if luminosity < darkest_luminosity:
                darkest_color = color
                darkest_color_position = x
                darkest_luminosity = luminosity

        print("Darkest color:", darkest_color)

        print(colors)
        # Data to be written
    
        if not os.path.exists(directory):
            os.makedirs(directory)
        

        # Writing files
        with open(directory + "/song_name", "w") as outfile:
            outfile.write(name_track)

        with open(directory + "/background_color", "w") as outfile:
            outfile.write(colors[darkest_color_position])

        with open(directory + "/text_color", "w") as outfile:
            outfile.write(colors[(darkest_color_position + 1) % len(colors)])

        with open(directory + "/indicator_color", "w") as outfile:
            outfile.write(colors[(darkest_color_position - 1 + len(colors)) % len(colors)])
    except:
        with open(directory + "/song_name", "w") as outfile:
            outfile.write("")

        with open(directory + "/background_color", "w") as outfile:
            outfile.write("9,7,16")

        with open(directory + "/text_color", "w") as outfile:
            outfile.write("255,255,255")

        with open(directory + "/indicator_color", "w") as outfile:
            outfile.write("59,59,63")

main()