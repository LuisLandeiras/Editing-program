import threading
from PIL import Image
from PIL import ImageShow
import numpy as np
import cv2
import moviepy.editor as mymovie

# Black algorithm:
def black(filename):
    image = Image.open(filename)
    black_image = Image.new(image.mode, image.size, 'black')
    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):
            pixelColorVals = image.getpixel((i, j)) 

            Pixel = int (0.2126*pixelColorVals[0] + 0.7152*pixelColorVals[1] + 0.0722*pixelColorVals[2])
            black_image.putpixel((i, j), (Pixel, Pixel, Pixel))

    black_image.show()
    black_image.save("black.jpeg")

# Canal vermelho de uma imagem
def red(filename):
    image = Image.open(filename)
    red_image = Image.new(image.mode, image.size, 'red')
    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):
            pixelColorVals = image.getpixel((i, j))

            red_image.putpixel((i, j), (pixelColorVals[0]))
    red_image.show()
    red_image.save("RedImage.jpeg")

# Adição de imagens
def add(filename1, filemane2):
    image = Image.open(filename1)
    image1 = Image.open(filemane2)
    adicao_image = Image.new(image.mode, image.size)
    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):
            pixelColorVals = image.getpixel((i, j))
            pixelColorVals1 = image1.getpixel((i, j))

            if pixelColorVals[0] + pixelColorVals1[0] < 255:
                Pixelred = pixelColorVals[0] + pixelColorVals1[0]
            else:
                Pixelred = 255

            if pixelColorVals[1] + pixelColorVals1[1] < 255:
                Pixelgreen = pixelColorVals[1] + pixelColorVals1[1]
            else:
                Pixelgreen = 255

            if pixelColorVals[2] + pixelColorVals1[2] < 255:
                Pixelblue = pixelColorVals[2] + pixelColorVals1[2]
            else:
                Pixelblue = 255

            adicao_image.putpixel((i, j), (Pixelred, Pixelgreen, Pixelblue))
            
            
    adicao_image.show()
    adicao_image.save("AdicaoImage.jpeg")
    
def sub(filename1, filemane2):
    image = Image.open(filename1)
    image1 = Image.open(filemane2)
    adicao_image = Image.new(image.mode, image.size)
    for i in range(0, image.size[0] - 1):
        for j in range(0, image.size[1] - 1):
            pixelColorVals = image.getpixel((i, j))
            pixelColorVals1 = image1.getpixel((i, j))

            if pixelColorVals[0] - pixelColorVals1[0] > 0:
                Pixelred = pixelColorVals[0] - pixelColorVals1[0]
            else:
                Pixelred = 0

            if pixelColorVals[1] - pixelColorVals1[1] > 0:
                Pixelgreen = pixelColorVals[1] - pixelColorVals1[1]
            else:
                Pixelgreen = 0

            if pixelColorVals[2] - pixelColorVals1[2] > 0:
                Pixelblue = pixelColorVals[2] - pixelColorVals1[2]
            else:
                Pixelblue = 0

            adicao_image.putpixel((i, j), (Pixelred, Pixelgreen, Pixelblue))
            
            
    adicao_image.show()
    adicao_image.save("SubImage.jpeg") 
               
def log(filename1, filename2):
    image_log1 = Image.open(filename1)
    image_log2 = Image.open(filename2)
    log1_image = Image.new(image_log1.mode, image_log1.size)
    log2_image = Image.new(image_log2.mode, image_log2.size)
    bollean_image = Image.new(image_log1.mode, image_log1.size)
    for i in range(0, image_log1.size[0] - 1):
        for j in range(0, image_log1.size[1] - 1):
            pixelColorVals1 = image_log1.getpixel((i, j))
            pixelColorVals2 = image_log2.getpixel((i, j))

            red = pixelColorVals1[0] in list(
                range(pixelColorVals2[0] - 2, pixelColorVals2[0] + 2))
            green = pixelColorVals1[1] in list(
                range(pixelColorVals2[1] - 2, pixelColorVals2[1] + 2))
            blue = pixelColorVals1[2] in list(
                range(pixelColorVals2[2] - 2, pixelColorVals2[2] + 2))

            if red and green and blue:
                Pixel = 255
            else:
                Pixel = 0

            bollean_image.putpixel((i, j), (Pixel, Pixel, Pixel))

    bollean_image.putpixel((i, j), (Pixel, Pixel, Pixel))
    bollean_image.show()
    bollean_image.save("Bollean.jpg")
    
