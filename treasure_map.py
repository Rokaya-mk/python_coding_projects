line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")

position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
line_index = position[0].upper();
column_index = int(position[1]) -1
if line_index == "A":
    map[column_index][0] = "X";
elif line_index == "B":
    map[column_index][1] = "X";
elif line_index == "C":
    map[column_index][2] = "X";
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")