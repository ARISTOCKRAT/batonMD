import numpy as np

import functions

ORDERED_COLUMN = 4

matritsa = np.genfromtxt("d:\\NUU documents\\Ilmiy ish\\Intervallar\\init_data\\Objects.csv")
class_desc = {1: "Sog'lomlar", 2: "Kasallar"}
description = []
with open(r"d:\NUU documents\Ilmiy ish\Intervallar\init_data\Description.csv", mode='r') as file:
    line = file.readline()
    while line:
        line = line.strip()
        description.append(line)
        line = file.readline()
m = matritsa.shape[0]
obj_id = np.arange(m).reshape((m, 1))
matritsa = np.hstack((obj_id, matritsa))
matritsa = functions.sorting_by_col(matritsa, ORDERED_COLUMN)
for n, row in enumerate(matritsa):
    print(f"{n}:: S:{int(row[0]):>3}::    {description[ORDERED_COLUMN-1]}: {row[ORDERED_COLUMN]}    "
          f"{class_desc[int(row[-1])]} ::")
labels = matritsa[:, -1].copy()
class_names, class_members = np.unique(labels, return_counts=True)
indexes = functions.get_uv(matritsa, col_n=ORDERED_COLUMN)
intervals = functions.finding_intervals(labels, indexes, class_members)
print(
    f"\n\n"
    f"Berilganlarga '{description[ORDERED_COLUMN-1]}' alomati bo'yicha ishlov berildi\n",
    f"{'Interval':^20}{'Kriteriyaning qiymati':^30}{'Dominant':^10}\n",
    f"=="*30
)
intervals.sort(key=lambda x: x[1], reverse=True)
for interval in intervals:
    print("\t{0:<25}{1:^15}\t{2:<15}".format(
        f'[{matritsa[interval[0]][ORDERED_COLUMN]}..{matritsa[interval[1]-1][ORDERED_COLUMN]}]',
        f'{interval[2]*100:<3.4}%',
        f'{class_desc[interval[3]]:<15}'
    ))