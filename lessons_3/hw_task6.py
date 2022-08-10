# We have an imaginary chessboard with pieces located on cells with coordinates from 1 to 10 along the x and y axes
# x1 and y1 indicate the position of the piece on the chessboard
move_x1 = int(input(' Enter the value of the location of the object along the x-axis: '))
move_y1 = int(input(' Enter the value of the location of the object along the y-axis: '))
# x2 and y2 indicate the location of the cell on which to place the shape
move_x2 = int(input('Enter the value of the cell where you want to place the shape on the x-axis:'))
move_y2 = int(input('Enter the value of the cell where you want to place the shape on the y-axis:'))
#We determine the possibility of movement of the figure
step_x = abs(move_x1 - move_x2)
step_y = abs(move_y1 - move_y2)
# Step Calculation: An object can step 1 cell along the x-axis and 2 steps along the y-axis or vice versa
if step_x == 1 and step_y == 2 or step_x == 2 and step_y == 1:
    print('You can make a move')
else:
    print('You can"t make a move')

#Задача сложная, практически всё за меня решил Александр написав решение в беседе