def area_triangle(base,height):
    area =.5*base*height


    check_area(area)
def area_rectangular(height,width):
    area= height*width

    check_area(area)

def area_circle(radius):
    area= 3.14*(radius**2)

    check_area(area)
def check_area(area):
    print(f"Area is {area}")
    if area>=10:
     print("area is bigger than 10")

    elif 10 > area > 0:
     print("area is smaller than 10")

    else:print("invalid area")


area_rectangular(10,2)
area_circle(-1)
area_triangle(5,7)