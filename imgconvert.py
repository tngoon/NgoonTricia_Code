#merge pngs

import os
import subprocess

subfile = open("test.txt",'r')
sublist = subfile.read().split('\n')
# del sublist[-1]

# Edit name of file containing list of sessions
imagefile = open("tasks.txt", 'r') #edit name of session list file
imagelist = imagefile.read().split('\n')
del imagelist[-1]


for subject in sublist:
	imgs = []
	for image in imagelist:
		# Specifies which image to display		
		filename = '/Users/triciangoon/Desktop/comics/%s-%s.png' % (subject, image)

		imgs.append(filename)
	print(imgs)
	final = '/Users/triciangoon/Desktop/comics/%s.png' % (subject)
		# #-append for vertical, +append for horizontal
	os.chdir('/usr/local/Cellar/imagemagick/7.0.10-28/bin/')
	cmd = 'mogrify -append'
	outputs = cmd + " " + str(imgs) + " "+ final
	print(outputs)	
	subprocess.call(outputs, shell=True)
	# '/usr/local/Cellar/imagemagick/7.0.10-28/bin/convert -append ' + str(imgs) + ' final', shell=True)

# f = os.popen('/bin/ls -1')
# fil = f.read()
# arfils = fil.split("\n")
# arfils.pop()
# num = 0
# tot = 0

# for snc in arfils:
# f = os.popen( "/usr/bin/identify -ping -format '%w %h' " + '\"' + snc + '\"' )
#     rslt = f.read()
#     woh = rslt.split(" ")
#     intvl = int(woh[0])
#     tot = tot + intvl
#     num = num + 1

# avg = tot // num

# num = 1
# allfil = ""
# for snc in arfils:
#     nout = "tmpf" + str(num).zfill(4) + ".png"
#     allfil = allfil + nout + " "
#     convcmd = "convert " + '\"' + snc + '\"' + " -resize " + str(avg) + " -quality 100 "
#     convcmd = convcmd + '\"' + nout + '\"'
#     #print convcmd
#     f = os.popen(convcmd)
#     num = num + 1

# mrg = "convert -append " + allfil + "output.png"
# f = os.popen(mrg)