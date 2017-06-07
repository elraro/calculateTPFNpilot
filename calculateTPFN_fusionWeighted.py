import MySQLdb as Mdb
import numpy as np

# Hardcoded
DB_HOST = "localhost"
DB_USER = "frav"
DB_PASS = "VXxL4UOLvB6wc01Y3Cxi"
DB_NAME = "piloto_ambos"

con = Mdb.connect(DB_HOST, DB_USER, DB_PASS, DB_NAME)
cur = con.cursor()

# SELECT (co.ScoreDactilar + co.ScoreReconocimientoFacialVivoChip) / 2 as media, co.ScoreDactilar, co.ScoreReconocimientoFacialVivoChip, ca.ISO_19794_5_OnlyOneFaceVisible, ca.ISO_19794_5_NoTintedGlasses, ca.ISO_19794_5_MouthClosedBestPractice, ca.ISO_19794_5_IsSharp, ca.ISO_19794_5_IsLightingUniform, ca.ISO_19794_5_IsFrontalBestPractice, ca.ISO_19794_5_HorizontallyCenteredFace, ca.ISO_19794_5_IsFrontal, ca.ISO_19794_5_HasNaturalSkinColour, ca.ISO_19794_5_GoodVerticalFacePosition, ca.ISO_19794_5_GoodExposure, ca.ISO_19794_5_EyesOpenBestPractice, ca.ISO_19794_5_EyesNotRedBestPractice, ca.EyeDistance, ca.Eye0Confidence, ca.Eye1Confidence, ca.Eye0GazeFrontal, ca.Eye1GazeFrontal, ca.Eye0Open, ca.Eye1Open, ca.Eye0Red, ca.Eye1Red, ca.Eye0Tinted, ca.Eye1Tinted, ca.Chin, ca.Crown, ca.MouthClosed, ca.Glasses, ca.Exposure, ca.Sharpness, ca.DeviationFromFrontalPose, ca.DeviationFromUniformLighting, ca.Age, ca.PaisEmisor, ca.Sexo, ca.NatualSkinColour FROM completados co, calidad ca WHERE co.Hash = ca.Hash AND co.FechaInicio = ca.FechaInicio

cur.execute("SELECT co.ScoreDactilar, co.ScoreReconocimientoFacialVivoChip, ca.ISO_19794_5_OnlyOneFaceVisible, ca.ISO_19794_5_NoTintedGlasses, ca.ISO_19794_5_MouthClosedBestPractice, ca.ISO_19794_5_IsSharp, ca.ISO_19794_5_IsLightingUniform, ca.ISO_19794_5_IsFrontalBestPractice, ca.ISO_19794_5_HorizontallyCenteredFace, ca.ISO_19794_5_IsFrontal, ca.ISO_19794_5_HasNaturalSkinColour, ca.ISO_19794_5_GoodVerticalFacePosition, ca.ISO_19794_5_GoodExposure, ca.ISO_19794_5_EyesOpenBestPractice, ca.ISO_19794_5_EyesNotRedBestPractice, ca.EyeDistance, ca.Eye0Confidence, ca.Eye1Confidence, ca.Eye0GazeFrontal, ca.Eye1GazeFrontal, ca.Eye0Open, ca.Eye1Open, ca.Eye0Red, ca.Eye1Red, ca.Eye0Tinted, ca.Eye1Tinted, ca.Chin, ca.Crown, ca.MouthClosed, ca.Glasses, ca.Exposure, ca.Sharpness, ca.DeviationFromFrontalPose, ca.DeviationFromUniformLighting, ca.Age, ca.PaisEmisor, ca.Sexo, ca.NatualSkinColour, co.CalidadH1 FROM completados co, calidad ca WHERE co.Hash = ca.Hash AND co.FechaInicio = ca.FechaInicio")
data = cur.fetchall()
data = np.asarray(data)

weights = []
fn_rate = np.empty(shape=0)
tp_rate = np.empty(shape=0)
umbrals = [40, 50, 60, 70, 80, 90, 91, 92, 93, 94, 95]

