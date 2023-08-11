from os.path import exists
from _io import TextIOWrapper as File
from math import floor

''' Determine whether FILE_NAME exists and where. '''
def is_stallion_file(file_dir:str):
    if(exists(file_dir)):
        return True
    return False

''' Create and initialize a dcx file of name DCX_NAME. '''
def create_dcx(dcx_name:str) -> File:
    try:
        file_ptr = open(dcx_name, "w+")
        file_ptr.write("<!DOCTYPE state>\n<state>\n <version>1</version>\n")
        return file_ptr, ""
    except FileNotFoundError as e:
        return None, str(e)

''' Add file FILE_PATH to the dcx file FILE. '''
def write_to_dcx(dcx_file:File, file_path:str, x_coord, y_coord, width, height):

    # append header opener of dcx file
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

    # write appended content to dcx file pointer
    try:
        dcx_file.write(content_window)
        return None
    except Exception as e:
        return str(e)

''' Close the dcx file of name DCX_NAME. '''
def close_dcx(dcx_file:File):
    try:
        dcx_file.write("</state>")
        dcx_file.close()
        return None
    except Exception as e:
        return str(e)

''' Calculate the position and dimensions '''
def get_pos_and_dims(i:int, x_dim:int, y_dim:int, pic_per_scr:int):
    if(i < (x_dim * y_dim)*pic_per_scr):
        return float('%.3f'%((0.167 / pic_per_scr) * (i%(x_dim * pic_per_scr)))), float('%.3f'%(0.337 * floor(i/(x_dim * pic_per_scr)))), 1.0, 0.326
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

''' Return a file name with ".dcx" at the end, if it doesn't already. '''
def dcx_file_name(file_name:str):
    # determine if file_name has period at the beginning and remove it
    is_hidden = True if file_name[0] == "." else False
    curr_name = file_name[1:] if is_hidden else file_name

    # length of file_name and index of ".dcx"
    name_len = len(curr_name) - 4
    dcx_idx = curr_name.rfind(".dcx")
    # print(dcx_idx, "/", name_len)

    # return the correct display cluster file based on these features
    if((dcx_idx > -1) and (name_len == dcx_idx)):
        # print("file name:", "."+curr_name if is_hidden else curr_name)
        return "."+curr_name if is_hidden else curr_name
    else:
        # print("file name:", "."+curr_name+".dcx" if is_hidden else curr_name+".dcx")
        return "."+curr_name+".dcx" if is_hidden else curr_name+".dcx"
