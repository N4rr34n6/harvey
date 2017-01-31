import os
import Analizador.fwhibbit_analyzer as fwhibbit_analyzer

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
    mostrar_logo()
    print "\n\tContacto:"
    print color.INFO + "\tEmail: " + color.ENDC + "info@fwhibbit.es"
    print color.INFO + "\tWeb: " + color.ENDC + "httpss://www.fwhibbit.es/"
    print color.INFO + "\tTwitter: " + color.ENDC + "@fwhibbit_blog\n"

def mostrar_menu_principal():
    mostrar_logo()
    print("+---------------------------------------------------------------------------+")
    print(color.INFO + "\t\t\t   >> MENU PRINCIPAL <<" + color.ENDC)
    print("+---------------------------------------------------------------------------+")
    print color.FAIL + "\n Bienvenido a fwibbit. Seleccione una opcion: \n" + color.ENDC
    print "\t1 - Analizar un objetivo"
    print "\t2 - Mapa ultimos tweets"
    print "\tq - Salir \n"
    eleccion_menu=raw_input("Elija la opcion que desee: ")
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
      `:yhh.
       `-:/+-`\033[1;m\n'''

################################################################################################
#                               PROGRAMA PRINCIPAL                                             #
################################################################################################

eleccion_menu =mostrar_menu_principal()
if(str(eleccion_menu) == "q"):
    salir()
elif(int(eleccion_menu) == 1):
    fwhibbit_analyzer.main()
    raw_input(color.FAIL+"Pulse cualquier tecla para volver al menu principal..."+color.ENDC)
    mostrar_menu_principal()
