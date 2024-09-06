import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import sys
import os
import re

# Colors in shades of green
colors = {
    'background': '#66bb6a',     # Light green
    'button': '#43a047',         # Green
    'button_hover': '#4caf50',   # Light green for hover
    'button_active': '#2e7d32',  # Dark green for button press
    'text': '#1b5e20'            # Very dark green
}

def send_file():
    # Open a file dialog to select a file
    file_path = filedialog.askopenfilename()
    
    if file_path:  # If a file is selected
        try:
            # Execute the 'croc send' command in a new CMD console
            command = f'start cmd /k croc send "{file_path}"'
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to send the file: {e}")

def receive_file():
    receive_code = receive_code_entry.get().strip()
    
    # Normalize internal spaces
    receive_code = re.sub(r'\s+', ' ', receive_code)
    
    if receive_code:
        # Check if the code starts with "croc", otherwise prepend it
        if not receive_code.startswith('croc'):
            receive_code = f'croc {receive_code}'
        
        try:
            # Open a new CMD window and execute the receive command
            command = f'start cmd /k {receive_code}'
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to open the CLI: {e}")
    else:
        messagebox.showwarning("Warning", "No receive code entered")

def close_application():
    root.destroy()

def on_enter(e):
    e.widget['background'] = colors['button_hover']  # Use light green for hover

def on_leave(e):
    e.widget['background'] = colors['button']  # Return to default green

# Create the main application window
root = tk.Tk()
root.title("croc tooth")  # Set the title of the GUI
root.configure(bg=colors['background'])

# Set a fixed size for the window with extra space
window_width = 420
window_height = 240  # Increased height to accommodate top and bottom padding
root.geometry(f"{window_width}x{window_height}")

# Create and place the buttons with hover and active background properties
send_button = tk.Button(
    root, text="Send File", command=send_file, bg=colors['button'], fg='white', 
    font=('Arial', 12), activebackground=colors['button_active'], activeforeground='white'
)
send_button.pack(pady=(15, 5), fill='x', padx=20)  # Add top padding
send_button.bind("<Enter>", on_enter)
send_button.bind("<Leave>", on_leave)

# Create and place the text label above the text input field
instructions_label = tk.Label(root, text="Enter a receive code and click 'Receive File'", bg=colors['background'], fg=colors['text'], font=('Arial', 12))
instructions_label.pack(pady=5, padx=20)

# Create and place the text input field for receive code
receive_code_entry = tk.Entry(root, font=('Arial', 12))
receive_code_entry.pack(pady=5, padx=20, fill='x')

# Create and place the receive file button below the text input field
receive_button = tk.Button(
    root, text="Receive File", command=receive_file, bg=colors['button'], fg='white', 
    font=('Arial', 12), activebackground=colors['button_active'], activeforeground='white'
)
receive_button.pack(pady=5, fill='x', padx=20)
receive_button.bind("<Enter>", on_enter)
receive_button.bind("<Leave>", on_leave)

# Create and place the close button at the bottom
close_button = tk.Button(
    root, text="Close", command=close_application, bg=colors['button'], fg='white', 
    font=('Arial', 12), activebackground=colors['button_active'], activeforeground='white'
)
close_button.pack(pady=(5, 15), fill='x', padx=20, side='bottom')  # Add bottom padding
close_button.bind("<Enter>", on_enter)
close_button.bind("<Leave>", on_leave)

# Determine the path to the resource
if getattr(sys, 'frozen', False):
    # Running in a bundle
    base_path = sys._MEIPASS
else:
    # Running in a normal Python environment
    base_path = os.path.dirname(__file__)

icon_path = os.path.join(base_path, 'icon.ico')
root.iconbitmap(icon_path)  # Use the variable, not the string

# Start the main event loop
root.mainloop()
