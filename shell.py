import turtle
import math


turtle.speed(0.2)
center_x = 0
center_y = 0
turtle.setup(width=500, height=500)

numOfTriangles = int(input("Please enter number of triangles: "))


lastX = 0
lastY = 0

#function to update the last position
def updatePos():
    global lastX, lastY
    lastX, lastY = turtle.position()

#function to go back to the center point
def goCenter():
    turtle.goto(center_x, center_y)

#function to go back to the last point
def goBack():
    turtle.goto(lastX, lastY)

#draws the first triangle
turtle.forward(10)
updatePos()
turtle.left(90)
turtle.forward(10)
updatePos()
goCenter()
goBack()

#draws rest of the triangles 
for i in range(1,numOfTriangles):   
    angle = math.degrees(math.atan(math.sqrt(i+1)/(i)))
    turtle.left(angle)
    turtle.forward(10 * math.sqrt(2))
    updatePos()
    goCenter()
    goBack()



turtle.mainloop()
