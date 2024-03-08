'''
Se determina un punct de pe o curba B-spline cubica, in plan, cu 5 puncte de control, folosind algortimul lui DeBoor
Datele de intrare sunt:
a) cele 5 puncte de control
b) cele 9 noduri
c)un t care apartine [t3,t5]
rezultatul este r(t)
'''

puncte_x = []
puncte_y = []
Noduri = []


def initializam_punctele(r):
    xd = []  # x-urile
    yd = []  # y-urile
    for i in range(r - 3, r + 1):
        xd.append(puncte_x[i])
    for i in range(r - 3, r + 1):
        yd.append(puncte_y[i])
    return xd, yd


# determinam ce valoare are t-ul
def determinam_r(t):
    if t > Noduri[3] and t < Noduri[4]:
        return 3

    elif t >= Noduri[4] and t <= Noduri[5]:
        return 4


# rezolvare pentru cazul in care t = 3
def cazul_pentru_r_3(t):
    xd, yd = initializam_punctele(3)

    alfa1 = []

    alfa1.append((t - Noduri[1]) / (Noduri[4] - Noduri[1]))
    alfa1.append((t - Noduri[2]) / (Noduri[5] - Noduri[2]))
    alfa1.append((t - Noduri[3]) / (Noduri[6] - Noduri[3]))

    xd1 = []
    yd1 = []
    # d12
    xd1.append((1 - alfa1[0]) * xd[0] + alfa1[0] * xd[1])
    yd1.append((1 - alfa1[0]) * yd[0] + alfa1[0] * yd[1])
    # d13
    xd1.append((1 - alfa1[1]) * xd[1] + alfa1[1] * xd[2])
    yd1.append((1 - alfa1[1]) * yd[1] + alfa1[1] * yd[2])
    # d14
    xd1.append((1 - alfa1[2]) * xd[2] + alfa1[2] * xd[3])
    yd1.append((1 - alfa1[2]) * yd[2] + alfa1[2] * yd[3])

    # k = 2
    alfa2 = [(t - Noduri[2]) / (Noduri[4] - Noduri[2]), (t - Noduri[3]) / (Noduri[5] - Noduri[3])]

    xd2 = []
    yd2 = []
    # d23
    xd2.append((1 - alfa2[0]) * xd1[0] + alfa2[0] * xd1[1])
    yd2.append((1 - alfa2[0]) * yd1[0] + alfa2[0] * yd1[1])
    # d24
    xd2.append((1 - alfa2[1]) * xd1[1] + alfa2[1] * xd1[2])
    yd2.append((1 - alfa2[1]) * yd1[1] + alfa2[1] * yd1[2])

    alfa = (t - Noduri[3]) / (Noduri[4] - Noduri[3])

    xrt = (1 - alfa) * xd2[0] + alfa * xd2[1]
    yrt = (1 - alfa) * yd2[0] + alfa * yd2[1]

    print("rezultat: ")
    print("r(t) = (", xrt, ", ", yrt, ")")


# rezolvare pentru cazul in care t = 4
def cazul_pentru_r_4(t):
    xd, yd = initializam_punctele(4)

    alfa1 = []

    alfa1.append((t - Noduri[2]) / (Noduri[5] - Noduri[2]))
    alfa1.append((t - Noduri[3]) / (Noduri[6] - Noduri[3]))
    alfa1.append((t - Noduri[4]) / (Noduri[7] - Noduri[4]))

    xd1 = []
    yd1 = []
    # d12
    xd1.append((1 - alfa1[0]) * xd[0] + alfa1[0] * xd[1])
    yd1.append((1 - alfa1[0]) * yd[0] + alfa1[0] * yd[1])
    # d13
    xd1.append((1 - alfa1[1]) * xd[1] + alfa1[1] * xd[2])
    yd1.append((1 - alfa1[1]) * yd[1] + alfa1[1] * yd[2])
    # d14
    xd1.append((1 - alfa1[2]) * xd[2] + alfa1[2] * xd[3])
    yd1.append((1 - alfa1[2]) * yd[2] + alfa1[2] * yd[3])

    # k = 2
    alfa2 = [(t - Noduri[3]) / (Noduri[5] - Noduri[3]), (t - Noduri[4]) / (Noduri[6] - Noduri[4])]

    xd2 = []
    yd2 = []
    # d23
    xd2.append((1 - alfa2[0]) * xd1[0] + alfa2[0] * xd1[1])
    yd2.append((1 - alfa2[0]) * yd1[0] + alfa2[0] * yd1[1])
    # d24
    xd2.append((1 - alfa2[1]) * xd1[1] + alfa2[1] * xd1[2])
    yd2.append((1 - alfa2[1]) * yd1[1] + alfa2[1] * yd1[2])

    alfa = (t - Noduri[4]) / (Noduri[5] - Noduri[4])

    xrt = (1 - alfa) * xd2[0] + alfa * xd2[1]
    yrt = (1 - alfa) * yd2[0] + alfa * yd2[1]

    print("rezultat: ")
    print("r(t) = (", xrt, ", ", yrt, ")")


def main():
    # punctele de control
    print("Dati punctele de control: ")
    for i in range(0, 5):
        print("Intoducem datele pentru punctul", i)
        punct_x = float(input("x" + str(i) + "= "))
        punct_y = float(input("y" + str(i) + "= "))
        puncte_x.append(punct_x)
        puncte_y.append(punct_y)

    # nodurile
    print("Dati nodurile: ")
    for i in range(0, 9):
        nod = float(input("nod " + str(i) + "= "))
        Noduri.append(nod)

    # t-ul
    print("Dati t-ul: ")
    t = float(input("t = "))

    r = determinam_r(t)

    # cazurile
    if r == 3:
        cazul_pentru_r_3(t)
    elif r == 4:
        cazul_pentru_r_4(t)


main()
