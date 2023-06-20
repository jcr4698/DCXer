import sys
import numpy as np
from check_dcx import is_stallion_file, create_dcx, write_to_dcx, close_dcx, get_pos_and_dims
import tkinter as tk
from tkinter import filedialog

CONTENT_DIR = "/mnt/c/Users/jan/Desktop/Files/Work_Material/Employment/Visualizations_Lab/Display_Cluster/DCXer/Content/"
DCX_DIR = "/mnt/c/Users/jan/Desktop/Files/Work_Material/Employment/Visualizations_Lab/Display_Cluster/DCXer/dcx_files/"

STALLION_SCREEN_WIDTH = 6
STALLION_SCREEN_HEIGHT = 3

def main():

    # Make sure func has at least a name
    if(len(sys.argv) <= 1):
        print("I require at least one file name")
        return

    # Func has at least a name, now ask for content for the dcx
    else:
        dcx_names = sys.argv[1:len(sys.argv)]
        # print(file_names)
        
        for dcx_name in dcx_names:

            # Name of dcx
            dcx_title = DCX_DIR + dcx_name

            if(not is_stallion_file(dcx_title)):

                # Prompt user for DCX information
                print("\nDCX file '" + dcx_name + "' will be created...")
                # file_amt = int(input("How many files will be in this file? "))
                print("Files selected are...\n")

                # Make dcx
                file_ptr = create_dcx(dcx_title)

                # Prompt user to open files in the filesystem
                tk.Tk().withdraw()
                filepath = filedialog.askopenfilenames(title="Open a Text File", initialdir=CONTENT_DIR, filetypes=(("text files","*.txt"), ("all files","*.*")))
                
                # At least one file on the DCX
                if(len(filepath) != 0):

                    for fpi in range(len(filepath)):
                        if(is_stallion_file(filepath[fpi])):

                            # determine the coordinates based on the index
                            x, y, w, h = get_pos_and_dims(fpi, STALLION_SCREEN_WIDTH, STALLION_SCREEN_HEIGHT)

                            # print file location
                            print(filepath[fpi])

                            # add file to dcx
                            write_to_dcx(file_ptr, filepath[fpi], x, y, w, h)

                        else:
                            print("file not found :(")
                
                # Close dcx
                close_dcx(file_ptr)
                print()

                # display array
                # for file_name in files:

                    # determine if file_name is an actual file
                    # is_stallion_file()

                    # add file into dcx
                    

                # inform user of file creation
                print("DCX file '" + dcx_name + "' has been created.\n")

            else:
                print("'" + dcx_title + "' already exists")

main()