def log1(filename1, filename2):
    image_log1 = Image.open(filename1)
    image_log2 = Image.open(filename2)
    log1_image = Image.new(image_log1.mode, image_log1.size)
    log2_image = Image.new(image_log2.mode, image_log2.size)
    bollean_image = Image.new(image_log1.mode, image_log1.size)
    for i in range(0, image_log1.size[0] - 1):
        for j in range(0, image_log1.size[1] - 1):
            pixelColorVals1 = image_log1.getpixel((i, j))
            pixelColorVals2 = image_log2.getpixel((i, j))

            red = pixelColorVals1[0] in list(
                range(pixelColorVals2[0] - 2, pixelColorVals2[0] + 2))
            green = pixelColorVals1[1] in list(
                range(pixelColorVals2[1] - 2, pixelColorVals2[1] + 2))
            blue = pixelColorVals1[2] in list(
                range(pixelColorVals2[2] - 2, pixelColorVals2[2] + 2))

            if red and green and blue:
                Pixel = 0
            else:
                Pixel = 255

            bollean_image.putpixel((i, j), (Pixel, Pixel, Pixel))

    bollean_image.putpixel((i, j), (Pixel, Pixel, Pixel))
    bollean_image.show()
    bollean_image.save("Bollean1.jpg")

#Adiciona o audio original ao video em grayscale
def sound(filename):
    cap = cv2.VideoCapture(filename)
    fps = cap.get(cv2.CAP_PROP_FPS)
    for i in range(0, len(filename)):
        if filename[i] == "/":
            x = i
    inputvideo = "out.mp4"
    inputaudio = filename#filename[-(len(filename) - x - 1):]
    outputvideo = "output.mp4"

    videoclip = mymovie.VideoFileClip(inputvideo)
    audioclip = mymovie.AudioFileClip(inputaudio)
    finalclip = videoclip.set_audio(audioclip)
    finalclip.write_videofile(outputvideo, fps)

#Abertura do ficheiro de video e converte o video para grayscale
def video(filename, a):
    # cap -> variable used to save original video:
    cap = cv2.VideoCapture(filename)
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    #Video height and Width in pixel:
    height = cap.get(4)
    width = cap.get(3)
    
    # out -> variable used to save black and white video:
    out = cv2.VideoWriter('out.mp4', 0x7634706d, fps, (int(width), int(height)))
    # frame_total = Number of all frames:
    frame_total = (int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
    x = 0
    while x < frame_total:
        x = x + 1
        ret, RGB = cap.read()
        # Save blue, red and green value in variables:
        b, g, r = RGB[:, :, 0], RGB[:, :, 1], RGB[:, :, 2]
        # Takes a weighted average of red, green and blue pixels:
        grayscale = r*0.2126 + g*0.7152 + b*0.0722
        # Change the red, green and blue value to the new value grayscale
        RGB[:, 0 : int(width/a), 0] = grayscale[:, 0 : int(width/a)]
        RGB[:, 0 : int(width/a), 1] = grayscale[:, 0 : int(width/a)]
        RGB[:, 0 : int(width/a), 2] = grayscale[:, 0 : int(width/a)]

        out.write(RGB)

        # Open windows because start video player:
        cv2.imshow('frame', RGB)

        # Permite ao utilizador sair quando preciona a tecla Q:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # the video capture object
    cap.release()
    # Closes all the frames
    cv2.destroyAllWindows()

def movie(filename, x):
    video(filename, x)
    sound(filename)
    
