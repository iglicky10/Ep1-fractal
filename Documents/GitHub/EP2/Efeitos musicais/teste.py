#nd = Sound()
#sd.read('4-casino.mp3')
#nd.play()

#mport Tkinter 
#kinter.Tk().tk.eval('info tclversion')
#nack::sound snd 
#nd read 134-casino.wav
#nd play



import pyglet

music = pyglet.resource.media("casino.mp3")
music.play()

pyglet.app.run()