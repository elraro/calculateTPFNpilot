import MySQLdb as Mdb
import numpy as np

# Hardcoded
DB_HOST = ""
DB_USER = ""
DB_PASS = ""
DB_NAME = ""
HIGH = 6
LOW = -6

attr = ["deviationFromFrontalPose", "deviationFromUniformLighting", "sharpness", "exposure", "eyeDistance", "glasses",
        "grayScaleDensity", "mouthClosed", "crown", "chin", "eye0GazeFrontal", "eye1GazeFrontal", "eye0Open",
        "eye1Open", "eye0Red", "eye1Red", "eye0Tinted", "eye1Tinted", "naturalSkinColour", "eye0Confidence",
        "eye1Confidence"]

con = Mdb.connect(DB_HOST, DB_USER, DB_PASS, DB_NAME)
cur = con.cursor()

for atr in attr:
    print("Leyendo atributo " + atr)
    cur.execute("SELECT id, " + atr + " FROM imgs_data")
    data = cur.fetchall()
    data = np.asarray(data)
    l = [float(i) for i in data[:, 1]]
    print("Convertido lista a float...")
    minimum = min(l)
    maximum = max(l)
    rng = maximum - minimum
    count = 0
    print("Vamos a actualizar valores")
    for val in l:
        v = HIGH - ((HIGH - LOW) * (maximum - val) / rng)
        cur.execute(
            "UPDATE imgs_data SET " + atr + "=" + str(v) + " WHERE id=" + str(data[count][0]))
        con.commit()
        count += 1
    print("Atributo listo")
    print("-----------------------------------------")
