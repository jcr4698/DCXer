from os.path import exists
from _io import TextIOWrapper as File

CONTENT = "/home/vislab/Gallery/Content/"
COMMON = "/home/vislab/Gallery/common_content/"

''' Determine whether FILE_NAME exists and where. '''
def is_stallion_file(file_name:str):
    if(exists(CONTENT + file_name)):
        return (True, CONTENT + file_name)
    elif(exists(COMMON + file_name)):
        return (True, COMMON + file_name)
    return (False, "")

''' Create and initialize a dcx file of name DCX_NAME. '''
def create_dcx(dcx_name:str) -> File:
    file_ptr = open(dcx_name, "w+")
    file_ptr.write("<!DOCTYPE state>\n<state>\n <version>1</version>\n")
    return file_ptr

''' Add file FILE_PATH to the dcx file FILE. '''
def write_to_dcx(dcx_file:File, file_path:str):
    content_window = " <ContentWindow>\n"
    content_window += " <URI>" + file_path + "</URI>\n"
    
    content_window += "    <centerX>0.5</centerX>\n    <centerY>0.5</centerY>\n  <zoom>1</zoom>\n  <selected>0</selected>\n <ContentWindow>\n"
    dcx_file.write(content_window)

def close_dcx(dcx_file:File):
    dcx_file.write("</state>")
    dcx_file.close()

file_ptr = create_dcx("hello.txt")
write_to_dcx(file_ptr, "hello, world!")
write_to_dcx(file_ptr, "hi!")
close_dcx(file_ptr)
