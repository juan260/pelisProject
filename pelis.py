'''
pelis.py

Random film mixer. Takes some films, chops them, picks random chops
and voila! Random mix of the films.

How to use:
    - The code takes at least 3 arguments:
        1. Number of chops that will compose the final mix
        2. Path of the final mix
        Rest. Paths of the different movie clips to be mixed

    - The code has only been tested with mp4 files
    - The movie clips must have a minimum duration specified by the
        variable called "duration". This duration will be the duration
        of each chop. In further updates arbitrary duration clip support
        might be implemented.
'''

from moviepy.editor import VideoFileClip, concatenate_videoclips
import sys
from random import randint, random
from math import floor

if len(sys.argv)<4:
    print("[ERROR] Modo de uso. Argumentos: ")
    print("   1. Numero de clips")
    print("   2. Nombre de la salida")
    print("   Etc: lista de pelis")
    exit()

duration=1

pelis = sys.argv[3:]
for i in range(len(pelis)):
    pelis[i]=VideoFileClip(pelis[i])
    if pelis[i].duration < duration:
        print("[ERROR] No se aceptan pelis de menos de " + str(duration) + " segundos")
        exit()

num = int(sys.argv[1])
peli = pelis[randint(0, len(pelis)-1)]
inicio = random()*(peli.duration-duration)
finalClip = peli.subclip(inicio, inicio+duration)

for i in range(1, num):
    print("[DEBUG] Duration :" + str(finalClip.duration))
    peli = pelis[randint(0, len(pelis)-1)]
    inicio = random()*(peli.duration-duration)
    finalClip = concatenate_videoclips([finalClip, peli.subclip(inicio, inicio+duration)], method="compose")

finalClip.write_videofile(sys.argv[2])
print("Done!")

