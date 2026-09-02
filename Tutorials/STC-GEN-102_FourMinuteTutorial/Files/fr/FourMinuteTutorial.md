
<div style="text-align: center; padding: 60px; background: linear-gradient(135deg, #003366 0%, #004d99 100%); color: white; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); margin: 30px auto; max-width: 1200px; min-height: 600px; display: flex; flex-direction: column; align-items: center; justify-content: center;">

<div style="max-width: 800px;">

# <span style="font-size: 5.5rem; font-weight: 700; margin-bottom: 30px; line-height: 1.2; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); display: block;">Slicer4 Minute
</span>

<p style="font-size: 2.5rem; font-weight: 300; margin-bottom: 15px; opacity: 0.95;">Sonia Pujol, Ph.D.</p>

<p style="font-size: 2rem; font-weight: 300; margin-bottom: 40px; opacity: 0.85;"> </p>

<p style="font-size: 2.1rem; line-height: 1.8; font-weight: 300; opacity: 0.9; max-width: 700px; margin: 0 auto;">Professeur adjoint en radiologie
Brigham and Women’s Hospital
Harvard Medical School</p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Tutoriel Slicer4 minute</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>Ce tutoriel est une introduction de 4 minutes aux capacités de visualisation 3D du logiciel Slicer5 pour l’analyse d’images médicales. </p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Logiciel et jeu de données Slicer5</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>*Téléchargez le logiciel Slicer5 disponible à l’adresse http://download.slicer.org</p><p></p><p>*Téléchargez le jeu de données Slicer4minute disponible à l’adresse https://www.slicer.org/wiki/Documentation/4.10/Training</p>

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

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Slicer affiche les éléments de la scène slicer4minute.
La scène contient une IRM ainsi que des modèles de surface 3D du cerveau.	</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>*Une scène Slicer est un fichier MRML (Medical Reality Modeling Language) qui contient une liste d’éléments chargés dans Slicer (volumes, modèles, repères, transformations, etc.)</p><p>*Dans l’exemple suivant, nous utilisons une scène « Slicer4minute.mrml » composée d’une IRM et de modèles 3D de la tête.</p><p>*Le fichier de scène et les jeux de données ont été enregistrés sous forme de fichier MRB (Medical Reality Bundle).</p><p>*Le format de fichier MRB est le format d’archive de Slicer.</p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Chargement du jeu de données Slicer4minute</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Chargement du jeu de données Slicer4minute](5_LoadingtheSlicer4minutedataset.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Scène Slicer4minute</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Scène Slicer4minute](6_Slicer4minuteScene.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Visualisation 3D</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Visualisation 3D](7_3DVisualization.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Visualisation 3D</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Visualisation 3D](8_3Dvisualization.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Visualisation 3D</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Visualisation 3D](9_3DVisualization.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Visualisation 3D</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Visualisation 3D](10_3DVisualization.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Visualisation 3D</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Visualisation 3D](11_3DVisualization.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Vues anatomiques</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Vues anatomiques](12_AnatomicalViews.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Visualisation 3D</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Visualisation 3D](13_3DVisualization.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Visualisation 3D</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Visualisation 3D](14_3DVisualization.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Visualisation 3D</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Visualisation 3D](15_3DVisualization.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Tutoriel Slicer4 minute</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>*Ce tutoriel était une courte introduction à la visualisation 3D interactive des données IRM et des modèles 3D dans Slicer.</p><p></p><p>*Le compendium de formation Slicer5 contient une série de tutoriels et de jeux de données pré-calculés pour apprendre à utiliser le logiciel.</p>

</div>

</div>

---

<div style="text-align: center; padding: 40px; background: linear-gradient(135deg, #004d99 0%, #003366 100%); color: white; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); margin: 30px auto; max-width: 1200px; min-height: 600px; display: flex; flex-direction: column; align-items: center; justify-content: center;">

<div style="max-width: 800px;">

# <span style="font-size: 4.5rem; margin-bottom: 40px; display: block; border-bottom: 2px solid rgba(255, 255, 255, 0.3); padding-bottom: 20px;">Remerciements</span>

<div style="text-align: left;">

<p>National Alliance for Medical Image</p><p>Computing</p><p>NIH U54EB005149</p><p></p><p>Neuroimage Analysis Center</p><p>NIH P41EB015902</p><p></p>

</div>

</div>

</div>

---
