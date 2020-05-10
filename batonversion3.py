import numpy as np

import functions

# ORDERED_COLUMN = 4
# object_file = r"d:\NUU documents\Ilmiy ish\Intervallar\init_data\Objects.csv"
object_file = r"d:\NUU documents\Ilmiy ish\Intervallar\init_data\skulls\Objects.csv"

target_file = r"d:\NUU documents\Ilmiy ish\Intervallar\init_data\skulls\Target.csv"

description_file = r"d:\NUU documents\Ilmiy ish\Intervallar\init_data\skulls\Description.csv"

matritsa = np.genfromtxt(object_file, delimiter=',')
labels = np.genfromtxt(target_file, delimiter=',')
description = np.genfromtxt(description_file, delimiter=',', dtype=str)

class_desc = {1: "Kasallar", 2: "Sog'lomlar"}

# description = []
# with open(r"d:\NUU documents\Ilmiy ish\Intervallar\init_data\Description.csv", mode='r') as file:
#     line = file.readline()
#     while line:
#         line = line.strip()
#         description.append(line)
#         line = file.readline()

m, n = matritsa.shape
id_col = np.arange(m).reshape((m, 1))
matritsa = np.hstack((id_col, matritsa))

# print(f"Matritsa: {matritsa}\nlabels: {labels}\ndescription: {description}")


for ORDERED_COLUMN in range(1, n):
    matritsa = functions.sorting_by_col(matritsa, ORDERED_COLUMN)
    # labels = matritsa[:, -1].copy()
    class_names, class_members = np.unique(labels, return_counts=True)
    indexes = functions.get_uv(matritsa, col_n=ORDERED_COLUMN)

    intervals = functions.finding_intervals(labels, indexes, class_members)
    print(F"int{intervals}")

    print(
        f"\n\n"
        f"Berilganlarga '{description[ORDERED_COLUMN-1]}' alomatlari bo'yicha ishlov berildi",
        f"\n {'Interval':^20}{'Kriteriyaning qiymati':^15}{'Dominant':^20}\n",
        f"="*55
    )

    intervals.sort(key=lambda x: x[2], reverse=True)
    # print(intervals)
    for interval in intervals:
        # print(interval)
        print("\t{0:<25}{1:^15}\t{2:<15}".format(
            f'[{matritsa[interval[0]][ORDERED_COLUMN]}..{matritsa[interval[1] - 1][ORDERED_COLUMN]}]',
            f'{interval[2]:<3.2f}',
            f'{class_desc[interval[3]]:<15}'
        ))
        pass

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


print("*"*50, '\tend\t', '*'*50)

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


