"""
Sök igenom vilka datum som en fil är senast modifierad genom att anvnäda sig
av funktionen som plockar ut alla filer från en viss path eller hela datorn.

"""

import os, time
import search_computer as s

def search_modified(date,files):
    files_mod = []
    # Leta igenom alla filer och kolla när dem senast är modifierade.
    for i in files:
        path = os.path.getmtime(i)
        moddate = time.strftime('%Y%m%d', time.localtime(path))
        # Ta ut år, månad och dag från filen.
        year = int(moddate[0:4])
        month = int(moddate[4:6])
        day = int(moddate[6:8])
        # Om datumet användaren skrivit in är mindre eller samma så
        # är filen modifierad efter eller samma dag som sökt datum.
        if int(date[0:4]) <= year and int(date[5:7]) <= month and int(date[8:10]) <= day:
            files_mod.append(i)
    # Retunera listan med filer som är modifierade senast det angivna datumet.
    return files_mod
try:
    files = s.search_computer(r'C:\Users\Användaren\PycharmProjects\mini')
    search_modified('2020-03-01', files)
except FileNotFoundError:
    pass