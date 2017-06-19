import MySQLdb as Mdb
import numpy as np

# Hardcoded
DB_HOST = ""
DB_USER = ""
DB_PASS = ""
DB_NAME = ""

con = Mdb.connect(DB_HOST, DB_USER, DB_PASS, DB_NAME)
cur = con.cursor()

# SELECT (co.ScoreDactilar + co.ScoreReconocimientoFacialVivoChip) / 2 as media, co.ScoreDactilar, co.ScoreReconocimientoFacialVivoChip, ca.ISO_19794_5_OnlyOneFaceVisible, ca.ISO_19794_5_NoTintedGlasses, ca.ISO_19794_5_MouthClosedBestPractice, ca.ISO_19794_5_IsSharp, ca.ISO_19794_5_IsLightingUniform, ca.ISO_19794_5_IsFrontalBestPractice, ca.ISO_19794_5_HorizontallyCenteredFace, ca.ISO_19794_5_IsFrontal, ca.ISO_19794_5_HasNaturalSkinColour, ca.ISO_19794_5_GoodVerticalFacePosition, ca.ISO_19794_5_GoodExposure, ca.ISO_19794_5_EyesOpenBestPractice, ca.ISO_19794_5_EyesNotRedBestPractice, ca.EyeDistance, ca.Eye0Confidence, ca.Eye1Confidence, ca.Eye0GazeFrontal, ca.Eye1GazeFrontal, ca.Eye0Open, ca.Eye1Open, ca.Eye0Red, ca.Eye1Red, ca.Eye0Tinted, ca.Eye1Tinted, ca.Chin, ca.Crown, ca.MouthClosed, ca.Glasses, ca.Exposure, ca.Sharpness, ca.DeviationFromFrontalPose, ca.DeviationFromUniformLighting, ca.Age, ca.PaisEmisor, ca.Sexo, ca.NatualSkinColour FROM completados co, calidad ca WHERE co.Hash = ca.Hash AND co.FechaInicio = ca.FechaInicio

cur.execute("SELECT co.ScoreDactilar, co.ScoreReconocimientoFacialVivoChip, ca.ISO_19794_5_OnlyOneFaceVisible, ca.ISO_19794_5_NoTintedGlasses, ca.ISO_19794_5_MouthClosedBestPractice, ca.ISO_19794_5_IsSharp, ca.ISO_19794_5_IsLightingUniform, ca.ISO_19794_5_IsFrontalBestPractice, ca.ISO_19794_5_HorizontallyCenteredFace, ca.ISO_19794_5_IsFrontal, ca.ISO_19794_5_HasNaturalSkinColour, ca.ISO_19794_5_GoodVerticalFacePosition, ca.ISO_19794_5_GoodExposure, ca.ISO_19794_5_EyesOpenBestPractice, ca.ISO_19794_5_EyesNotRedBestPractice, ca.EyeDistance, ca.Eye0Confidence, ca.Eye1Confidence, ca.Eye0GazeFrontal, ca.Eye1GazeFrontal, ca.Eye0Open, ca.Eye1Open, ca.Eye0Red, ca.Eye1Red, ca.Eye0Tinted, ca.Eye1Tinted, ca.Chin, ca.Crown, ca.MouthClosed, ca.Glasses, ca.Exposure, ca.Sharpness, ca.DeviationFromFrontalPose, ca.DeviationFromUniformLighting, ca.Age, ca.PaisEmisor, ca.Sexo, ca.NatualSkinColour FROM completados co, calidad ca WHERE co.Hash = ca.Hash AND co.FechaInicio = ca.FechaInicio")
data = cur.fetchall()
data = np.asarray(data)

weights = []
fn_rate = np.empty(shape=0)
tp_rate = np.empty(shape=0)
umbrals = [40, 50, 60, 70, 80, 81, 82, 83]

for d in data:
    weight_face = 50
    weight_finger = 50
    # ca.ISO_19794_5_NoTintedGlasses
    if float(d[3]) == 1:
        weight_face += 2
        weight_finger -= 2
    else:
        weight_face -= 2
        weight_finger += 2
    # ca.ISO_19794_5_MouthClosedBestPractice
    if float(d[4]) == 1:
        weight_face += 2
        weight_finger -= 2
    else:
        weight_face -= 2
        weight_finger += 2
    # ca.ISO_19794_5_IsSharp
    if float(d[5]) == 1:
        weight_face += 0.5
        weight_finger -= 0.5
    else:
        weight_face -= 0.5
        weight_finger += 0.5
    # ca.ISO_19794_5_IsLightingUniform
    if float(d[6]) == 1:
        weight_face += 0.5
        weight_finger -= 0.5
    else:
        weight_face -= 0.5
        weight_finger += 0.5
    # ca.ISO_19794_5_IsFrontalBestPractice
    if float(d[7]) == 1:
        weight_face += 0.5
        weight_finger -= 0.5
    else:
        weight_face -= 0.5
        weight_finger += 0.5
    # ca.ISO_19794_5_HorizontallyCenteredFace
    if float(d[8]) == 1:
        weight_face += 0.5
        weight_finger -= 0.5
    else:
        weight_face -= 0.5
        weight_finger += 0.5
    # ca.ISO_19794_5_IsFrontal
    if float(d[9]) == 1:
        weight_face += 0.5
        weight_finger -= 0.5
    else:
        weight_face -= 0.5
        weight_finger += 0.5
    # ca.ISO_19794_5_HasNaturalSkinColour
    if float(d[10]) == 1:
        weight_face += 1
        weight_finger -= 1
    else:
        weight_face -= 1
        weight_finger += 1
    # ca.ISO_19794_5_GoodVerticalFacePosition
    if float(d[11]) == 1:
        weight_face += 0.5
        weight_finger -= 0.5
    else:
        weight_face -= 0.5
        weight_finger += 0.5
    # ca.ISO_19794_5_EyesOpenBestPractice
    if float(d[13]) == 1:
        weight_face += 0.5
        weight_finger -= 0.5
    else:
        weight_face -= 0.5
        weight_finger += 0.5
    # ca.EyeDistance
    if float(d[15]) > -3.3 and float(d[15]) < 3.3:
        weight_face += 1
        weight_finger -= 1
    else:
        weight_face -= 1
        weight_finger += 1
    # ca.Eye0Confidence
    if float(d[16]) > 0.8 and float(d[16]) < 3.3:
        weight_face += 2
        weight_finger -= 2
    else:
        weight_face -= 2
        weight_finger += 2
    # ca.Eye1Confidence
    if float(d[17]) > 0.8 and float(d[17]) < 3.3:
        weight_face += 2
        weight_finger -= 2
    else:
        weight_face -= 2
        weight_finger += 2
    # ca.Eye0GazeFrontal
    if float(d[18]) > -1 and float(d[18]) < 3.7:
        weight_face += 2
        weight_finger -= 2
    else:
        weight_face -= 2
        weight_finger += 2
    # ca.Eye1GazeFrontal
    if float(d[19]) > -1 and float(d[19]) < 3.7:
        weight_face += 2
        weight_finger -= 2
    else:
        weight_face -= 2
        weight_finger += 2
    weights.append(np.array([weight_face, float(d[1]), weight_finger, float(d[0])]))

print(weights)
for umbral in umbrals:
    tp = 0
    fn = 0
    for d in weights:
        if (d[1]*(d[0]/100)+d[3]*(d[2]/100)) >= umbral:
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
