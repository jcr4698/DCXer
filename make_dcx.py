#!/usr/bin/python3

import sys
import signal
import os
# from os import devnull as DEVNULL
import numpy as np
from check_dcx import is_stallion_file, create_dcx, write_to_dcx, close_dcx, get_pos_and_dims, print_err, print_txt, print_end, dcx_file_name
import subprocess

# CONTENT_DIR = "/home/vislab/Gallery/Content/"
# DCX_DIR = "/home/vislab/Gallery/jan-projects/DCXer/dcx_files/"

CONTENT_DIR = "/mnt/c/Users/jan/Desktop/Files/Work_Material/Employment/Visualizations_Lab/Display_Cluster/Content/"
DCX_DIR = "/mnt/c/Users/jan/Desktop/Files/Work_Material/Employment/Visualizations_Lab/Display_Cluster/DCXer/dcx_files/"

STALLION_SCREEN_WIDTH = 6
STALLION_SCREEN_HEIGHT = 3

def main():

    # interruption handler variables
    dcx_location = None
    dcx_name = None

    # initialize and set-up handler for keyboard interrupt
    def signal_handler(*args):
        if(dcx_location and os.path.isfile(dcx_location)):
            os.remove(dcx_location)
        print_err("\n<Keyboard Signal Interruption>")
        if(dcx_name):
            print_end("\nDCX file '" + dcx_name + "' has been cancelled.\n")
        else:
            print_end("\nDCX file has been cancelled.\n")
        print("--------------------------------------------------")
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)

    # make dcx file named from user input
    if(len(sys.argv) <= 1):

        # prompt user to enter the name of dcx file
        dcx_name = ""
        try:
            dcx_name += input("\nName of the DCX: ")
        except Exception as e:
            print_err("\n<Keyboard Signal Interruption>")
            print_end("\nDCX file has been cancelled.\n")
            sys.exit(0)

        # change file name to its ".dcx" version, if need be
        dcx_name = dcx_file_name(dcx_name)

        # set absolute location of dcx
        dcx_location = DCX_DIR + dcx_name

        # verify that the file name doesn't already exist
        if(not is_stallion_file(dcx_location)):

            # Prompt user to select media files for creation of dcx
            print("\nDCX file '" + dcx_name + "' will be created...")
            print("Files selected are...\n")
            media_str, media_arr = zenity_filesys_prompt(dcx_location, dcx_name)

            # Create the dcx from the media files
            file_ptr = dcxify(dcx_location, dcx_name, media_str, media_arr)

        # notify user of file existence
        else:
            print_err("\n'" + dcx_location + "' already exists\n")
        print("--------------------------------------------------")

    # make dcx file with pre-determined arguments
    else:
        dcx_names = sys.argv[1:len(sys.argv)]
        
        for dcx_name in dcx_names:

            # change file name to its ".dcx" version, if need be
            dcx_name = dcx_file_name(dcx_name)

            # set absolute location of dcx
            dcx_location = DCX_DIR + dcx_name

            # verify that the file name doesn't already exist
            if(not is_stallion_file(dcx_location)):

                # Prompt user to select files for creation of dcx
                print("\nDCX file '" + dcx_name + "' will be created...")
                print("Files selected are...\n")
                media_str, media_arr = zenity_filesys_prompt(dcx_location, dcx_name)

                # Create the dcx from the media files
                file_ptr = dcxify(dcx_location, dcx_name, media_str, media_arr)

            else:
                print_err("\n'" + dcx_location + "' already exists\n")
            print("--------------------------------------------------")


def dcxify(dcx_location, dcx_name, media_str, media_arr):
    # make dcx and check for error
    file_ptr, msg = create_dcx(dcx_location)
    if(file_ptr == None):
        print_err("<Error in 'check_dcx.create_dcx(...)': " + str(msg) + ">")
        print_end("\nDCX file '" + dcx_name + "' has been cancelled.\n")
        sys.exit(0)

    # verify user selected at least one media file
    if(len(media_str) > 0 and len(media_arr) > 0):

        # prompt user to enter media files per stallion screen
        pic_per_scr = int(input("How many media files per screen? "))

        # append each media file to the dcx file
        for m_idx in range(len(media_arr)):

            # determine whether media file exists in filesys
            if(is_stallion_file(media_arr[m_idx])):

                # determine the coordinates based on the index
                x, y, w, h = get_pos_and_dims(m_idx, STALLION_SCREEN_WIDTH, STALLION_SCREEN_HEIGHT, pic_per_scr)

                # print file location
                print_txt(media_arr[m_idx])

                # add file to dcx
                msg = write_to_dcx(file_ptr, media_arr[m_idx], x, y, w, h)
                if(msg != None):
                    print_err("<Error in 'check_dcx.write_to_dcx(...)': " + str(msg) + ">")
                    print_end("\nDCX file '" + dcx_name + "' has been cancelled.\n")
                    sys.exit(0)

            else:
                print_err("<file not found>")

        # close dcx and check for error
        msg = close_dcx(file_ptr)
        if(msg != None):
            print_err("<Error in 'check_dcx.close_dcx(...)': " + str(msg) + ">")
            print_end("\nDCX file '" + dcx_name + "' has been cancelled.\n")
            sys.exit(0)

        # inform user of file creation
        print_end("\nDCX file '" + dcx_name + "' has been created.\n")

        return file_ptr

    # no files were selected
    else:
        close_dcx(file_ptr)
        if(os.path.isfile(dcx_location)):
            os.remove(dcx_location)
        print_err("<No files were selected>")
        print_end("\nDCX file '" + dcx_name + "' has been cancelled.\n")
        return None

def zenity_filesys_prompt(dcx_location, dcx_name):

    try:
        # values used for user prompt
        DEVNULL = open(os.devnull, 'wb')
        FILE_DIALOG_CMD = ["zenity", "--file-selection", "--multiple", "--text='Select Files...'"]

        # Prompt user to open files in the filesystem and parse the resonse
        zenity_response = subprocess.run(FILE_DIALOG_CMD, stdout=subprocess.PIPE, stderr=DEVNULL)
        parsed_response = zenity_response.stdout.decode("utf-8").strip()

        media_str = parsed_response[0:len(parsed_response)]
        media_arr = media_str.split("|")

        # print(parsed_response)
        # print(media_str)
        # print(media_arr)

        return media_str, media_arr

    except Exception as e:
        print_err("<Error in 'zenity_filesys_prompt(...)': " + str(e) + ">")
        print_end("\nDCX file '" + dcx_name + "' has been cancelled.\n")
        sys.exit(0)

if __name__ == '__main__':
    main()
