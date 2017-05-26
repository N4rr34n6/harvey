#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import os
import time
import Analyzer.target_analyzer as target_analyzer
import Streaming.stream_tweets as streaming_tweets
import Streaming.geo_spain as geo_spain
import Maps.myMapWorld as myMapWorld
import Maps.myMapSpain as myMapSpain
from Options.options import color as color
from Options.options import clear_window

option_choosed = 0


def info_harvey():
    """Gives general info about Harvey"""
    print(color.INFO + '''\t\t\t
       _     _
       \`\ /`/
        \ V /        Harvey - The invisible rabbit
        /. .\        v1.0 alpha
       =\ T /=
        / ^ \        Author: @juanvelasc0
       /\   /\       Follow the white rabbit (@fwhibbit_blog)
     __\ " " /__
    (____/^\____)

''' + color.ENDC)


def quit():
    """Quitting Harvey..."""
    clear_window()
    info_harvey()
    time.sleep(1)
    print(color.BOLD + """\t\t\tHave a nice day! Please don't stop talking to Harvey. Only you can see him""" + color.ENDC)


def show_menu():
    """Menu options for Harvey"""
    info_harvey()
    print color.BLUE + "[/] " + color.INFO +"Welcome to Harvey, digital vigilance. \n" + color.ENDC
    print color.BLUE + "\t1 - " + color.ENDC+"Analyze target."
    print color.BLUE + "\t2 - " + color.ENDC+"Digital vigilance in Spain"
    print color.BLUE + "\t3 - " + color.ENDC+"Digital vigilance using keyword"
    print color.BLUE + "\t4 - " + color.ENDC+"Worldwide Geo-positioning"
    print color.BLUE + "\t5 - " + color.ENDC+"National Geo-positioning"
    print color.BLUE + "\tq - " + color.ENDC+"Quit\n"
    option_choosed=raw_input(color.BLUE + "[x] " + color.ENDC + color.INFO + "Choose an option: " + color.ENDC)
    return option_choosed

#--------------------------------------------------------------------------------------------
#                                        MAIN PROGRAM                                       #
#--------------------------------------------------------------------------------------------
def main():
    option_choosed = show_menu()
    while(str(option_choosed) is not "q"):
        if(int(option_choosed) == 1):
            target_analyzer.main()
        elif(int(option_choosed) == 2):
            geo_spain.main()
        elif(int(option_choosed) == 3):
            streaming_tweets.main()
        elif(int(option_choosed) == 4):
            myMapWorld.main()
        elif(int(option_choosed) == 5):
            myMapSpain.main()

        raw_input(color.FAIL+"Press any key to return to menu..."+color.ENDC)
        option_choosed = show_menu()

    quit()

main()
