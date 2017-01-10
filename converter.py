from Tkinter import *
import subprocess

def callback(radioButtonValue, textBoxvalue, fileTypeValue):
	if (fileTypeValue == "mp3"):
		if (radioButtonValue == 1):
			qualityString = '(bestaudio/best)[protocol^=http]'
		else:
			qualityString = '(worstaudio/worst)[protocol^=http]'
			 
		try:
			subprocess.check_output('youtube-dl -f "' + qualityString + '" --extract-audio --audio-format mp3 --output "%(title)s.%(ext)s" ' + textBoxvalue , shell=True)
			# subprocess.check_output('youtube-dl -f mp4 --output "%(title)s.%(ext)s" ' + textBoxvalue , shell=True)

		except subprocess.CalledProcessError as e:
			print ('Link is invalid')
	else:
		try:
			subprocess.check_output('youtube-dl -f ' + fileTypeValue + ' --output "%(title)s.%(ext)s" ' + textBoxvalue , shell=True)

		except subprocess.CalledProcessError as e:
			print ('Link is invalid')

def makeGUI():
	root = Tk()
	root.wm_title("Youtube to Mp3")
	root.resizable(False, False)

	radioFrame = Frame(root)
	radioFrame.pack(side=TOP, pady=10, padx=10)

	var = StringVar()
	label = Label(radioFrame, textvariable=var)
	var.set("Quality" + "\n" + "(mp3)")
	label.grid(row=1, column=1, sticky="w", pady=5)


	qualityBtn = IntVar()
	Radiobutton(radioFrame, text="Best", variable=qualityBtn, value=1, anchor="w").grid(row=2, column=1, sticky="w", pady=2, padx=5)
	Radiobutton(radioFrame, text="Worst", variable=qualityBtn, value=2, anchor="w").grid(row=3, column=1, sticky="w", pady=2, padx=5)

	var = StringVar()
	label = Label(radioFrame, textvariable=var)
	var.set("File Type")
	label.grid(row=1, column=3, sticky="w", pady=5, padx=5)

	fileTypeBtn = StringVar()
	Radiobutton(radioFrame, text="3gp", variable=fileTypeBtn, value="3gp", anchor="w").grid(row=2, column=2, sticky="w", pady=2, padx=5)
	Radiobutton(radioFrame, text="acc", variable=fileTypeBtn, value="acc", anchor="w").grid(row=3, column=2, sticky="w", pady=2, padx=5)
	Radiobutton(radioFrame, text="flv", variable=fileTypeBtn, value="flv", anchor="w").grid(row=4, column=2, sticky="w", pady=2, padx=5)
	Radiobutton(radioFrame, text="m4a", variable=fileTypeBtn, value="m4a", anchor="w").grid(row=2, column=3, sticky="w", pady=2, padx=5)
	Radiobutton(radioFrame, text="mp3", variable=fileTypeBtn, value="mp3", anchor="w").grid(row=3, column=3, sticky="w", pady=2, padx=5)
	Radiobutton(radioFrame, text="mp4", variable=fileTypeBtn, value="mp4", anchor="w").grid(row=4, column=3, sticky="w", pady=2, padx=5)
	Radiobutton(radioFrame, text="ogg", variable=fileTypeBtn, value="ogg", anchor="w").grid(row=2, column=4, sticky="w", pady=2, padx=5)
	Radiobutton(radioFrame, text="wav", variable=fileTypeBtn, value="wav", anchor="w").grid(row=3, column=4, sticky="w", pady=2, padx=5)
	Radiobutton(radioFrame, text="webm", variable=fileTypeBtn, value="webm", anchor="w").grid(row=4, column=4, sticky="w", pady=2, padx=5)
	fileTypeBtn.set("mp3")

	sumbitFrame = Frame(root)
	sumbitFrame.pack(side=BOTTOM)

	e1 = Entry(sumbitFrame, bd = 1, highlightcolor="white")
	e1.insert(0, "Enter a link")
	e1.grid(row=1, column=1, sticky="w")

	MyButton1 = Button(sumbitFrame, text="Submit", width=10, command= lambda: callback(qualityBtn.get(), e1.get(), fileTypeBtn.get()))
	MyButton1.grid(row=1, column=2)

	mainloop()

def Main():
	makeGUI()

if __name__ == '__main__':
	Main()


