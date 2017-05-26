#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
from ascii_graph import Pyasciigraph
from ascii_graph.colors import *
from ascii_graph.colordata import vcolor, hcolor
from tqdm import tqdm
import tweepy, time, numpy, argparse, datetime, os
from Secrets.secrets import consumer_key, consumer_secret, access_token, access_token_secret
from Options.options import color as color
from Options.options import clear_window

# ------------------------------
# Variables globales
# ------------------------------
fecha_inicio = 0
fecha_final = 0

actividad_horaria = {
    "00:00": 0,
    "01:00": 0,
    "02:00": 0,
    "03:00": 0,
    "04:00": 0,
    "05:00": 0,
    "06:00": 0,
    "07:00": 0,
    "08:00": 0,
    "09:00": 0,
    "10:00": 0,
    "11:00": 0,
    "12:00": 0,
    "13:00": 0,
    "14:00": 0,
    "15:00": 0,
    "16:00": 0,
    "17:00": 0,
    "18:00": 0,
    "19:00": 0,
    "20:00": 0,
    "21:00": 0,
    "22:00": 0,
    "23:00": 0
    }

actividad_semanal = {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0
    }

lenguajes_detectados = {}
detected_sources = {}
lugares_detectados = {}
geo_activo_tweets = 0
hashtags_detectados = {}
zonahoraria_detectados = {}
retweets = 0
usuarios_retweeteados = {}
usuarios_mencionados = {}
id_screen_names = {}
limite_tweets = 500
usuario = ""

# ------------------------------
# Procesar tweet
# ------------------------------
def process_tweet(tweet):
    """ Procesar un unico tweet y actualizar la base de datos """
    global actividad_horaria
    global actividad_semanal
    global fecha_inicio
    global fecha_final
    global lenguajes_detectados
    global detected_sources
    global lugares_detectados
    global geo_activo_tweets
    global hashtags_detectados
    global zonahoraria_detectados
    global retweets
    global retweeted_names
    global usuarios_mencionados

    tw_date = tweet.created_at

    # Updating most recent tweet
    if fecha_final == 0:
        fecha_final = tw_date
    fecha_inicio = tw_date

    # Handling retweets
    try:
        # We use id to get unique accounts (screen_name can be changed)
        rt_id_user = tweet.retweeted_status.user.id_str
        if rt_id_user in usuarios_retweeteados:
            usuarios_retweeteados[rt_id_user] += 1
        else:
            usuarios_retweeteados[rt_id_user] = 1

        if not tweet.retweeted_status.user.screen_name in id_screen_names:
            id_screen_names[rt_id_user] = "@%s" % tweet.retweeted_status.user.screen_name

        retweets += 1
    except:
        pass

    # Updating our activity datasets (distribution maps)
    actividad_horaria["%s:00" % str(tw_date.hour).zfill(2)] += 1
    actividad_semanal[str(tw_date.weekday())] += 1

    # Updating langs
    if tweet.lang in lenguajes_detectados:
        lenguajes_detectados[tweet.lang] += 1
    else:
        lenguajes_detectados[tweet.lang] = 1

    # Updating sources
    tweet.source = tweet.source.encode('utf-8') # fix bug in python2, some source string are unicode
    if tweet.source in detected_sources:
        detected_sources[tweet.source] += 1
    else:
        detected_sources[tweet.source] = 1

    # Detecting geolocation
    if tweet.place:
        geo_activo_tweets += 1
        tweet.place.name = tweet.place.name.encode('utf-8')
        if tweet.place.name in lugares_detectados:
            lugares_detectados[tweet.place.name] += 1
        else:
            lugares_detectados[tweet.place.name] = 1

    # Updating hashtags list
    if tweet.entities['hashtags']:
        for ht in tweet.entities['hashtags']:
            ht['text'] = "#%s" % ht['text'].encode('utf-8')
            if ht['text']in hashtags_detectados:
                hashtags_detectados[ht['text']] += 1
            else:
                hashtags_detectados[ht['text']] = 1

    # Updating mentioned users list
    if tweet.entities['user_mentions']:
        for ht in tweet.entities['user_mentions']:

            if ht['id_str'] in usuarios_mencionados:
                usuarios_mencionados[ht['id_str']] += 1
            else:
                usuarios_mencionados[ht['id_str']] = 1

            if not ht['screen_name'] in id_screen_names:
                id_screen_names[ht['id_str']] = "@%s" % ht['screen_name']