for d in data:
    weight_face = 50
    # esto es la query,
    # 1 co.ScoreDactilar, 2 co.ScoreReconocimientoFacialVivoChip,
    # 3 ca.ISO_19794_5_OnlyOneFaceVisible, 4 ca.ISO_19794_5_NoTintedGlasses,
    # 5 ca.ISO_19794_5_MouthClosedBestPractice, 6 ca.ISO_19794_5_IsSharp,
    # 7 ca.ISO_19794_5_IsLightingUniform, 8 ca.ISO_19794_5_IsFrontalBestPractice,
    # 9 ca.ISO_19794_5_HorizontallyCenteredFace, 10 ca.ISO_19794_5_IsFrontal,
    # 11 ca.ISO_19794_5_HasNaturalSkinColour, 12 ca.ISO_19794_5_GoodVerticalFacePosition,
    # 13 ca.ISO_19794_5_GoodExposure, 14 ca.ISO_19794_5_EyesOpenBestPractice,
    # 15 ca.ISO_19794_5_EyesNotRedBestPractice, 16 ca.EyeDistance, 17 ca.Eye0Confidence,
    # 18 ca.Eye1Confidence, 19 ca.Eye0GazeFrontal, 20 ca.Eye1GazeFrontal,
    # 21 ca.Eye0Open, 22 ca.Eye1Open, 23 ca.Eye0Red, 24 ca.Eye1Red, 25 ca.Eye0Tinted, 26 ca.Eye1Tinted,
    # 27 ca.Chin, 28 ca.Crown, 29 ca.MouthClosed, 30 ca.Glasses, 31 ca.Exposure, 32 ca.Sharpness,
    # 33 ca.DeviationFromFrontalPose, 34 ca.DeviationFromUniformLighting, 35 ca.Age,
    # 36 ca.PaisEmisor, 37 ca.Sexo, 38 ca.NatualSkinColour
    # ----------------
    # estos son los mejores atributos de FRAV-ABC
    # de mejor atributo a peor atributo  1-10: 2% 11-20: 1% 21-37: 0,5%
    # 1 ISO_19794_5_NoTintedGlasses, 2 DeviationFromFrontalPose
    # 3 Eye1GazeFrontal, 4 eye0Confidence, 5 eye0Open, 6 eye1Confidence
    # 7 eye1Open, 8 exposure, 9 faceConfidence, 10 DeviationFromUniformLighting
    # 11 Eye0GazeFrontal, 12 eye1Tinted, 13 eyeDistance, 14 ear1
    # 15 Glasses, 16 eye0Tinted, 17 ear0, 18 ISO_19794_5_HasNaturalSkinColour
    # 19 NaturalSkinColour, 20 age, 21 ISO_19794_5_HorizontallyCenteredFace
    # 22 sharpness, 23 eye0X, 24 BackgroundUniformity, 25 ISO_19794_5_IsBackgroundUniformBestPractice
    # 26 ISO_19794_5_IsSharp, 27 eye0Y, 28 ISO_19794_5_EyesGazeFrontalBestPractice
    # 29 eye1X, 30 grayScaleDensity, 31 ISO_19794_5_GoodVerticalFacePosition, 32 ISO_19794_5_IsLightingUniform
    # 33 ISO_19794_5_IsFrontalBestPractice, 34 poseAngleRoll, 35 crown, 36 ISO_19794_5_MouthClosedBestPractice
    # 37 ISO_19794_5_ResolutionBestPractice

    # ca.ISO_19794_5_NoTintedGlasses
    if float(d[3]) == 1:
        weight_face += 10
    else:
        weight_face -= 10
    # ca.ISO_19794_5_MouthClosedBestPractice
    if float(d[4]) == 1:
        weight_face += 10
    else:
        weight_face -= 10
    # ca.ISO_19794_5_IsSharp
    if float(d[5]) == 1:
        weight_face += 5
    else:
        weight_face -= 5
    # ca.ISO_19794_5_IsLightingUniform
    if float(d[6]) == 1:
        weight_face += 5
    else:
        weight_face -= 5
    # ca.ISO_19794_5_IsFrontalBestPractice
    if float(d[7]) == 1:
        weight_face += 5
    else:
        weight_face -= 5
    # ca.ISO_19794_5_HorizontallyCenteredFace
    if float(d[8]) == 1:
        weight_face += 5
    else:
        weight_face -= 5
    # ca.ISO_19794_5_IsFrontal
    if float(d[9]) == 1:
        weight_face += 5
    else:
        weight_face -= 5
    # ca.ISO_19794_5_HasNaturalSkinColour
    if float(d[10]) == 1:
        weight_face += 7.5
    else:
        weight_face -= 7.5
    # ca.ISO_19794_5_GoodVerticalFacePosition
    if float(d[11]) == 1:
        weight_face += 5
    else:
        weight_face -= 5
    # ca.ISO_19794_5_GoodExposure
    # ca.ISO_19794_5_EyesOpenBestPractice <- ojo con este que no estaba
    if float(d[13]) == 1:
        weight_face += 5
    else:
        weight_face -= 5
    # ca.ISO_19794_5_EyesNotRedBestPractice
    # ca.EyeDistance
    if float(d[15]) > -3.3 and float(d[15]) < 3.3:
        weight_face += 7.5
    else:
        weight_face -= 7.5
    # ca.Eye0Confidence
    if float(d[16]) > 0.8 and float(d[16]) < 3.3:
        weight_face += 7.5
    else:
        weight_face -= 7.5
    # ca.Eye1Confidence
    if float(d[17]) > 0.8 and float(d[17]) < 3.3:
        weight_face += 10
    else:
        weight_face -= 10
    # ca.Eye0GazeFrontal
    if float(d[18]) > -1 and float(d[18]) < 3.7:
        weight_face += 10
    else:
        weight_face -= 10
    # ca.Eye1GazeFrontal
    if float(d[19]) > -1 and float(d[19]) < 3.7:
        weight_face += 10
    else:
        weight_face -= 10
    # ca.Eye0Open
    # ca.Eye1Open
    # ca.Eye0Red
    # ca.Eye1Red
    # ca.Eye0Tinted
    # ca.Eye1Tinted
    # ca.Chin
    # ca.Crown
    # ca.MouthClosed
    # ca.Glasses
    # ca.Exposure
    # ca.Sharpness
    # ca.DeviationFromFrontalPose
    # ca.DeviationFromUniformLighting
    # ca.NatualSkinColour
    # calidadH1
    weights.append(np.array([weight_face, float(d[1]), 100-weight_face, float(d[0])]))

print(weights)
for umbral in umbrals:
    tp = 0
    fn = 0
    for d in weights:
        if d[3] != 0:
            if (d[1]*(d[0]/100)+d[3]*(d[2]/100)) >= umbral:
                tp += 1
            else:
                fn += 1
        else:
            if d[1] >= umbral:
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
