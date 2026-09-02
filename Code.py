import threading
import time
import tkinter as tk
import urllib.request


class InternetSpeedometer:
    def __init__(self, root):
        self.root = root
        self.root.title("Speedometer")
        self.root.geometry("280x220")
        self.root.configure(bg="black")

        tk.Label(
            root, text="SPEED TEST", font=("Arial", 12, "bold"), fg="white", bg="black"
        ).pack(pady=(15, 5))

        self.speed_label = tk.Label(
            root, text="-- Mbps", font=("Arial", 28, "bold"), fg="white", bg="black"
        )
        self.speed_label.pack(pady=10)

        self.status_label = tk.Label(
            root, text="Click Start to test", font=("Arial", 9), fg="#888888", bg="black"
        )
        self.status_label.pack(pady=5)

        self.test_btn = tk.Button(
            root,
            text="START TEST",
            fg="white",
            bg="#222222",
            bd=1,
            relief="solid",
            command=self.start_test_thread,
        )
        self.test_btn.pack(pady=10)

    def start_test_thread(self):
        self.test_btn.config(state="disabled")
        self.status_label.config(text="Testing download speed...")
        self.speed_label.config(text="... Mbps")
        # Run network test in a background thread to prevent UI freezing
        threading.Thread(target=self.run_speed_test, daemon=True).start()

    def run_speed_test(self):
        # 10MB test payload file link
        url = "http://speedtest.tele2.net/10MB.zip"
        start_time = time.time()
        received_bytes = 0
        try:
            req = urllib.request.urlopen(url, timeout=10)
            while True:
                chunk = req.read(1024 * 32)
                if not chunk:
                    break
                received_bytes += len(chunk)
            elapsed_time = time.time() - start_time
            megabits = (received_bytes * 8) / (1024 * 1024)
            mbps = megabits / elapsed_time if elapsed_time > 0 else 0
            self.root.after(0, self.update_results, f"{mbps:.2f} Mbps", "Test Complete")
        except Exception:
            self.root.after(0, self.update_results, "Error", "Connection Failed")

    def update_results(self, speed_text, status_text):
        self.speed_label.config(text=speed_text)
        self.status_label.config(text=status_text)
        self.test_btn.config(state="normal")


if __name__ == "__main__":
    root = tk.Tk()
    app = InternetSpeedometer(root)
    root.mainloop()