import time


def format_choix():
    choix = input("Voulez vous afficher en:\n1) Mode 24 Heures\n2) Mode 12 Heures\n")
    if choix == "1":
        check = False
    elif choix == "2":
        check = True
    else:
        raise ValueError("Choix Invalide")
    return check


def afficher_heure(input_tuple):
    hh = input_tuple[0]
    mm = input_tuple[1]
    ss = input_tuple[2]
    if hh < 0 or hh > 24:
        raise ValueError("Heure Invalide")
    if mm < 0 or mm > 60:
        raise ValueError("Minutes Invalide")
    if ss < 0 or ss > 60:
        raise ValueError("Secondes Invalide")

    while True:
        if hh >= 12 and twelve == True:
            tw = hh - 12
            meridiem = "PM"
        elif hh < 12 and twelve == True:
            tw = hh
            meridiem = "AM"

        ss = (ss + 60 + 1) % 60

        if ss == 0:
            mm = (mm + 60 + 1) % 60

        if mm == 0 and twelve == False:
            hh = (hh + 24 + 1) % 24
        elif mm == 0 and twelve == True:
            tw = (tw + 12 + 1) % 12

        if twelve == True:
            current_time = f"{tw:02d}:{mm:02d}:{ss:02d} {meridiem}"
        else: 
            current_time = f"{hh:02d}:{mm:02d}:{ss:02d}"

        yield current_time


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

    if mm == 0 and twelve == False:
        hh = (hh + 24 + 1) % 24
    elif mm == 0 and twelve == True:
        tw = (tw + 12 + 1) % 12

    current_time = next(input_hour)
    if twelve == True:
        heure_alarme = f"{tw:02d}:{mm:02d}:{ss:02d} {meridiem}"
    else:
        heure_alarme = f"{hh:02d}:{mm:02d}:{ss:02d}"

    while True:
        print(f"{current_time} | Alarme: {heure_alarme}", end="\r")
        if current_time == heure_alarme:
            print("\nL'alarme sonne")
            break
        time.sleep(1)


twelve = bool(format_choix())
print(twelve)

time_tuple = (10, 59, 55)
display_heure = afficher_heure(time_tuple)

alarme_tuple = (11, 27, 53)
display_alarme = alarme(alarme_tuple, display_heure)

while True:
    print(next(display_heure), end="\r")
    time.sleep(1)
