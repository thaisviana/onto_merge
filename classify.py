import retina
from PyWANN.WiSARD import WiSARD
from statistics import mean, pvariance, pstdev
import numpy as np
#from matrix_of_words import matrix


def wisard_with_bleaching():
        w = WiSARD(num_bits_addr=2, bleaching=True, defaul_b_bleaching=2)
        result(w)


def wisard_without_bleaching():
        w = WiSARD(num_bits_addr=2, bleaching=False)
        result(w)


def result(w):
    X = retina[:4] + retina[249:273] + retina[273:]
    y = ["A"] * 4 + ["CSO"] * 24 + ["COSC"] * 6

    # training discriminators
    w.fit(X, y)

    percentage = w.predict_proba(retina[4:249])
    A_test = w.predict(retina[4:249])
    stats_percentage = [a for a, c, co in percentage]
    mu = mean(stats_percentage)
    dev = pstdev(stats_percentage)
    print(mu, pvariance(stats_percentage, mu), dev)
    for index, (i, j) in enumerate(zip(percentage, A_test)):
        if i[0] > (mu + dev):
            print(index, i, j)


if __name__ == "__main__":
        #retina = matrix()
        retina = retina.retina
        wisard_with_bleaching()
        print("----------------")
        wisard_without_bleaching()
        print("----------------")

