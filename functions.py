import numpy as np


def get_uv(df, col_n):
    indexes = [0]
    m = df.shape[0]
    for u in range(1, m):
        if df[u][col_n] != df[u-1][col_n]:
            indexes.append(u)
    if indexes[-1] != len(df)-1:
        indexes.append(len(df)-1)
    ind = tuple(indexes)
    return ind


def sorting_by_col(df, col_n):
    sorting_order = list(df[:, col_n].argsort())
    return df[sorting_order]


def finding_intervals(sorted_labels, indexes=None, K_pow=None):
    answer = []
    if indexes is None or K_pow is None:
        print(f"ERROR:\tinterval:{indexes}; K_pow:{K_pow}")
        return None
    best_interval = (0, 0, float('-inf'))
    N_ = M_ = None
    for n, u in enumerate(indexes[:-1]):
        for m, v in enumerate(indexes[n+1:]):
            if u == v: continue
            Ki, di = np.unique(sorted_labels[u:v], return_counts=True)
            d1 = d2 = 0.
            if len(Ki) == 1:
                if int(Ki[0]) == 1:
                    d1 = di[0]
                    d2 = 0.
                elif int(Ki[0]) == 2:
                    d1 = 0.
                    d2 = di[0]
                dominator = Ki[0]
            else:
                if int(Ki[0]) == 1:
                    d1 = di[0]
                    d2 = di[1]
                elif int(Ki[0]) == 2:
                    d1 = di[0]
                    d2 = di[1]
                if di[0] > di[1]:
                    dominator = Ki[0]
                else:
                    dominator = Ki[1]

            summa = abs((d1 / K_pow[0]) - (d2 / K_pow[1]))

            if best_interval[2] < summa:
                N_ = n
                M_ = n + m + 1
                best_interval = (u, v, summa, int(dominator))

    answer.append(best_interval)
    if N_ is None or M_ is None:
        print('error')
    if len(indexes[:N_]):
        a = finding_intervals(sorted_labels, indexes[:N_ + 1], K_pow)
        for e in a: answer.append(e)
    if indexes[M_] != indexes[-1] and M_ != len(indexes)-1:
        a = finding_intervals(sorted_labels, indexes[M_:], K_pow)  # ??
        for e in a: answer.append(e)

    return answer


def tegishlilik_funksiyasi_qiymati(obyektning_alomat_qiymati, df_ustuni, intervallar_ruyhati, labels):
    """
    :param obyektning_alomat_qiymati:  # qaysi obyekt haqida gap ketyapganini bilish uchun
    :param df_ustuni:               # E0 tanlama (butun ustun)
    :param intervallar_ruyhati:     # obyektimiz qaysi intervalga tushishini bilish un
    :param labels:                  # tartiblangan sinf vektori
    :return:                          tegishlilik funksiyasini qiymatini
    """

    K1_pow = K2_pow = 0
    for qiymat in labels:
        # print(qiymat)
        if qiymat == 1:
            K1_pow += 1
        else:
            K2_pow += 1
    # DEBUG
    # print(K1_pow, K2_pow)
    # print(f"obyektning_alomat_qiymati :: {obyektning_alomat_qiymati}\n df_ustuni :: {df_ustuni}\n"
    #       f"intervallar_ruyhati :: {intervallar_ruyhati}\n labels :: {labels}")

    javob = -1
    for interval in intervallar_ruyhati:
        if df_ustuni[interval[0]] <= obyektning_alomat_qiymati <= df_ustuni[interval[1]]:
            d1 = d2 = 0
            for qiymat in labels[interval[0]:interval[1]+1]:
                if qiymat == 1:
                    d1 += 1
                else:
                    d2 += 1
            nu1 = d1 / K1_pow
            nu2 = d2 / K2_pow
            javob = nu1 / (nu1 + nu2)
            # DEBUG
            # print(f"labels[{interval[0]} : {interval[1]+1}] = {labels[interval[0]:interval[1]+1]}; len={len(labels[interval[0]:interval[1]+1])}")
            # print(f"nu1 = {d1} / {K1_pow} = {nu1};\n"
            #       f"nu2 = {d2} / {K2_pow} = {nu2};\nf = {javob}")
            break

    if javob == -1:
        print("ERROR :: Ko'rsatilgan qiymat boron bir ko'rsatilgan inetvalga tushmadi O_o")

    return javob


def finding_intervals_with_tegishlilik_f(sorted_labels, indexes=None, K_pow=None):
    answer = []
    if indexes is None or K_pow is None:
        print(f"ERROR:\tinterval:{indexes}; K_pow:{K_pow}")
        return None
    best_interval = (0, 0, float('-inf'))
    N_ = M_ = None
    for n, u in enumerate(indexes[:-1]):
        for m, v in enumerate(indexes[n+1:]):
            if u == v: continue
            Ki, di = np.unique(sorted_labels[u:v], return_counts=True)
            d1 = d2 = 0.
            if len(Ki) == 1:
                if int(Ki[0]) == 1:
                    d1 = di[0]
                    d2 = 0.
                elif int(Ki[0]) == 2:
                    d1 = 0.
                    d2 = di[0]
                dominator = Ki[0]
            else:
                if int(Ki[0]) == 1:
                    d1 = di[0]
                    d2 = di[1]
                elif int(Ki[0]) == 2:
                    d1 = di[0]
                    d2 = di[1]
                if di[0] > di[1]:
                    dominator = Ki[0]
                else:
                    dominator = Ki[1]

            summa = abs((d1 / K_pow[0]) - (d2 / K_pow[1]))
            nu1 = d1 / K_pow[0]
            nu2 = d2 / K_pow[1]
            tegishlilik_f = nu1 / (nu1 + nu2)

            if best_interval[2] < summa:
                N_ = n
                M_ = n + m + 1
                best_interval = (u, v, summa, int(dominator), tegishlilik_f, nu1, nu2)

    # if K_pow[0] == 1:
    #     K1_pow = K_pow[0]
    #     K2_pow = K_pow[1]
    # else:
    #     K1_pow = K_pow[1]
    #     K2_pow = K_pow[0]
    #
    # for idn in range(best_interval[0], best_interval[1]):
    #     d1 = d2 = 0
    #     if int(sorted_labels[idn]) == 1:
    #         d1 += 1
    #     else:
    #         d2 += 1
    # nu1 = d1 / K1_pow
    # nu2 = d2 / K2_pow
    # tegishlilik_f = nu1 / (nu1 + nu2)
    # print(K_pow, K1_pow, K2_pow)
    # best_interval = (best_interval[0], best_interval[1], best_interval[2], best_interval[3],
    #                  tegishlilik_f, nu1, nu2)

    answer.append(best_interval)
    # print(f"TEST: {best_interval}")
    if N_ is None or M_ is None:
        print('error')
    if len(indexes[:N_]):
        a = finding_intervals_with_tegishlilik_f(sorted_labels, indexes[:N_ + 1], K_pow)
        for e in a: answer.append(e)
    if indexes[M_] != indexes[-1] and M_ != len(indexes)-1:
        a = finding_intervals_with_tegishlilik_f(sorted_labels, indexes[M_:], K_pow)  # ??
        for e in a: answer.append(e)

    return answer

