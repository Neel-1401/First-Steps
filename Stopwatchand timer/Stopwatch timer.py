import os
import platform
import tkinter as tk


class TimeTools:

    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch & Timer")
        self.root.geometry("340x380")
        self.root.configure(bg="black")

        self.mode = "STOPWATCH"  # "STOPWATCH" or "TIMER"
        self.is_running = False
        self.timer_id = None

        # Stopwatch state (tenths of seconds)
        self.sw_elapsed = 0

        # Timer state (seconds)
        self.tm_seconds = 300  # Default 5 minutes

        # Mode Selection
        mode_frame = tk.Frame(self.root, bg="black")
        mode_frame.pack(pady=10)

        self.sw_mode_btn = tk.Button(
            mode_frame,
            text="Stopwatch",
            fg="black",
            bg="white",
            width=10,
            command=self.set_stopwatch_mode,
        )
        self.sw_mode_btn.grid(row=0, column=0, padx=5)

        self.tm_mode_btn = tk.Button(
            mode_frame,
            text="Timer",
            fg="white",
            bg="#222222",
            width=10,
            command=self.set_timer_mode,
        )
        self.tm_mode_btn.grid(row=0, column=1, padx=5)

        # Time Display
        self.display_label = tk.Label(
            self.root, text="00:00.0", font=("Arial", 40, "bold"), fg="white", bg="black"
        )
        self.display_label.pack(pady=20)

        # Controls
        btn_frame = tk.Frame(self.root, bg="black")
        btn_frame.pack(pady=10)

        self.start_btn = tk.Button(
            btn_frame,
            text="START",
            width=8,
            fg="white",
            bg="#222222",
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
            bd=1,
            relief="solid",
            command=self.reset,
        )
        self.reset_btn.grid(row=0, column=1, padx=5)

        # Timer Adjustment Controls
        self.adj_frame = tk.Frame(self.root, bg="black")
        tk.Button(
            self.adj_frame,
            text="-1m",
            fg="white",
            bg="#222222",
            command=lambda: self.adjust_timer(-60),
        ).grid(row=0, column=0, padx=2)
        tk.Button(
            self.adj_frame,
            text="-10s",
            fg="white",
            bg="#222222",
            command=lambda: self.adjust_timer(-10),
        ).grid(row=0, column=1, padx=2)
        tk.Button(
            self.adj_frame,
            text="+10s",
            fg="white",
            bg="#222222",
            command=lambda: self.adjust_timer(10),
        ).grid(row=0, column=2, padx=2)
        tk.Button(
            self.adj_frame,
            text="+1m",
            fg="white",
            bg="#222222",
            command=lambda: self.adjust_timer(60),
        ).grid(row=0, column=3, padx=2)

    def play_sound(self):
        sys_os = platform.system()
        if sys_os == "Windows":
            import winsound

            winsound.Beep(1000, 800)
        elif sys_os == "Darwin":
            os.system("afplay /System/Library/Sounds/Glass.aiff")
        else:
            print("\a")

    def set_stopwatch_mode(self):
        self.reset()
        self.mode = "STOPWATCH"
        self.sw_mode_btn.config(bg="white", fg="black")
        self.tm_mode_btn.config(bg="#222222", fg="white")
        self.adj_frame.pack_forget()
        self.update_display()

    def set_timer_mode(self):
        self.reset()
        self.mode = "TIMER"
        self.tm_mode_btn.config(bg="white", fg="black")
        self.sw_mode_btn.config(bg="#222222", fg="white")
        self.adj_frame.pack(pady=10)
        self.update_display()

    def toggle(self):
        if self.is_running:
            self.is_running = False
            self.start_btn.config(text="START")
            if self.timer_id:
                self.root.after_cancel(self.timer_id)
        else:
            self.is_running = True
            self.start_btn.config(text="PAUSE")
            self.tick()

    def tick(self):
        if not self.is_running:
            return

        if self.mode == "STOPWATCH":
            self.sw_elapsed += 1
            self.update_display()
            self.timer_id = self.root.after(100, self.tick)
        else:
            if self.tm_seconds > 0:
                self.tm_seconds -= 1
                self.update_display()
                self.timer_id = self.root.after(1000, self.tick)
            else:
                self.is_running = False
                self.start_btn.config(text="START")
                self.play_sound()

    def reset(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        self.is_running = False
        self.start_btn.config(text="START")
        if self.mode == "STOPWATCH":
            self.sw_elapsed = 0
        else:
            self.tm_seconds = 300
        self.update_display()

    def adjust_timer(self, amount):
        if not self.is_running and self.mode == "TIMER":
            self.tm_seconds = max(0, self.tm_seconds + amount)
            self.update_display()

    def update_display(self):
        if self.mode == "STOPWATCH":
            mins, remainder = divmod(self.sw_elapsed, 600)
            secs, tenths = divmod(remainder, 10)
            self.display_label.config(text=f"{mins:02d}:{secs:02d}.{tenths}")
        else:
            mins, secs = divmod(self.tm_seconds, 60)
            self.display_label.config(text=f"{mins:02d}:{secs:02d}")


if __name__ == "__main__":
    root = tk.Tk()
    app = TimeTools(root)
    root.mainloop()