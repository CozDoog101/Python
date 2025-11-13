def SOfTriangle():
    siteA = int(input("Site A: "))
    siteB = int(input("Site B: "))
    triangleS = (siteA*siteB)/2
    result = print(f"The result is: {triangleS}")
    return result
    
def SOfSquare(a):
    siteA = a
    squareS = siteA*siteA
    return squareS
def SOfRectangle(a,b):
    siteA = a
    siteB = b
    rectangleS = siteA* siteB
    result = print(f"The result is: {rectangleS}")
    return result

end = True
while(end):
    name = input("enter figure name: ").lower()
    if name == "triangle":
        SOfTriangle()
    elif name == "square":
        a = int(input("enter: "))
        result = SOfSquare(a)
        print(result)
    elif name == "rectangle":
        a = int(input("Site A: "))
        b = int(input("Site B: "))
        result = SOfRectangle(a,b)
        print(result)
    elif name == "end":
        end = False
    else:
        print("Not a valid value")