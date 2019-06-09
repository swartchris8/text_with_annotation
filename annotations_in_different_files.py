import os
import os.path

for file_name in os.listdir("data"):
    if file_name.endswith(".txt"):
        print(os.path.join("data", file_name))
	# get file name that doesn't contain .txt so in this case
	# it will make example from example.txt this way we get the link
	# between text files and their annotations
	file_base_name = file_name[:-4]

	file_name_a1 = file_base_name + ".a1" # this would be example.a1
	if os.path.isfile(file_name_a1): # check if annotation exists
	    
	    # code to read in txt file and code to read a1...
