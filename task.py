def task():
    fruits_1 = {"apple", "banana", "cherry", "grape", "mango", "pineapple", "papaya","sprite", "orange", "lemon", "strawberry"}
    fruits_2 = {"raspberry", "banana", "cherry", "grape", "mango", "blueberry", "papaya", "melon", "lemon", "steak"}

    fruits_1.remove("sprite")
    fruits_2.remove("steak")

    duplicate_fruits = (fruits_1.intersection(fruits_2))
    individual_fruits = (fruits_1.symmetric_difference(fruits_2))

    return [duplicate_fruits, individual_fruits]