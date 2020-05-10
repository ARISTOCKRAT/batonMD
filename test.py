import numpy as np

import functions

ORDERED_COLUMN = 4

df = np.genfromtxt(r"d:\NUU documents\Ilmiy ish\Intervallar\init_data\Objects.csv")
# print(df)  # DEBUG

class_desc = {1: "Kasallar", 2: "Sog'lomlar"}

description = []
with open(r"d:\NUU documents\Ilmiy ish\Intervallar\init_data\Description.csv", mode='r') as file:
    line = file.readline()
    while line:
        line = line.strip()
        description.append(line)
        line = file.readline()

m = df.shape[0]
id_col = np.arange(m).reshape((m, 1))
df = np.hstack((id_col, df))
df = functions.sorting_by_col(df, ORDERED_COLUMN)

for n, row in enumerate(df):
    print(f"{n}:: S:{int(row[0]):>3}::    {description[ORDERED_COLUMN-1]}: {row[ORDERED_COLUMN]}    "
          f": {class_desc[int(row[-1])]} ::")

labels = df[:, -1].copy()
#print(labels)

class_names, class_members = np.unique(labels, return_counts=True)
# print(class_names, class_members) ##
indexes = functions.get_uv(df, col_n=ORDERED_COLUMN)

intervals = functions.finding_intervals(labels, indexes, class_members)
# print(F"int{intervals}")

print(
    f"\n\n"
    f"Berilganlarga {description[ORDERED_COLUMN-1]} alomatlar bo'yicha ishlov berildi",
    f"\n {'Interval':^30}{'Kriteriyaning qiymati':^15}{'Dominant':^15}\n",
    f"="*55
)
intervals.sort(key=lambda x: x[1], reverse=True)
for interval in intervals:

    print("\t{0:<25}{1:^15}\t{2:<15}".format(
        f'[{df[interval[0]][ORDERED_COLUMN]}..{df[interval[1]-1][ORDERED_COLUMN]}]',
        f'{interval[2]:<3.2}',
        f'{class_desc[interval[3]]:<15}'
    ))

# BETTA = 0.
# summa = 0.
#
# for interval in intervals:
#     f = functions.prenadlejnost(df[:, -1], ORDERED_COLUMN, interval)
#     # if f > 0.5:
#
#     # print(f"f{f}")
#     summa += (abs(interval[0]-interval[1])) * f
#     # print(f"SUMMA:{summa}")
# BETTA = summa / m
# print(f"\nBETTA = {BETTA}")
#
# functions.get_uv(df, ORDERED_COLUMN)
