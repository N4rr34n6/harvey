import os
import fwhibbit_analyzer as fwhibbit_analyzer

eleccion_menu = 0

#####COLORES
class color:  # COLOR TEXTO
    FAIL = '\033[91m'
    BLUE = '\033[94m'
    INFO = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    GREEN = '\033[92m'
    UNDERLINE = '\033[4m'

####MENUS
def limpiar():  # LIMPIAR PANTALLA
    if os.name == "nt":
        os.system("cls")
    else:
        os.system('tput reset')

def salir():
    limpiar()
    print "\tScript escrito por " + color.BOLD + "Fwhibbit" + color.ENDC
    print "\nContacto:"
    print color.INFO + "Email: " + color.ENDC + "info@fwhibbit.es"
    print color.INFO + "Web: " + color.ENDC + "httpss://www.fwhibbit.es/"
    print color.INFO + "Twitter: " + color.ENDC + "@fwhibbit_blog\n"


def logo():  # LOGO
    limpiar()
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
logo()
print(color.INFO + "\t\t\t>> MENU PRINCIPAL <<" + color.ENDC)
print("+---------------------------------------------------------------------------+")
print color.FAIL + "\n Selecciona una opcion" + color.ENDC
print "\t1 - Analizar un objetivo"
print "\t2 - OPCION2"
print "\t3 - OPCION3"
print "\t0 - Salir"

eleccion_menu=raw_input("Elija la opcion que desee: ")

if(int(eleccion_menu) == 1):
    fwhibbit_analyzer.main()
