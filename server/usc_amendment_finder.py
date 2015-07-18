## USC Plug-IN
## v. 0.1
## 7-18-2015
## python 2.x
##
## These functions are part of a larger program designed to find
## if statutes referred to in Google Scholar case citations
## have been amended since the case was decided
##
## Changes log
## 0.1  changing website output to GPO rather than uscode.gov
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

vol = "28"
sec = "713"
year = "1981"

# sample dictionary of program codes and metrics is being used to develop function which will find the solicitations at nsf

## imported files

import os #loads os so I can use different directories later.
import urllib # to search uscode.house.gov for USC pages

from flask import Flask

app = Flask(__name__)

@app.route('/<volume>/<section>/<year>')
def execute_cf(volume, section, year):
    """Works for: 18, 28, 35, 38, 39"""

    (update_flag, url) = cf(volume, section, year)
    return '["{0}", "{1}"]'.format(update_flag, url)

def cf(t,s,y): # going to uscode.house.gov to retrieve code section
        amendyear = [] # creates list to store amendment years
        site1 = "http://uscode.house.gov/view.xhtml?hl=false&edition=prelim&req=granuleid%3AUSC-prelim-title" # + title number +
        site2 = "-section" # + section number +
        site3 = "&num=0&saved=%7CZ3JhbnVsZWlkOlVTQy1wcmVsaW0tdGl0bGUxOC1zZWN0aW9uODE%3D%7C%7C%7C0%7Cfalse%7Cprelim"
        website = site1 + t + site2 + s + site3
        page = urllib.urlopen(website)
        statute = page.read()
        index1 = statute.find("<!-- field-start:amendment-note -->")
        index2 = statute.find("<!-- field-end:amendment-note -->")
        amendments = statute[index1+35:index2]
        index3 = amendments.find("<b>")
        amendments = amendments[index3:]
        amendments = amendments.split("<b>")
        amendments.pop(0)
        index4 = statute.find("<!-- field-start:expcite -->")  # this constructs an URL for fdsys
        index5 = statute.find("<!-- field-end:expcite -->")
        gpoitems = statute[index4+28:index5]
        index6 = gpoitems.find("PART ")
        part = gpoitems[index6+5:index6+9]
        index7 = part.find("-")
        part = part[:index7]
        index8 = gpoitems.find("CHAPTER ")
        chapter = gpoitems[index8+8:index8+14]
        index9 = chapter.find("-")
        chapter = chapter[:index9]
        gsite1="http://www.gpo.gov/fdsys/pkg/USCODE-2013-title" #+ title number
        gsite2="/html/USCODE-2013-title" #+title number
        gsite3="-part" #+part num
        gsite4="-chap"  #+ch num
        gsite5="-sec" # + sec num
        gsite6=".htm"
        gpowebsite=gsite1+t+gsite2+t+gsite3+part+gsite4+chapter+gsite5+s+gsite6
        for item in amendments:
                item = item[:4]
                if item < y:  #checks the statute date againse the decision date
                        return False , gpowebsite # sets 'answer to' false where all amendments were prior to decision
                else:
                        return True , gpowebsite

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
