#!/usr/bin/python3
import cv2
import numpy as np
import subprocess
import os,time
import re
from pathlib import Path

directory = str(Path.home()) + "/.cache/eww/music_player"

def defaultData():
    with open(directory + "/song_name", "w") as outfile:
        outfile.write("")

    with open(directory + "/background_color", "w") as outfile:
        outfile.write("9,7,16")

    with open(directory + "/text_color", "w") as outfile:
        outfile.write("255,255,255")

    with open(directory + "/indicator_color", "w") as outfile:
        outfile.write("199,201,217")

def main():


    music_player = subprocess.run('playerctl metadata',shell=True,stdout=subprocess.PIPE, text=True).stdout
    if(music_player == '' or music_player == 'No player could handle this command'):
        return defaultData()

    # Verify if title is equal to the data
    name_track = subprocess.run("playerctl metadata --format '{{title}}'",shell=True,stdout=subprocess.PIPE, text=True).stdout
    image_track = subprocess.run("playerctl metadata --format '{{mpris:artUrl}}'",shell=True,stdout=subprocess.PIPE, text=True).stdout.strip()
    
    content = ''

    if(os.path.isfile(directory + "/song_name")):
        file = open(directory + "/song_name", "r")
        content = file.read()

    if content == name_track:
        return

    try:
        # Read the image path
        # Check if the image is obtained from file://
        is_file = re.match(r"(file)://", image_track)
       
        if is_file:
            split_path = image_track.split('file://',1)[1]
            path_image = split_path
        else:
            w_download = f"wget --adjust-extension {image_track} -O {directory}/image"
            subprocess.run(w_download, shell=True)
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
        
        def calculate_contrast(color1, color2):
            luminosity1 = calculate_luminosity(color1)
            luminosity2 = calculate_luminosity(color2)
            contrast = (max(luminosity1, luminosity2) + 0.05) / (min(luminosity1, luminosity2) + 0.05)
            return contrast
        
        def increase_contrast(color, factor):
            r, g, b = color.split(',')
            r = round(float(r))
            g = round(float(g))
            b = round(float(b))
            new_r = min(int(round(r) * factor), 255)
            new_g = min(int(round(g) * factor), 255)
            new_b = min(int(round(b) * factor), 255)
            return f'{new_r}, {new_g}, {new_b}'

        darkest_color = 0
        darkest_color_position = 0
        darkest_luminosity = float('inf')

        for x, color in enumerate(colors):
            luminosity = calculate_luminosity(color)
            if luminosity < darkest_luminosity:
                darkest_color = color
                darkest_color_position = x
                darkest_luminosity = luminosity

        # Compare darkest_color with other colors
        for x, color in enumerate(colors):
            if color != darkest_color:
                contrast = calculate_contrast(darkest_color, color)
                if contrast < 4:
                    new_color = increase_contrast(color, 1.8)
                    colors[x] = new_color

                if x > 0 and contrast < 7:
                    new_color = increase_contrast(color, 2.3)
                    colors[x] = new_color

                

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

    except Exception as error:
        print(error)
        defaultData()
while True:
    main()
    time.sleep(3)