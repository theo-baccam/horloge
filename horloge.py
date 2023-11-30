# Le module time nous permet d'attendre x secondes.
import time


# Pour choisir entre modes d'affichage
def format_choix():
    choix = input(
        "Voulez vous afficher en:\n" "1) Mode 24 Heures\n" "2) Mode 12 Heures\n"
    )
    if choix == "1":
        twelve = False
    elif choix == "2":
        twelve = True
    else:
        raise ValueError("Choix Invalide")
    return twelve


def afficher_heure(input_tuple):
    # Pour extraire les valeurs du tuple
    hh = input_tuple[0]
    mm = input_tuple[1]
    ss = input_tuple[2]
    # Si une des valeurs est invalide
    if hh < 0 or hh > 24:
        raise ValueError("Heure Invalide")
    if mm < 0 or mm > 60:
        raise ValueError("Minutes Invalide")
    if ss < 0 or ss > 60:
        raise ValueError("Secondes Invalide")

    # Boucle pour calculer l'heure
    while True:
        # Pour calculer en mode 12 heures
        if hh > 12 and twelve == True:
            tw = hh - 12
            meridiem = "PM"
        elif hh < 0 and twelve == True:
            tw = hh
            meridiem = "AM"
        elif hh == 12 and twelve == True:
            tw = 12
            meridiem = "PM"
        elif hh == 0 and twelve == True:
            tw = 12
            meridiem = "AM"

        if twelve == True:
            current_time = f"{tw:02d}:{mm:02d}:{ss:02d} {meridiem}"
        else:
            current_time = f"{hh:02d}:{mm:02d}:{ss:02d}"

        # Les différences entre return et yield:
        # return marque la fin d'une fonction, avec yield ce n'est pas le cas
        # return n'envoient qu'une valeur, yield génère une séquence de valeurs.
        yield current_time

        # Modulo permet de faire un wrap-around entre une série de nombres.
        # index = (index + longueur + valeur incrémentation) % longueur
        ss = (ss + 60 + 1) % 60

        if ss == 0:
            mm = (mm + 60 + 1) % 60

        # mm == ss == 0 pour 24h sinon heure est compté toutes les secondes
        if mm == ss == 0:
            hh = (hh + 24 + 1) % 24


def alarme(input_tuple, input_hour):
    hh = input_tuple[0]
    mm = input_tuple[1]
    ss = input_tuple[2]
    if hh < 0 or hh > 24:
        raise ValueError("Heure Invalide")
    if mm < 0 or mm > 60:
        raise ValueError("Minutes Invalide")
    if ss < 0 or ss > 60:
        raise ValueError("Secondes Invalide")

    if hh >= 12 and twelve == True:
        tw = hh - 12
        meridiem = "PM"
    elif hh < 12 and twelve == True:
        tw = hh
        meridiem = "AM"

    if twelve == True:
        heure_alarme = f"{tw:02d}:{mm:02d}:{ss:02d} {meridiem}"
    else:
        heure_alarme = f"{hh:02d}:{mm:02d}:{ss:02d}"

    # Ceci remplace l'affichage normal de l'horloge, lorsque l'alarme sonne
    # on revient à la loop normale pour afficher.
    while True:
        current_time = next(input_hour)
        if current_time == heure_alarme:
            print(f"{current_time} | L'alarme a sonné   ", end="\r")
            time.sleep(1)
            break
        if current_time != heure_alarme:
            print(f"{current_time} | Alarme: {heure_alarme}", end="\r")
            time.sleep(1)


# Il ne faut pas oublier de spécifier que c'est un boolean
# sinon c'est considérée comme un string.
twelve = bool(format_choix())

time_tuple = (12, 59, 52)
display_heure = afficher_heure(time_tuple)

alarme_tuple = (13, 00, 00)
display_alarme = alarme(alarme_tuple, display_heure)

while True:
    # end="\r" revient au début de la ligne pour overwrite le dernier print.
    print(next(display_heure),end="\r")
    time.sleep(1)
