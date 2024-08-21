import cv2


print("\nGreetings Sir/Mam, Your good name please....")
name=input("\nPlease Enter your name: ")
print(f"\nHello {name}, Welcome to the Image Resizer created by Mr. Vishwas Gandham.\nPlease provide the required details. [Note: To STOP the program, type \"DONE\" when asked for image's name.]")

while(True):
    source=input("\n\nEnter the image name with type (ex: image.jpg): ")
    if(source.lower()=="done"):
        break
    
    destination=input("Enter the desired name for your resized image with desired type (ex: new_image.jpeg): ")
    if(destination.lower()=="done"):
        break

    scale_breadth=int(input("Enter the breadth(in %) by which you want to resize the image (ex: 50): "))
    scale_height=int(input("Enter the height(in %) by which you want to resize the image (ex: 50): "))
    
    image=cv2.imread(source)
    new_breadth=int(image.shape[1] * scale_breadth / 100)
    new_height=int(image.shape[0] * scale_height / 100)
    output=cv2.resize(image, (new_breadth, new_height))
    
    cv2.imwrite(destination, output)
    
    print("\nImage has been resized and generated successfully, please check your taskbar if the image is not prompted automatically.\n\nPlease VIEW your image and CLOSE it to RUN the resizer AGAIN.\nThank You!")
    
    newimage=cv2.imread(destination)
    cv2.imshow("New Image", newimage)
    print("\n-x- END OF THE PROGRAM -x-")
    cv2.waitKey(0)
    
    