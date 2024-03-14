# Author: Aidan Rudd
# Date: 3/6/24
# Description: Draws a GUI that asks for user input text and translates it into speech
from gtts import gTTS
import pygame
import tkinter as tk

j = 1

def clicked():
    global j
    i = 0
    if txt.get() == "":
        return
    for char in txt.get():
        if char != " ":
            i = 1
    if i == 0:
        return
    memory = tk.Label(root, text=txt.get())
    memory.grid(column=1, row=j)
    j += 1
    tts = gTTS(text=txt.get(), lang="en", tld="us", slow=False)
    tts.save("TTS.wav")
    pygame.mixer.init()
    sound_file = "C:/Users/fluff/PycharmProjects/TTS/TTS.wav"
    sound = pygame.mixer.Sound(sound_file)
    sound.play()

root = tk.Tk()
root.title("Text-to-Speech Program")
root.geometry("700x400")
lbl = tk.Label(root, text="Please input text to read out:")
lbl.grid()
hist = tk.Label(root, text="History:")
hist.grid(column=0, row=1)
txt = tk.Entry(root, width=50)
txt.grid(column=1, row=0)
btn = tk.Button(root, text="Click to input", width=25, fg="blue", command=clicked)
btn.grid(column=2, row=0)
root.mainloop()
