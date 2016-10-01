import unittest

from PyWANN.WiSARD import WiSARD
import numpy as np
from samples import *
from samplesunlabel import *
import file_labels as labels

class TestWiSARD(unittest.TestCase):

    def test_T_versus_A_without_bleaching(self):

        num_bits_addr = 84
        bleaching = False
        
        w = WiSARD(num_bits_addr, bleaching)

        X = A_samples[0:-2] + T_samples[0:-2]
        y = labels

        # training discriminators
        w.fit(X, y)

        A_test = w.predict(A_samples)
        T_test = w.predict(T_samples)

        tot_A = np.sum([1 for x in A_test if x == 'A'])
        tot_T = np.sum([1 for x in T_test if x == 'T'])

        self.assertEqual(tot_A, len(A_samples))
        self.assertEqual(tot_T, len(T_samples))

if __name__ == "__main__":
    unittest.main()