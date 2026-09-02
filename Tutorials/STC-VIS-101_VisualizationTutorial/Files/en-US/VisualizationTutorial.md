
<div style="text-align: center; padding: 60px; background: linear-gradient(135deg, #003366 0%, #004d99 100%); color: white; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); margin: 30px auto; max-width: 1200px; min-height: 600px; display: flex; flex-direction: column; align-items: center; justify-content: center;">

<div style="max-width: 800px;">

# <span style="font-size: 5.5rem; font-weight: 700; margin-bottom: 30px; line-height: 1.2; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); display: block;">Basics of Data Loading and 3D Visualization in 3D Slicer</span>

<p style="font-size: 2.5rem; font-weight: 300; margin-bottom: 15px; opacity: 0.95;">Author: Sonia Pujol, Ph.D.</p>

<p style="font-size: 2rem; font-weight: 300; margin-bottom: 40px; opacity: 0.85;">24/11/2024</p>

<p style="font-size: 2.1rem; line-height: 1.8; font-weight: 300; opacity: 0.9; max-width: 700px; margin: 0 auto;">Assistant Professor of Radiology Brigham and Women’s Hospital Harvard Medical School</p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Overall Goal</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>This tutorial is an introduction to the basics of loading and viewing DICOM images and 3D models in 3D Slicer.</p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Learning Objectives</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p> • Following this tutorial, you will be able</p><p></p><p>• to load and visualize DICOM images in Slicer</p><p></p><p>• to perform volume rendering of CT data</p><p></p><p>• to load and visualize 3D models reconstructed from MRI data</p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Tutorial materials</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>• 3D Slicer version 5.10</p><p></p><p>•  3D VisualizationDataSet.zip</p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Tutorial dataset</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>The file 3DVisualizationDataset.zip contains two directories:</p><p></p><p>- dataset1_Thorax_Abdomen </p><p>- dataset2_Head</p><p></p><p>Unzip the file 3DVisualizationDataset.zip on your computer to access the datasets</p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Disclaimer</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>• 3D Slicer is a free open source software application distributed under a BSD style license. </p><p></p><p></p><p>• The software is not FDA approved or CE-Marked, and is for research use only.</p><p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Tutorial Outline</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>•  Part 1: Loading and Viewing DICOM data</p><p></p><p>•  Part 2: Volume Rendering</p><p></p><p></p><p>• Part 3: Loading and Viewing 3D models</p>

</div>

</div>

---

<div style="text-align: center; padding: 60px; background: linear-gradient(135deg, #003366 0%, #004d99 100%); color: white; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); margin: 30px auto; max-width: 1200px; min-height: 600px; display: flex; align-items: center; justify-content: center;">

# <span style="font-size: 5.5rem; font-weight: 700; line-height: 1.2; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); display: block;">Part 1: DICOM Data Loading</span>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Loading a DICOM volume</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Loading a DICOM volume](8_LoadingaDICOMvolume.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Loading a DICOM volume</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Loading a DICOM volume](9_LoadingaDICOMvolume.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Visualizing DICOM images</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Visualizing DICOM images](10_VisualizingDICOMimages.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Visualizing DICOM images</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Visualizing DICOM images](11_VisualizingDICOMimages.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Visualizing DICOM images</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Visualizing DICOM images](12_VisualizingDICOMimages.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Visualizing DICOM images</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Visualizing DICOM images](13_VisualizingDICOMimages.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Visualizing DICOM images</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Visualizing DICOM images](14_VisualizingDICOMimages.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Visualizing DICOM images</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Visualizing DICOM images](15_VisualizingDICOMimages.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Visualizing DICOM images</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Visualizing DICOM images](16_VisualizingDICOMimages.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Visualizing DICOM images</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Visualizing DICOM images](17_VisualizingDICOMimages.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Visualizing DICOM images</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Visualizing DICOM images](18_VisualizingDICOMimages.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">3D Viewer Controller</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![3D Viewer Controller](19_3DViewerController.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">3D Viewer Controller</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![3D Viewer Controller](20_3DViewerController.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="text-align: center; padding: 60px; background: linear-gradient(135deg, #003366 0%, #004d99 100%); color: white; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); margin: 30px auto; max-width: 1200px; min-height: 600px; display: flex; align-items: center; justify-content: center;">

