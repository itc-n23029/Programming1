s_coordi_list = ["1.0,2.2,3.5", "2.1,3.2,5.5", "1.2,1.3,2.2", "2.1,3.1,4.5"]


def str_to_float_coordi(s_coordi):
    p = s_coordi.split(",")
    f_coordi = [float(n) for n in p]
    return f_coordi


f_coordi_list = [str_to_float_coordi(s_coordi) for s_coordi in s_coordi_list]
print(f_coordi_list)
