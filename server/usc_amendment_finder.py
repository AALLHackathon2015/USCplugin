## USC Plug-IN
## v. 0.0
## 7-18-2015 
## python 2.x
##
## These functions are part of a larger program designed to find
## if statutes referred to in Google Scholar case citations
## have been amended since the case was decided
##  
## Process:
##
## 1st --> inputs the title number, section number, and year of the USC section from the Chrome Google Scholar Plug-in
## 2nd --> finds the Statute page from the us house website 
## 3rd --> searches page and creates list of pub-law numbers on page (list of amendments)
## 4th --> compares pub law dates with date of case to determine whether to flag as 'questionable'
## 5th --> returns flag, to Google Scholar Plug-in

## from here code begins

## sample data

vol = "18"
sec = "1001"
year = "2002"

# sample dictionary of program codes and metrics is being used to develop function which will find the solicitations at nsf


## imported files

import os #loads os so I can use different directories later.
import urllib # to search uscode.house.gov for USC pages
 
        
def cf(v,s,y): # going to uscode.house.gov to retrieve code section
        amendyear = [] # creates list to store amendment years
        site1 = "http://uscode.house.gov/view.xhtml?hl=false&edition=prelim&req=granuleid%3AUSC-prelim-title" # + volume number +
        site2 = "-section" # + section number +
        site3 = "&num=0&saved=%7CZ3JhbnVsZWlkOlVTQy1wcmVsaW0tdGl0bGUxOC1zZWN0aW9uODE%3D%7C%7C%7C0%7Cfalse%7Cprelim"
        website = site1 + v + site2 + s + site3
        page = urllib.urlopen(website)
        statute = page.read()
        index1 = statute.find("<!-- field-start:amendment-note -->")
        index2 = statute.find("<!-- field-end:amendment-note -->")
        amendments = statute[index1+35:index2]
        index3 = amendments.find("<b>")
        amendments = amendments[index3:]
        amendments = amendments.split("<b>")
        amendments.pop(0)
        for item in amendments:
                item = item[:4]
                if item < y:
                        return False, website  # returns false where all amendments were prior to decision
                else:
                        return True, website
                
        
        
    

