import MySQLdb as Mdb
import numpy as np

# Hardcoded
DB_HOST = "localhost"
DB_USER = "frav"
DB_PASS = "VXxL4UOLvB6wc01Y3Cxi"
DB_NAME = "piloto_barajas"

con = Mdb.connect(DB_HOST, DB_USER, DB_PASS, DB_NAME)
cur = con.cursor()

# SELECT (co.ScoreDactilar + co.ScoreReconocimientoFacialVivoChip) / 2 as media, co.ScoreDactilar, co.ScoreReconocimientoFacialVivoChip, ca.ISO_19794_5_OnlyOneFaceVisible, ca.ISO_19794_5_NoTintedGlasses, ca.ISO_19794_5_MouthClosedBestPractice, ca.ISO_19794_5_IsSharp, ca.ISO_19794_5_IsLightingUniform, ca.ISO_19794_5_IsFrontalBestPractice, ca.ISO_19794_5_HorizontallyCenteredFace, ca.ISO_19794_5_IsFrontal, ca.ISO_19794_5_HasNaturalSkinColour, ca.ISO_19794_5_GoodVerticalFacePosition, ca.ISO_19794_5_GoodExposure, ca.ISO_19794_5_EyesOpenBestPractice, ca.ISO_19794_5_EyesNotRedBestPractice, ca.EyeDistance, ca.Eye0Confidence, ca.Eye1Confidence, ca.Eye0GazeFrontal, ca.Eye1GazeFrontal, ca.Eye0Open, ca.Eye1Open, ca.Eye0Red, ca.Eye1Red, ca.Eye0Tinted, ca.Eye1Tinted, ca.Chin, ca.Crown, ca.MouthClosed, ca.Glasses, ca.Exposure, ca.Sharpness, ca.DeviationFromFrontalPose, ca.DeviationFromUniformLighting, ca.Age, ca.PaisEmisor, ca.Sexo, ca.NatualSkinColour FROM completados co, calidad ca WHERE co.Hash = ca.Hash AND co.FechaInicio = ca.FechaInicio

cur.execute("SELECT co.ScoreDactilar, co.ScoreReconocimientoFacialVivoChip, ca.ISO_19794_5_OnlyOneFaceVisible, ca.ISO_19794_5_NoTintedGlasses, ca.ISO_19794_5_MouthClosedBestPractice, ca.ISO_19794_5_IsSharp, ca.ISO_19794_5_IsLightingUniform, ca.ISO_19794_5_IsFrontalBestPractice, ca.ISO_19794_5_HorizontallyCenteredFace, ca.ISO_19794_5_IsFrontal, ca.ISO_19794_5_HasNaturalSkinColour, ca.ISO_19794_5_GoodVerticalFacePosition, ca.ISO_19794_5_GoodExposure, ca.ISO_19794_5_EyesOpenBestPractice, ca.ISO_19794_5_EyesNotRedBestPractice, ca.EyeDistance, ca.Eye0Confidence, ca.Eye1Confidence, ca.Eye0GazeFrontal, ca.Eye1GazeFrontal, ca.Eye0Open, ca.Eye1Open, ca.Eye0Red, ca.Eye1Red, ca.Eye0Tinted, ca.Eye1Tinted, ca.Chin, ca.Crown, ca.MouthClosed, ca.Glasses, ca.Exposure, ca.Sharpness, ca.DeviationFromFrontalPose, ca.DeviationFromUniformLighting, ca.Age, ca.PaisEmisor, ca.Sexo, ca.NatualSkinColour FROM completados co, calidad ca WHERE co.Hash = ca.Hash AND co.FechaInicio = ca.FechaInicio")
data = cur.fetchall()
data = np.asarray(data)

weights = np.empty(shape=0)
fn_rate = np.empty(shape=0)
tp_rate = np.empty(shape=0)
umbrals = [40, 50, 60, 70, 80, 81, 82, 83]

for d in data:
    weight_face = 50
    weight_finger = 50
    # esto es la query
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
    FROM
    completados
    co, calidad
    ca
    WHERE
    co.Hash = ca.Hash
    AND
    co.FechaInicio = ca.FechaInicio
    ")

    # ----------------
    ISO_19794_5_NoTintedGlasses
    DeviationFromFrontalPose
    media
    Eye1GazeFrontal
    media
    eye0Confidence
    eye0Open
    eye1Confidence
    eye1Open
    exposure
    faceConfidence
    DeviationFromUniformLighting
    media
    Eye0GazeFrontal
    media
    eye1Tinted
    eyeDistance
    ear1
    Glasses > 0, < 0
    eye0Tinted
    ear0
    ISO_19794_5_HasNaturalSkinColour
    NaturalSkinColour > 0.5, < 0.5
    Features_WearsGlasses = 0, = 1
    light
    age
    camera
    ISO_19794_5_HorizontallyCenteredFace
    sharpness > 0.5, < 0.5
    eye0X
    BackgroundUniformity
    ISO_19794_5_IsBackgroundUniformBestPractice
    ethnicityWhite < 0, > 0
    ISO_19794_5_IsSharp
    eye0Y
    ISO_19794_5_EyesGazeFrontalBestPractice
    eye1X
    grayScaleDensity
    ISO_19794_5_GoodVerticalFacePosition
    ISO_19794_5_IsLightingUniform
    ISO_19794_5_IsFrontalBestPractice
    Features_Ethnicity = 0, = 1, = 2
    Features_Gender = 0, = 1
    IsMale > 0, < 0
    poseAngleRoll
    crown
    ISO_19794_5_MouthClosedBestPractice
    ISO_19794_5_ResolutionBestPractice

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
