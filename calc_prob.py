#!/usr/bin/env python3
# --------------------------------------
# Ryan Chern
# 7/03/19

# Beliveau Lab
# calc_prob.py
# --------------------------------------

import random
import tempfile
import subprocess
from subprocess import PIPE, Popen


def prob(seq, structure, temp, formamide, sodiumConc, material):
    """ Runs the NUPACK 'prob' command """

    if 'N' in seq:
        return None

    correctedTemp = float(temp) + 0.65 * float(formamide)

    seq = str(seq)
    structure = str(structure)
    correctedTemp = str(correctedTemp)
    sodiumConc = str(sodiumConc)
    material = str(material)

    # Generate a random number for parallelization
    randomInt = random.randrange(1000000000)

    # Uses a context manager to create/destroy the temp file(s)
    with tempfile.TemporaryDirectory() as tmpdir:
        # Write to .in file
        in_File = open('%s/strand_%d_temp.in' % (tmpdir, randomInt), 'w')
        in_File.write('%s\n%s' % (seq, structure))
        in_File.close()

        # Run 'prob', extract prob value
        with Popen(['prob', '-T', correctedTemp, '-sodium', sodiumConc, '-material', material, '%s/strand_%d_temp' % (tmpdir, randomInt)], stdout=PIPE) as proc:
            prob_val = float(proc.stdout.readlines()[14])

        if prob_val is not None:
            return prob_val
