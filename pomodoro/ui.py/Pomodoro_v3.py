import os
import platform
import tkinter as tk


class Pomodoro_25v3:

    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro")
        self.root.geometry("300x320")
        self.root.configure(bg="black")

        self.WORK_TIME = 25 * 60
        self.BREAK_TIME = 5 * 60

        self.time_left = self.WORK_TIME
        self.is_running = False
        self.is_work_mode = True
        self.timer_id = None
        self.streak_count = 0

        self.mode_label = tk.Label(
            root, text="FOCUS", font=("Arial", 14, "bold"), fg="white", bg="black"
        )
        self.mode_label.pack(pady=(15, 5))

        self.time_label = tk.Label(
            root, text="25:00", font=("Arial", 44, "bold"), fg="white", bg="black"
        )
        self.time_label.pack(pady=10)

        btn_frame = tk.Frame(root, bg="black")
        btn_frame.pack(pady=10)

        self.start_btn = tk.Button(
            btn_frame,
            text="START",
            width=8,
            fg="white",
            bg="#222222",
            activeforeground="black",
            activebackground="white",
            bd=1,
            relief="solid",
            command=self.toggle,
        )
        self.start_btn.grid(row=0, column=0, padx=5)

        self.reset_btn = tk.Button(
            btn_frame,
            text="RESET",
            width=8,
            fg="white",
            bg="#222222",
            activeforeground="black",
            activebackground="white",
            bd=1,
            relief="solid",
            command=self.reset,
        )
        self.reset_btn.grid(row=0, column=1, padx=5)

        self.streak_label = tk.Label(
            root,
            text="🔥 Streak: 0",
            font=("Arial", 11, "bold"),
            fg="white",
            bg="black",
        )
        self.streak_label.pack(pady=15)

    def play_sound(self):
        system_os = platform.system()
        if system_os == "Windows":
            import winsound

            winsound.Beep(1000, 800)
        elif system_os == "Darwin":
            os.system("afplay /System/Library/Sounds/Glass.aiff")
        else:
            print("\a")

    def toggle(self):
        if self.is_running:
            self.is_running = False
            self.start_btn.config(text="START")
            if self.timer_id:
                self.root.after_cancel(self.timer_id)
        else:
            self.is_running = True
            self.start_btn.config(text="PAUSE")
            self.count_down()

    def count_down(self):
        if not self.is_running:
            return

        mins, secs = divmod(self.time_left, 60)
        self.time_label.config(text=f"{mins:02d}:{secs:02d}")

        if self.time_left > 0:
            self.time_left -= 1
            self.timer_id = self.root.after(1000, self.count_down)
        else:
            self.play_sound()

            if self.is_work_mode:
                self.streak_count += 1
                self.streak_label.config(text=f"🔥 Streak: {self.streak_count}")
                self.is_work_mode = False
                self.time_left = self.BREAK_TIME
                self.mode_label.config(text="BREAK")
            else:
                self.is_work_mode = True
                self.time_left = self.WORK_TIME
                self.mode_label.config(text="FOCUS")

            self.count_down()

    def reset(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        self.is_running = False
        self.is_work_mode = True
        self.time_left = self.WORK_TIME
        self.start_btn.config(text="START")
        self.mode_label.config(text="FOCUS")
        self.time_label.config(text="25:00")


if __name__ == "__main__":
    root = tk.Tk()
    app = Pomodoro_25v3(root)
    root.mainloop()