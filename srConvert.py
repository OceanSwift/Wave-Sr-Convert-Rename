import sys
import os

from scipy.io import wavfile

thisdir = os.getcwd()
pattern = ".wav"
samplerate = 32000
subdir = "converted"
rename = True

def main():
	if len(sys.argv) > 1:
		if sys.argv[1] == '?':
			print("arg1 = sub dir name")
			print("arg2 = samplerate")
			print("arg3 = rename numbering true/false")
			return
		else:			
			subdir = sys.argv[1]
	else:
		subdir = "converted"
	if len(sys.argv) > 2:
		samplerate = int(sys.argv[2])
	else:
		samplerate = 32000					
	if len(sys.argv) > 3:
		if sys.argv[3] == 'true':
			rename = True
		else:			
			rename = False
	else:
		rename = True

	if os.path.isdir(thisdir + "\\" + subdir) == False:
		os.mkdir(thisdir + "\\" + subdir)

	entriesList = [x for x in os.listdir() if x.endswith(".wav")]
	for entry in entriesList:
		if entry != '':
			sr, data = wavfile.read(thisdir +"\\"+ entry)
			wavfile.write((os.path.join(thisdir,subdir,entry)), samplerate, data)

	print(str(len(entriesList)-1) + " Samples converted")

	numberList = ["%.2d" % i for i in range(len(entriesList))]

	if rename == True:
		fileList = [x for x in os.listdir(thisdir + "\\" + subdir + "\\") if x.endswith(".wav")]	
		i = 0
		for selections in fileList:
			if selections != '':
				os.rename(thisdir + "\\" + subdir + "\\" + selections, thisdir + "\\" + subdir + "\\" + numberList[i] + ".wav")
				i +=1	

if __name__ == "__main__":
    main()
       
