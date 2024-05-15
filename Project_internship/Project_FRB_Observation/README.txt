FRB_Observation Project

Overview:

The FRB_Observation project is designed to automate the processing of Fast Radio Burst (FRB) observations. 
The project consists of ONE main directorie call "Conf"
There is another directory called Process_Example and a PathFileExample file to show examples.

Directory Structure:

1. Conf:
   - Contains scripts necessary for processing FRB observations, including the main script (process.sh) 
and data processing scripts (DDplan_NenuFAR_ModiftcpFRB2.py, single_pulse_search_NenuFAR.py and FRB-search_PULSARmode_vFRBObservation.csh).

2. Process_Exemple_20230614:
   - Provides an example directory showcasing the expected output of the processing script (process.sh).

3. PathFileExemple 
   - Is an example of the desired format for the saving path of the observations that we want to process.

Main Processing Script: process.sh in the directory Conf

Usage:

1. Configuration:
   - Update parameters in the script as needed (Save parameter and Proccessing parameter).
   - Ensure the environment setup and sourced configuration files are appropriate for your system.

2. Observation Paths:
   - Provide a file containing paths to FRB observations in the specified format (PathFileExemple is an exemple) .
   - Customize the case statement to set Dispersion Measures (DM) based on your observation names.

3. Execution:
   - Run the script in the terminal using: bash process.sh

4. Output:
   - Processed data will be organized in the specified directories.

Script Details:

- Parameters:
  - Adjust SigmaF, SigmaT, BerrF, BerrT, and BlockSize according to your processing requirements.

- Observation Processing:
  - Processes each observation individually, creating directories and running the processing script specific to each observation.

- Logging:
  - Details of the processing, including parameters used, are logged in a designated log file.

Cleanup:

- Removes unnecessary files generated during the processing.

