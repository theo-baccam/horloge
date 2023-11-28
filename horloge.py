import time


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
        ss = (ss + 60 + 1) % 60
        if ss == 0:
            mm = (mm + 60 + 1) % 60
        if mm == 0:
            hh = (hh + 24 + 1) % 24

        current_time = f"{hh:02d}:{mm:02d}:{ss:02d}"
        yield current_time


# def alarme(input_tuple, input_hour):
#     hh = input_tuple[0]
#     mm = input_tuple[1]
#     ss = input_tuple[2]
#     if hh < 0 or hh > 24:
#         raise ValueError("Heure Invalide")
#     if mm < 0 or mm > 60:
#         raise ValueError("Minutes Invalide")
#     if ss < 0 or ss > 60:
#         raise ValueError("Secondes Invalide")
#     heure_alarme = f"{hh:02d}:{mm:02d}:{ss:02d}"
# 
#     while True:
#         current_time = next(input_hour)
#         print(f"{current_time} | Heure de l'alarme: {heure_alarme}", end="\r")
#         if current_time == heure_alarme:
#             print("\nL'alarme sonne")
#             break
#         time.sleep(1)
# 
# 
time_tuple = (23, 59, 55)
display_heure = afficher_heure(time_tuple)
# 
# alarme_tuple = (0, 1, 2)
# display_alarme = alarme(alarme_tuple, display_heure)

while True:
    print(next(display_heure), end="\r")
    time.sleep(1)
