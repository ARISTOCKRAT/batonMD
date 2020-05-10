import numpy as np

import functions
import turgunlikv1

# project_path = r"d:\NUU documents\Ilmiy ish\Intervallar"
project_path = r"d:\_NUU\2020\batonMD"


np.seterr(all='raise')


# def turgunlik(ustun, alomat1, alomat2, amal):
#     """Bu funksiya kelgan ustunni turg'unligini hisoblaydi"""
#     print(f"X{alomat1} {amal} X{alomat2} ustuni: {ustun}")


# class_desc = {1: "Kasallar", 2: "Sog'lomlar"}


# id_col = np.arange(m).reshape((m, 1))
# matritsa = np.hstack((id_col, matritsa))

def turgunlik(column, labels, explain_text):
    # K_pow, indexes

    ORDERED_COLUMN = 1

    m = len(column)
    matrix = np.array(column).reshape((m, 1))
    id_col = np.arange(m).reshape((m, 1))

    matrix = np.hstack((id_col, matrix, labels.reshape((m, 1))))

    # print("Unsorted", matrix)
    matrix = functions.sorting_by_col(matrix, ORDERED_COLUMN)
    # print("Sorted", matrix)
    labels = matrix[:, 2].copy()
    class_names, class_members = np.unique(labels, return_counts=True)
    indexes = functions.get_uv(matrix, col_n=ORDERED_COLUMN)
    # indexes = [int(x) for x in matritsa[:, 0]]
    # print(indexes)

    intervals = functions.finding_intervals(labels, indexes, class_members)
    # print(intervals)

    intervals.sort(key=lambda x: x[2], reverse=True)


    print(f"LATENT ALOMAT QIYMATLARI: {explain_text} \n"
          "t/r id   sinf qiymati")
    for n, el in enumerate(matrix):
        print(f"{n:<3} {int(el[0]):<4} {int(labels[int(el[0])]):<5} {float(el[1]):<4.2f}")

    print(
        f"intervallari: {intervals}\n"
    )


    # for obyekt in matritsa[:, 0]:
    #     gamma = 0.
    #     for interval in intervals:
    #         print(matritsa[int(obyekt)][1])
    #         f = functions.tegishlilik_funksiyasi_qiymati(matritsa[int(obyekt), 1], 1, interval, labels)
    #         print(f"obj[{obyekt}]:: interval:{interval}:: f = {f}")
    # BETTA = 0.
    # summa = 0.
    #
    # for interval in intervals:
    #     f = functions.prenadlejnost(matritsa[:, -1], ORDERED_COLUMN, interval)
    #     # if f > 0.5:
    #
    #     # print(f"f{f}")
    #     summa += (abs(interval[0]-interval[1])) * f
    #     # print(f"SUMMA:{summa}")
    # BETTA = summa / m
    # print(f"\nBETTA = {BETTA}")


# print("*"*50, '\tend\t', '*'*50)

############################################################################################
# ISHONCHLILIK ME'YORI #####################################################################
############################################################################################
# labels = np.genfromtxt(target_file, delimiter=';')
# for obyekt_tr in matritsa:
#     # obyekt_tr = matritsa[37].copy()
#
#     print(f"Obyekt {int(obyekt_tr[0])}", end='\n')
#     fa1 = 0
#     for alomat_nomeri in range(1, n+1):
#         sorting_order = list(matritsa[:, alomat_nomeri].argsort())
#         indexes = functions.get_uv(matritsa[sorting_order], col_n=alomat_nomeri)
#         intervals = functions.finding_intervals(labels[sorting_order], indexes, class_members)
#
#         fa2 = functions.tegishlilik_funksiyasi_qiymati(
#             obyekt_tr[alomat_nomeri],
#             matritsa[sorting_order, alomat_nomeri],
#             intervals,
#             labels[sorting_order]
#         )
#
#         print(f"Qadam-{alomat_nomeri-1:0>2} :: f(a1) + f(a{alomat_nomeri}) * (1 - f(a1) = {fa1:0.2f} + {fa2:.2f} * ({1-fa1:.2f})", end=" ")
#         fa1 = fa1 + fa2 * (1 - fa1)
#         print(f" = {fa1:.2f}")
#     print(fa1)
#
#
########################################################################################################################
matritsa = np.genfromtxt(project_path + r"\init_data\giper\Objects.csv", delimiter=',')
labels = np.genfromtxt(project_path + r"\init_data\giper\Target.csv", delimiter=",")

shape = matritsa.shape
feature_sorting = []

for alomat1 in range(shape[1]):

    for alomat2 in range(shape[1]):
        latent_kupaytma = []
        latent_bulinma = []
        #
        for qator in range(shape[0]):

            # Kopaytma
            if alomat1 < alomat2:
                lat = matritsa[qator][alomat1] * matritsa[qator][alomat2]
                # print(matritsa[qator][alomat1], " * ", matritsa[qator][alomat2], " = ", lat)
                latent_kupaytma.append(lat)
            else:
                latent_kupaytma = None

            # Bo'linma
            if alomat1 != alomat2:
                try:
                    lat = matritsa[qator][alomat1] / matritsa[qator][alomat2]
                    latent_bulinma.append(lat)
                except Exception as e:
                    # print(f"m[{qator}][{alomat1}] / m[{qator}][{alomat2}] = {matritsa[qator][alomat1]} / {matritsa[qator][alomat2]} = ERROR:{e.args}")
                    latent_bulinma.append(float("-inf"))
            else:
                latent_bulinma = None

        if latent_kupaytma:
            # turgunlik(latent_kupaytma, labels, f"x{alomat1} * x{alomat2}")
            # turgunlikv1.turgunlik(latent_kupaytma, labels, f"x{alomat1} * x{alomat2}")
            feature_sorting.append(
                turgunlikv1.turgunlik_ishchi(latent_kupaytma, labels, f"x{alomat1} * x{alomat2}")
            )
        if latent_bulinma:
            # turgunlik(latent_bulinma, labels, f"x{alomat1} / x{alomat2}")
            # turgunlikv1.turgunlik(latent_bulinma, labels, f"x{alomat1} / x{alomat2}")
            feature_sorting.append(
                turgunlikv1.turgunlik_ishchi(latent_bulinma, labels, f"x{alomat1} / x{alomat2}")
            )
        print(f"{alomat1}:{alomat2}", end=" ")
        # turgunlik(latent_kupaytma, alomat1, alomat2, " * ")
        # turgunlik(latent_bulinma, alomat1, alomat2, " / ")

sort_turgunlik = sorted(feature_sorting, key=lambda L:L[0], reverse=True)
sort_interval_soni = sorted(feature_sorting, key=lambda L:L[1], reverse=False)

c = 0
print("Turg'unlik bo'yicha tartiblagandagi birinchi 10 tasi: \n"
      "Latent formulasi\t::\tTurg'unlik ko'rsatkichi")
for row in sort_turgunlik:
    print(f"{row[-1]} :: {row[0]:1.2f}")
    c+=1
    if c == 10:
        break
c = 0
print("Intervallar soni bo'yicha tartiblagandagi birinchi 10 tasi: \n"
      "Latent formulasi\t::\tintervallar soni")
for row in sort_interval_soni:
    print(f"{row[-1]} :: {row[1]:1.2f}")
    c+=1
    if c == 10:
        break