def get_tweets(api, username, limit):
    """ Download Tweets from username account """
    i = 0
    for status in tqdm(tweepy.Cursor(api.user_timeline, screen_name=username).items(),unit="tw", total=limit):
        process_tweet(status)
        i += 1
        if i >= limit:
            break;
    return i

def get_last_tweet(api,username):
    tweet = api.user_timeline(username, count = 1)[0]
    return tweet.text

def int_to_weekday(day):
    if day == "0":
        return "Lunes"
    elif day == "1":
        return "Martes"
    elif day == "2":
        return "Miercoles"
    elif day == "3":
        return "Jueves"
    elif day == "4":
        return "Viernes"
    elif day == "5":
        return "Sabado"
    else:
        return "Domingo"

def print_stats(dataset, top=5):
    """ Displays top values by order """
    sum = numpy.sum(dataset.values())
    i = 0
    if sum != 0:
        sorted_keys = sorted(dataset, key=dataset.get, reverse=True)
        max_len_key = max([len(x) for x in sorted_keys][:top]) # use to adjust column width
        for k in sorted_keys:
            print(("- \033[1m{:<%d}\033[0m {:>6} {:<4}" % max_len_key).format(k, dataset[k], "(%d%%)" % ((float(dataset[k])/sum)*100)))
            i += 1
            if i >= top:
                break
    else:
        print ("No data")
    print("")

def print_charts(dataset, title, weekday=False):
    """ Prints nice charts based on a dict {(key, value), ...} """
    chart = []
    keys = dataset.keys()
    mean = numpy.mean(dataset.values())
    median = numpy.median(dataset.values())

    keys.sort()
    for key in keys:

        if (dataset[key] >= median*1.33):
            displayed_key = "%s (\033[92m+\033[0m)" % (int_to_weekday(key) if weekday else key)
        elif (dataset[key] <= median*0.66):
            displayed_key = "%s (\033[91m-\033[0m)" % (int_to_weekday(key) if weekday else key)
        else:
            displayed_key = (int_to_weekday(key) if weekday else key)

        chart.append((displayed_key, dataset[key]))

    thresholds = {
        int(mean):  Gre, int(mean*2): Yel, int(mean*3): Red,
    }
    data = hcolor(chart, thresholds)

    graph = Pyasciigraph(
        separator_length=4,
        multivalue=False,
        human_readable='si',
        )

    for line in graph.graph(title, data):
        print(line)
    print("")

def get_user():
    username_target = raw_input(color.BLUE + "[x] " + color.ENDC + color.INFO + "Introduzca el alias de twitter del objetivo:" + color.ENDC)
    return username_target

