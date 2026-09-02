
<div style="text-align: center; padding: 60px; background: linear-gradient(135deg, #003366 0%, #004d99 100%); color: white; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); margin: 30px auto; max-width: 1200px; min-height: 600px; display: flex; flex-direction: column; align-items: center; justify-content: center;">

<div style="max-width: 800px;">

# <span style="font-size: 5.5rem; font-weight: 700; margin-bottom: 30px; line-height: 1.2; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); display: block;">Noções básicas de carregamento de dados e visualização 3D no 3D Slicer</span>

<p style="font-size: 2.5rem; font-weight: 300; margin-bottom: 15px; opacity: 0.95;">Autor: Sonia Pujol, Ph.D.</p>

<p style="font-size: 2rem; font-weight: 300; margin-bottom: 40px; opacity: 0.85;">24/11/2024</p>

<p style="font-size: 2.1rem; line-height: 1.8; font-weight: 300; opacity: 0.9; max-width: 700px; margin: 0 auto;">Professora Assistente de Radiologia Brigham e Escola Médica de Harvard do Hospital das Mulheres</p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Objetivo geral</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>Este tutorial é uma introdução aos conceitos básicos de carregamento e visualização de imagens DICOM e modelos 3D no 3D Slicer.</p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Objetivos de aprendizagem</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p> • Ao seguir este tutorial, poderá</p><p></p><p>• carregar e visualizar imagens DICOM no Slicer</p><p></p><p>• efetuar renderização de volume de dados CT</p><p></p><p>• carregar e visualizar modelos 3D reconstruidos a partir de dados MRI</p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Materiais do tutorial</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>-3D Slicer versão 5.10</p><p></p><p>-3D VisualizationDataSet.zip</p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Conjunto de dados do tutorial</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>O ficheiro 3DVisualiztionDataset.zip contém dois diretórios:</p><p></p><p>- dataset1_Thorax_Abdomen </p><p>- dataset2_Head</p><p></p><p>Descompacte o ficheiro 3DVisualizationDataset.zip no seu computador para aceder aos conjuntos de dados</p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Isenção de responsabilidade</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>• 3D Slicer é uma aplicação de software open source grátis distribuída sob uma licença estilo BSD. </p><p></p><p></p><p>• O software não é aprovado pela FDA ou CE-Marked, e é apenas para fins investigativos.</p><p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Resumo do tutorial</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>•  Part 1: Carregar e Visualizar dados DICOM</p><p></p><p>•  Part 2: Renderização de Volume</p><p></p><p></p><p>• Part 3: Carregar e Visualizar modelos 3D</p>

</div>

</div>

---

<div style="text-align: center; padding: 60px; background: linear-gradient(135deg, #003366 0%, #004d99 100%); color: white; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); margin: 30px auto; max-width: 1200px; min-height: 600px; display: flex; align-items: center; justify-content: center;">

# <span style="font-size: 5.5rem; font-weight: 700; line-height: 1.2; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); display: block;">Parte 1: Carregar Dados DICOM</span>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">A carregar um volume DICOM</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![A carregar um volume DICOM](8_LoadingaDICOMvolume.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">A carregar um volume DICOM</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![A carregar um volume DICOM](9_LoadingaDICOMvolume.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">A visualizar imagens DICOM</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![A visualizar imagens DICOM](10_VisualizingDICOMimages.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">A visualizar imagens DICOM</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![A visualizar imagens DICOM](11_VisualizingDICOMimages.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">A visualizar imagens DICOM</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![A visualizar imagens DICOM](12_VisualizingDICOMimages.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">A visualizar imagens DICOM</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![A visualizar imagens DICOM](13_VisualizingDICOMimages.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">A visualizar imagens DICOM</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![A visualizar imagens DICOM](14_VisualizingDICOMimages.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">A visualizar imagens DICOM</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![A visualizar imagens DICOM](15_VisualizingDICOMimages.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">A visualizar imagens DICOM</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![A visualizar imagens DICOM](16_VisualizingDICOMimages.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">A visualizar imagens DICOM</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![A visualizar imagens DICOM](17_VisualizingDICOMimages.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">A visualizar imagens DICOM</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![A visualizar imagens DICOM](18_VisualizingDICOMimages.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Controlador de visualização 3D</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Controlador de visualização 3D](19_3DViewerController.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Controlador de visualização 3D</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Controlador de visualização 3D](20_3DViewerController.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="text-align: center; padding: 60px; background: linear-gradient(135deg, #003366 0%, #004d99 100%); color: white; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); margin: 30px auto; max-width: 1200px; min-height: 600px; display: flex; align-items: center; justify-content: center;">

