import MySQLdb as Mdb
import numpy as np

# Hardcoded
DB_HOST = ""
DB_USER = ""
DB_PASS = ""
DB_NAME = ""

con = Mdb.connect(DB_HOST, DB_USER, DB_PASS, DB_NAME)
cur = con.cursor()

cur.execute("SELECT `ScoreReconocimientoFacialVivoChip`, `ScoreDactilar` FROM `completados`;")
data = cur.fetchall()
data = np.asarray(data)

umbrals = [10, 40, 50, 60, 61, 62, 63, 64, 65, 66]

for umbral in umbrals:
    fn = np.empty(shape=0)
    for d in data:
        if d[1] < umbral:
            fn = np.append(fn, d[0])
    print("umbral: " + str(umbral))
    print(*fn, sep='\n')
    print("numero total: " + str(fn.size))
    print("---------")
