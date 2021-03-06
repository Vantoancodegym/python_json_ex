# -----------------------------------------------------------
#Cafedev.vn - Kênh thông tin IT hàng đầu Việt Nam
#@author cafedevn
#Contact: cafedevn@gmail.com
#Fanpage: https://www.facebook.com/cafedevn
#Group: https://www.facebook.com/groups/cafedev.vn/
#Instagram: https://instagram.com/cafedevn
#Twitter: https://twitter.com/CafedeVn
#Linkedin: https://www.linkedin.com/in/cafe-dev-407054199/
#Pinterest: https://www.pinterest.com/cafedevvn/
#YouTube: https://www.youtube.com/channel/UCE7zpY_SlHGEgo67pHxqIoA/
# -----------------------------------------------------------

from thu_vien.giao_dich import *
import json
import datetime

if __name__ == "__main__":
# pdb.set_trace()
    print("Quản lý giao dịch:")
    list_vang = []
    list_tien = []
    tiep_tuc = 1
    while tiep_tuc == 1:        
        ma = input("Nhập mã GD:\t")
        ngay = input("Nhập ngày GD:\t")
        
        so_luong = int(input("Nhập số lượng:\t"))
        
        
        i = int(input("Chọn loại giao dịch: 1: Vàng, 2: Tiền Tệ:\t"))
        if i == 1:
            tong_slv = 0
            tong_tien_vang = 0
            loai = input("Chọn loai: 18k / 24k / 9999:\t")
            don_gia = eval(input("Nhập đơn giá:\t"))
            gdv = GiaoDich(ma, ngay, don_gia, so_luong, loai)
            list_vang.append(gdv)
            for item in list_vang:
                tong_slv += item.so_luong
                tong_tien_vang += item.thanh_tien()
                print(item.in_giao_dich())        
            print("Tổng số lượng:", tong_slv)
            print("Tổng số tiền:", tong_tien_vang)
        if i == 2:
            tong_slt = 0
            tong_tien_tien = 0
            loai = input("Chọn loai: USD / EUR / AUD:\t")
            don_gia = eval(input("Nhập tỷ giá:\t"))
            mua = True
            gd = int(input("Bạn mua hay bán? 1: mua, 0: bán:\t"))
            if gd == 0:
                mua = False 
            gdtt = GiaoDichTienTe(ma, ngay, don_gia, so_luong, loai, mua)
            list_tien.append(gdtt)
            for item in list_tien:
                tong_slt += item.so_luong
                tong_tien_tien += item.thanh_tien()
                print(item.in_giao_dich())        
            print("Tổng số lượng:", tong_slt)
            print("Tổng số tiền:", tong_tien_tien)
        
        tiep_tuc = int(input("Bạn muốn tiếp tục giao dịch? 1: Có, 0: Không\t"))
        
# Xu ly xuat file json giao dich

DS_GiaoDich = {}
 #xu ly giao dich vao tu doi tuong thanh distionary 
if len(list_vang)> 0:
    list_giao_dich_vang=[]
    for item_vang in list_vang:
        di_giao_dich_vang={"ma":item_vang.ma,"ngay":item_vang.ngay,"don_gia":item_vang.don_gia,"so_luong":str (item_vang.so_luong),"loai":str(item_vang.loai)} 
        list_giao_dich_vang.append(di_giao_dich_vang)
    DS_GiaoDich["giao_dich_vang"]=list_giao_dich_vang 
 #xu ly giao dich vao tu doi tuong thanh distionary 
if len(list_tien)> 0:
    list_giao_dich_tien=[] 
    for item_tien in list_tien: 
        di_giao_dich_tien={"ma":item_tien.ma,"ngay":item_tien.ngay,"don_gia":item_tien.don_gia,"so_luong":str (item_tien.so_luong),"loai":str(item_tien.loai),"mua":item_tien.mua}
        list_giao_dich_tien.append(di_giao_dich_tien)
    DS_GiaoDich["giao_dich_tien"]=list_giao_dich_tien

ngay_hien_hanh=datetime.datetime.now()
fileName=ngay_hien_hanh.strftime('%Y_%m_%d_%H_%M_%S')
path='du_lieu/'+fileName+'.json'
data_file=open(path,'w', encoding='utf-8')
json.dump(DS_GiaoDich,data_file,indent=4)
data_file.close() 
