import random
import retina
from PyWANN.WiSARD import WiSARD
from statistics import mean, pvariance, pstdev
import numpy as np
from math import *
from matrix_of_words import matrix
from cops_labels import cops_labels
from bib_extractor import create_ontology_data


retina = retina.retina
#retina = np.array(retina).flatten()
# cosc 5 cso 17 algpedia 4 cops 15
cosc = retina[:5]
cosc_labels = ['profile'] + ['characteristic'] + ['license'] + ['software-library'] + ['software-component']
cso = retina[5:22]
cso_labels = ['data'] + ['class'] + ['policy-subject'] + ['input'] + ['exception'] + ['output'] + \
             ['task-collection'] + ['policy-object'] + ['computational-task'] + ['interface'] + ['policy-description'] + \
             ['software'] + ['user-group'] + ['constraint'] + ['user'] + ['abtract-data'] + ['method']
algpedia = retina[22:26]
cops = retina[26:]
algpedia_labels = ['algorithm'] + ['classification'] + ['author'] + ['programming languages']

retina_labels = cosc_labels + cso_labels + algpedia_labels + cops_labels

def wisard_with_bleaching():
    w = WiSARD(num_bits_addr=2, bleaching=True, defaul_b_bleaching=2)
    result(w)


def wisard_without_bleaching():
    seed = random.randint(0, 10000)
    w = WiSARD(num_bits_addr=2, bleaching=True, ignore_zero_addr=True, seed= seed)

    # USING COPS TRAIN
    print("USING COPS TO TRAIN AND FIT A, CSO AND COSC")
    X = cops
    y = cops_labels
    P = cosc + cso + algpedia
    P_labels = cosc_labels + cso_labels + algpedia_labels
    result(w, X, y, P, P_labels)

    seed = random.randint(0, 10000)
    w = WiSARD(num_bits_addr=2, bleaching=True, ignore_zero_addr=True, seed=seed)
    # USING A, CSO AND COSC TO TRAIN
    print("USING A, CSO AND COSC TO TRAIN AND FIT COPS")
    X = algpedia + cso + cosc
    y = algpedia_labels + cso_labels + cosc_labels
    result(w, X,y, cops, cops_labels)

    seed = random.randint(0, 10000)
    w = WiSARD(num_bits_addr=2, bleaching=True, ignore_zero_addr=True, seed=seed)
    print("USING A, CSO TO TRAIN AND FIT COSC")
    X = algpedia + cso
    y = algpedia_labels + cso_labels
    result(w, X, y, cosc, cosc_labels)

    print("USING A, COSC TO TRAIN AND FIT CSO ")
    seed = random.randint(0, 10000)
    w = WiSARD(num_bits_addr=2, bleaching=True, ignore_zero_addr=True, seed = seed)
    X = algpedia + cosc
    y = algpedia_labels + cosc_labels
    result(w, X, y, cso, cso_labels)

    print("USING CSO, COSC TO TRAIN AND FIT A ")
    X = cso + cosc
    y = cso_labels + cosc_labels
    seed = random.randint(0, 10000)
    w = WiSARD(num_bits_addr=2, bleaching=True, ignore_zero_addr=True, seed=seed)
    result(w, X, y, algpedia, algpedia_labels)


def result(w, X,y, P, P_labels):
    # training discriminators
    w.fit(X, y)
    percentage = w.predict_proba(P)
    A_test = w.predict(P)
    stats_percentage = [line[0] for line in percentage]
    mu = mean(stats_percentage)
    dev = pstdev(stats_percentage)
    print(mu, pvariance(stats_percentage, mu), dev)
    for index, (i, label) in enumerate(zip(percentage, A_test)):
        if i[0] > (mu + dev):
            print(P_labels[index], max(i), label)


def similarity(f_sim, mu, de):
    sims = []
    for index, line in enumerate(retina):
        for i, l in enumerate(retina):
            if index != i:
                sim = f_sim(np.array(l), np.array(line))
                if not isnan(sim) and sim > 0.0:
                    sims.append(sim)
                    # 0.0131588057897 0.000221764997588 0.014891776173044236
                    if sim > (mu + 3*de):
                        print(retina_labels[index], retina_labels[i], sim)
    mu = mean(sims)
    dev = pstdev(sims)
    print(mu, pvariance(sims, mu), dev)


if __name__ == "__main__":
    create_ontology_data()
    #retina = matrix()
    #wisard_with_bleaching()

    print("----------------")
    #wisard_without_bleaching()
    print("----------------")

    cosine_similarity = lambda a, b: (np.dot(a, b)) / (a.dot(a) * b.dot(b))
    euclidean_distance = lambda x, y: sqrt(sum(pow(a - b, 2) for a, b in zip(x, y)))
    manhattan_distance = lambda x, y: sum(abs(a - b) for a, b in zip(x, y))

    print("-------EUCLIDEAN---------")
    #similarity(euclidean_distance, 5.2391438859779536, 1.184697722250712)
    print("-------COSINE---------")
    #similarity(cosine_similarity, 0.0131588057897, 0.014891776173044236)
    print("-------MANHATTAN---------")
    #similarity(manhattan_distance, 28.8521373511, 12.680312695269397)
