import torch
import numpy as  np
import cv2
import urllib.request

def get_yolov5():
    torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='./best.pt')
    model.conf = 0.4 #  ty le nhan dang
    return model
model = get_yolov5()

url='http://172.20.10.2/cam-hi.jpg'
urllib.request.urlretrieve(url, "saveimg/abc.jpg")
url='http://172.20.10.4/cam-hi.jpg'
urllib.request.urlretrieve(url, "saveimg/xyz.jpg")

imgs1 = ['saveimg/abc.jpg']
results = model(imgs1)
results.show()
results.save()
results.xyxy  # img1 predictions (tensor)
results.pandas().xyxy
# print(results.xyxy)
print(results.pandas().xyxy)

imgs2 = ['saveimg/xyz.jpg']
res = model(imgs2)
res.show()
res.save()
res.xyxy  # img1 predictions (tensor)
res.pandas().xyxy
# print(results.xyxy)
print(res.pandas().xyxy)

for i in results.xyxy:
    if len(i) == 0:
             print("thuc hien lai")
             break 
    if int(i[0][5]) == 0:
        if len(i) == 1:
              print("thuc hien lai")
              break   
        if int(i[1][5]) == 1:
            print("hu hai: chot hop xich")
            print("so tien den bu: 80.000 vnd")
        if int(i[1][5]) == 2:
            print("hu hai: chot khung xe phai")
            print("so tien den bu: 80.000 vnd")
        if int(i[1][5]) == 3:
            print("hu hai: mat gio")
            print("so tien den bu: 200.000 vnd")
        if int(i[1][5]) == 4:
            print("hu hai: binh thuong")
            print("so tien den bu: 0 vnd")
        if int(i[1][5]) == 5:
            print("hu hai: hu ban dap phai")
            print("so tien den bu: 100.000 vnd")
        if int(i[1][5]) == 6:
            print("hu hai: dut xich")
            print("so tien den bu: 150.000 vnd")
        if int(i[1][5]) == 7:
            print("hu hai: rach yen sau phai")
            print("so tien den bu: 100.000 vnd")
        if int(i[1][5]) == 8:
            print("hu hai: rach yen truoc phai")
            print("so tien den bu: 100.000 vnd")
        if int(i[1][5]) == 9:
            print("binh thuong trai")
            print("so tien den bu: 0 vnd")
        if int(i[1][5]) == 10:
            print("hu hai: rach yen sau trai")
            print("so tien den bu: 100.000 vnd")
        if int(i[1][5]) == 11:
            print("hu hai: rach yen truoc trai")
            print("so tien den bu: 100.000 vnd")
        if int(i[1][5]) == 12:
            print("hu hai: chot khung xe trai")
            print("so tien den bu: 80.000 vnd")
        if int(i[1][5]) == 13:
            print("hu hai: hu ban dap trai")
            print("so tien den bu: 100.000 vnd")
        if int(i[1][5]) == 14:
            print("hu hai: mat chan chong")
            print("so tien den bu: 150.000 vnd")
    else :
         print("hay thuc hien lai")

for i in res.xyxy:
    if len(i) == 0:
             print("thuc hien lai")
             break 
    if int(i[0][5]) == 0:
        if len(i) == 1:
              print("thuc hien lai")
              break   
        if int(i[1][5]) == 1:
            print("hu hai: chot hop xich")
            print("so tien den bu: 80.000 vnd")
        if int(i[1][5]) == 2:
            print("hu hai: chot khung xe phai")
            print("so tien den bu: 80.000 vnd")
        if int(i[1][5]) == 3:
            print("hu hai: mat gio")
            print("so tien den bu: 200.000 vnd")
        if int(i[1][5]) == 4:
            print("hu hai: binh thuong")
            print("so tien den bu: 0 vnd")
        if int(i[1][5]) == 5:
            print("hu hai: hu ban dap phai")
            print("so tien den bu: 100.000 vnd")
        if int(i[1][5]) == 6:
            print("hu hai: dut xich")
            print("so tien den bu: 150.000 vnd")
        if int(i[1][5]) == 7:
            print("hu hai: rach yen sau phai")
            print("so tien den bu: 100.000 vnd")
        if int(i[1][5]) == 8:
            print("hu hai: rach yen truoc phai")
            print("so tien den bu: 100.000 vnd")
        if int(i[1][5]) == 9:
            print("binh thuong trai")
            print("so tien den bu: 0 vnd")
        if int(i[1][5]) == 10:
            print("hu hai: rach yen sau trai")
            print("so tien den bu: 100.000 vnd")
        if int(i[1][5]) == 11:
            print("hu hai: rach yen truoc trai")
            print("so tien den bu: 100.000 vnd")
        if int(i[1][5]) == 12:
            print("hu hai: chot khung xe trai")
            print("so tien den bu: 80.000 vnd")
        if int(i[1][5]) == 13:
            print("hu hai: hu ban dap trai")
            print("so tien den bu: 100.000 vnd")
        if int(i[1][5]) == 14:
            print("hu hai: mat chan chong")
            print("so tien den bu: 150.000 vnd")
    else :
         print("hay thuc hien lai")
