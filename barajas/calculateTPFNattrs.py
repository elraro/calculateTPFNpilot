import MySQLdb as Mdb
import numpy as np

# Hardcoded
DB_HOST = "localhost"
DB_USER = "frav"
DB_PASS = "VXxL4UOLvB6wc01Y3Cxi"
DB_NAME = "piloto_barajas"

con = Mdb.connect(DB_HOST, DB_USER, DB_PASS, DB_NAME)
cur = con.cursor()

sex = ["'Masculino'", "'Femenino'"]
document = ["'PasaportePrimeraGeneracion'", "'PasaporteSegundaGeneracion'"]
country = ["'ARG'", "'AUS'", "'BRA'", "'CHL'", "'COL'", "'ESP'", "'MAR'", "'PER'", "'RUS'", "'TWN'", "'URY'", "'USA'", "'VEN'"]
umbrals = [10, 40, 50, 60, 70, 80, 90]

# sex
# for s in sex:
#     fn_rate = np.empty(shape=0)
#     tp_rate = np.empty(shape=0)
#     # ScoreDactilar
#     cur.execute("SELECT `ScoreReconocimientoFacialVivoChip` FROM `completados` WHERE Sexo=" + s + ";")
#     data = cur.fetchall()
#     data = np.asarray(data)
#     for umbral in umbrals:
#         tp = 0
#         fn = 0
#         for d in data:
#             if d[0] >= umbral:
#                 tp += 1
#             else:
#                 fn += 1
#         try:
#             fn_rate_eer = fn / (fn + tp)
#         except ZeroDivisionError:
#             fn_rate_eer = 1
#         try:
#             tp_rate_eer = tp / (tp + fn)
#         except ZeroDivisionError:
#             tp_rate_eer = 1
#         fn_rate = np.append(fn_rate, fn_rate_eer)
#         tp_rate = np.append(tp_rate, tp_rate_eer)
#     print("Sexo: " + s)
#     print("TP")
#     print(*tp_rate, sep='\n')
#     print("FN")
#     print(*fn_rate, sep='\n')
#     print("------------------")


# document
# for d in document:
#     fn_rate = np.empty(shape=0)
#     tp_rate = np.empty(shape=0)
#     cur.execute("SELECT `ScoreReconocimientoFacialVivoChip` FROM `completados` WHERE TipoDocumento=" + d + ";")
#     data = cur.fetchall()
#     data = np.asarray(data)
#     for umbral in umbrals:
#         tp = 0
#         fn = 0
#         for d in data:
#             if d[0] >= umbral:
#                 tp += 1
#             else:
#                 fn += 1
#         try:
#             fn_rate_eer = fn / (fn + tp)
#         except ZeroDivisionError:
#             fn_rate_eer = 1
#         try:
#             tp_rate_eer = tp / (tp + fn)
#         except ZeroDivisionError:
#             tp_rate_eer = 1
#         fn_rate = np.append(fn_rate, fn_rate_eer)
#         tp_rate = np.append(tp_rate, tp_rate_eer)
#     print("TipoDocumento" + d)
#     print("TP")
#     print(*tp_rate, sep='\n')
#     print("FN")
#     print(*fn_rate, sep='\n')
#     print("------------------")


# age
# fn_rate = np.empty(shape=0)
# tp_rate = np.empty(shape=0)
# cur.execute("SELECT `ScoreReconocimientoFacialVivoChip` FROM `completados` WHERE (Edad>=60);")
# data = cur.fetchall()
# data = np.asarray(data)
# for umbral in umbrals:
#     tp = 0
#     fn = 0
#     for d in data:
#         if d[0] >= umbral:
#             tp += 1
#         else:
#             fn += 1
#     try:
#         fn_rate_eer = fn / (fn + tp)
#     except ZeroDivisionError:
#         fn_rate_eer = 1
#     try:
#         tp_rate_eer = tp / (tp + fn)
#     except ZeroDivisionError:
#         tp_rate_eer = 1
#     fn_rate = np.append(fn_rate, fn_rate_eer)
#     tp_rate = np.append(tp_rate, tp_rate_eer)
# print("Edad")
# print("TP")
# print(*tp_rate, sep='\n')
# print("FN")
# print(*fn_rate, sep='\n')
# print("------------------")


# country
for c in country:
    fn_rate = np.empty(shape=0)
    tp_rate = np.empty(shape=0)
    cur.execute("SELECT `ScoreReconocimientoFacialVivoChip` FROM `completados` WHERE PaisEmisor=" + c + ";")
    data = cur.fetchall()
    data = np.asarray(data)
    for umbral in umbrals:
        tp = 0
        fn = 0
        for d in data:
            if d[0] >= umbral:
                tp += 1
            else:
                fn += 1
        try:
            fn_rate_eer = fn / (fn + tp)
        except ZeroDivisionError:
            fn_rate_eer = 1
        try:
            tp_rate_eer = tp / (tp + fn)
        except ZeroDivisionError:
            tp_rate_eer = 1
        fn_rate = np.append(fn_rate, fn_rate_eer)
        tp_rate = np.append(tp_rate, tp_rate_eer)
    print("Pais" + c)
    print("TP")
    print(*tp_rate, sep='\n')
    print("FN")
    print(*fn_rate, sep='\n')
    print("------------------")