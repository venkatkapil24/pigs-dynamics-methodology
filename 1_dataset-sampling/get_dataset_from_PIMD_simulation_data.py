import sys as sys
import numpy as np
import ase as ase
from ase.io import write
from ipi.utils.io import read_file_raw
import traceback

def get_dataset_from_PIMD_simulation_data(units='au', DROOT='./', maxdata=-1):
    """
    Reads a PIMD simulation directory (in an expected format)
    and returns parsed data (with centroid and born-oppenheimer
    forces) in different formats.
    """

    sys.stderr.write('\nThis code will read the simulation.xc.xyz, simulation.fc.xyz, and replay.for_0.xyz files. \nIt will assume they are all in atomic units and that the replay file has ne additional entry (the 0th structure which is repeated). \n\n')

    if units == 'au':
        sys.stderr.write('The extended xyz file will be in a.u. (i.e. the same units as the i-PI input) \n')
        qunits = 1
        eunits = 1
    elif units == 'ev-ang':
        sys.stderr.write('The extended xyz file will be in ev / angstrom units (i.e. the units used popularly in ASE extxyz files) \n')
        qunits = 0.52917721
        eunits = 27.211386
    else:
        sys.stderr.write("invalid units provided. Use au or ev-ang \n")
        return

    funits = eunits / qunits
    maxdata = int(maxdata)

    # identifies files to read centroid positions and forces
    try:
        file_centroid_pos = open(DROOT + 'simulation.xc.xyz')
        file_centroid_for = open(DROOT + 'simulation.fc.xyz')
        file_centroid_for_cl = open(DROOT + 'replay.for_0.xyz')
    except:
        sys.stderr.write("Could not open one of simulation.xc.xyz, simulation.fc.xyz, or replay.for_0 \n")
        traceback.print_exc()

    # skips the 0th step for the replay run
    read_file_raw('xyz', file_centroid_for_cl)

    atoms_list = []

    while True:

        try:
            atoms = read_file_raw('xyz', file_centroid_pos)
            q = atoms['data'] * qunits

            h = atoms['cell'] * qunits

            atoms = read_file_raw('xyz', file_centroid_for)
            f = atoms['data'] * funits

            atoms = read_file_raw('xyz', file_centroid_for_cl)
            fcl = atoms['data'] * funits

            s = atoms['names']
            nat = len(s)
            atoms = ase.Atoms(s, positions=q.reshape((nat,3)), cell=h, pbc=True)
            atoms.arrays['force'] = f.reshape((nat,3))
            atoms.arrays['force_on_centroid_position'] = fcl.reshape((nat,3))
            atoms.arrays['delta_force'] = f.reshape((nat,3)) - fcl.reshape((nat,3))

            atoms_list.append(atoms)

        except EOFError:
            atoms_list = atoms_list[0:maxdata]
            sys.stderr.write(str(len(atoms_list)) +  " datapoint(s) \n")
            write('-', atoms_list[0:maxdata], format='extxyz')
            break
   
args = sys.argv[1:]
try:
  get_dataset_from_PIMD_simulation_data(args[0], args[1], args[2]) 
except IndexError:
  sys.stderr.write('USAGE: from_PIMD_simulation_data.py UNITS[au / ev-ang] ABSOLUTE_PATH_OF_DIRECTORY MAXIMUM_DATA\n')
  sys.stderr.write('e.g.   from_PIMD_simulation_data.py ev-ang ./ -1\n')
