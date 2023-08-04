# STEPS

## Step 1

For a given system, enter the directory and run the `setup.sh` command to generate a folder structure to perform path-integral molecular dynamics simulations across various temperatures. First, perform a standard i-pi simulation to sample centroid positions (average of all replica positions) and forces (average of all replica forces). Subsequently, perform a "replay" simulation to calculate the physical force acting on the centroid position. 

## Step 2

You can use the script `get_dataset_from_PIMD_simulation_data.py` to convert the i-PI output files into an extended XYZ file in atomic units or the more commonly used eV-Ansgtrom units.

##
_Note that you can use your favourite MLP code to fit a potential on the centroid positions and the differential force._
