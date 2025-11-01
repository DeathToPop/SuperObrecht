import pygame as pg
from . import setup, tools
from . import constants as c
from .states import main_menu, load_screen, level
from . import audio
import os
import sys
from pygame import mixer

def main():
    # Sound beim Start abspielen
    play_start_sound()
    
    game = tools.Control()
    state_dict = {c.MAIN_MENU: main_menu.Menu(),
                  c.LOAD_SCREEN: load_screen.LoadScreen(),
                  c.LEVEL: level.Level(),
                  c.GAME_OVER: load_screen.GameOver(),
                  c.TIME_OUT: load_screen.TimeOut()
                  }
    game.setup_states(state_dict, c.MAIN_MENU)
    game.main()

def play_start_sound():
    try:
        # Verschiedene Pfad-Optionen versuchen
        sound_file = "musik.wav"
        
        # Option 1: Aktuelles Verzeichnis
        if os.path.exists(sound_file):
            sound = pg.mixer.Sound(sound_file)
            sound.play()
            print("Start-Sound wird abgespielt")
            return
        
        # Option 2: Verzeichnis der main.py Datei
        current_dir = os.path.dirname(os.path.abspath(__file__))
        sound_path = os.path.join(current_dir, sound_file)
        
        if os.path.exists(sound_path):
            sound = pg.mixer.Sound(sound_path)
            sound.play()
            print("Start-Sound wird abgespielt (aus Hauptverzeichnis)")
            return
        
        # Option 3: In Unterordnern suchen
        for root, dirs, files in os.walk(os.path.dirname(os.path.abspath(__file__))):
            if sound_file in files:
                sound_path = os.path.join(root, sound_file)
                sound = pg.mixer.Sound(sound_path)
                sound.play()
                print(f"Start-Sound wird abgespielt (gefunden in: {root})")
                return
        
        print(f"Sound-Datei '{sound_file}' nicht gefunden")
        print(f"Aktuelles Verzeichnis: {os.getcwd()}")
        print(f"Main-Verzeichnis: {os.path.dirname(os.path.abspath(__file__))}")
        
    except pg.error as e:
        print(f"Fehler beim Abspielen des Sounds: {e}")
    except Exception as e:
        print(f"Unerwarteter Fehler: {e}")

# Automatisch ausführen wenn main.py direkt ausgeführt wird
if __name__ == "__main__":
    main()