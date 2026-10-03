# Cancer Cell Agent Simulation

## Overview

This project is an agent-based model designed to simulate cancer cell behavior within a 3D tissue microenvironment. The model enables researchers to study tumor growth, cell interactions, immune responses, and the effects of microenvironmental factors on cancer progression, with a specific focus on studying heterogeneous tumor-derived organoid response to CAR T-cell therapy.

The simulation is an off-lattice agent-based model where individual cells are modeled as autonomous agents with their own properties, states, and behaviors that interact within a biochemical microenvironment containing various substrates and factors.

## Published Research

This simulation framework has been published in **Scientific Reports** (Nature Portfolio):

> **In silico study of heterogeneous tumour-derived organoid response to CAR T-cell therapy**  
> *Scientific Reports*, volume 14, Article number: 11999 (2024)  
> Published: May 29, 2024  
> DOI: [https://www.nature.com/articles/s41598-024-63125-5](https://www.nature.com/articles/s41598-024-63125-5)

This publication describes the application of this agent-based model to study how heterogeneous tumor-derived organoids respond to CAR T-cell therapy, providing insights into the complex interactions between immune cells and tumor microenvironments.

The model builds upon previous research published in **PLOS Computational Biology**:

> **Physics-based tissue simulator to model multicellular systems: A study of liver regeneration and hepatocellular carcinoma recurrence**  
> *PLOS Computational Biology*, 19(3): e1010920 (2023)  
> Published: March 6, 2023  
> DOI: [https://doi.org/10.1371/journal.pcbi.1010920](https://doi.org/10.1371/journal.pcbi.1010920)

This earlier work introduced the core concepts of the agent-based model, focusing on tissue regeneration and tumor development in the context of liver regeneration after surgical hepatectomy.

## Key Features

- **Object-oriented design** with modular architecture and clear separation of concerns
- **Cell Life Cycle Modeling** with individual cell tracking, Ki67-based proliferation modeling, and multiple death pathways
- **Physical Interactions** including off-lattice cell movement, mechanical cell interactions, and 3D spatial organization
- **Microenvironment Modeling** with substrate diffusion, oxygen gradients, and multiple biochemical factors
- **Configurable Simulation Process** with separate time steps for diffusion, mechanics, and biology
- **CAR T-cell Therapy Simulation** for modeling immunotherapy interventions in heterogeneous tumor environments

## CAR T-cell Therapy Simulation

This model specifically simulates the interaction between CAR T-cells (Chimeric Antigen Receptor T-cells) and tumor-derived organoids. Key aspects of this simulation include:

- **T-cell Infiltration**: Modeling how CAR T-cells enter and navigate the tumor microenvironment
- **Target Recognition**: Simulating how CAR T-cells identify and bind to tumor cells
- **Cytotoxic Response**: Replicating the mechanisms by which CAR T-cells induce apoptosis in tumor cells
- **T-cell Exhaustion**: Accounting for the limited capacity of T-cells to repeatedly engage and kill tumor cells
- **Tumor Heterogeneity**: Modeling how varied tumor cell populations respond differently to CAR T-cell therapy

This sophisticated modeling approach provides researchers with a powerful tool to explore the complex dynamics of immunotherapy interventions in heterogeneous tumor environments.

## Implementation Details

- **Language**: C++
- **Spatial Framework**: 3D Cartesian grid
- **Numerical Methods**: Finite volume method, vector-based mechanics
- **Default Resolution**: 20μm voxels (cellular scale)
- **Domain Size**: Configurable (default ±500μm in each dimension)
- **Time Units**: Minutes for cellular processes

## Project Structure

The codebase consists of ~52 source files organized into logical categories:

1. **Core Components** (9 files)
   - Cell definition and implementation
   - Microenvironment system
   - Tissue organization
   - Cell container management
   - Main simulation control

2. **Cell Cycle System** (10 files)
   - Cell cycle model framework
   - Standard cycle implementations
   - Phase and transition management
   - Individual cycle tracking

3. **Cell Death and Phenotype** (12 files)
   - Death pathway modeling
   - Cell phenotype integration
   - Motility and secretion
   - Mechanical properties

4. **Spatial Components** (6 files)
   - Grid system implementation
   - Vector mathematics
   - Voxel-based discretization

5. **Mathematical Utilities** (6 files)
   - Random number generation
   - Geometric calculations
   - Volume management

6. **Parameters and Constants** (8 files)
   - Global parameter system
   - Oxygen thresholds
   - Cell-specific parameters
   - Environment configuration

7. **Utility Files** (1 file)
   - Spatial indexing macros

## Building the Project

To build the project:

1. Clone this repository
2. From the project root directory, run:
   ```
   make -f MakefileRo
   ```
3. The executable will be generated in the `build/` directory as `ciclo`

### Build System

- All compiled objects (.o files) are placed in the `build/` directory
- The executable (`ciclo`) is generated in the `build/` directory
- The build directory is automatically created if it doesn't exist
- To clean the build files, run `make -f MakefileRo clean`

## Running a Simulation

To run a simulation:

1. Build the project as described above
2. Run the executable with a parameter file:
   ```
   ./build/ciclo params.ini
   ```
3. The simulation will generate output data based on the parameters specified

### Output Files

The simulation creates output files in a "results" directory (which is created automatically if it doesn't exist):

- `datos_finales.csv` - Summary data for comparison with the model CARTopiaX.
- `DatosFinales.dat` - Summary data (time, tumor volume, radius, cell counts)
- `Datos_[time].xyz` - Detailed cell state data at specific time points
- `PM1_[time].xml` - VTK visualization data for cells (optional)
- `HM1_[time].xml` - VTK visualization data for microenvironment (optional)

### Plotting

`plot_output.py` reads `out/datos_finales.csv` and saves the plots as images in the `plots/` folder (requires `pandas` and `matplotlib`):

```
python plot_output.py
```

Additionally, the project includes an `/outcomes` folder containing example output files and documentation for visualization and analysis. This folder provides researchers with sample data to understand the expected outputs and demonstrates how to visualize and interpret simulation results graphically.

## Documentation

Full documentation is available through Doxygen:

- **Source Code Documentation** - The source code is thoroughly documented with:
  - File headers describing purpose and functionality
  - Class documentation explaining simulation roles
  - Method documentation with parameters and return values
  - Cancer research context throughout

- **Doxygen Documentation** - Comprehensive API documentation:
  - Generated in the `docs/doxygen/html/` directory
  - Open `index.html` to browse the full API documentation
  - To regenerate the documentation, run the following from the project root:
    ```
    ./generate_docs.sh
    ```

## Research Applications

This model is particularly suited for cancer research in several key areas:

1. **Tumor Growth Dynamics**: Understanding how tumors develop and expand in tissue environments
2. **Microenvironmental Influences**: Studying how factors like hypoxia affect cancer cell behavior
3. **Heterogeneity**: Exploring how diverse cell populations within a tumor contribute to progression and treatment resistance
4. **Immune Interactions**: Investigating how immune cells interact with and potentially eliminate cancer cells
5. **Therapeutic Response**: Modeling how cancer cells respond to treatments like CAR T-cell therapy

## How to Cite

If you use this software in your research, please cite:

> *In silico study of heterogeneous tumour-derived organoid response to CAR T-cell therapy*  
> Scientific Reports, volume 14, Article number: 11999 (2024)  
> DOI: [https://www.nature.com/articles/s41598-024-63125-5](https://www.nature.com/articles/s41598-024-63125-5)

## License

Private - For research purposes only.

Copyright © 2024. All rights reserved. This software is provided for research purposes only. Any commercial use is subject to licensing. For licensing inquiries, please contact the authors.

## Contributors

This software was developed as part of research published in Scientific Reports (2024):

- Luciana Melina Luque - Primary Developer
- Additional contributors as listed in the publication: [https://www.nature.com/articles/s41598-024-63125-5](https://www.nature.com/articles/s41598-024-63125-5)
