from image import Image
from image_list import ImageList
from text_summarizer import summarize2


def setup():
    list_directory = []
    image_directory = []
    breakout = "False"
    while breakout == "False":
        user_input = int(input(
            "Welcome to Image Text Summarizer. Please select from options below:\n1) Summarize image\n2) "
            "Create gallery\n3) Add image to gallery\n4) Sort gallery\n5) View in gallery\n6) Quit\n"))

        if user_input == 1:
            image = Image(input('Image name: '), input('Image file directory: '))
            image_directory.append(image)
            x = image.text_summary
            y = summarize2(x).split(',')
            print('---' + image.get_image_name() + '---')
            for i in range(len(y)):
                print(y[i])


        elif user_input == 2:
            image_list = ImageList(input("Gallery name: ").lower())
            list_directory.append(image_list)
            print("Gallery created")

        elif user_input == 3:
            list_name = input("Gallery name: ").lower()
            for i in range(len(list_directory)):
                if list_directory[i].get_list_name() == list_name:
                    image = Image(str(input("Image name: ")), str(input("Image file directory: ")))
                    image_directory.append(image)
                    list_directory[i].add_image_to_list(image)
                    print("Image added")

        elif user_input == 4:
            list_name = input("Gallery to sort: ").lower()
            for i in range(len(list_directory)):
                if list_directory[i].get_list_name() == list_name:
                    list_directory[i].sort_a_to_z()
                    print('---', list_directory[i].get_list_name(), '---')
                    num = 1
                    for key in list_directory[i].gallery:
                        print(num, '.', list_directory[i].gallery[key])
                        num += 1

        elif user_input == 5:
            list_name = input("Gallery name: ").lower()
            for i in range(len(list_directory)):
                if list_directory[i].get_list_name() == list_name:
                    for key in list_directory[i].gallery:
                        print(list_directory[i].gallery[key].get_image_name())
                    im_selected = input("Enter image name to view: ")
                    back = "no"
                    while back != "yes":
                        what_to_view = int(input("View:\n1) Image\n2) Image Text\n3) Image Text Summary\n"))
                        if what_to_view == 1:
                            list_directory[i].gallery[im_selected].print_image()
                        elif what_to_view == 2:
                            print(list_directory[i].gallery[im_selected].get_image_text())
                        elif what_to_view == 3:
                            print(list_directory[i].gallery[im_selected].get_text_summary())
                        else:
                            break
                        back = input("Exit?(yes/no): ").lower()
        else:
            breakout = 'True'
        print()


def main():
    setup()


main()
