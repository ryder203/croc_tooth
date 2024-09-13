import customtkinter as ctk  # Import customtkinter for modern GUI
from tkinter import filedialog, messagebox
import subprocess
import sys
import os
import re
import locale

# Set appearance and color theme
ctk.set_appearance_mode("Dark")  # Modes: "Dark", "Light", or "System"
ctk.set_default_color_theme("green")  # Use green color theme for consistency

# Translation dictionary for the 14 most spoken languages
translations = {
    'en': {
        'send_file': 'Send file',
        'send_folder': 'Send folder',
        'receive_instructions': (
            'Enter a receive code and click\n'
            '"Receive file or folder"'
        ),
        'receive_button': 'Receive file or folder',
        'close_button': 'Close',
        'warning_no_code': 'No receive code entered',
        'error_failed_send': 'Failed to send the file: ',
        'error_failed_folder': 'Failed to send the folder: ',
        'error_failed_receive': 'Failed to open the CLI: ',
    },
    'zh': {
        'send_file': '发送文件',
        'send_folder': '发送文件夹',
        'receive_instructions': (
            '输入接收代码，然后点击\n'
            '“接收文件或文件夹”'
        ),
        'receive_button': '接收文件或文件夹',
        'close_button': '关闭',
        'warning_no_code': '没有输入接收代码',
        'error_failed_send': '发送文件失败: ',
        'error_failed_folder': '发送文件夹失败: ',
        'error_failed_receive': '打开CLI失败: ',
    },
    'hi': {
        'send_file': 'फ़ाइल भेजें',
        'send_folder': 'फ़ोल्डर भेजें',
        'receive_instructions': (
            'प्राप्त कोड दर्ज करें और\n'
            '"फ़ाइल या फ़ोल्डर प्राप्त करें" पर क्लिक करें'
        ),
        'receive_button': 'फ़ाइल या फ़ोल्डर प्राप्त करें',
        'close_button': 'बंद करें',
        'warning_no_code': 'कोई प्राप्त कोड दर्ज नहीं किया गया',
        'error_failed_send': 'फ़ाइल भेजने में विफल: ',
        'error_failed_folder': 'फ़ोल्डर भेजने में विफल: ',
        'error_failed_receive': 'CLI खोलने में विफल: ',
    },
    'es': {
        'send_file': 'Enviar archivo',
        'send_folder': 'Enviar carpeta',
        'receive_instructions': (
            'Ingrese un código de recepción y haga clic en\n'
            '"Recibir archivo o carpeta"'
        ),
        'receive_button': 'Recibir archivo o carpeta',
        'close_button': 'Cerrar',
        'warning_no_code': 'No se ingresó ningún código de recepción',
        'error_failed_send': 'Error al enviar el archivo: ',
        'error_failed_folder': 'Error al enviar la carpeta: ',
        'error_failed_receive': 'Error al abrir el CLI: ',
    },
    'fr': {
        'send_file': 'Envoyer fichier',
        'send_folder': 'Envoyer dossier',
        'receive_instructions': (
            'Entrez un code de réception et cliquez sur\n'
            '"Recevoir un fichier ou un dossier"'
        ),
        'receive_button': 'Recevoir fichier ou dossier',
        'close_button': 'Fermer',
        'warning_no_code': 'Aucun code de réception saisi',
        'error_failed_send': 'Échec de l\'envoi du fichier: ',
        'error_failed_folder': 'Échec de l\'envoi du dossier: ',
        'error_failed_receive': 'Échec de l\'ouverture du CLI: ',
    },
    'ar': {
        'send_file': 'إرسال ملف',
        'send_folder': 'إرسال مجلد',
        'receive_instructions': (
            'أدخل رمز الاستلام وانقر على\n'
            '"استلام ملف أو مجلد"'
        ),
        'receive_button': 'استلام ملف أو مجلد',
        'close_button': 'إغلاق',
        'warning_no_code': 'لم يتم إدخال رمز الاستلام',
        'error_failed_send': 'فشل في إرسال الملف: ',
        'error_failed_folder': 'فشل في إرسال المجلد: ',
        'error_failed_receive': 'فشل في فتح CLI: ',
    },
    'bn': {
        'send_file': 'ফাইল পাঠান',
        'send_folder': 'ফোল্ডার পাঠান',
        'receive_instructions': (
            'একটি রিসিভ কোড প্রবেশ করুন এবং\n'
            '"ফাইল বা ফোল্ডার গ্রহণ করুন" ক্লিক করুন'
        ),
        'receive_button': 'ফাইল বা ফোল্ডার গ্রহণ করুন',
        'close_button': 'বন্ধ করুন',
        'warning_no_code': 'কোনো রিসিভ কোড প্রবেশ করা হয়নি',
        'error_failed_send': 'ফাইল পাঠাতে ব্যর্থ: ',
        'error_failed_folder': 'ফোল্ডার পাঠাতে ব্যর্থ: ',
        'error_failed_receive': 'CLI খুলতে ব্যর্থ: ',
    },
    'ru': {
        'send_file': 'Отправить файл',
        'send_folder': 'Отправить папку',
        'receive_instructions': (
            'Введите код получения и нажмите\n'
            '"Получить файл или папку"'
        ),
        'receive_button': 'Получить файл или папку',
        'close_button': 'Закрыть',
        'warning_no_code': 'Код получения не введен',
        'error_failed_send': 'Не удалось отправить файл: ',
        'error_failed_folder': 'Не удалось отправить папку: ',
        'error_failed_receive': 'Не удалось открыть CLI: ',
    },
    'pt': {
        'send_file': 'Enviar arquivo',
        'send_folder': 'Enviar pasta',
        'receive_instructions': (
            'Insira um código de recebimento e clique em\n'
            '"Receber arquivo ou pasta"'
        ),
        'receive_button': 'Receber arquivo ou pasta',
        'close_button': 'Fechar',
        'warning_no_code': 'Nenhum código de recebimento inserido',
        'error_failed_send': 'Falha ao enviar o arquivo: ',
        'error_failed_folder': 'Falha ao enviar a pasta: ',
        'error_failed_receive': 'Falha ao abrir o CLI: ',
    },
    'id': {
        'send_file': 'Kirim file',
        'send_folder': 'Kirim folder',
        'receive_instructions': (
            'Masukkan kode penerimaan dan klik\n'
            '"Terima file atau folder"'
        ),
        'receive_button': 'Terima file atau folder',
        'close_button': 'Tutup',
        'warning_no_code': 'Tidak ada kode penerimaan yang dimasukkan',
        'error_failed_send': 'Gagal mengirim file: ',
        'error_failed_folder': 'Gagal mengirim folder: ',
        'error_failed_receive': 'Gagal membuka CLI: ',
    },
    'ur': {
        'send_file': 'فائل بھیجیں',
        'send_folder': 'فولڈر بھیجیں',
        'receive_instructions': (
            'ایک وصول کوڈ درج کریں اور\n'
            '"فائل یا فولڈر وصول کریں" پر کلک کریں'
        ),
        'receive_button': 'فائل یا فولڈر وصول کریں',
        'close_button': 'بند کریں',
        'warning_no_code': 'کوئی وصول کوڈ داخل نہیں کیا گیا',
        'error_failed_send': 'فائل بھیجنے میں ناکام: ',
        'error_failed_folder': 'فولڈر بھیجنے میں ناکام: ',
        'error_failed_receive': 'CLI کھولنے میں ناکام: ',
    },
    'ja': {
        'send_file': 'ファイルを送信',
        'send_folder': 'フォルダを送信',
        'receive_instructions': (
            '受信コードを入力し、\n'
            '「ファイルまたはフォルダを受信」をクリックしてください'
        ),
        'receive_button': 'ファイルまたはフォルダを受信',
        'close_button': '閉じる',
        'warning_no_code': '受信コードが入力されていません',
        'error_failed_send': 'ファイルの送信に失敗しました: ',
        'error_failed_folder': 'フォルダの送信に失敗しました: ',
        'error_failed_receive': 'CLIを開けませんでした: ',
    },
    'de': {
        'send_file': 'Datei senden',
        'send_folder': 'Ordner senden',
        'receive_instructions': (
            'Geben Sie einen Empfangscode ein und\n'
            'klicken Sie auf "Datei oder Ordner empfangen"'
        ),
        'receive_button': 'Datei oder Ordner empfangen',
        'close_button': 'Schließen',
        'warning_no_code': 'Kein Empfangscode eingegeben',
        'error_failed_send': 'Fehler beim Senden der Datei: ',
        'error_failed_folder': 'Fehler beim Senden des Ordners: ',
        'error_failed_receive': 'Fehler beim Öffnen des CLI: ',
    },
    'ko': {
        'send_file': '파일 전송',
        'send_folder': '폴더 전송',
        'receive_instructions': (
            '수신 코드를 입력하고\n'
            '"파일 또는 폴더 받기"를 클릭하세요'
        ),
        'receive_button': '파일 또는 폴더 받기',
        'close_button': '닫기',
        'warning_no_code': '수신 코드가 입력되지 않았습니다',
        'error_failed_send': '파일 전송 실패: ',
        'error_failed_folder': '폴더 전송 실패: ',
        'error_failed_receive': 'CLI 열기 실패: ',
    },
    'vi': {
        'send_file': 'Gửi tệp',
        'send_folder': 'Gửi thư mục',
        'receive_instructions': (
            'Nhập mã nhận và nhấp vào\n'
            '"Nhận tệp hoặc thư mục"'
        ),
        'receive_button': 'Nhận tệp hoặc thư mục',
        'close_button': 'Đóng',
        'warning_no_code': 'Chưa nhập mã nhận',
        'error_failed_send': 'Gửi tệp thất bại: ',
        'error_failed_folder': 'Gửi thư mục thất bại: ',
        'error_failed_receive': 'Mở CLI thất bại: ',
    },
    'pl': {
        'send_file': 'Wyślij plik',
        'send_folder': 'Wyślij folder',
        'receive_instructions': (
            'Wprowadź kod odbioru i kliknij\n'
            '„Odbierz plik lub folder”'
        ),
        'receive_button': 'Odbierz plik lub folder',
        'close_button': 'Zamknij',
        'warning_no_code': 'Nie wprowadzono kodu odbioru',
        'error_failed_send': 'Nie udało się wysłać pliku: ',
        'error_failed_folder': 'Nie udało się wysłać folderu: ',
        'error_failed_receive': 'Nie udało się otworzyć CLI: ',
    },
    'th': {
        'send_file': 'ส่งไฟล์',
        'send_folder': 'ส่งโฟลเดอร์',
        'receive_instructions': (
            'กรอกรหัสรับและคลิก\n'
            '"รับไฟล์หรือโฟลเดอร์"'
        ),
        'receive_button': 'รับไฟล์หรือโฟลเดอร์',
        'close_button': 'ปิด',
        'warning_no_code': 'ไม่มีรหัสรับ',
        'error_failed_send': 'ส่งไฟล์ล้มเหลว: ',
        'error_failed_folder': 'ส่งโฟลเดอร์ล้มเหลว: ',
        'error_failed_receive': 'เปิด CLI ล้มเหลว: ',
    },
}