# <span style="font-size: 5.5rem; font-weight: 700; line-height: 1.2; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); display: block;">Part 2: Volume Rendering</span>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Volume Rendering</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>• Volume rendering </p><p>techniques enable 3D </p><p>visualization of 3D </p><p>datasets</p><p></p><p>• The Volume Rendering </p><p>module in Slicer enables </p><p>interactive 3D visualization </p><p>of DICOM images</p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Volume Rendering</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Volume Rendering](23_VolumeRendering.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Volume Rendering</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Volume Rendering](24_VolumeRendering.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Volume Rendering</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Volume Rendering](25_VolumeRendering.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Volume Rendering</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Volume Rendering](26_VolumeRendering.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Volume Rendering</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Volume Rendering](27_VolumeRendering.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Volume Rendering</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Volume Rendering](28_VolumeRendering.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Volume Rendering</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Volume Rendering](29_VolumeRendering.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Volume Rendering</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Volume Rendering](30_VolumeRendering.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Volume Rendering</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Volume Rendering](31_VolumeRendering.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="text-align: center; padding: 60px; background: linear-gradient(135deg, #003366 0%, #004d99 100%); color: white; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); margin: 30px auto; max-width: 1200px; min-height: 600px; display: flex; align-items: center; justify-content: center;">

# <span style="font-size: 5.5rem; font-weight: 700; line-height: 1.2; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); display: block;">Part 3: Loading and 
viewing 3D models
</span>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Tutorial dataset</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>• The directory dataset2_Head contains the Slicer scene called Head_scene.mrb</p><p></p><p>• The scene contains 3D models from the SPL brain atlas developed by the department of Radiology at Brigham and Women’s Hospital, Harvard Medical School (NIH P41 RR013218, NIH R01 MH05074)</p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Slicer Scene</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>Slicer stores all loaded data in a repository called a scene</p><p></p><p></p><p>Each data set, such as an image volume, surface model, or point set, is represented as a node in a Slicer scene.</p><p></p><p></p><p>All Slicer modules operate on the data stored in a Slicer scene.</p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Loading a Scene</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Loading a Scene](35_LoadingaScene.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Viewing 3D models</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Viewing 3D models](36_Viewing3Dmodels.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Viewing 3D models</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Viewing 3D models](37_Viewing3Dmodels.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Viewing 3D models</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Viewing 3D models](38_Viewing3Dmodels.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Viewing 3D models</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Viewing 3D models](39_Viewing3Dmodels.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Viewing 3D models</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Viewing 3D models](40_Viewing3Dmodels.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Interacting with 3D models</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Interacting with 3D models](41_Interactingwith3Dmodels.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Interacting with 3D models</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Interacting with 3D models](42_Interactingwith3Dmodels.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Interacting with 3D models</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Interacting with 3D models](43_Interactingwith3Dmodels.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Interacting with 3D models</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Interacting with 3D models](44_Interactingwith3Dmodels.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Conclusion</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>• 3D Slicer provides advanced functionalities for loading and viewing 3D medical imaging data</p><p></p><p>• The tutorial demonstrates how to use volume rendering and 3D surface modeling for interactive visualization of CT and MRI data</p><p></p><p></p><p>Contact: spujol@bwh.harvard.edu</p>

</div>

</div>

---

<div style="text-align: center; padding: 40px; background: linear-gradient(135deg, #004d99 0%, #003366 100%); color: white; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); margin: 30px auto; max-width: 1200px; min-height: 600px; display: flex; flex-direction: column; align-items: center; justify-content: center;">

<div style="max-width: 800px;">

# <span style="font-size: 4.5rem; margin-bottom: 40px; display: block; border-bottom: 2px solid rgba(255, 255, 255, 0.3); padding-bottom: 20px;">Acknowledgements</span>

<div style="text-align: left;">

<p>Neuroimage Analysis Center (NIBIB P41 EB015902)</p>

</div>

</div>

</div>

---
