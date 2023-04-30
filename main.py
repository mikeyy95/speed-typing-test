import tkinter as tk
import time

class SpeedTypingTester(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()
        self.word_list = ["hello", "world", "python", "programming", "computer", "science", "data", "analysis", "machine", "learning"]
        self.current_word = None
        self.correct_count = 0
        self.total_count = 0
        self.start_time = None
        self.time_label = tk.Label(self, text="Time: 0 seconds")
        self.time_label.grid(row=3, column=0, columnspan=2)
        self.pack()

    def create_widgets(self):
        self.instruction_label = tk.Label(self, text="Type the word below:")
        self.instruction_label.grid(row=0, column=0)
        self.word_label = tk.Label(self, text="")
        self.word_label.grid(row=1, column=0)
        self.input_box = tk.Entry(self)
        self.input_box.grid(row=2, column=0)
        self.start_button = tk.Button(self, text="Start", command=self.start_test)
        self.start_button.grid(row=2, column=1)

    def start_test(self):
        self.input_box.delete(0, tk.END)
        self.input_box.focus()
        self.start_button.config(state=tk.DISABLED)
        self.current_word = self.word_list.pop(0)
        self.word_label.config(text=self.current_word)
        self.start_time = time.time()
        self.master.bind('<Return>', self.check_word)

    def check_word(self, event):
        input_word = self.input_box.get().strip()
        self.input_box.delete(0, tk.END)
        if input_word == self.current_word:
            self.correct_count += 1
        self.total_count += 1
        if len(self.word_list) > 0:
            self.current_word = self.word_list.pop(0)
            self.word_label.config(text=self.current_word)
        else:
            self.master.unbind('<Return>')
            self.end_test()

    def end_test(self):
        self.time_label.config(text="Time: {} seconds".format(round(time.time()-self.start_time)))
        accuracy = round(self.correct_count/self.total_count*100, 2)
        result_message = "Accuracy: {}%\nTotal words: {}\nCorrect words: {}\nIncorrect words: {}".format(
            accuracy, self.total_count, self.correct_count, self.total_count-self.correct_count)
        result_label = tk.Label(self, text=result_message)
        result_label.grid(row=4, column=0, columnspan=2)

root = tk.Tk()
root.title("Speed Typing Tester")
app = SpeedTypingTester(master=root)
app.mainloop()
