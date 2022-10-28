#!/usr/bin/env python3

"""
Main file.
Collect information, setup folderstructure and starts script
"""

import setup, os
import functions

# onlyfiles = next(os.walk(dir)) #dir is your directory path as string
# print (len(onlyfiles))

FOLDERS = {
    "baseFolder": "result",
    "finishedFolder": "finished",
    "unfinishedFolder": "unfinished",
    "videoFolder": "video",
    "unsortedFolder": "images"
}



def menu():
    """ The main menu """
    print("""
    ##################################
    Welcome to the image sorter!
    ##################################

    Default foldernames: (Final will be, for example: result/finished, result/videos)
    ----------------------------------
    Base folder:            result/
    Finished images:        finished/
    Unfinished images:      unfinished/
    Videos:                 videos/
    ----------------------------------
    Unsorted images (your imagefolder):        images/
    """)

    print("1) Setup image folder. Press Enter for default")
    print("2) Scan folder")
    print("3) Start sorting!")
    print("R) Remove baseFolder")
    print("q) Quit program")

def checkResultFolder():
    """ checks for Result folder """
    setup.checkResultFolder()

def main():
    """ Main loop """

    while True:
        menu()
        choice = input("--> ")

        if choice == "q":
            print("Bye.")
            return

        elif choice == "1":
            setup.setup_folders(FOLDERS)

        elif choice == "2":
            print("\n### Available folders ###\n")
            functions.presentFolders(FOLDERS)

        elif choice == "3":
            functions.startSort(FOLDERS)

        elif choice == "R":
            setup.remove_folder(FOLDERS["baseFolder"])


        else:
            print("Try again.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    checkResultFolder()
    main()
