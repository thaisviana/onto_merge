import random
from PyWANN.PyWANN.WiSARD import WiSARD
from statistics import mean, pvariance, pstdev
import numpy as np
from math import *
from matrix_of_words import matrix
from matrices.energy_matrix import matrix as energy_matrix
from matrices.energy_words import words as energy_words


def wisard_with_bleaching(retina, retina_labels):
    seed = random.randint(0, 10000)
    w = WiSARD(num_bits_addr=4, bleaching=True, ignore_zero_addr=True, seed= seed)

    X = retina[:int(len(retina)/2)]
    y = retina_labels[:int(len(retina_labels)/2)]
    P = retina[int(len(retina) / 2)+1:]
    P_labels = retina_labels[int(len(retina_labels) / 2)+1:]
    result(w, X, y, P, P_labels)


def result(w, X, y, P, P_labels):
    # training discriminators
    w.fit(X, y)
    percentage = w.predict_proba(P)
    A_test = w.predict(P)
    percentages = []
    index = 0
    for line in percentage:
        match_percentage = max(line)
        if match_percentage != 0:
            match_indexs = []
            for i, j in enumerate(line):
                if j == match_percentage:
                    match_indexs.append(i)
            print(P_labels[index], " - ", match_percentage, " - ", [P_labels[i] for i in match_indexs])
        percentages.append(match_percentage)
        index += 1

    mu = mean(match_percentage)
    dev = pstdev(match_percentage)
    print(mu, pvariance(match_percentage, mu), dev)


def similarity(f_sim, mu, de):
    sims = []
    for index, line in enumerate(retina):
        for i, l in enumerate(retina):
            if index != i and line != l:
                sim = f_sim(np.array(l), np.array(line))
                if not isnan(sim) and sim > 0.0:
                    sims.append(sim)
                    if sim:
                        print(retina_labels[index], retina_labels[i], sim)
    mu = mean(sims)
    dev = pstdev(sims)
    print(mu, pvariance(sims, mu), dev)


if __name__ == "__main__":
    #create_ontology_data()
    label_ontology_list=['cosc', 'cso', 'algpedia', 'cops']
    #label_ontology_list=['ical', 'index', 'ifc']
    #retina = matrix(label_ontology_list=label_ontology_list)

    retina_labels = list(line[1] for line in energy_matrix)
    retina = []
    for line in energy_matrix:
        retina_line = []
        for column in energy_words:
            if column in list(line[2].keys()):
                retina_line.append(line[2][column])
            else:
                retina_line.append(0)
        retina.append(retina_line)
    print(retina_labels)

    wisard_with_bleaching(retina, retina_labels)



        #wisard_with_bleaching()
"""
    cosine_similarity = lambda a, b: (np.dot(a, b)) / (a.dot(a) * b.dot(b))
    euclidean_distance = lambda x, y: sqrt(sum(pow(a - b, 2) for a, b in zip(x, y)))
    manhattan_distance = lambda x, y: sum(abs(a - b) for a, b in zip(x, y))

"""