from os.path import exists
from _io import TextIOWrapper as File
from math import floor

# CONTENT = "/mnt/c/Users/jan/Desktop/Files/Work_Material/Employment/Visualizations_Lab/Display_Cluster/DCXer/Content/"
# COMMON = "/mnt/c/Users/jan/Desktop/Files/Work_Material/Employment/Visualizations_Lab/Display_Cluster/DCXer/Common/"

''' Determine whether FILE_NAME exists and where. '''
def is_stallion_file(file_dir:str):
    if(exists(file_dir)):
        return True
    return False

''' Create and initialize a dcx file of name DCX_NAME. '''
def create_dcx(dcx_name:str) -> File:
    file_ptr = open(dcx_name, "w+")
    file_ptr.write("<!DOCTYPE state>\n<state>\n <version>1</version>\n")
    return file_ptr

''' Add file FILE_PATH to the dcx file FILE. '''
def write_to_dcx(dcx_file:File, file_path:str, x_coord, y_coord, width, height):

    # append hearder opener of dcx file
    content_window = " <ContentWindow>\n"

    # append associated location of file
    content_window += "  <URI>" + file_path + "</URI>\n"

    # append x & y location and width & height
    content_window += "  <x>" + str(float(x_coord)) + "</x>\n"
    content_window += "  <y>" + str(float(y_coord)) + "</y>\n"
    content_window += "  <w>" + str(float(width)) + "</w>\n"
    content_window += "  <h>" + str(float(height)) + "</h>\n"

    # append center, zoom, and selection (whatever that means)
    content_window += "  <centerX>0.5</centerX>\n  <centerY>0.5</centerY>\n  <zoom>1</zoom>\n  <selected>0</selected>\n"

    # append header closer of dcx file
    content_window += " </ContentWindow>\n"
    dcx_file.write(content_window)

''' Close the dcx file of name DCX_NAME. '''
def close_dcx(dcx_file:File):
    dcx_file.write("</state>")
    dcx_file.close()

''' Calculate the position and dimensions '''
def get_pos_and_dims(i:int, x_dim:int, y_dim:int):
    if(i < x_dim * y_dim):
        return float('%.3f'%(0.167 * (i%x_dim))), float('%.3f'%(0.337 * floor(i/x_dim))), 1.0, 0.326
    return 0.0, float('%.3f'%(0.674+0.337)), 1.0, 1.0

''' Print text in error format (RED) '''
def print_err(err:str):
    print("\033[91m{}\033[00m".format(err))

''' Print text in file format (GREEN) '''
def print_txt(txt:str):
    print("\033[1;32m{}\033[00m".format(txt))

''' Print text in ending format (BLUE)'''
def print_end(txt:str):
    print("\033[1;34m{}\033[00m".format(txt))

# file_ptr = create_dcx("hello.txt")
# write_to_dcx(file_ptr, "hello, world!", 1.01, 2.02, 3.1, 4.2)
# write_to_dcx(file_ptr, "hi!", 2.01, 1.02, 3.18, 0.2)
# close_dcx(file_ptr)

# for n in range(19):
#     print(n, get_pos_and_dims(n, 6, 3))
