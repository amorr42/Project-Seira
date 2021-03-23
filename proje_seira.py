from controller import Control
import speech_recognition as sr
import tkinter as tk
import pygame


def sesCal():
    # Müzik dosyasında bulunan sesi çalar.
    # Bu ses mikrofonun aktif hale geldiğini kullanıcıya bildirmiş olur.
    pygame.mixer.init()
    pygame.mixer.music.load("click.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue


def asistan():
    try:
        global root
        root.destroy()
    except:
        pass
    while True:
        sesCal()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)
        try:
            data = ""
            data = r.recognize_google(audio, language='tr-TR')
            print(data)
            komut = Control(data)
            komut.komutBul()
        except sr.UnknownValueError:
            i = "geçici"
            komut = Control(i)
            komut.seslendirme("Anlayamadım")
        except sr.RequestError:
            i = "geçici"
            komut = Control(i)
            komut.seslendirme("Sistem çalışmıyor")


root = tk.Tk()
root.image = tk.PhotoImage(file='resim.png')
button = tk.Button(root, image=root.image, bg='white', command=asistan)
root.overrideredirect(True)
root.geometry("400x400+800+300")
root.wm_attributes("-transparentcolor", "white")
button.pack()
root.mainloop()
