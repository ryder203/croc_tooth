import customtkinter as ctk  # Import customtkinter for modern GUI
from tkinter import filedialog, messagebox
import subprocess
import sys
import os
import re

# Set appearance and color theme
ctk.set_appearance_mode("Dark")  # Modes: "Dark", "Light", or "System"
ctk.set_default_color_theme("green")  # Use green color theme for consistency

def send_file():
    """Open a file dialog and execute the 'croc send' command for the selected file."""
    file_path = filedialog.askopenfilename(title="Select File")
    
    if file_path:
        try:
            command = f'start cmd /k croc send "{file_path}"'
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to send the file: {e}")

def send_folder():
    """Open a folder dialog and execute the 'croc send' command for the selected folder."""
    folder_path = filedialog.askdirectory(title="Select Folder")
    
    if folder_path:
        try:
            command = f'start cmd /k croc send "{folder_path}"'
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to send the folder: {e}")

def receive_file():
    """Retrieve the receive code from the input field and execute the 'croc receive' command with '--yes' flag."""
    receive_code = receive_code_entry.get().strip()
    receive_code = re.sub(r'\s+', ' ', receive_code)  # Normalize spaces
    
    if receive_code:
        # Ensure the receive code starts with 'croc --yes'
        if not receive_code.startswith('croc'):
            receive_code = f'croc --yes {receive_code}'
        else:
            receive_code = receive_code.replace('croc', 'croc --yes', 1)
        
        try:
            command = f'start cmd /k {receive_code}'
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to open the CLI: {e}")
    else:
        messagebox.showwarning("Warning", "No receive code entered")

def close_application():
    """Terminate the application."""
    app.destroy()

# Create the main application window
app = ctk.CTk()
app.title("croc tooth")
app.geometry("444x404")  # Initial size of the window

# Set the minimum window size to prevent resizing smaller than content
app.minsize(444, 404)

# Determine the path to the icon file
if getattr(sys, 'frozen', False):
    # If running as a bundled executable
    base_path = sys._MEIPASS
else:
    # If running in a standard Python environment
    base_path = os.path.dirname(__file__)

icon_path = os.path.join(base_path, 'icon.ico')

# Set the application icon
try:
    app.iconbitmap(icon_path)
except Exception as e:
    print(f"Failed to load icon: {e}")

# Create and pack the main frame
frame = ctk.CTkFrame(app)
frame.pack(pady=30, padx=30, fill="both", expand=True)

# Button to send files
send_file_button = ctk.CTkButton(
    frame, text="Send file", command=send_file, font=('Arial', 16), width=250
)
send_file_button.pack(pady=(30, 10))  # Extra space above and between buttons

# Button to send folders
send_folder_button = ctk.CTkButton(
    frame, text="Send folder", command=send_folder, font=('Arial', 16), width=250
)
send_folder_button.pack(pady=(10, 10))  # Space between buttons

# Instructions label with larger font size and additional top padding
instructions_label = ctk.CTkLabel(
    frame, text="Enter a receive code and click 'Receive file or folder'", font=('Arial', 14)
)
instructions_label.pack(pady=(20, 5))  # Additional space above the label

# Entry field for the receive code with larger font size
receive_code_entry = ctk.CTkEntry(frame, font=('Arial', 16), width=300)
receive_code_entry.pack(pady=(5, 15))

# Receive button with larger font size and extra bottom padding
receive_button = ctk.CTkButton(
    frame, text="Receive file or folder", command=receive_file, font=('Arial', 16), width=250
)
receive_button.pack(pady=(0, 20))  # Extra space below the button

# Close button with larger font size, more space above, and minimal space below
close_button = ctk.CTkButton(
    frame, text="Close", command=close_application, font=('Arial', 16), width=250, fg_color="#d32f2f"
)
close_button.pack(pady=(20, 5))  # More space above and minimal space below

# Start the Tkinter event loop
app.mainloop()
