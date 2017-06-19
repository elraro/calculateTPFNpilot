import MySQLdb as Mdb
import numpy as np

# Hardcoded
DB_HOST = ""
DB_USER = ""
DB_PASS = ""
DB_NAME = ""
HIGH = 70
LOW = 0

attr = ["ScoreDactilar"]

con = Mdb.connect(DB_HOST, DB_USER, DB_PASS, DB_NAME)
cur = con.cursor()

for atr in attr:
    print("Leyendo atributo " + atr)
    cur.execute("SELECT FechaInicio, Hash, " + atr + " FROM completados")
    data = cur.fetchall()
    data = np.asarray(data)
    l = [float(i) for i in data[:, 2]]
    print("Convertido lista a float...")
    minimum = min(l)
    maximum = max(l)
    print(minimum)
    print(maximum)
    rng = maximum - minimum
    count = 0
    print("Vamos a actualizar valores")
    for val in l:
        v = HIGH - ((HIGH - LOW) * (maximum - val) / rng)
        cur.execute(
            "UPDATE completados SET " + atr + "=" + str(v) + " WHERE FechaInicio='" + data[count][0] + "' AND Hash='" + data[count][1] + "'")
        con.commit()
        count += 1
    print("Atributo listo")
    print("-----------------------------------------")
