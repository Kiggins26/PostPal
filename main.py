import tkinter as tk
from tkinter import filedialog

from utils import get_image_files

class MyApp:
    def __init__(self, master):
        self.master = master
        self.master.title("File Selector App")

        # Dracula color scheme
        bg_color = "#282a36"
        fg_color = "#f8f8f2"
        button_bg = "#6272a4"
        button_fg = "#f8f8f2"

        # Set root background color
        self.master.configure(bg=bg_color)

        # Logo
        self.logo_image = tk.PhotoImage(file="logo.png")  # Replace "your_logo.png" with your actual image file
        self.logo_image = self.logo_image.subsample(2, 2)  # Adjust the subsample factors as needed
        self.logo_label = tk.Label(master, image=self.logo_image, bg=bg_color)
        self.logo_label.pack(pady=10)

        # Title and Slogan
        self.title_label = tk.Label(master, text="PostPal", font=("Helvetica", 16, "bold"), fg=fg_color, bg=bg_color)
        self.title_label.pack(pady=5)

        self.slogan_label = tk.Label(master, text="We'll handle it in post", font=("Helvetica", 12, "italic"), fg=fg_color, bg=bg_color)
        self.slogan_label.pack(pady=10)

        # Frames for better organization
        self.top_frame = tk.Frame(master, bg=bg_color)
        self.top_frame.pack(pady=10)

        self.middle_frame = tk.Frame(master, bg=bg_color)
        self.middle_frame.pack(pady=10)

        self.bottom_frame = tk.Frame(master, bg=bg_color)
        self.bottom_frame.pack(pady=10)

        # Widgets in the top frame
        self.file_path_label = tk.Label(self.top_frame, text="Selected File/Directory:", fg=fg_color, bg=bg_color)
        self.file_path_label.grid(row=0, column=0, sticky='w', padx=10)

        self.file_path_var = tk.StringVar()
        self.file_path_entry = tk.Entry(self.top_frame, textvariable=self.file_path_var, state='disabled', width=40, fg=fg_color, bg=bg_color)
        self.file_path_entry.grid(row=0, column=1, padx=10)

        self.browse_button = tk.Button(self.top_frame, text="Browse", command=self.browse_file, bg=button_bg, fg=button_fg)
        self.browse_button.grid(row=0, column=2, padx=10)

        # Widgets in the middle frame
        self.ranking_checkbox_var = tk.BooleanVar()
        self.ranking_checkbox_checkbox = tk.Checkbutton(self.middle_frame, text="Rank Photos", variable=self.ranking_checkbox_var, fg=fg_color, bg=bg_color)
        self.ranking_checkbox_checkbox.pack(side='left', padx=10)

        # Widgets in the bottom frame
        self.finddup_var = tk.BooleanVar()
        self.finddup = tk.Checkbutton(self.middle_frame, text="Find Duplicates", variable=self.finddup_var, fg=fg_color, bg=bg_color)
        self.finddup.pack(side='left', padx=10)

        self.autoedit_var = tk.BooleanVar()
        self.autoedit = tk.Checkbutton(self.middle_frame, text="Edit with AI", variable=self.autoedit_var, fg=fg_color, bg=bg_color)
        self.autoedit.pack(side='left', padx=10)

        self.submit_button = tk.Button(self.bottom_frame, text="Submit", command=self.submit, bg=button_bg, fg=button_fg)
        self.submit_button.pack(pady=10)

    def browse_file(self):
        file_path = filedialog.askdirectory()  # You can use askdirectory() for directories
        if file_path:
            self.file_path_var.set(file_path)

    def submit(self):
        selected_path = self.file_path_var.get()
        ranking_checkbox = self.ranking_checkbox_var.get()
        finddup_state = self.finddup_var.get()
        autoedit_state = self.autoedit_var.get()
        image_paths = get_image_files(selected_path)


        print(f"Selected Path: {selected_path}")
        print(f"Toggle Dots: {ranking_checkbox}")
        print(f"Checkbutton 1 State: {finddup_state}")
        print(f"Checkbutton 2 State: {autoedit_state}")
        print(f"images: {image_paths}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()

