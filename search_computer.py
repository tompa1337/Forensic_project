"""
Leta igenom en path eller en hel hårdisk för att hitta filer.
"""

import os
import os.path
from os.path import isfile,isdir,join

filer = []
def search_computer(dir):
    # Hitta alla filer genom att köra en for loop och för varje mapp som den hittar köra om programmet.
    try:
        for i in os.listdir(dir):
            # Om pathen är en direction så gå in och kör funktionen igen
            # för att leta efter fler filer.
            if isdir(join(dir, i)):
                search_computer(join(dir, i))
            # Om pathen är en fil så lägg till den i en lista
            if isfile(join(dir, i)):
                filer.append(join(dir, i))
    except PermissionError:
        pass
    return filer