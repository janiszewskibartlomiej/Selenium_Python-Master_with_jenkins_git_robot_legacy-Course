import os

def create_folder(foldername):
    os.mkdir("E:\\"+ foldername)

def create_sub_folder(subfolername):
    os.mkdir("E:\\TestingWorldIndia\\"+ subfolername)

def concatenate_two_values(val1, val2):
    val3 = val1+" " + val2
    return val3
