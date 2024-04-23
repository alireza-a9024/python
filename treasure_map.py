row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
Map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("where do you want to put the treasure? ")

print(position)

horizontal = int(position[0])
vertical = int(position[1])
print(horizontal, ",", vertical)
tmp1 = Map[horizontal-1]
tmp1[vertical-1] = "#"
print(f"{row1}\n{row2}\n{row3}")