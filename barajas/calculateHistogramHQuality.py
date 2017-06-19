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

for umbral in umbrals:
    plt.figure()
    cur.execute("SELECT `ScoreDactilar` FROM `completados` WHERE CalidadH1=" + str(umbral) + ";")
    data = cur.fetchall()
    data = np.asarray(data)
    plt.hist(data, 50, histtype='stepfilled', facecolor='g', alpha=0.75)
    plt.title("ScoreDactilar CalidadH1=" + str(umbral))
    plt.savefig("densityH1/" + str(umbral) + ".png")
    plt.close()

plt.figure()
colors = ["green", "red", "yellow", "blue", "purple"]
for umbral in umbrals:
    cur.execute("SELECT `ScoreDactilar` FROM `completados` WHERE CalidadH1=" + str(umbral) + ";")
    data = cur.fetchall()
    data = np.asarray(data)
    plt.hist(data, 50, histtype='stepfilled', facecolor=colors.pop(0), alpha=0.75)
plt.title("ScoreDactilar")
plt.savefig("densityH1/total.png")
plt.close()