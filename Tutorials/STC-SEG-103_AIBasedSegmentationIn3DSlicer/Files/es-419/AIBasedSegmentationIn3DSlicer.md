
<div style="text-align: center; padding: 60px; background: linear-gradient(135deg, #003366 0%, #004d99 100%); color: white; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); margin: 30px auto; max-width: 1200px; min-height: 600px; display: flex; flex-direction: column; align-items: center; justify-content: center;">

<div style="max-width: 800px;">

# <span style="font-size: 5.5rem; font-weight: 700; margin-bottom: 30px; line-height: 1.2; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); display: block;">Segmentación basada en IA en 3D Slicer</span>

<p style="font-size: 2.5rem; font-weight: 300; margin-bottom: 15px; opacity: 0.95;">Dra. Sonia Pujol
Brigham and Women's Hospital,
Harvard Medical School
Boston, MA</p>

<p style="font-size: 2rem; font-weight: 300; margin-bottom: 40px; opacity: 0.85;"> </p>

<p style="font-size: 2.1rem; line-height: 1.8; font-weight: 300; opacity: 0.9; max-width: 700px; margin: 0 auto;">Slicer Workshop Ribeirão Preto 
Junio 30, 2025</p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Segmentación manual vs. segmentación asistida por IA</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>Las imágenes médicas han sido segmentadas tradicionalmente de forma manual, lo cual es un proceso que consume mucho tiempo, requiere un esfuerzo intensivo por parte de los radiólogos y está sujeto a variabilidad entre radiólogos.</p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Segmentación manual vs. segmentación asistida por IA</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>En la última década, la segmentación de imágenes ha sido impulsada por el desarrollo de algoritmos de aprendizaje profundo (p. ej., nnUnet del Centro Alemán de Investigación del Cáncer (DKFZ)/Helmholtz Research).</p><p></p><p></p><p> Las herramientas de segmentación basadas en IA pueden reducir el tiempo de segmentación y proporcionar resultados más reproducibles.</p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Terminología de IA</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>Un modelo de IA es un algoritmo de IA que fue entrenado para realizar una tarea específica (p. ej., un modelo de segmentación de tumores cerebrales). </p><p></p><p>Los pesos de un modelo de IA son números pequeños que determinan cuánta importancia le da el modelo a diferentes características de la imagen. </p><p></p><p>Durante la fase de entrenamiento, un modelo aprende patrones a partir de datos etiquetados por expertos y ajusta sus pesos para mejorar sus predicciones. </p><p></p><p>Durante la fase de validación/prueba, el modelo se evalúa en un conjunto de datos separado que no fue utilizado durante la fase de entrenamiento. </p><p></p><p>Durante la inferencia, el modelo se aplica a nuevos conjuntos de datos para realizar la tarea específica para la que fue entrenado.</p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Workshop de IA en 3D Slicer</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>Este tutorial se centra en la ejecución de tareas de inferencia utilizando diversos modelos de IA preentrenados para la segmentación automatizada de estructuras anatómicas y patológicas.</p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Slicer extension MONAIAuto3DSeg</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>Este tutorial utiliza los modelos preentrenados de la extensión MONAIAuto3DSeg de Slicer.</p><p></p><p></p><p>La herramienta está diseñada para funcionar en laptops o en computadoras de escritorio promedio sin GPU.</p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Slicer extension MONAIAuto3DSeg</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>Compatible con múltiples modalidades (TC, RM).</p><p></p><p></p><p>Múltiples anatomías (cabeza, tórax, abdomen, pelvis, etc.). </p><p></p><p></p><p>Múltiples patologías (tumor, hemorragia, edema).</p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Tutorial de IA en Slicer: Tareas de segmentación</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>Tarea de segmentación 1: Próstata</p><p></p><p></p><p>Tarea de segmentación 2: Glioma cerebral</p><p></p><p></p><p>Tarea de segmentación 3: Segmentación de cuerpo completo</p>

