# Mad Libs Generator
# ----------------------------------------

# Loop back to this point once code finishes
loop = 1
while loop < 10:
    # All the questions that the program asks the user
    noun = input("Choose a noun: ")
    p_noun = input("Choose a plural noun: ")
    noun2 = input("Choose another noun: ")
    place = input("Name a place: ")
    adjective = input("Choose an adjective (describing word): ")
    noun3 = input("Choose a final noun: ")

    # Displays the story based on the user's input
    print("------------------------------------------")
    print("Be kind to your", noun, "-footed", p_noun)
    print("For a duck may be somebody's", noun2 + ",")
    print("Be kind to your", p_noun, "in", place)
    print("Where the weather is always", adjective + ".")
    print()
    print("You may think that this is the", noun3 + ",")
    print("Well, it is.")
    print("------------------------------------------")

    # Loop back
    loop += 1
