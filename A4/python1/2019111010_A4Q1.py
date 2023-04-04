def count_words(filename,filename2):
    try:
        with open(filename) as file_object:
            contents=file_object.read()
    except FileNotFoundError:
        msg="Sorry,the file "+filename+" does not exist."
        print(msg)
    else:
        words=contents.split()
        num_words=len(words)
        print("The file "+filename+" has about "+str(num_words)+" words.")
        with open(filename2,'w') as f_obj:
            f_obj.write(str(num_words))
filename='Harry_Potter.txt'
filename2='Count_Words.txt'
Count_Words=count_words(filename,filename2)
