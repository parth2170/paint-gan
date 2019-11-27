import os
import numpy as np 
from requests import get

def down(url, file_name):
	with open(file_name, "wb") as file:
		response = get(url)
		file.write(response.content)


def read(path):
	label = path[4:-4]
	print(label)
	savepath = 'down/'+label
	os.system('mkdir '+ savepath)
	with open(path) as file:
		i = 0
		for line in file:
			url = line[10:-14]
			i += 1
			down(url, savepath+'/'+str(i)+'.jpg')

if __name__ == '__main__':
	files = os.listdir('bam/')
	for file in files:
		if file[-3:] != 'htm':
			continue
		read('bam/'+file)