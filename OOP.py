class Student:
    
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def Print(self):
        print(f"{self.name} 考了 {self.score} 分")


s1 = Student("小明",95)
s1.Print()