#!/usr/bin/python3

import sys
import os
import numpy as np
from check_dcx import is_stallion_file, create_dcx, write_to_dcx, close_dcx, get_pos_and_dims, print_err, print_txt, print_end
import subprocess

CONTENT_DIR = "/home/vislab/Gallery/Content/"
DCX_DIR = "/home/vislab/Gallery/jan-projects/DCXer/dcx_files/"

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
                
                try:
                    # zenity command and null value
                    FILE_DIALOG_CMD = ["zenity", "--file-selection", "--multiple", "--text='Select Files...'"]
                    DEVNULL = open(os.devnull, 'wb')

                    # Prompt user to open files in the filesystem
                    file_dialog_res = subprocess.run(FILE_DIALOG_CMD, stdout=subprocess.PIPE, stderr=DEVNULL).stdout.decode("utf-8")
                    fp_str = file_dialog_res[0:len(file_dialog_res)-1]
                    fp_arr = fp_str.split("|")
                    # tk.Tk().withdraw()
                    # filepath = filedialog.askopenfilenames(title="Open a Text File", initialdir=CONTENT_DIR, filetypes=(("text files","*.txt"), ("all files","*.*")))

                    # At least one file on the DCX
                    if(len(fp_str) > 0 and len(fp_arr) > 0):

                        for fpi in range(len(fp_arr)):

                            #elif():
                            #    # verify file is a media type
                            #    pass

                            if(is_stallion_file(fp_arr[fpi])):

                                # determine the coordinates based on the index
                                x, y, w, h = get_pos_and_dims(fpi, STALLION_SCREEN_WIDTH, STALLION_SCREEN_HEIGHT)

                                # print file location
                                print_txt(fp_arr[fpi])

                                # add file to dcx
                                write_to_dcx(file_ptr, fp_arr[fpi], x, y, w, h)

                            else:
                                print_err("<file not found>")

                        # Close dcx
                        close_dcx(file_ptr)

                        # inform user of file creation
                        print_end("\nDCX file '" + dcx_name + "' has been created.\n")

                    # no files were selected
                    else:
                        close_dcx(file_ptr)
                        if(os.path.isfile(dcx_title)):
                            os.remove(dcx_title)
                        print_err("<no files were selected>")
                        print_end("\nDCX file '" + dcx_name + "' has been cancelled.\n")

                except subprocess.CalledProcessError as e:
                    close_dcx(file_ptr)
                    if(os.path.isfile(dcx_title)):
                        os.remove(dcx_title)
                    print_err("<a zenity error has occurred>")
                    print_end("\nDCX file '" + dcx_name + "' has been cancelled.\n")

                except Exception as e:
                    close_dcx(file_ptr)
                    if(os.path.isfile(dcx_title)):
                        os.remove(dcx_title)
                    print_err("An unexpected error has occurred:")
                    #print("\nDCX file '" + dcx_name + "' has been cancelled.\n")
                    print_err(str(e))
                    print_end("\nDCX file '" + dcx_name + "' has been cancelled.\n")

            else:
                print("'" + dcx_title + "' already exists")
            print("--------------------------------------------------")

main()
