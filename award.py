swimming_time = int(input("Enter swimming time. "))
cycling_time = int(input("Enter cycling time. "))
running_time = int(input("Enter running time. "))

total_time = swimming_time + cycling_time + running_time

if total_time <= 100:
    print("Provincial Colours")

elif (total_time >= 101) and (total_time <= 105):
    print("Provisional Half Colours")

elif (total_time >= 106) and (total_time <= 110):
    print("Provincial Scroll")

else:
    print("No award")
