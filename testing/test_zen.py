#!/usr/bin/python3

import os
import subprocess

''' FILE SYSTEM SELECTION '''

# Prompt user to open files in the filesystem
#FILE_DIALOG_CMD = ["zenity", "--file-selection", "--multiple", "--text='Select Files...'"]
#DEVNULL = open(os.devnull, 'wb')
#file_dialog_res = subprocess.run(FILE_DIALOG_CMD, stdout=subprocess.PIPE, stderr=DEVNULL).stdout.decode("utf-8")
#filepath = file_dialog_res[0:len(file_dialog_res)-1].split("|")
#print(filepath)

''' DETERMINE WHETHER FILE IS PNG '''

#import mimetypes
#mimetypes.init()

#file = "/home/vislab/Gallery/Content/Dance_at_Le_Moulin_de_la_Galette.pyr"
#file = ".png"
#
#mimestart = mimetypes.guess_type(file)[0]
#
#print(file[len(file)-4:len(file)])
#if len(file) > 5 and file[len(file)-4:len(file)] == ".pyr":
#    print("pyr file")
#
#if mimestart != None:
#    mimestart = mimestart.split("/")[0]
#    if mimestart in ["video", "image"]:
#        print("media type")

''' RESOLUTION OF IMAGE '''

import 
