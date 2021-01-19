year,month,day = input().split(".")
#zfill(인자) 인자의 길이만큼 공간을 할당하고 빈공간은 0으로 채워출력한다
print(year.zfill(4)+"."+month.zfill(2)+"."+day.zfill(2))