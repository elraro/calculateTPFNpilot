import MySQLdb as Mdb
import numpy as np
import matplotlib.pyplot as plt

# Hardcoded
DB_HOST = ""
DB_USER = ""
DB_PASS = ""
DB_NAME = ""

con = Mdb.connect(DB_HOST, DB_USER, DB_PASS, DB_NAME)
cur = con.cursor()

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'cm'
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
plt.rcParams['axes.xmargin'] = 0
plt.rcParams['axes.ymargin'] = 0
plt.figure()

umbrals = [1, 2, 3, 4, 5]
umbrals_score = [10, 40, 50, 60, 61, 62, 63, 64, 65, 66]

for umbral in umbrals:
    fn_rate = np.empty(shape=0)
    tp_rate = np.empty(shape=0)
    cur.execute("SELECT `ScoreDactilar` FROM `completados` WHERE CalidadH1=" + str(umbral) + ";")
    data = cur.fetchall()
    data = np.asarray(data)
    for umbral_s in umbrals_score:
        tp = 0
        fn = 0
        for d in data:
            if d[0] >= umbral_s:
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
    print("Umbral " + str(umbral))
    print("TP")
    print(*tp_rate, sep='\n')
    print("FN")
    print(*fn_rate, sep='\n')
    print("------------------")