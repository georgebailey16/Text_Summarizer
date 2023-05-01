from image import Image
from image_list import ImageList


def main():
    list_directory = []
    image_directory = []
    breakout = "False"
    while breakout == "False":
        user_input = int(input(
            "Welcome to Image Text Summarizer. Please select from options below:\n1) Summarize image\n2) "
            "Create gallery\n3) Add image to gallery\n4) Search gallery\n5) View in gallery\n6) Quit\n"))

        if user_input == 1:
            image = Image(input('Image name: '), input('Image file directory: '))
            image_directory.append(image)
            print(image.text_summary)

        elif user_input == 2:
            image_list = ImageList(input("Gallery name: ").lower)
            list_directory.append(image_list)
            print("Gallery created")

        elif user_input == 3:
            list_name = input("Gallery name: ").lower
            for i in range(len(list_directory)):
                if list_directory[i].name == list_name:
                    image = Image(input('Image name: '), input('Image file directory: '))
                    image_directory.append(image)
                    list_directory[i].add_image_to_list(image)
                    print("Image added")

        elif user_input == 4:
            relevant_images = []
            list_name = input("Gallery to search (or type directory to search all images): ").lower
            query = input("Word or phrase to search: ")
            for i in range(len(list_directory)):
                if list_directory[i].name == list_name:
                    for j in range(len(list_directory[i].list)):
                        if query in list_directory[i].list[j].image_text:
                            relevant_images.append(list_directory[i].list[j])
            save_list = input("Save as new gallery? (y/n): ").lower()
            if save_list == 'y':
                new_image_list = ImageList(query)
                for i in range(len(relevant_images)):
                    new_image_list.add_image_to_list(relevant_images[i])
                print("Gallery saved")
            else:
                print("Relevant files: ")
                for i in range(len(relevant_images)):
                    print(relevant_images[i].image_name)

        elif user_input == 5:
            list_name = input("Gallery name: ").lower
            for i in range(len(list_directory)):
                if list_directory[i].name == list_name:
                    for j in range(len(list_directory[i].list)):
                        print(str(j+1) + list_directory[i].list[j].image_name)
                    num_selected = int(input("Select image to view: "))-1
                    what_to_view = input("View:\n1) Image\n2) Image Text\n3) Image Text Summary")
                    if what_to_view == 1:
                        list_directory[i].list[num_selected].print_image()
                    elif what_to_view == 2:
                        print(list_directory[i].list[num_selected].image_text)
                    elif what_to_view == 3:
                        print(list_directory[i].list[num_selected].text_summary)
                    else:
                        break
        else:
            breakout = 'True'


main()
