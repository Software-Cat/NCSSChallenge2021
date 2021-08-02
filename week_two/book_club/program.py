whoReadWhichBooks = {}
people = []

# Input
bookReadBy = input("Book read: ")
while bookReadBy:
    book, person = bookReadBy.split(':')

    if not book in whoReadWhichBooks:
        whoReadWhichBooks[book] = []
    whoReadWhichBooks[book].append(person)

    if not person in people:
        people.append(person)

    bookReadBy = input("Book read: ")

# Sorting
whoReadWhichBooks = sorted(whoReadWhichBooks.items())

# Output
for book in whoReadWhichBooks:
    print(book[0] + ": ", end="")

    if book[1] == people:
        print("Everyone has read this!")
    else:
        peopleNotRead = []
        for person in people:
            if not person in book[1]:
                peopleNotRead.append(person)
        peopleNotRead.sort()
        print(", ".join(peopleNotRead))
