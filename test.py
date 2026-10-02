ngay_sinh="1/2/2006"

def hien_thi(a,b=1):
    # print(ngay_sinh)
    print(b)
    global ngay_sinh
    print(ngay_sinh)
    ngay_sinh='1/2/2005'
    print(ngay_sinh)
    return b+a

hien_thi(1)

set_demo = {1,2,3}
a={"đỏ","cam","xanh"}
for i in set_demo:
    print(i)

print(set_demo.isdisjoint(a))