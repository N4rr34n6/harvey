#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import os,time
import Analizador.fwhibbit_analyzer as fwhibbit_analyzer
import Streaming.stream_tweets as streaming_tweets
import Streaming.geo_spain as geo_spain
import Mapas.myMapWorld as myMapWorld
import Mapas.myMapSpain as myMapSpain

eleccion_menu = 0

################################################################################################
#                                   COLORES                                                    #
################################################################################################
class color:  # COLOR TEXTO
    FAIL = '\033[91m'
    BLUE = '\033[94m'
    INFO = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    GREEN = '\033[92m'
    UNDERLINE = '\033[4m'

################################################################################################
#                               MENU PRINCIPAL                                                 #
################################################################################################
def salir():
    fwhibbit_analyzer.limpiar_pantalla()
    print(color.BOLD + """\t\t\t
                                                    _       _
                                                    \ \     / /              (\_/)
                                                      \ \_/ /                (0.0)
                                                      ( -.- )               (") (")
                                                    (,,) . (,,)             (      )
                                                    (" _)-(_ ")             (,,)(,,)

                                                            Have a nice day
                                                    Please don't stop talking to Harvey
                                                          Only you can see him
                                                            >--------------<
    """ + color.ENDC)
    time.sleep(2)
    fwhibbit_analyzer.limpiar_pantalla()
    mostrar_logo()
    print "\n\tContacto:"
    print color.INFO + "\tEmail: " + color.ENDC + "info@fwhibbit.es"
    print color.INFO + "\tWeb: " + color.ENDC + "httpss://www.fwhibbit.es/"
    print color.INFO + "\tTwitter: " + color.ENDC + "@fwhibbit_blog\n"

def mostrar_menu_principal():
    mostrar_logo()
    print(color.INFO + '''\t\t\t
	 ██░ ██  ▄▄▄       ██▀███   ██▒   █▓▓█████▓██   ██▓
	▓██░ ██▒▒████▄    ▓██ ▒ ██▒▓██░   █▒▓█   ▀ ▒██  ██▒
	▒██▀▀██░▒██  ▀█▄  ▓██ ░▄█ ▒ ▓██  █▒░▒███    ▒██ ██░
	░▓█ ░██ ░██▄▄▄▄██ ▒██▀▀█▄    ▒██ █░░▒▓█  ▄  ░ ▐██▓░
	░▓█▒░██▓ ▓█   ▓██▒░██▓ ▒██▒   ▒▀█░  ░▒████▒ ░ ██▒▓░
	 ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒▓ ░▒▓░   ░ ▐░  ░░ ▒░ ░  ██▒▒▒
	 ▒ ░▒░ ░  ▒   ▒▒ ░  ░▒ ░ ▒░   ░ ░░   ░ ░  ░▓██ ░▒░
	 ░  ░░ ░  ░   ▒     ░░   ░      ░░     ░   ▒ ▒ ░░
	 ░  ░  ░      ░  ░   ░           ░     ░  ░░ ░
		                        ░          ░ ░
                                                ''' + color.ENDC)
    print color.INFO + "\n Bienvenido a Harvey, servicio de Vigilancia Digital. Seleccione una opcion: \n" + color.ENDC
    print color.BLUE + "\t1 - " + color.ENDC+"Analizar un Objetivo"
    print color.BLUE + "\t2 - " + color.ENDC+"Vigilancia Digital en España"
    print color.BLUE + "\t3 - " + color.ENDC+"Vigilancia Digital con Keyword"
    print color.BLUE + "\t4 - " + color.ENDC+"Geoposicionamiento Mundial"
    print color.BLUE + "\t5 - " + color.ENDC+"Geoposicionamiento Nacional"
    print color.BLUE + "\tq - " + color.ENDC+"Salir\n"
    eleccion_menu=raw_input(color.BLUE + "[x] " + color.ENDC + color.INFO + "Elija la opción que desee: " + color.ENDC)
    return eleccion_menu

def mostrar_logo():  # LOGO
    fwhibbit_analyzer.limpiar_pantalla()
    print '''\033[1;32m\t

        `.--:++/.
      `.-::::/ymm+
    ```.`.-shmdd/      `
  .//-/++yhmmdy-     `//`
 :y:odNMNNmmmh/   .:smm.       ____         __    _ __    __    _ __
 ooydNNNy:..`    osNMMm:`     / __/      __/ /_  (_) /_  / /_  (_) /_
 `hdsMN+         .hNMmho-    / /_| | /| / / __ \/ / __ \/ __ \/ / __/
  oh/m/           -yyyyy-   / __/| |/ |/ / / / / / /_/ / /_/ / / /_
  :ydy`              ```   /_/   |__/|__/_/ /_/_/_.___/_.___/_/\__/
  ``/ooo/-`
      `:yhh.		   Copyright (c) 2017 Follow the white rabbit
	`-:/+-`		   All Rights Reserved
       	\033[1;m\n'''

################################################################################################
#                               PROGRAMA PRINCIPAL                                             #
################################################################################################
eleccion_menu = mostrar_menu_principal()
while(str(eleccion_menu) is not "q"):
    if(int(eleccion_menu) == 1):
        fwhibbit_analyzer.main()
    elif(int(eleccion_menu) == 2):
        geo_spain.main()
    elif(int(eleccion_menu) == 3):
        streaming_tweets.main()
    elif(int(eleccion_menu) == 4):
        myMapWorld.main()
    elif(int(eleccion_menu) == 5):
        myMapSpain.main()

    raw_input(color.FAIL+"Pulse cualquier tecla para volver al menu principal..."+color.ENDC)
    eleccion_menu = mostrar_menu_principal()

salir()
