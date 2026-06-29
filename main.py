import cv2


def display(img):
    cv2.imshow("Grayscale Image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def save(img, output_name):
    cv2.imwrite(output_name,img)

def color_input():
    print("Enter color in BGR format with space:")
    b, g, r = map(int, input("B G R: ").split())
    return (b, g, r)

def line(img):
    print("\n--- DRAW A LINE ---")
    print("Enter start coordinates (x1, y1):")
    x1 = int(input("x1: "))
    y1 = int(input("y1: "))
    print("Enter end coordinates (x2, y2):")
    x2 = int(input("x2: "))
    y2 = int(input("y2: "))
    line_color = color_input()
    line_thickness = int(input("Enter line thickness: "))
    cv2.line(img, (x1, y1), (x2, y2), line_color, line_thickness)

def rectangle(img):
    print("\n--- DRAW A RECTANGLE ---")
    print("Enter top-left corner coordinates (x, y):")
    rx1 = int(input("rx: "))
    ry1 = int(input("rx: "))
    print(f"Enter bottom-right corner coordinates (x, y):")
    rx2 = int(input("rx2: "))
    ry2 = int(input("ry2: "))
    rect_color = color_input()
    rect_thickness = int(input("Enter thickness (or -1 to fill the rectangle): "))
    
    cv2.rectangle(img, (rx1, ry1), (rx2, ry2), rect_color, rect_thickness)

def circle(img):
    print("\n--- DRAW A CIRCLE ---")
    print("Enter center coordinates (x, y): ")
    cx = int(input("cx: "))
    cy = int(input("cy: "))
    radius = int(input("Enter radius: "))
    circle_color = color_input()
    circle_thickness = int(input("Enter thickness (or -1 to fill the circle): "))
    
    cv2.circle(img, (cx, cy), radius, circle_color, circle_thickness)

def text(img):
    print("\n--- ADD TEXT OVERLAY ---")
    text = input("Enter the text you want to overlay: ")
    print(f"Enter origin coordinates (bottom-left corner of the text x, y):")
    tx = int(input("tx: "))
    ty = int(input("ty: "))
    text_color = color_input()
    font_scale = float(input("Enter font scale: "))
    text_thickness = int(input("Enter text thickness: "))
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, text, (tx, ty), font, font_scale, text_color, text_thickness)



print("------------Image Drawing Tool--------------")

while True:


    print("\nType 1 to insert image\nType 2 to save it\nType 3 to display it\nType 4 to draw line\nType 5 to draw rectangle\nType 6 to draw circle\nType 7 to add text overlay\nType 8 to exit....")
    ch = int(input("Enter your choice: "))


    if ch == 1:
        image_path = input("Enter the path to your input image: ")
        img = cv2.imread(image_path)
        if img is None:
            print("Error: Could not load the image.")
        else:
            h, w, c = img.shape
            print(f"Image loaded successfully! Dimensions: {w}x{h}")


    if ch == 2:
        output_name = input("Name the file to save with extension(for eg. output.jpg): ")
        save(img, output_name)
        print("image saved successfully")


    if ch == 3:
        display(img)

    if ch == 4:
         line(img)

    if ch == 5:
         rectangle(img)

    if ch == 6:
         circle(img)

    if ch == 7:
         text(img)

    if ch == 8:
        break
           