# <span style="font-size: 5.5rem; font-weight: 700; line-height: 1.2; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); display: block;">Parte 2: Renderização de Volume</span>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Renderização de volume</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>• Renderização de volume </p><p>técnicas permitem visualização </p><p>3D de conjuntos de dados</p><p>3D</p><p></p><p>• O módulo de Volume de Renderização</p><p>no Slicer permite</p><p>visualização 3D interativa</p><p>de imagens DICOM</p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Renderização de volume</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Renderização de volume](23_VolumeRendering.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Renderização de volume</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Renderização de volume](24_VolumeRendering.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Renderização de volume</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Renderização de volume](25_VolumeRendering.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Renderização de volume</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Renderização de volume](26_VolumeRendering.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Renderização de volume</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Renderização de volume](27_VolumeRendering.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Renderização de volume</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Renderização de volume](28_VolumeRendering.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Renderização de volume</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Renderização de volume](29_VolumeRendering.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Renderização de volume</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Renderização de volume](30_VolumeRendering.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Renderização de volume</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Renderização de volume](31_VolumeRendering.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="text-align: center; padding: 60px; background: linear-gradient(135deg, #003366 0%, #004d99 100%); color: white; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); margin: 30px auto; max-width: 1200px; min-height: 600px; display: flex; align-items: center; justify-content: center;">

# <span style="font-size: 5.5rem; font-weight: 700; line-height: 1.2; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); display: block;">Parte 3: Carregar e 
visualizar modelos 3D
</span>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Conjunto de dados do tutorial</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>• O diretório dataset2_Head contém a cena do Slicer chamada Head_scene.mrb</p><p></p><p>• A cena contém modelos 3D do atlas do cérebro SPL desenvolvido pelo departamento de Radiologia no Brigham and Women’s Hospital, Harvard Medical School (NIH P41 RR013218, NIH R01 MH05074)</p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Cena do Slicer</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>Slicer guarda toda a informação carregada num repositório chamado cena</p><p></p><p></p><p>Em cada conjunto de dados, como um volume de imagem, modelo de superfície, ou conjunto de pontos, é representado como um nó numa cena do Slicer.</p><p></p><p></p><p>Todos os módulos do Slicer operam sobre os dados armazenados numa cena Slicer.</p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">A carregar uma cena</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![A carregar uma cena](35_LoadingaScene.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">A visualizar modelos 3D</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![A visualizar modelos 3D](36_Viewing3Dmodels.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">A visualizar modelos 3D</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![A visualizar modelos 3D](37_Viewing3Dmodels.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">A visualizar modelos 3D</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![A visualizar modelos 3D](38_Viewing3Dmodels.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">A visualizar modelos 3D</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![A visualizar modelos 3D](39_Viewing3Dmodels.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">A visualizar modelos 3D</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![A visualizar modelos 3D](40_Viewing3Dmodels.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Interagir com modelos 3D</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Interagir com modelos 3D](41_Interactingwith3Dmodels.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Interagir com modelos 3D</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Interagir com modelos 3D](42_Interactingwith3Dmodels.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Interagir com modelos 3D</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Interagir com modelos 3D](43_Interactingwith3Dmodels.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Interagir com modelos 3D</span>

<div style="text-align: center; margin: 30px 0; background: #fafafa; padding: 20px; border-radius: 4px;">

![Interagir com modelos 3D](44_Interactingwith3Dmodels.png)

</div>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify; margin-top: 25px;">

<p></p>

</div>

</div>

---

<div style="background: white; max-width: 1200px; margin: 30px auto; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); padding: 40px;">

## <span style="color: #003366; font-size: 3.5rem; font-weight: 600; display: block; margin-bottom: 30px; padding-bottom: 15px; border-bottom: 3px solid #003366;">Conclusão</span>

<div style="font-size: 2rem; line-height: 1.8; color: #444; text-align: justify;">

<p>• 3D Slicer fornece funcionalidades avançadas para carregar e visualizar dados de imagiologia médica 3D</p><p></p><p>• O tutorial demonstra como utilizar a renderização de volume e modelação de superfície 3D para visualização interativa de dados de TC e RM</p><p></p><p></p><p>Contact: spujol@bwh.harvard.edu</p>

</div>

</div>

---

<div style="text-align: center; padding: 40px; background: linear-gradient(135deg, #004d99 0%, #003366 100%); color: white; border-radius: 8px; box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); margin: 30px auto; max-width: 1200px; min-height: 600px; display: flex; flex-direction: column; align-items: center; justify-content: center;">

<div style="max-width: 800px;">

# <span style="font-size: 4.5rem; margin-bottom: 40px; display: block; border-bottom: 2px solid rgba(255, 255, 255, 0.3); padding-bottom: 20px;">Agradecimentos</span>

<div style="text-align: left;">

<p>Centro de Análise de Neuroimagens (NIBIB P41 EB015902)</p>

</div>

</div>

</div>

---
