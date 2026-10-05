def create_lid(title, *tag, **details):
    print("Title:", title)
    print("Tag:", tag)
    print("Detail", details)

create_lid(
    "Python Journey",
    "Python",
    "Django",
    author = "Dhanush",
    mode = "Learning"
)