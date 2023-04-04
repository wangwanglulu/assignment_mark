with open('Harry_Potter.txt') as file_object:
 contents = file_object.read() # string
 counts = 0
 words = contents.split()
 for word in words:
        counts = counts + 1
filename = 'Count_Words.txt'
with open(filename, 'w') as file_object:
    file_object.write("There are {} words in the file.".format(counts))
