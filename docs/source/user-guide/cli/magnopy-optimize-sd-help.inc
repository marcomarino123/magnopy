usage: magnopy-optimize-sd [-h] -sf filename -ss name [-sv [S1 S2 S3 ... ...]]
                           [-et ENERGY_TOLERANCE] [-tt TORQUE_TOLERANCE]
                           [-mf MAGNETIC_FIELD MAGNETIC_FIELD MAGNETIC_FIELD]
                           [-of OUTPUT_FOLDER]

███╗   ███╗  █████╗   ██████╗  ███╗   ██╗  ██████╗  ██████╗  ██╗   ██╗
████╗ ████║ ██╔══██╗ ██╔════╝  ████╗  ██║ ██╔═══██╗ ██╔══██╗ ╚██╗ ██╔╝
██╔████╔██║ ███████║ ██║  ███╗ ██╔██╗ ██║ ██║   ██║ ██████╔╝  ╚████╔╝
██║╚██╔╝██║ ██╔══██║ ██║  ╚██║ ██║╚██╗██║ ██║   ██║ ██╔═══╝    ╚██╔╝
██║ ╚═╝ ██║ ██║  ██║ ╚██████╔╝ ██║ ╚████║ ╚██████╔╝ ██║         ██║
╚═╝     ╚═╝ ╚═╝  ╚═╝  ╚═════╝  ╚═╝  ╚═══╝  ╚═════╝  ╚═╝         ╚═╝
                                                           ▄   ▄
                      Version: 0.1.7                       █▀█▀█
                Documentation: magnopy.org                 █▄█▄█
                Release date: 12 June 2025                  ███   ▄▄
                    License: GNU GPLv3                      ████ █  █
          Copyright (C) 2023-2025  Magnopy Team             ████    █
                                                            ▀▀▀▀▀▀▀▀

This script optimizes classical energy of the spin Hamiltonian and finds the spin
directions that describe a local minima of the energy landscape.

options:
  -h, --help            show this help message and exit
  -sf, --spinham-filename filename
                        Path to the spin Hamiltonian file, from where the
                        parameters would be read.
  -ss, --spinham-source name
                        Source of the spin Hamiltonian. Either "GROGU" or
                        "TB2J"
  -sv, --spin-values [S1 S2 S3 ... ...]
                        In the case when the parameters of spin Hamiltonian
                        comes from TB2J, one might want to change the values
                        of spins to be closer to half-integers. This option
                        allows that. Order of the M numbers should match the
                        order of magnetic atoms in the spin Hamiltonian. Note
                        that those numbers are always positive. To specify AFM
                        order use opposite spin directions and not spin values
                        of the opposite sign.
  -et, --energy-tolerance ENERGY_TOLERANCE
                        Tolerance parameter. Difference between classical
                        energies of two consecutive optimization steps.
  -tt, --torque-tolerance TORQUE_TOLERANCE
                        Maximum torque among all spins.
  -mf, --magnetic-field MAGNETIC_FIELD MAGNETIC_FIELD MAGNETIC_FIELD
                        Vector of external magnetic field, given in the units
                        of Tesla.
  -of, --output-folder OUTPUT_FOLDER
                        Folder where all output files of magnopy wil be saved.
