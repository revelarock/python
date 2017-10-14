# Faca um programa em python que abra e repoduca o audio de um arquivo MP3

import pyglet

music = pyglet.resource.media('hard2.mp3')
music.play()

pyglet.app.run()

