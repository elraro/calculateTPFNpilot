import MySQLdb as Mdb
import numpy as np
import matplotlib.pyplot as plt

# Hardcoded
DB_HOST = "localhost"
DB_USER = "frav"
DB_PASS = "VXxL4UOLvB6wc01Y3Cxi"
DB_NAME = "piloto_barajas"

# Listado de atributos
attributes = ["DeviationFromFrontalPose", "DeviationFromUniformLighting", "Sharpness", "Exposure",
              "EyeDistance", "Glasses", "GrayScaleDensity", "Male", "MouthClosed", "Age", "Crown", "Chin",
              "Eye0GazeFrontal", "Eye1GazeFrontal", "Eye0Open", "Eye1Open", "Eye0Red",
              "Eye1Red", "Eye0Tinted", "Eye1Tinted", "NatualSkinColour", "Eye0Confidence",
              "Eye1Confidence"]

binary_attributes = ["ISO_19794_5_EyesGazeFrontalBestPractice", "ISO_19794_5_EyesNotRedBestPractice",
                     "ISO_19794_5_EyesOpenBestPractice", "ISO_19794_5_GoodExposure", "ISO_19794_5_GoodGrayScaleProfile",
                     "ISO_19794_5_GoodVerticalFacePosition", "ISO_19794_5_HasNaturalSkinColour",
                     "ISO_19794_5_HorizontallyCenteredFace", "ISO_19794_5_ImageWidthToHeightBestPractice",
                     "ISO_19794_5_IsBackgroundUniformBestPractice", "ISO_19794_5_IsBestPractice",
                     "ISO_19794_5_IsCompliant", "ISO_19794_5_IsFrontal", "ISO_19794_5_IsFrontalBestPractice",
                     "ISO_19794_5_IsLightingUniform", "ISO_19794_5_IsSharp", "ISO_19794_5_LengthOfHead",
                     "ISO_19794_5_LengthOfHeadBestPractice", "ISO_19794_5_MouthClosedBestPractice",
                     "ISO_19794_5_NoHotSpots", "ISO_19794_5_NoTintedGlasses", "ISO_19794_5_OnlyOneFaceVisible",
                     "ISO_19794_5_Resolution", "ISO_19794_5_ResolutionBestPractice", "ISO_19794_5_WidthOfHead",
                     "ISO_19794_5_WidthOfHeadBestPractice"]


def calculate_hist(attr):
    con = Mdb.connect(DB_HOST, DB_USER, DB_PASS, DB_NAME)
    cur = con.cursor()
    # primero vamos a calcular la media
    cur.execute("SELECT AVG(" + attr + ") FROM calidad c;")
    data = cur.fetchall()
    data = np.asarray(data)
    average = data[0][0]
    formules = ["<", ">"]

    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = 'cm'
    plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
    plt.rcParams['axes.xmargin'] = 0
    plt.rcParams['axes.ymargin'] = 0
    plt.figure()
    for f in formules:
        cur.execute(
            "SELECT co.ScoreReconocimientoFacialVivoChip FROM completados co INNER JOIN calidad ca ON (ca.FechaInicio = co.FechaInicio AND ca.Hash = co.Hash) WHERE ca." + attr + f + str(
                average) + ";")
        data = cur.fetchall()
        data = np.asarray(data)

        i_plot = 1 if f == "<" else 2
        plt.subplot(210 + i_plot)
        if i_plot == 1:
            plt.hist(data, 50, histtype='stepfilled', facecolor='green', alpha=0.75)
        else:
            plt.hist(data, 50, histtype='stepfilled', facecolor='blue', alpha=0.75)
        if f == "<":
            plt.title(attr + " < " + str("{0:.4f}".format(average)))
        else:
            plt.title(attr + " > " + str("{0:.4f}".format(average)))
    plt.tight_layout()
    plt.savefig("densityAttr/" + attr + ".png")
    print("Readed " + attr)
    plt.close()
    con.close()


def calculate_bin_hist(attr):
    con = Mdb.connect(DB_HOST, DB_USER, DB_PASS, DB_NAME)
    cur = con.cursor()

    value = [0, 1]

    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = 'cm'
    plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
    plt.rcParams['axes.xmargin'] = 0
    plt.rcParams['axes.ymargin'] = 0
    plt.figure()
    for v in value:
        cur.execute(
            "SELECT co.ScoreReconocimientoFacialVivoChip FROM completados co INNER JOIN calidad ca ON (ca.FechaInicio = co.FechaInicio AND ca.Hash = co.Hash) WHERE ca." + attr + "=" + str(
                v) + ";")
        data = cur.fetchall()
        data = np.asarray(data)

        i_plot = 1 if v == 0 else 2
        plt.subplot(210 + i_plot)
        if i_plot == 1:
            plt.hist(data, 50, histtype='stepfilled', facecolor='green', alpha=0.75)
        else:
            plt.hist(data, 50, histtype='stepfilled', facecolor='blue', alpha=0.75)
        if v == 0:
            plt.title(attr + " = 0")
        else:
            plt.title(attr + " = 1")
    plt.tight_layout()
    plt.savefig("densityAttr/" + attr + ".png")
    print("Readed " + attr)
    plt.close()
    con.close()


for attr in attributes:
    calculate_hist(attr)
for attr in binary_attributes:
    calculate_bin_hist(attr)
