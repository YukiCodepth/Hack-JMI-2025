import tkinter as tk
from tkinter import messagebox
import random

# Expanded question set with various subjects and difficulty levels
quiz_data = {
    "Math 🧮": {
        "Beginner 🍼": [
            ("What is 1 + 1?", "2"),
            ("What comes after 3?", "4"),
            ("What shape has 3 sides?", "Triangle")
        ],
        "Easy 🍭": [
            ("What is 2 + 2?", "4"),
            ("What is 5 - 3?", "2"),
            ("What is 10 / 2?", "5"),
            ("What is 7 + 6?", "13")
        ],
        "Medium 🍕": [
            ("What is 9 x 3?", "27"),
            ("What is the square root of 16?", "4"),
            ("What is 15 divided by 3?", "5"),
            ("What is 8 squared?", "64")
        ],
        "Hard 🚀": [
            ("Solve: 2x + 5 = 15", "5"),
            ("What is the derivative of x^2?", "2x"),
            ("What is the integral of 3x^2?", "x^3"),
            ("Solve: 5x - 3 = 2x + 6", "3")
        ]
    },
    "Science 🔬": {
        "Beginner 🍼": [
            ("What do plants need to grow?", "Water"),
            ("What is the color of the sky?", "Blue"),
            ("What do we breathe in to survive?", "Oxygen")
        ],
        "Easy 🍭": [
            ("What planet is known as the Red Planet?", "Mars"),
            ("What gas do plants absorb?", "Carbon Dioxide"),
            ("What is H2O commonly known as?", "Water")
        ],
        "Medium 🍕": [
            ("What is the chemical symbol for gold?", "Au"),
            ("Who developed the theory of relativity?", "Einstein"),
            ("What is the speed of light?", "299792458 m/s")
        ],
        "Hard 🚀": [
            ("What is the heaviest naturally occurring element?", "Uranium"),
            ("What is the smallest unit of life?", "Cell"),
            ("Which law states that for every action, there is an equal and opposite reaction?", "Newton's Third Law")
        ]
    },
    "Space 🌌": {
        "Beginner 🍼": [
            ("What shape is the Earth?", "Round"),
            ("What color is the sun?", "Yellow"),
            ("Is the moon bigger than Earth?", "No")
        ],
        "Easy 🍭": [
            ("What is the closest planet to the sun?", "Mercury"),
            ("Which planet is known as the Red Planet?", "Mars"),
            ("What does Earth orbit around?", "Sun")
        ],
        "Medium 🍕": [
            ("What is the largest planet in our solar system?", "Jupiter"),
            ("Which planet has rings around it?", "Saturn"),
            ("Who was the first person to walk on the moon?", "Neil Armstrong")
        ],
        "Hard 🚀": [
            ("What is the name of the galaxy we live in?", "Milky Way"),
            ("Which planet has the most moons?", "Jupiter"),
            ("What is a black hole?", "A region of space where gravity is so strong that nothing can escape")
        ]
    },
    "Animals 🐶": {
        "Beginner 🍼": [
            ("What does a cat say?", "Meow"),
            ("What color are pandas?", "Black and White"),
            ("What animal gives us milk?", "Cow")
        ],
        "Easy 🍭": [
            ("What does a cow say?", "Moo"),
            ("What is the fastest land animal?", "Cheetah"),
            ("Which bird can mimic speech?", "Parrot")
        ],
        "Medium 🍕": [
            ("Which mammal can fly?", "Bat"),
            ("What is the largest animal on Earth?", "Blue Whale"),
            ("How many legs does a spider have?", "8")
        ],
        "Hard 🚀": [
            ("Which animal has the longest lifespan?", "Giant Tortoise"),
            ("What type of animal is a Komodo dragon?", "Lizard"),
            ("Which bird lays the largest eggs?", "Ostrich")
        ]
    }
}


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎉 Fun Kids Quiz! 🎈")
        self.root.geometry("600x500")
        self.root.configure(bg="#ffebcd")
        self.subject = tk.StringVar()
        self.difficulty = tk.StringVar()
        self.questions = []
        self.current_question = 0
        self.score = 0
        self.create_main_menu()

    def create_main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="💡 Choose a Subject! 🎨", font=("Comic Sans MS", 16), bg="#ffebcd").pack(pady=10)
        for subject in quiz_data.keys():
            tk.Radiobutton(self.root, text=subject, variable=self.subject, value=subject, font=("Comic Sans MS", 12), bg="#ffd700").pack()
        
        tk.Label(self.root, text="🚀 Choose Difficulty Level! 🎯", font=("Comic Sans MS", 16), bg="#ffebcd").pack(pady=10)
        for level in ["Beginner 🍼", "Easy 🍭", "Medium 🍕", "Hard 🚀"]:
            tk.Radiobutton(self.root, text=level, variable=self.difficulty, value=level, font=("Comic Sans MS", 12), bg="#ffd700").pack()
        
        tk.Button(self.root, text="✨ Start Quiz! 🎉", command=self.start_quiz, font=("Comic Sans MS", 14), bg="#32cd32").pack(pady=10)
    
    def start_quiz(self):
        subject = self.subject.get()
        difficulty = self.difficulty.get()
        
        if not subject or not difficulty:
            messagebox.showwarning("⚠️ Oops!", "Please select all options! 😅")
            return
        
        self.questions = quiz_data[subject][difficulty]
        random.shuffle(self.questions)
        self.current_question = 0
        self.score = 0
        self.display_question()
    
    def display_question(self):
        if self.current_question < len(self.questions):
            q_text, self.correct_answer = self.questions[self.current_question]
            
            for widget in self.root.winfo_children():
                widget.destroy()
            
            tk.Label(self.root, text=f"🤔 {q_text}", font=("Comic Sans MS", 14), bg="#ffebcd").pack(pady=20)
            self.answer_entry = tk.Entry(self.root, font=("Comic Sans MS", 14))
            self.answer_entry.pack(pady=10)
            tk.Button(self.root, text="🎯 Submit Answer! ✅", command=self.check_answer, font=("Comic Sans MS", 14), bg="#ffa500").pack(pady=20)
        else:
            self.end_quiz()
    
    def check_answer(self):
        user_answer = self.answer_entry.get().strip()
        if user_answer.lower() == self.correct_answer.lower():
            self.score += 1
            messagebox.showinfo("🎉 Correct!", "You're a genius! 😎")
        else:
            messagebox.showinfo("❌ Oops!", f"Wrong answer! The correct one was {self.correct_answer}. 🤯")
        self.current_question += 1
        self.display_question()
    
    def end_quiz(self):
        if self.score == len(self.questions):
            messagebox.showinfo("🏆 Amazing!", f"Perfect Score! {self.score}/{len(self.questions)} 🎉 You're a legend! 🔥")
        elif self.score >= len(self.questions) // 2:
            messagebox.showinfo("👏 Well Done!", f"Good Score! {self.score}/{len(self.questions)} 😃 Keep it up!")
        else:
            messagebox.showinfo("😢 Better Luck Next Time!", f"Your score: {self.score}/{len(self.questions)} 💔 Try again!")
        self.create_main_menu()

root = tk.Tk()
app = QuizApp(root)
root.mainloop()
