from Tkinter import *
import subprocess

def callback(radioButtonValue, textBoxvalue):
	if (radioButtonValue == 1):
		qualityString = 'bestaudio/best'
	else:
		qualityString = 'worstaudio/worst'
		 
	try:
		subprocess.check_output('youtube-dl -f "(' + qualityString + ')[protocol^=http]" --extract-audio --audio-format mp3 --output "%(title)s.%(ext)s" ' + textBoxvalue , shell=True)
	except subprocess.CalledProcessError as e:
		print ('Link is invalid')
		e1.highlightcolor="red"

def makeGUI():
	root = Tk()
	root.wm_title("Youtube to Mp3")

	var = StringVar()
	label = Label(root, textvariable=var)
	var.set("Audio Quality")
	label.pack(anchor=CENTER)


	v = IntVar()
	Radiobutton(root, text="Best", variable=v, value=1).pack(anchor=CENTER)
	Radiobutton(root, text="Worst", variable=v, value=2).pack(anchor=CENTER)
	v.set(1)

	e1 = Entry(root, bd = 1, highlightcolor="white")
	e1.insert(0, "Enter a link")
	e1.pack(anchor=CENTER)

	MyButton1 = Button(root, text="Submit", width=10, command= lambda: callback(v.get(), e1.get()))
	MyButton1.pack(anchor=CENTER)


	root.minsize(width=500, height=300)
	mainloop()

def Main():
	makeGUI()

if __name__ == '__main__':
	Main()


