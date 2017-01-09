from Tkinter import *
import subprocess

def callback():
	link =  e1.get()
	try:
		subprocess.check_output('youtube-dl -f "(bestaudio/best)[protocol^=http]" --extract-audio --audio-format mp3 --output "%(title)s.%(ext)s"' + " " + link , shell=True)
	except subprocess.CalledProcessError as e:
		print ('Link is invalid')

root = Tk()
root.wm_title("Youtube to Mp3")

# v = IntVar()

# Radiobutton(root, text="One", variable=v, value=1).pack(anchor=W)
# Radiobutton(root, text="Two", variable=v, value=2).pack(anchor=W)

e1 = Entry(root, bd = 1, highlightcolor="white")
e1.insert(0, "Enter a link")
e1.pack(anchor=W)

MyButton1 = Button(root, text="Submit", width=10, command=callback)
MyButton1.pack(anchor=W)


# root.minsize(width=500, height=500)
mainloop()


