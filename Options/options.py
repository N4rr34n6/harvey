import os
#--------------------------------------------------------------------------------------------
#                                           COLORS                                          #
#--------------------------------------------------------------------------------------------
class color:  # COLOR TEXTO
    FAIL = '\033[91m'
    BLUE = '\033[94m'
    INFO = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    GREEN = '\033[92m'
    UNDERLINE = '\033[4m'

#--------------------------------------------------------------------------------------------
#                                     GENERAL OPTIONS                                       #
#--------------------------------------------------------------------------------------------

def clear_window():
    """Clears output from terminal"""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system('tput reset')

#--------------------------------------------------------------------------------------------
#                            Delete content from file                                       #
#--------------------------------------------------------------------------------------------
def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()