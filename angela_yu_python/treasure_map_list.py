row1 = ["o","o","o"]
row2 = ["o","o","o"]
row3 = ["o","o","o"]
map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
vertical = int(position[0])
horizontal = int(position[1])
map[horizontal-1][vertical-1]= "X"
# selected_row = map[vertical-1]
# selected_row[horizontal-1]="X"
print(f"{row1}\n{row2}\n{row3}")