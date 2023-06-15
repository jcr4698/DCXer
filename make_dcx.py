import sys
import numpy as np

def main():

    # Make sure func has at least a name
    if(len(sys.argv) <= 1):
        print("I require at least one file name")
        return

    # Func has at least a name, now ask for content for the dcx
    else:
        dcx_names = sys.argv[1:len(sys.argv)]
        # print(file_names)
        
        print()
        for dcx_name in dcx_names:

            # Prompt user for DCX information
            print("DCX file '" + dcx_name + "' will be created.")
            file_amt = int(input("How many files will be in this file? "))
            print("OK...\n")
            
            # files to add to dcx file
            files = np.array([])

            # prompt user the names of the files
            for file_num in range(file_amt):
                file_name = input("file " + str(file_num) + ": ")
                files = np.append(files, file_name)
            
            print()

            # display array
            for file_name in files:
                print(file_name)
                # make a dcx
                # determine if file_name is an actual file
                # add file into dcx

            # inform user of file creation
            print("DCX file '" + dcx_name + "' has been created.\n")

main()
