
<div style="text-align: center; padding: 60px; background: linear-gradient(135deg, #003366 0%, #004d99 100%); color: white; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); margin: 30px auto; max-width: 1200px; min-height: 600px; display: flex; flex-direction: column; align-items: center; justify-content: center;">

<div style="max-width: 800px;">

# <span style="font-size: 5.5rem; font-weight: 700; margin-bottom: 30px; line-height: 1.2; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); display: block;">Slicer4 Minuten
</span>

<p style="font-size: 2.5rem; font-weight: 300; margin-bottom: 15px; opacity: 0.95;">Dr. Sonia Pujol</p>

<p style="font-size: 2rem; font-weight: 300; margin-bottom: 40px; opacity: 0.85;"> </p>

<p style="font-size: 2.1rem; line-height: 1.8; font-weight: 300; opacity: 0.9; max-width: 700px; margin: 0 auto;">Assistenzprofessor für Radiologie
Brigham and Women’s Hospital
Harvard Medical School</p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Slicer4 Minuten Tutorial</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>Dieses Tutorial bietet eine 4-minütige Einführung in die 3D-Visualisierungsfunktionen der Software „Slicer5“ zur medizinischen Bildanalyse. </p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Slicer5-Software und Datensatz</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>*Laden Sie die Slicer5-Software unter http://download.slicer.org herunter.</p><p></p><p>*Laden Sie den Slicer4minute-Datensatz unter https://www.slicer.org/wiki/Documentation/4.10/Training herunter.</p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">3D Slicer version 5</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![3D Slicer version 5](3_3DSlicerversion5.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">3D-Slicer-Szene</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>*Eine Slicer-Szene ist eine MRML-Datei (Medical Reality Modeling Language), die eine Liste der in Slicer geladenen Elemente enthält (Volumen, Modelle, Referenzmarken, Transformationen usw.).</p><p>*Im folgenden Beispiel verwenden wir eine Szene namens „Slicer4minute.mrml“, die aus einem MRT-Scan und 3D-Modellen des Kopfes besteht. </p><p>*Die Szenendatei und die Datensätze wurden als MRB-Datei (Medical Reality Bundle) gespeichert. </p><p>*Das MRB-Dateiformat ist das Archivdateiformat von Slicer.</p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Laden des Datensatzes „Slicer4minute“</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Laden des Datensatzes „Slicer4minute“](5_LoadingtheSlicer4minutedataset.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Szene aus „Slicer4minute“</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Szene aus „Slicer4minute“](6_Slicer4minuteScene.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">3D-Visualisierung</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![3D-Visualisierung](7_3DVisualization.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">3D-Visualisierung</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![3D-Visualisierung](8_3Dvisualization.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">3D-Visualisierung</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![3D-Visualisierung](9_3DVisualization.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">3D-Visualisierung</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![3D-Visualisierung](10_3DVisualization.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">3D-Visualisierung</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![3D-Visualisierung](11_3DVisualization.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Anatomische Darstellungen</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Anatomische Darstellungen](12_AnatomicalViews.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">3D-Visualisierung</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![3D-Visualisierung](13_3DVisualization.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">3D-Visualisierung</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![3D-Visualisierung](14_3DVisualization.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">3D-Visualisierung</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![3D-Visualisierung](15_3DVisualization.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Slicer4 Minuten Tutorial</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>*Dieses Tutorial bot eine kurze Einführung in die interaktive 3D-Visualisierung von MRT-Daten und 3D-Modellen in Slicer.</p><p></p><p>*Das Slicer5-Schulungskompendium enthält eine Reihe von Tutorials und vorberechneten Datensätzen, mit denen Sie den Umgang mit der Software erlernen können.</p>

</div>

</div>

---

<div style="text-align: center; padding: 40px; background: linear-gradient(135deg, #004d99 0%, #003366 100%); color: white; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); margin: 30px auto; max-width: 1200px; min-height: 600px; display: flex; flex-direction: column; align-items: center; justify-content: center;">

<div style="max-width: 800px;">

# <span style="font-size: 4.5rem; margin-bottom: 40px; display: block; border-bottom: 2px solid rgba(255, 255, 255, 0.3); padding-bottom: 20px;">Danksagungen</span>

<div style="text-align: left;">

<p>Nationale Allianz für medizinische Bildverarbeitung</p><p>(National Alliance for Medical Image</p><p>Computing)</p><p>NIH U54EB005149</p><p></p><p>Zentrum für Neurobildanalyse</p><p>NIH P41EB015902</p><p></p>

</div>

</div>

</div>

---
