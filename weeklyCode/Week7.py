# class Sieunhan:
#     pass
# sieu_nhan_a = Sieunhan() # sieu_nhan_a is a object of Sieunhan class
# print(sieu_nhan_a)

# sieu_nhan_a.ten = "Sieu nhan do"
# sieu_nhan_a.vukhi = "kiem"
# sieu_nhan_a.mausac = "do"

# print("Ten cua sieu nhan la :", sieu_nhan_a.ten)
# print("Vu khi cua sieu nhan la :", sieu_nhan_a.vukhi)
# print("Sieu nhan mau :", sieu_nhan_a.mausac)



class Sieunhan:
    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = "Sieu nhan " + para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac
    def xinchao(self):
        return "Xinchao, ta chinh la " + self.ten

sieu_nhan_a = Sieunhan("do", "Kiem", "do")
print("ten cua sieu nhan la :", sieu_nhan_a.ten)
print("Vu khi cua sieu nhan la :", sieu_nhan_a.vu_khi)
print("Sieu nhan mau :", sieu_nhan_a.mau_sac)

print(sieu_nhan_a.xinchao())
print(Sieunhan.xinchao(sieu_nhan_a))

