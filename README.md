
![croc tooth banner](https://github.com/ryder203/croc_tooth/blob/main/res/promo/header.png?raw=true)

# For Windows only

Croc tooth is for Microsoft Windows OS only, written in Python and compiled with AutoPyToExe.<br>
Croc itself is available for various OS.

# Screenshot

![Demo Preview](https://github.com/ryder203/croc_tooth/blob/main/res/promo/screenshot_croc_tooth.png?raw=true)

Croc tooth is a graphical user interface (GUI) for the "croc" command-line tool,<br>designed to simplify secure file transfers between devices.<br>
It was created to have a GUI to do the most basic thing croc does - sending a file or receiving it, nothing more.<br>
Overall, the app makes using the "croc" tool more convenient by <br>providing a visual interface for secure file sharing.<br><br>

# Installation

Not needed. Just copy croc_tooth.exe next to latest croc.exe.<br>
Croc can be found here:<br>
https://github.com/schollz/croc/releases
<br>
<br>

# Graphical user interface languages

- English (en)
- Chinese (Simplified) (zh)
- Hindi (hi)
- Spanish (es)
- French (fr)
- Arabic (ar)
- Bengali (bn)
- Russian (ru)
- Portuguese (pt)
- Indonesian (id)
- Urdu (ur)
- Japanese (ja)
- German (de)
- Korean (ko)

# Usage

1. **Open the App:**
   - Launch the "croc tooth" application. The main window will appear with options to send or receive files.

2. **Send a File:**
   - Click on the **"Send File"** button.
   - A file dialog will open. Select the file you want to send.
   - The app will execute the `croc send` command in the background to securely send the file. A terminal window will open, displaying a unique code for the transfer.
   - Share this code with the person you want to receive the file.
   - **Important:** Keep the terminal window open and active until the file transfer is complete.

3. **Receive a File:**
   - Get the unique code from the sender.
   - Enter the code in the text field labeled "Enter a receive code."
   - Click the **"Receive File"** button.
   - The app will execute the `croc receive` command with the provided code, and a terminal window will open to show the progress of the file transfer.
   - **Important:** Keep the terminal window open and active while the file is being received.

4. **Close the App:**
   - To exit the app, simply click the **"Close"** button.

Both users need to keep the "croc" tool active throughout the entire process to ensure a successful file transfer.

# Stats

![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/ryder203/croc_tooth/total?style=flat&label=Downloads%20all%20releases&labelColor=%2366bb6a)
<br>
![GitHub Downloads (all assets, latest release)](https://img.shields.io/github/downloads/ryder203/croc_tooth/latest/total?style=flat&label=Downloads%20latest%20release&labelColor=%2326a69a)

# License

MIT License

Copyright (c) 2024 t-ryder

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

