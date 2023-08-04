import os
import sys
import numpy as np

from ase.calculators.socketio import SocketClient
from ase.calculators.calculator import Calculator, all_changes
from ase.io import read


class Morse2DCalculator(Calculator):
    """Wrapper class to implement a 2D Morse potential

    Parameters
    ----------
    D0 : float
        the dissociation constant of the potential
    alpha : float
        the anharmonicity
    req : float
        the equilibrium distance
    """

    implemented_properties = ["energy", "forces", "stress" ]
    "Properties calculator can handle (energy, forces, ...)"

    default_parameters = {}
    "Default parameters"

    nolabel = True

    def __init__(self, D0, req, alpha, **kwargs):
        super(Morse2DCalculator, self).__init__(**kwargs)
        self.D0 = D0
        self.alpha = alpha
        self.D0 = D0
        self.alpha = alpha
        self.req = req
        self.kwargs = kwargs

    def calculate(self, atoms=None, properties=["energy", "forces", "stress"], system_changes=all_changes):
        Calculator.calculate(self, atoms, properties, system_changes)

        x, y, z  = atoms.positions[0]
        x = x 
        y = y 

        r = np.sqrt(x**2 + y**2)
        exp_term = np.exp(-1.0 * self.alpha * (r - self.req))

        # print (x, y, r, exp_term)

        e = self.D0 * (1.0 - exp_term)**2
        gx = 2.0 * self.D0 * self.alpha * x * (exp_term - exp_term**2) / r 
        gy = 2.0 * self.D0 * self.alpha * y * (exp_term - exp_term**2) / r

        #print (e, np.asarray([[-gx, -gy, 0]]))

        self.results["energy"] = e 
        self.results["free_energy"] = e
        self.results["forces"] = np.asarray([[-gx, -gy, 0]])



# Define atoms object

atoms = read("init.xyz", 0)

# Set ASE calculator #################
calc = Morse2DCalculator(D0=0.18748 * 27.211386 , req=1.8324 * 0.52917721, alpha=1.1605 / 0.52917721 )

atoms.set_calculator(calc)

# Create Client
# inet
host = "2DMorse_PIMD_efficient_sampling_xxxTxxxK"
client = SocketClient(unixsocket=host)

client.run(atoms)
