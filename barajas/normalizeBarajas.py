import MySQLdb as Mdb
import numpy as np

# Hardcoded
DB_HOST = "localhost"
DB_USER = "frav"
DB_PASS = "VXxL4UOLvB6wc01Y3Cxi"
DB_NAME = "piloto_barajas"
HIGH = 6
LOW = -6

attr = ["DeviationFromFrontalPose", "DeviationFromUniformLighting", "Sharpness", "Exposure", "EyeDistance", "Glasses",
        "GrayScaleDensity", "MouthClosed", "Crown", "Chin", "Eye0GazeFrontal", "Eye1GazeFrontal", "Eye0Open",
        "Eye1Open", "Eye0Red", "Eye1Red", "Eye0Tinted", "Eye1Tinted", "NatualSkinColour", "Eye0Confidence",
        "Eye1Confidence"]

con = Mdb.connect(DB_HOST, DB_USER, DB_PASS, DB_NAME)
cur = con.cursor()

for atr in attr:
    cur.execute("SELECT FechaInicio, Hash, " + atr + " FROM calidad")
    data = cur.fetchall()
    data = np.asarray(data)
    l = [float(i) for i in data[:, 2]]
    minimum = min(l)
    maximum = max(l)
    rng = maximum - minimum
    count = 0
    for val in l:
        v = HIGH - ((HIGH - LOW) * (maximum - val) / rng)
        cur.execute(
            "UPDATE calidad SET " + atr + "=" + str(v) + " WHERE FechaInicio='" + data[count][0] + "' AND Hash='" +
            data[count][
                1] + "'")
        con.commit()
        count += 1
