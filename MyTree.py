#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys


def MyTree():
    '''
    Description:
    The program saves a tree of files and folders to a file named MyTree_in_Folder.txt

    Start:
    python3 MyTree.py FolderForTree

    If FolderForTree is not specified, the tree of the folder in which the program is running is saved

    Example home directory tree:
    python3 MyTree.py ~/

    myemail = '646976696b733230303840676d61696c2e636f6d'
    '''
    try:
        folder_rab = os.path.normpath(sys.argv[1])
    except:
        folder_rab = os.getcwd()
    if not os.path.exists(folder_rab):
        folder_rab = os.getcwd()

    n = -1
    file_out = os.path.normpath(os.path.join(folder_rab, 'MyTree_in_{}.txt'.format(os.path.basename(folder_rab))))

    with open(file_out, 'w') as f:
        f.write('Tree in folder: {}\n{}\n'.format(folder_rab, '-'*(len(folder_rab)+16)))

        def sort_by_name(fd):
            return fd.lower()

        def sort_by_ext(fd):
            return os.path.splitext(fd)[1].lower()

        def list_in_folder(folder, n):
            n += 1
            files = [file for file in os.listdir(folder) if os.path.isfile(os.path.join(folder, file))]
            files.sort(key=sort_by_name)
            for file in sorted(files, key=sort_by_ext):
                f.write('{}{}\n'.format(' '*n*4, file))
            dirs = [dir for dir in os.listdir(folder) if os.path.isdir(os.path.join(folder, dir))]
            for dir in sorted(dirs, key=sort_by_name):
                f.write('{}+{}\n'.format(' ' * n * 4, dir))
                list_in_folder(os.path.join(folder, dir), n)

        list_in_folder(folder_rab, n)

    return file_out


if __name__ == '__main__':
    MyTree()
