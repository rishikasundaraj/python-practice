class Book:
    def __init__(self, title, author, pages):
        self.title=title
        self.author=author
        self.pages=pages

    def info(self):
        
        print(f"Book: {self.title} by {self.author}, {self.pages} pages")
        # print book info here
        pass

# Create 2 book objects and call their info method
book1 = Book("Python for Beginners", "Rishika", 150)
book2 = Book("AI for Kids", "chinnumai", 100)

book1.info()
book2.info()

#Create a class Student with:
#name, roll_no, marks (out of 100)
#A method show_report() that prints:
#"Name: [name], Roll No: [roll_no], Marks: [marks]"
class student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def info(self):
        print(f"student: {self.name} by {self.roll_no}, {self.marks}")

# Create book objects
student1 = student("rishika", 154, 150)
student2 = student("chinnu",134, 100)

# Call the info method
student1.info()
student2.info()

