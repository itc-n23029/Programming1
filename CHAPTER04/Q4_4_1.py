vote_num = 0


def vote():
    global vote_num
    vote_num += 1
    print("投票します")


def reset_box():
    global vote_num
    vote_num = 0
    print("箱を空にします")


def check_box():
    global vote_num
    print("票の数は{}です".format(vote_num))


vote()
check_box()
vote()
check_box()
for i in range(3):
    vote()
check_box()
reset_box()
check_box()
