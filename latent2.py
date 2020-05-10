import numpy as np

np.seterr(all="ignore")


project_path = r"d:\_NUU\2020\batonMD"
# proof


def turgunlik(ustun, alomat1, alomat2, amal):
    """Bu funksiya kelgan ustunni turg'unligini hisoblaydi"""
    print(f"X{alomat1} {amal} X{alomat2} ustuni: {len(ustun)}")


matritsa = np.genfromtxt(project_path + r"\init_data\giper\Objects.csv", delimiter=',')
labels = np.genfromtxt(project_path + r"\init_data\giper\Target.csv", delimiter=",")

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





