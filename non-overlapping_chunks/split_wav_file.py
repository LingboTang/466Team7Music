from pydub import AudioSegment
import os

def main():
	""" This dumb script splits the first 30 seconds of every wav track in a directory,
		and saves every 100 of them in different directories (so at most 3000 file per new directory).
		Splits the 507 tracks in 1 sec chunks and further distributes them in multiple folders for easy task distribution. 
	"""


	directory = ''
	count = 0
	folder = 0
	inputdir = "/Users/Maxime/Documents/University/2015/Cmput466/Project/ILAM_samples_wav/" 	# change this
	for filename in os.listdir(inputdir):

		song = AudioSegment.from_wav(inputdir+filename)

		start = 0
		end = 1000

		if count % 100 == 0:
			folder +=1

			if not os.path.exists("chunks"+str(folder)):
				print("chunks"+str(folder))
				os.makedirs("chunks"+str(folder))
			directory = "chunks"+str(folder)

		for interval in range(30):
			
			chunk = song[start:end]

			print(directory+'/'+filename+str(interval+1)+".wav")
			chunk.export(directory+'/'+filename+str(interval+1)+".wav", format="wav")

			start += 1000 
			end += 1000 

		count +=1

if __name__ == "__main__":
	main()