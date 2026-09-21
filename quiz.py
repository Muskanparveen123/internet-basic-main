import tkinter as tk
from tkinter import messagebox
from certificate import CertificateWindow
import database


class QuizWindow:

    def __init__(self, parent, student_name="Student", learner_id=None):

        self.student_name = student_name
        self.learner_id = learner_id

        self.window = tk.Toplevel(parent)
        self.window.title("Internet Basics Quiz")
        self.window.geometry("1000x700")
        self.window.configure(bg="#F5F0FF")

        self.questions = [

            {
                "question": "1. 🌐 What is the Internet?",
                "options": [
                    "A worldwide network connecting computers",
                    "A computer game",
                    "A type of printer",
                    "A mobile application"
                ],
                "answer": "A worldwide network connecting computers"
            },

            {
                "question": "2. 🌍 Which application is used to browse websites?",
                "options": [
                    "Google Chrome",
                    "Calculator",
                    "Camera",
                    "Notepad"
                ],
                "answer": "Google Chrome"
            },

            {
                "question": "3. 🔍 You want to find information about Mumbai. What should you use?",
                "options": [
                    "Search Engine",
                    "Calculator",
                    "Paint",
                    "Music Player"
                ],
                "answer": "Search Engine"
            },

            {
                "question": "4. 📧 What is Email mainly used for?",
                "options": [
                    "Sending and receiving messages online",
                    "Taking photographs",
                    "Playing offline games",
                    "Editing videos"
                ],
                "answer": "Sending and receiving messages online"
            },

            {
                "question": "5. 📩 In an email, where do you enter the receiver's email address?",
                "options": [
                    "To",
                    "Subject",
                    "Message",
                    "Attachment"
                ],
                "answer": "To"
            },

            {
                "question": "6. 📝 What should you write in the Subject of an email?",
                "options": [
                    "The main topic of the email",
                    "Your password",
                    "Your OTP",
                    "Your phone PIN"
                ],
                "answer": "The main topic of the email"
            },

            {
                "question": "7. 📎 You want to send a photo with an email. What can you use?",
                "options": [
                    "Attachment",
                    "Subject",
                    "Search Bar",
                    "Browser History"
                ],
                "answer": "Attachment"
            },

            {
                "question": "8. 🔐 Which action is safest while using the Internet?",
                "options": [
                    "Never share your OTP or password",
                    "Click every unknown link",
                    "Share your password with friends",
                    "Use the same password everywhere"
                ],
                "answer": "Never share your OTP or password"
            },

            {
                "question": "9. ⚠️ You receive a message saying 'You won a prize! Click this unknown link.' What should you do?",
                "options": [
                    "Avoid clicking the link",
                    "Click immediately",
                    "Share it with friends",
                    "Give your OTP"
                ],
                "answer": "Avoid clicking the link"
            },

            {
                "question": "10. 🔑 Which password is the strongest?",
                "options": [
                    "123456",
                    "password",
                    "N@ziya123!",
                    "abcdef"
                ],
                "answer": "N@ziya123!"
            }
        ]

        self.colors = [
            "#2196F3",
            "#00A896",
            "#FF9800",
            "#E91E63",
            "#673AB7",
            "#009688",
            "#3F51B5",
            "#4CAF50",
            "#F44336",
            "#9C27B0"
        ]

        self.vars = []

        self.create_header()
        self.create_quiz_area()

    # ==================================================
    # HEADER
    # ==================================================

    def create_header(self):

        header = tk.Frame(
            self.window,
            bg="#542C85",
            height=85
        )

        header.pack(fill="x")
        header.pack_propagate(False)

        title = tk.Label(
            header,
            text="❓ Internet Basics Quiz",
            font=("Arial", 25, "bold"),
            bg="#542C85",
            fg="white"
        )

        title.pack(pady=22)

    # ==================================================
    # QUIZ AREA
    # ==================================================

    def create_quiz_area(self):

        welcome = tk.Label(
            self.window,
            text=f"Good luck, {self.student_name}! 🍀",
            font=("Arial", 18, "bold"),
            bg="#F5F0FF",
            fg="#542C85"
        )

        welcome.pack(pady=(12, 3))

        instruction = tk.Label(
            self.window,
            text="Answer all questions and score 60% or more to pass.",
            font=("Arial", 12),
            bg="#F5F0FF",
            fg="#666666"
        )

        instruction.pack(pady=(0, 10))

        # Scroll container

        container = tk.Frame(
            self.window,
            bg="#F5F0FF"
        )

        container.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=5
        )

        self.canvas = tk.Canvas(
            container,
            bg="#F5F0FF",
            highlightthickness=0
        )

        scrollbar = tk.Scrollbar(
            container,
            orient="vertical",
            command=self.canvas.yview
        )

        self.quiz_frame = tk.Frame(
            self.canvas,
            bg="#F5F0FF"
        )

        self.canvas_window = self.canvas.create_window(
            (0, 0),
            window=self.quiz_frame,
            anchor="nw"
        )

        self.quiz_frame.bind(
            "<Configure>",
            self.update_scroll_region
        )

        self.canvas.bind(
            "<Configure>",
            self.resize_frame
        )

        self.canvas.configure(
            yscrollcommand=scrollbar.set
        )

        self.canvas.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.canvas.bind_all(
            "<MouseWheel>",
            self.mouse_scroll
        )

        # Create questions

        for i, question in enumerate(self.questions):

            self.create_question_card(
                i,
                question
            )

        # Buttons

        button_frame = tk.Frame(
            self.window,
            bg="#F5F0FF"
        )

        button_frame.pack(
            fill="x",
            pady=10
        )

        submit_button = tk.Button(
            button_frame,
            text="✅ Submit Quiz",
            font=("Arial", 13, "bold"),
            bg="#00A896",
            fg="white",
            activebackground="#00796B",
            relief="flat",
            cursor="hand2",
            width=18,
            height=2,
            command=self.submit_quiz
        )

        submit_button.pack(
            side="left",
            padx=15
        )

        restart_button = tk.Button(
            button_frame,
            text="🔄 Restart",
            font=("Arial", 13, "bold"),
            bg="#FF9800",
            fg="white",
            activebackground="#EF6C00",
            relief="flat",
            cursor="hand2",
            width=15,
            height=2,
            command=self.restart_quiz
        )

        restart_button.pack(
            side="left",
            padx=15
        )

        close_button = tk.Button(
            button_frame,
            text="❌ Close",
            font=("Arial", 13, "bold"),
            bg="#E53935",
            fg="white",
            activebackground="#B71C1C",
            relief="flat",
            cursor="hand2",
            width=15,
            height=2,
            command=self.close_window
        )

        close_button.pack(
            side="right",
            padx=15
        )

    # ==================================================
    # QUESTION CARD
    # ==================================================

    def create_question_card(self, index, question):

        color = self.colors[index]

        card = tk.Frame(
            self.quiz_frame,
            bg="white",
            highlightbackground=color,
            highlightthickness=3
        )

        card.pack(
            fill="x",
            padx=10,
            pady=8
        )

        question_label = tk.Label(
            card,
            text=question["question"],
            font=("Arial", 14, "bold"),
            bg=color,
            fg="white",
            anchor="w",
            padx=15,
            pady=10
        )

        question_label.pack(fill="x")

        var = tk.StringVar(value="__none__")

        self.vars.append(var)

        for option in question["options"]:

            radio = tk.Radiobutton(
                card,
                text=option,
                variable=var,
                value=option,
                font=("Arial", 12),
                bg="white",
                fg="#333333",
                activebackground="#F5F5F5",
                selectcolor="#E8EAF6",
                anchor="w",
                cursor="hand2"
            )

            radio.pack(
                fill="x",
                padx=25,
                pady=4
            )

        tk.Frame(
            card,
            bg="white",
            height=8
        ).pack()

    # ==================================================
    # SCROLL
    # ==================================================

    def update_scroll_region(self, event=None):

        self.canvas.configure(
            scrollregion=self.canvas.bbox("all")
        )

    def resize_frame(self, event):

        self.canvas.itemconfig(
            self.canvas_window,
            width=event.width
        )

    def mouse_scroll(self, event):

        self.canvas.yview_scroll(
            int(-1 * (event.delta / 120)),
            "units"
        )

    # ==================================================
    # SUBMIT QUIZ
    # ==================================================

    def submit_quiz(self):

        score = 0

        for i, question in enumerate(self.questions):

            if self.vars[i].get() == question["answer"]:

                score += 1

        total_questions = len(self.questions)

        percentage = (
            score / total_questions
        ) * 100

        # Determine result

        if percentage >= 60:

            result = "PASSED"

        else:

            result = "FAILED"

        # ==================================================
        # SAVE QUIZ ATTEMPT
        # ==================================================

        if self.learner_id is not None:

            database.add_quiz_attempt(
                self.learner_id,
                score,
                total_questions,
                percentage,
                result
            )

        # ==================================================
        # PASS
        # ==================================================

        if percentage >= 60:

            messagebox.showinfo(
                "🎉 Quiz Result",
                f"🎉 Congratulations, {self.student_name}!\n\n"
                f"🏆 Score: {score}/{total_questions}\n"
                f"📊 Percentage: {percentage:.0f}%\n\n"
                f"✅ YOU PASSED!\n\n"
                f"Your certificate will now open."
            )

            CertificateWindow(
                self.window,
                self.student_name
            )

        # ==================================================
        # FAIL
        # ==================================================

        else:

            messagebox.showwarning(
                "📚 Quiz Result",
                f"Keep learning, {self.student_name}!\n\n"
                f"📝 Score: {score}/{total_questions}\n"
                f"📊 Percentage: {percentage:.0f}%\n\n"
                f"❌ YOU DID NOT PASS.\n\n"
                f"Please review the course and try again!"
            )

    # ==================================================
    # RESTART
    # ==================================================

    def restart_quiz(self):

        for var in self.vars:

            var.set("")

        self.canvas.yview_moveto(0)

        messagebox.showinfo(
            "🔄 Quiz Restarted",
            "All answers have been cleared.\n\n"
            "Good luck! 🍀"
        )

    # ==================================================
    # CLOSE
    # ==================================================

    def close_window(self):

        self.canvas.unbind_all(
            "<MouseWheel>"
        )

        self.window.destroy()
