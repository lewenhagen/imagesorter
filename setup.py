#!/usr/bin/env python3

import os
import shutil
import helpers


"""
Setup functions, regarding folder structure
"""

def create_folders(pathToFolder):
    """ Creates the folders based on setup """
    try:
        if not os.path.exists(pathToFolder):
            os.makedirs(pathToFolder)
            print("Created folder:", pathToFolder)
        else:
            print("Folder --->", pathToFolder ,"<--- exists. Skipping.")

    except FileNotFoundError:
        print("File not found error. Try again.")

def checkResultFolder():

    """ checks for resultfolder """

    path = "./result"

    if not os.path.exists(path):
        sure = input("Folder 'result' not detected. Create it and continue? [Y/n] ").lower()
        if sure in ("n", "no"):
            pass
        else:
            os.path.makedirs(path)
    else:
        if len(os.listdir(path)) != 0:
            deleteit = input("Folder 'result' not empty. Delete the content? [Y/n] ").lower()
            if deleteit in ("n", "no"):
                pass
            else:
                for filename in os.listdir(path):
                    file_path = os.path.join(path, filename)
                    try:
                        if os.path.isfile(file_path) or os.path.islink(file_path):
                            os.unlink(file_path)
                        elif os.path.isdir(file_path):
                            shutil.rmtree(file_path)
                    except Exception as e:
                        print('Failed to delete %s. Reason: %s' % (file_path, e))


def setup_folders(FOLDERS):

    """ Change name on folders """

    # for folder in sorted(FOLDERS.keys()):

    #     ff = helpers.remove_illegal_chars(input("Folder name for " + folder + "? (Enter for default) "))

    #     if ff == "":
    #         input("### Leaving " + folder + " folder as default. Press Enter. ###")
    #     else:
    #         FOLDERS[folder] = ff

    #     if folder == "baseFolder" or folder == "unsortedFolder":
    #         create_folders(FOLDERS[folder])
    #     else:
    #         create_folders(FOLDERS["baseFolder"] + "/" + FOLDERS[folder])



    ff = helpers.remove_illegal_chars(input("Folder name for your images? (Enter for default) "))

    if ff == "":
        ff = FOLDERS["unsortedFolder"]
        input("### Leaving the 'images'-folder as default. Press Enter. ###")
    else:
        FOLDERS["unsortedFolder"] = ff

    # if folder == "baseFolder" or folder == "unsortedFolder":
    #     create_folders(FOLDERS[folder])
    # else:
    #     create_folders(FOLDERS["baseFolder"] + "/" + FOLDERS[folder])

    input("------ Base foldername is now '"+ ff +"'. Press any key. -------")


def remove_folder(folderToRemove):
    """ Deletes baseFolder """
    try:
        sure = input("Are you sure you want to delete the folder: '" + folderToRemove + "'? [y/N] ").lower()
        if sure in ("y", "yes"):
            # shutil.rmtree(folderToRemove, ignore_errors=False, onerror=None)
            for root, dirs, files in os.walk(folderToRemove):
                for file in files:
                    os.remove(os.path.join(root, file))
        else:
            pass
    except FileNotFoundError:
        print("Folder: '" + folderToRemove + "' is not created.")
