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
			url = line[10:-13]
			i += 1
			down(url, savepath+'/'+str(i)+'.jpg')

if __name__ == '__main__':
	read('bam/content_bird.htm')