def main():

    username_target = get_user()

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    twitter_api = tweepy.API(auth, wait_on_rate_limit_notify=True,
        wait_on_rate_limit=True)

    clear_window()
    print(color.BLUE + "[+] " + color.ENDC + color.INFO + "Comenzando el análisis de objetivo..." + color.ENDC)
    #Pausa dramatica
    time.sleep(3)

    print(color.BLUE + "\n# ----------------------------------------------------------------------------------------------------------------------------------------" + color.ENDC)
    print(color.INFO + "\t\t\t\t >>> Ultimo tweet de " + str(username_target) + " <<<" + color.ENDC)
    print(get_last_tweet(twitter_api, username_target))
    print(color.BLUE + "# ----------------------------------------------------------------------------------------------------------------------------------------\n" + color.ENDC)

    # Getting data on account
    print(color.BLUE + "[+] " + color.ENDC +" Obteniendo informacion sobre " + color.BLUE + "@" + str(username_target) + color.ENDC)
    user_info = twitter_api.get_user(screen_name=username_target)

    print(color.BLUE + "[+] " + color.ENDC + color.INFO +" Lenguaje de la cuenta           : "+ color.ENDC +" \033[1m%s\033[0m" % user_info.lang)
    print(color.BLUE + "[+] " + color.ENDC + color.INFO +" Geolocalizacion activa          : "+ color.ENDC +" \033[1m%s\033[0m" % user_info.geo_enabled)
    print(color.BLUE + "[+] " + color.ENDC + color.INFO +" Zona horaria                    : "+ color.ENDC +" \033[1m%s\033[0m" % user_info.time_zone)
    print(color.BLUE + "[+] " + color.ENDC + color.INFO +" Intervalo UTC                   : "+ color.ENDC +" \033[1m%s\033[0m" % user_info.utc_offset)

    if user_info.utc_offset is None:
        print("[\033[91m!\033[0m] No se ha podido encontrar zona horaria")

    print(color.BLUE + "[+] " + color.ENDC + color.INFO +" Tweets totales : "+ color.ENDC +" \033[1m%s\033[0m" % user_info.statuses_count)


    # Obtener ultimos tweets
    num_tweets = numpy.amin([limite_tweets, user_info.statuses_count])
    print(color.BLUE + "[+] " + color.ENDC + " Obteniendo ultimos " + color.BLUE + str(num_tweets) + color.ENDC +" tweets...")

    # DESCARGA DE TWEETS
    num_tweets = get_tweets(twitter_api, username_target, limit=limite_tweets)
    print(color.BLUE + "[+] " + color.ENDC +" Descargando %d tweets desde %s hasta %s (%d dias)" % (num_tweets, fecha_inicio, fecha_final, (fecha_final - fecha_inicio).days))

    if (fecha_final - fecha_inicio).days != 0:
        print(color.BLUE + "[+] " + color.ENDC +" Media de tweets por dia: \033[1m%.1f\033[0m" % (num_tweets / float((fecha_final - fecha_inicio).days)))

    # GRAFICAS
    print("\n\n")
    print_charts(actividad_horaria, color.BLUE + "[+] "+ color.INFO +" Distribucion de actividad horaria (por horas)"+ color.ENDC)
    print_charts(actividad_semanal, color.BLUE + "[+] "+ color.INFO +" Distribucion de actividad semanal (por dias)"+ color.ENDC, weekday=True)
    print("\n\n")

    print color.BLUE + "[+] " + color.ENDC + color.INFO + " Lenguajes detectados" + color.ENDC + " (top 5)"
    print_stats(lenguajes_detectados)

    print color.BLUE + "[+] " + color.ENDC + color.INFO + " Plataformas detectadas" + color.ENDC
    print_stats(detected_sources, top=10)

    print(color.BLUE + "[+] " + color.ENDC +" Hay \033[1m%d\033[0m tweets con geolocalizacion activa" % geo_activo_tweets)
    if len(lugares_detectados) != 0:
        print color.BLUE + "[+] " + color.ENDC + color.INFO + " Lugares detectados" + color.ENDC + " (top 10)"
        print_stats(lugares_detectados, top=10)

    print color.BLUE + "[+] " + color.ENDC + color.INFO + " Top detectados" + color.ENDC + " 10 " + color.INFO + "hashtags" + color.ENDC
    print_stats(hashtags_detectados, top=10)

    print color.BLUE + "[+] " + color.ENDC +" @%s hizo \033[1m%d\033[0m RTs de un total de %d tweets (%.1f%%)" % (username_target, retweets, num_tweets, (float(retweets)*100/num_tweets))

    # Converting users id to screen_names
    usuarios_retweeteados_names = {}
    for k in usuarios_retweeteados.keys():
        usuarios_retweeteados_names[id_screen_names[k]] = usuarios_retweeteados[k]

    print color.BLUE + "[+] " + color.ENDC + color.INFO + " Top " + color.ENDC + "5 " + color.INFO + "usuarios mas retweeteados" + color.ENDC
    print_stats(usuarios_retweeteados_names, top=5)

    usuarios_mencionados_names = {}
    for k in usuarios_mencionados.keys():
        usuarios_mencionados_names[id_screen_names[k]] = usuarios_mencionados[k]
    print color.BLUE + "[+] " + color.ENDC + color.INFO + " Top " + color.ENDC + "5 " + color.INFO + "usuarios mas mencionados" + color.ENDC
    print_stats(usuarios_mencionados_names, top=5)

if __name__ == '__main__':
    try:
	menu()
        main()
    except tweepy.error.TweepError as e:
        print("[\033[91m!\033[0m] Twitter error: %s" % e)
    except Exception as e:
        print("[\033[91m!\033[0m] Error: %s" % e)
