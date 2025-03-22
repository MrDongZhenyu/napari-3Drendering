# napari-3Drendering

This repository contains the codes and examples for generating 3D renderings using Napari, a fast, interactive, multi-dimensional image viewer for Python. While Napari is a powerful tool, there is a lack of comprehensive tutorials that provide a systematic approach for visualizing 3D data and creating videos, particularly for scientific papers. This repository aims to fill that gap.

Note: This repository is also used to generate 3D visualizations in the Analytic Fourier Ptychotomography (AFP) paper. [Paper link]() 


Top-level folder structure:

```bash
├── Data                               # Data used for 3D visualiztion
├── utils.py                           # Subfunctions
├── Volumerendering_Embryo.ipynb       # A demo jupyter notebook code
└── README.md                          # Documentation (this file)
```

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Data source](#datasource)
- [Example results](#demo)
- [Contact](#contact)

## Introduction
* This code is designed for 3D rendering in Napari and provides several key functionalities:

    1. Add multiple 3D objects with Maximum Intensity Projection (MIP) rendering or other rendering.

    2. Customize colormaps for different channels.

    3. Add 3D bounding boxes to the volume.

    4. Edit axes and the scale bar.

    5. Adjust viewing angles and zoom levels.

    6. Overlay cross-sectional boxes onto the 3D visualization.

    7. Save screenshots of static views.

    8. Generate 3D rendering videos for dynamic presentations.

* A demo code is provided in jupyter notebook: `Volumerendering_Embryo.ipynb`

## Installation
* Follow the [installation instructions](https://napari.org/stable/tutorials/fundamentals/installation.html) and then install a few additional required libraries and napari plugins (napari-bbox, napari-animation). For example:
    ```Python
    conda create -y -n napari-env -c conda-forge python=3.10
    conda activate napari-env

    pip install "napari[all]"
    pip install h5py os numpy jupyter matplotlib

    pip install napari-bbox
    pip install napari-animation
    ```

* Note: After installing the `napari_bbox` plugin, open the file `qt_bounding_box_control.py` in the installation folder, and comment out the lines that import or use the `QSlider` module.

## Data source
Please download the data and put them in the 'Data' folder. The data link will be opened later on. The data are stored as `.h5` file.

## Example results
1. Fixed mouse embryo (Eight cell stage)


https://github.com/user-attachments/assets/e80e1526-4313-4c7f-a2b8-c3605ca3d14a


2. Fixed mouse embryo (Blasto stage)

3. 3D Pathology slide

## Contact
For any questions or comments about this code, please contact [zdong@caltech.edu](mailto:zdong@caltech.edu).


