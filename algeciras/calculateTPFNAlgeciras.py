import MySQLdb as Mdb
import numpy as np

# Hardcoded
DB_HOST = "localhost"
DB_USER = "frav"
DB_PASS = "VXxL4UOLvB6wc01Y3Cxi"
DB_NAME = "piloto_algeciras"

con = Mdb.connect(DB_HOST, DB_USER, DB_PASS, DB_NAME)
cur = con.cursor()

# cur.execute("SELECT `ScoreReconocimientoFacialVivoChip` FROM `completados`;")
cur.execute("SELECT `ScoreDactilar` FROM `completados`;")
data = cur.fetchall()
data = np.asarray(data)

fn_rate = np.empty(shape=0)
tp_rate = np.empty(shape=0)
# umbrals = [10, 40, 50, 50, 60, 70, 80, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
umbrals = [10, 40, 50, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]

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

print(*tp_rate, sep='\n')
print("------------------")
print(*fn_rate, sep='\n')
