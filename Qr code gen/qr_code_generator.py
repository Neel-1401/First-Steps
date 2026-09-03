import tkinter as tk
from tkinter import messagebox, filedialog

import qrcode
from PIL import Image, ImageTk


class QRCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("320x460")
        self.root.configure(bg="black")
        self.current_image = None  # keep a PIL reference for saving

        tk.Label(
            root, text="QR GENERATOR", font=("Arial", 14, "bold"), fg="white", bg="black"
        ).pack(pady=10)

        self.entry = tk.Entry(
            root, width=25, bg="#222222", fg="white", insertbackground="white", bd=1
        )
        self.entry.pack(pady=5)
        self.entry.insert(0, "https://github.com")

        btn_frame = tk.Frame(root, bg="black")
        btn_frame.pack(pady=10)

        tk.Button(
            btn_frame,
            text="GENERATE",
            fg="white",
            bg="#222222",
            bd=1,
            relief="solid",
            command=self.draw_qr,
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            btn_frame,
            text="SAVE",
            fg="white",
            bg="#222222",
            bd=1,
            relief="solid",
            command=self.save_qr,
        ).grid(row=0, column=1, padx=5)

        self.canvas = tk.Canvas(root, width=250, height=250, bg="white", highlightthickness=0)
        self.canvas.pack(pady=10)

        self.draw_qr()

    def draw_qr(self):
        text = self.entry.get().strip()
        if not text:
            messagebox.showwarning("Warning", "Text cannot be empty!")
            return

        # Build a real, spec-compliant QR code (auto-sizes, adds error correction)
        qr = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=2,
        )
        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
        img = img.resize((250, 250), Image.NEAREST)

        self.current_image = img
        self.tk_image = ImageTk.PhotoImage(img)

        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor="nw", image=self.tk_image)

    def save_qr(self):
        if self.current_image is None:
            messagebox.showwarning("Warning", "Generate a QR code first!")
            return
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG image", "*.png")],
            title="Save QR Code As",
        )
        if file_path:
            self.current_image.save(file_path)
            messagebox.showinfo("Saved", f"QR code saved to:\n{file_path}")


if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeApp(root)
    root.mainloop()
