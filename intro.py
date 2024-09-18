from PIL import Image, ImageFilter, ImageDraw
import face_recognition
import numpy as np
from sys import argv
import sys


def main():
    exit()


def hello():
    print("Hello world!")


def blur(image):
    before = Image.open(image)
    after = before.filter(ImageFilter.BoxBlur(5))
    after.save("blurred.jpg")


def edges(image):
    before = Image.open(image)
    after = before.filter(ImageFilter.FIND_EDGES)
    after.save("edges.jpg")


def find_faces(image):
    image_to_search = face_recognition.load_image_file(image)
    face_locations = face_recognition.face_locations(image_to_search)
    for face_location in face_locations:
        top, right, bottom, left = face_location
        face_image = image_to_search[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.show()


def find_person_in_group(person_image, group_image):
    known_face = face_recognition.load_image_file(person_image)
    known_encoding = face_recognition.face_encodings(known_face)[0]
    group_image = face_recognition.load_image_file(group_image)
    face_locations = face_recognition.face_locations(group_image)
    face_encodings = face_recognition.face_encodings(group_image, face_locations)
    pil_image = Image.fromarray(group_image)
    draw = ImageDraw.Draw(pil_image)
    for (top, right, bottom, left), face_encodings in zip(
        face_locations, face_encodings
    ):
        matches = face_recognition.compare_faces([known_encoding], face_encodings)
        face_distances = face_recognition.face_distance(
            [known_encoding], face_encodings
        )
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            draw.rectangle(
                ((left - 20, top - 20), (right + 20, bottom + 20)),
                outline=(0, 255, 0),
                width=20,
            )
    del draw
    pil_image.show()


def hello_person():
    name = input("What is your name: ")
    print(f"Hello {name}")


def variable_test():
    counter = 0
    counter += 1


def python_types():
    # string, int, float, bool
    my_age = 8
    print(my_age.bit_length())
    # print(my_age)


def calculator():
    x = get_int()
    y = get_int()
    print(f"{x} + {y} = {x+y}")


def get_int():
    while True:
        try:
            x = int(input("Enter int: "))
            break
        except ValueError:
            print("Not an integer")
    return x


def conditionals():
    x = get_int()
    y = get_int()
    if x < y:
        print("x is less than y")
    elif x > y:
        print("x is greater than y")
    else:
        print("x is equal to y")


def agree():
    answer = input("Do you agree? ")
    if answer.lower() in ["yes", "y"]:
        print("You agree")
    else:
        print("You do not agree")


def while_loop():
    i = 0
    while i < 3:
        print("I love IoT on Wednesday mornings")
        i += 1


def for_loop():
    for i in range(3):
        print("I love IoT on Wednesday mornings")


def pet_sounds(sound, times):
    for _ in range(times):
        print(sound)


def truncation():
    print(f"{(5/3):.50f}")


def print_column():
    while True:
        height = get_int()
        if height > 0:
            break
    for i in range(height):
        print("#")


def print_row():
    while True:
        length = get_int()
        if length > 0:
            break
    for i in range(length):
        print("#", end="")
    print()


def print_2d_grid(length, height):
    if length <= 0 or height <= 0:
        print("Only works with positive numbers")
        return
    else:
        for i in range(height):
            for j in range(length):
                print("#", end="")
            print()


def average_scores(scores):
    return sum(scores) / len(scores)


def get_scores():
    scores = []
    # ask the user for n scores, save in list and return
    while True:
        score = get_int()
        if score < 0:
            break
        scores.append(score)
    return scores


def phone_book():
    names = [
        "Thao",
        "Timon",
        "Daniel",
        "Luke",
        "Mohammad",
        "Rory",
        "Luke",
        "Caitlin",
        "Jamie",
        "Katie",
        "Shahzad",
    ]
    name = input("Name: ")
    if name in names:
        print("Found")
    else:
        print("Not found")


def phone_book_dict():
    people = {
        "Thao": "085 1245667",
        "Timon": "083 1234567",
        "Daniel": "086 1234567",
        "Luke": "086 1234567",
        "Mohammad": "086 1234567",
        "Rory": "086 1234567",
        "Luke": "086 1234567",
        "Caitlin": "086 1234567",
        "Jamie": "086 1234567",
        "Katie": "086 1234567",
        "Shahzad": "086 1234567",
    }

    name = input("Name: ")
    if name in people:
        print(f"Number: {people[name]}")
    else:
        print("Not found")


def command_line_args():
    if len(argv) == 2:
        print(f"Hello, {argv[1]}")
    else:
        print("Hello, world")


def exit():
    if len(sys.argv) != 2:
        print("Missing command line args")
        sys.exit(1)
    print(f"hello, {sys.argv[1]}")
    sys.exit(0)


if __name__ == "__main__":
    main()
