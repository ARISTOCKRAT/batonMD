import numpy as np

np.seterr(all="ignore")


def turgunlik(ustun, alomat1, alomat2, amal):
    """Bu funksiya kelgan ustunni turg'unligini hisoblaydi"""
    print(f"X{alomat1} {amal} X{alomat2} ustuni: {len(ustun)}")


matritsa = np.genfromtxt(r"d:\NUU documents\Ilmiy ish\Intervallar\init_data\giper\Objects.csv", delimiter=',')
labels = np.genfromtxt(r"d:\NUU documents\Ilmiy ish\Intervallar\init_data\giper\Target.csv", delimiter=",")

shape = matritsa.shape


for alomat1 in range(shape[1]):

    for alomat2 in range(shape[1]):

        # kupaytma
        if alomat1 < alomat2:
            latent = matritsa[:, alomat1] * matritsa[:, alomat2]
            turgunlik(latent, alomat1, alomat2, " * ")

        # bulinma
        if alomat1 != alomat2:
            latent = np.divide(matritsa[:, alomat1], matritsa[:, alomat2])
            turgunlik(latent, alomat1, alomat2, " / ")