</div>

</div>

---

<div style="text-align: center; padding: 60px; background: linear-gradient(135deg, #003366 0%, #004d99 100%); color: white; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); margin: 30px auto; max-width: 1200px; min-height: 600px; display: flex; align-items: center; justify-content: center;">

# <span style="font-size: 5.5rem; font-weight: 700; line-height: 1.2; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); display: block;">Tarea de segmentación de IA n.° 1: Próstata</span>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;"> </span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>Segmentación basada en IA de la zona periférica (ZP) y la zona de transición (ZT) de la próstata en imágenes de RM ponderadas en T2. </p><p></p><p></p><p>Conjunto de datos: </p><p>msd_prostate_01-t2</p><p>msd_prostate_01-adc</p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;"></span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![](10_slide.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;"></span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![](11_slide.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;"></span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![](12_slide.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;"></span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![](13_slide.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;"></span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![](14_slide.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;"></span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![](15_slide.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;"></span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![](16_slide.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="text-align: center; padding: 60px; background: linear-gradient(135deg, #003366 0%, #004d99 100%); color: white; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); margin: 30px auto; max-width: 1200px; min-height: 600px; display: flex; align-items: center; justify-content: center;">

# <span style="font-size: 5.5rem; font-weight: 700; line-height: 1.2; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); display: block;">Tarea de segmentación de IA n.° 2: Glioma cerebral</span>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;"> </span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>Segmentación basada en IA de Neoplasia, Necrosis y Edema en imágenes de RM del cerebro.</p><p></p><p></p><p>Conjuntos de datos: </p><p>1) BraTS-GLI_00005-000-t1n (ponderada en T1) </p><p>2) BraTS-GLI_00005-000-t1c (ponderada en T1 post-Gd) </p><p>3) BraTS-GLI_00005-000-t2w (ponderada en T2) </p><p>4) BraTS-GLI_00005-000-t2f (T2-FLAIR)</p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;"></span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![](19_slide.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;"></span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![](20_slide.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;"></span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![](21_slide.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;"></span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![](22_slide.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;"></span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![](23_slide.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="text-align: center; padding: 60px; background: linear-gradient(135deg, #003366 0%, #004d99 100%); color: white; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); margin: 30px auto; max-width: 1200px; min-height: 600px; display: flex; align-items: center; justify-content: center;">

# <span style="font-size: 5.5rem; font-weight: 700; line-height: 1.2; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); display: block;">Tarea de segmentación de IA n.° 3: Segmentación de cuerpo completo</span>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;"> </span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>Segmentación de cuerpo completo basada en IA. </p><p></p><p></p><p>Conjunto de datos: </p><p>CT_ThoraxAbdomen</p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;"></span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![](26_slide.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;"></span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![](27_slide.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;"></span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![](28_slide.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;"></span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![](29_slide.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Conclusión</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>La extensión MONAIAuto3DSeg de 3D Slicer proporciona segmentación rápida basada en IA de estructuras anatómicas y patológicas. </p><p></p><p></p><p>El módulo puede ejecutarse en laptops y computadoras de escritorio estándar sin GPU.</p>

</div>

</div>

---

<div style="text-align: center; padding: 40px; background: linear-gradient(135deg, #004d99 0%, #003366 100%); color: white; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); margin: 30px auto; max-width: 1200px; min-height: 600px; display: flex; flex-direction: column; align-items: center; justify-content: center;">

<div style="max-width: 800px;">

# <span style="font-size: 4.5rem; margin-bottom: 40px; display: block; border-bottom: 2px solid rgba(255, 255, 255, 0.3); padding-bottom: 20px;">Agradecimientos</span>

<div style="text-align: left;">

<p>El proyecto de internacionalización de 3D Slicer y el proyecto 3D Slicer para América Latina han sido posibles gracias al financiamiento de la iniciativa Chan Zuckerberg.</p>

</div>

</div>

</div>

---