# Get the default locale
try:
    language_code = locale.getlocale()[0][:2]  # Get the first two letters of the locale code
except Exception as e:
    print(f"Error getting locale: {e}")
    language_code = 'en'  # Default to English if locale detection fails

# Get the translations for the detected language or fall back to English
current_translations = translations.get(language_code, translations['en'])

def send_file():
    """Open a file dialog and execute the 'croc send' command for the selected file."""
    file_path = filedialog.askopenfilename(title="Select File")
    
    if file_path:
        try:
            command = f'start cmd /k croc send "{file_path}"'
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", current_translations['error_failed_send'] + str(e))

def send_folder():
    """Open a folder dialog and execute the 'croc send' command for the selected folder."""
    folder_path = filedialog.askdirectory(title="Select Folder")
    
    if folder_path:
        try:
            command = f'start cmd /k croc send "{folder_path}"'
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", current_translations['error_failed_folder'] + str(e))

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
            messagebox.showerror("Error", current_translations['error_failed_receive'] + str(e))
    else:
        messagebox.showwarning("Warning", current_translations['warning_no_code'])

def close_application():
    """Terminate the application."""
    app.destroy()

# Create the main application window
app = ctk.CTk()
app.title("croc tooth")
app.geometry("444x404")  # Initial size of the window
app.minsize(444, 404)  # Set the minimum window size to prevent resizing smaller than content

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
    frame, text=current_translations['send_file'], command=send_file, font=('Arial', 16), width=250
)
send_file_button.pack(pady=(30, 10))  # Extra space above and between buttons

# Button to send folders
send_folder_button = ctk.CTkButton(
    frame, text=current_translations['send_folder'], command=send_folder, font=('Arial', 16), width=250
)
send_folder_button.pack(pady=(10, 10))  # Space between buttons

# Instructions label with larger font size and additional top padding
instructions_label = ctk.CTkLabel(
    frame, text=current_translations['receive_instructions'], font=('Arial', 14)
)
instructions_label.pack(pady=(20, 5))  # Additional space above the label

# Entry field for the receive code with larger font size
receive_code_entry = ctk.CTkEntry(frame, font=('Arial', 16), width=300)
receive_code_entry.pack(pady=(5, 15))

# Receive button with larger font size and extra bottom padding
receive_button = ctk.CTkButton(
    frame, text=current_translations['receive_button'], command=receive_file, font=('Arial', 16), width=250
)
receive_button.pack(pady=(0, 20))  # Extra space below the button

# Close button with larger font size, more space above, and minimal space below
close_button = ctk.CTkButton(
    frame, text=current_translations['close_button'], command=close_application, font=('Arial', 16), width=250, fg_color="#d32f2f"
)
close_button.pack(pady=(20, 5))  # More space above and minimal space below

# Start the Tkinter event loop
app.mainloop()
