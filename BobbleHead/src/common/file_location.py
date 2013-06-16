from os.path import join


class FileLocation(object):
    
    _IMAGES = "images"
    _SOUNDS = "sounds"
    
    BACKGROUND_IMAGE_LOCATION = join(_IMAGES, "background.png")
    HEAD_IMAGE_LOCATION = join(_IMAGES, "timhead.png")
    ICON_IMAGE_LOCATION = join(_IMAGES, "BobbleHead Bill_32X32.ico")
    
    MIDI = join(_SOUNDS, "Liberty Bell(midi sound).mp3")
    ARMY = join(_SOUNDS, "Monty Python`s Flying Circus Theme 1969 - 1974.mp3")
    VOCAB = join(_SOUNDS, "05 abeyance _ temporary inactivity or suspension.mp3")
    