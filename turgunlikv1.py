"""Created by Akbarov"""
import numpy as np

import functions


def turgunlik(feature_col, labels, explain_text):

    m = len(feature_col)
    matrix = np.array(feature_col).reshape((m, 1))
    id_col = np.arange(m).reshape((m, 1))

    ORDERED_COLUMN = 1

    matrix = np.hstack((id_col, matrix, labels.reshape((m, 1))))

    # print("Unsorted", matrix)
    matrix = functions.sorting_by_col(matrix, ORDERED_COLUMN)
    # print("Sorted", matrix)
    labels = matrix[:, 2].copy()
    class_names, class_members = np.unique(labels, return_counts=True)
    indexes = functions.get_uv(matrix, col_n=ORDERED_COLUMN)
    # indexes = [int(x) for x in matritsa[:, 0]]
    # print(indexes)

    # intervals = functions.finding_intervals(labels, indexes, class_members)
    intervals = functions.finding_intervals_with_tegishlilik_f(labels, indexes, class_members)

    # intervals.sort(key=lambda x: x[2], reverse=True)

    # intervallar = 0     # 'intervallar'
    # tegishlilik_f = 0   # 'har bir intervallning tegishlilik funksiyasi qiymati'
    # m = 0               # Obyektlar soni

    summa = 0
    for interval in intervals:
        if interval[4] > .5:
            summa += interval[4] * (interval[1]-interval[0])
        else:
            summa += (1 - interval[4]) * (interval[1] - interval[0])

    javob = summa / m
    #
    print(f"{explain_text} TURG'UNLIGI: {javob:1.2f} :: intervallar: {intervals}")

    return javob


def turgunlik_ishchi(feature_col, labels, explain_text):

    m = len(feature_col)
    matrix = np.array(feature_col).reshape((m, 1))
    id_col = np.arange(m).reshape((m, 1))

    ORDERED_COLUMN = 1

    matrix = np.hstack((id_col, matrix, labels.reshape((m, 1))))

    # print("Unsorted", matrix)
    matrix = functions.sorting_by_col(matrix, ORDERED_COLUMN)
    # print("Sorted", matrix)
    labels = matrix[:, 2].copy()
    class_names, class_members = np.unique(labels, return_counts=True)
    indexes = functions.get_uv(matrix, col_n=ORDERED_COLUMN)
    # indexes = [int(x) for x in matritsa[:, 0]]
    # print(indexes)

    # intervals = functions.finding_intervals(labels, indexes, class_members)
    intervals = functions.finding_intervals_with_tegishlilik_f(labels, indexes, class_members)

    # intervals.sort(key=lambda x: x[2], reverse=True)

    # intervallar = 0     # 'intervallar'
    # tegishlilik_f = 0   # 'har bir intervallning tegishlilik funksiyasi qiymati'
    # m = 0               # Obyektlar soni

    summa = 0
    for interval in intervals:
        if interval[4] > .5:
            summa += interval[4] * (interval[1]-interval[0])
        else:
            summa += (1 - interval[4]) * (interval[1] - interval[0])

    javob = summa / m
    javob = (javob, len(intervals), explain_text)
    #print(f"{explain_text} TURG'UNLIGI: {javob:1.2f} :: intervallar: {intervals}")

    return javob


