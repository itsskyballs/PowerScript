import tkinter as tk
from tkinter import messagebox
import os
import tempfile

def show_description(description):
    description_label.config(text="Description: " + description)

def hide_description():
    description_label.config(text="")

def shutdown():
    result = messagebox.askyesno("Shutdown", "Are you sure you want to shut down the computer?")
    if result:
        os.system("shutdown /s /t 0")

def restart():
    result = messagebox.askyesno("Restart", "Are you sure you want to restart the computer?")
    if result:
        os.system("shutdown /r /t 0")

def sleep():
    try:
        os.system("rundll32.exe powrprof.dll,SetSuspendState Sleep")  # Put the computer to sleep
    except Exception as e:
        messagebox.showerror("Error", "Cannot execute sleep mode: " + str(e))

def hibernate():
    # Implement hibernate operation (platform-specific)
    pass

def slide_to_shutdown():
    if os.name == "nt" and os.sys.getwindowsversion().major >= 6:
        os.system("slidetoshutdown")  # Initiate Slide to Shutdown
    else:
        messagebox.showerror("Error", "Slide to Shutdown is not available for Windows 7.")

def open_advanced_boot_options():
    result = messagebox.askyesno("Advanced Boot Options", "Initiate Advanced Boot Option? No restart needed")
    if result:
        os.system("shutdown /o")  # Open Advanced Boot Options

def open_remote_shutdown_dialog():
    os.system("shutdown /i")  # Open Remote Shutdown Dialog

def log_out():
    result = messagebox.askyesno("Log Out", "Are you sure you want to log out?")
    if result:
        os.system("shutdown -l")  # Log Out

def about_os():
    os.system("winver")

def open_full_code():
    code = '''
import tkinter as tk
from tkinter import messagebox
import os
import tempfile

def show_description(description):
    description_label.config(text="Description: " + description)

def hide_description():
    description_label.config(text="")

def shutdown():
    result = messagebox.askyesno("Shutdown", "Are you sure you want to shut down the computer?")
    if result:
        os.system("shutdown /s /t 0")

def restart():
    result = messagebox.askyesno("Restart", "Are you sure you want to restart the computer?")
    if result:
        os.system("shutdown /r /t 0")

def sleep():
    try:
        os.system("rundll32.exe powrprof.dll,SetSuspendState Sleep")  # Put the computer to sleep
    except Exception as e:
        messagebox.showerror("Error", "Cannot execute sleep mode: " + str(e))

def hibernate():
    # Implement hibernate operation (platform-specific)
    pass

def slide_to_shutdown():
    if os.name == "nt" and os.sys.getwindowsversion().major >= 6:
        os.system("slidetoshutdown")  # Initiate Slide to Shutdown
    else:
        messagebox.showerror("Error", "Slide to Shutdown is not available for Windows 7.")

def open_advanced_boot_options():
    result = messagebox.askyesno("Advanced Boot Options", "Initiate Advanced Boot Option? No restart needed")
    if result:
        os.system("shutdown /o")  # Open Advanced Boot Options

def open_remote_shutdown_dialog():
    os.system("shutdown /i")  # Open Remote Shutdown Dialog

def log_out():
    result = messagebox.askyesno("Log Out", "Are you sure you want to log out?")
    if result:
        os.system("shutdown -l")  # Log Out

def about_os():
    os.system("winver")

def open_full_code():
   Code Forbidden due to missing part of the code

def fade_out_buttons():
    for button in power_buttons:
        button.pack_forget()

def fade_in_buttons():
    for button in power_buttons:
        button.pack(pady=5)

def toggle_submenu():
    if submenu_frame.winfo_ismapped():
        fade_in_buttons()  # Fade in power buttons
        submenu_frame.pack_forget()
        root.update()  # Update the window
    else:
        fade_out_buttons()  # Fade out power buttons
        submenu_frame.pack()
        root.update()  # Update the window

root = tk.Tk()
root.title("PowerScript Beta")
root.geometry("800x600")  # Set the window size to 800x600 pixels
root.resizable(False, False)  # Disable resizing and maximize button

background_color = "#2c3e50"  # Set the background color
root.configure(bg=background_color)

description_label = tk.Label(root, text="", font=("Arial", 12), bg=background_color, fg="white")
description_label.pack(pady=10)

buttons_frame = tk.Frame(root, bg=background_color)
buttons_frame.pack(pady=20)

def create_rounded_button(parent, label, context, action):
    button = tk.Button(parent, text=label, command=action, font=("Arial", 10, "bold"), bg="#3498db", fg="white", padx=20, pady=10, relief="flat", borderwidth=2)
    button.config(cursor="hand2", activebackground="#2980b9")
    button.bind("<Enter>", lambda event, context=context: show_description(context))
    button.bind("<Leave>", lambda event: hide_description())
    return button

# Other Buttons
power_buttons = [
    create_rounded_button(buttons_frame, "Shutdown", "Shuts down the computer. Click to initiate a system shutdown.", shutdown),
    create_rounded_button(buttons_frame, "Restart", "Restarts the computer. Click to initiate a system restart.", restart),
    create_rounded_button(buttons_frame, "Sleep", "Puts the computer to sleep. Click to enter sleep mode.", sleep),
    create_rounded_button(buttons_frame, "Hibernate", "Puts the computer into hibernation. Click to enter hibernation mode.", hibernate),
    create_rounded_button(buttons_frame, "Log Out", "Logs out the current user. Click to log out.", log_out)
]

for button in power_buttons:
    button.pack(pady=5)

software_version_label = tk.Label(root, text="Software Version: 1.0.7exebeta", font=("Arial", 8), bg=background_color, fg="white")
software_version_label.pack(side="left", padx=10, pady=5, anchor="sw")

# Create More Options Button (Bottom Right)
more_options_button = create_rounded_button(root, "More Options", "More Windows things", toggle_submenu)
more_options_button.pack(side="bottom", padx=10, pady=10, anchor="se")

about_os_button = create_rounded_button(root, "About Your OS", "Open the About Your OS dialog.", about_os)
about_os_button.pack(side="bottom", padx=10, pady=10, anchor="se")

full_code_button = create_rounded_button(root, "Full Code", "Open the Full Code in Notepad", open_full_code)
full_code_button.pack(side="bottom", padx=10, pady=10, anchor="se")

submenu_frame = tk.Frame(buttons_frame, bg=background_color)

# Create Submenu Buttons
submenu_buttons = [
    create_rounded_button(submenu_frame, "Advanced Boot Option", "Access Windows Advanced Boot Options Menu. Click to access advanced boot options.", open_advanced_boot_options),
    create_rounded_button(submenu_frame, "Remote Shutdown Dialog", "Open the Remote Shutdown Dialog. Click to initiate remote shutdown.", open_remote_shutdown_dialog),
    create_rounded_button(submenu_frame, "Slide to Shutdown", "Initiate Slide to Shutdown feature.", slide_to_shutdown)
]

for button in submenu_buttons:
    button.pack(pady=5)

root.mainloop()



    '''
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".py")
    with open(temp_file.name, "w") as f:
        f.write(code)
    os.system(f'notepad.exe {temp_file.name}')

def fade_out_buttons():
    for button in power_buttons:
        button.pack_forget()

def fade_in_buttons():
    for button in power_buttons:
        button.pack(pady=5)

def toggle_submenu():
    if submenu_frame.winfo_ismapped():
        fade_in_buttons()  # Fade in power buttons
        submenu_frame.pack_forget()
        root.update()  # Update the window
    else:
        fade_out_buttons()  # Fade out power buttons
        submenu_frame.pack()
        root.update()  # Update the window

root = tk.Tk()
root.title("PowerScript Beta")
root.geometry("800x600")  # Set the window size to 800x600 pixels
root.resizable(False, False)  # Disable resizing and maximize button

background_color = "#2c3e50"  # Set the background color
root.configure(bg=background_color)

description_label = tk.Label(root, text="", font=("Arial", 12), bg=background_color, fg="white")
description_label.pack(pady=10)

buttons_frame = tk.Frame(root, bg=background_color)
buttons_frame.pack(pady=20)

def create_rounded_button(parent, label, context, action):
    button = tk.Button(parent, text=label, command=action, font=("Arial", 10, "bold"), bg="#3498db", fg="white", padx=20, pady=10, relief="flat", borderwidth=2)
    button.config(cursor="hand2", activebackground="#2980b9")
    button.bind("<Enter>", lambda event, context=context: show_description(context))
    button.bind("<Leave>", lambda event: hide_description())
    return button

# Other Buttons
power_buttons = [
    create_rounded_button(buttons_frame, "Shutdown", "Shuts down the computer. Click to initiate a system shutdown.", shutdown),
    create_rounded_button(buttons_frame, "Restart", "Restarts the computer. Click to initiate a system restart.", restart),
    create_rounded_button(buttons_frame, "Sleep", "Puts the computer to sleep. Click to enter sleep mode.", sleep),
    create_rounded_button(buttons_frame, "Hibernate", "Puts the computer into hibernation. Click to enter hibernation mode.", hibernate),
    create_rounded_button(buttons_frame, "Log Out", "Logs out the current user. Click to log out.", log_out)
]

for button in power_buttons:
    button.pack(pady=5)

software_version_label = tk.Label(root, text="Software Version: 1.0.7exebeta", font=("Arial", 8), bg=background_color, fg="white")
software_version_label.pack(side="left", padx=10, pady=5, anchor="sw")

# Create More Options Button (Bottom Right)
more_options_button = create_rounded_button(root, "More Options", "More Windows things", toggle_submenu)
more_options_button.pack(side="bottom", padx=10, pady=10, anchor="se")

about_os_button = create_rounded_button(root, "About Your OS", "Open the About Your OS dialog.", about_os)
about_os_button.pack(side="bottom", padx=10, pady=10, anchor="se")

full_code_button = create_rounded_button(root, "Full Code", "Open the Full Code in Notepad", open_full_code)
full_code_button.pack(side="bottom", padx=10, pady=10, anchor="se")

submenu_frame = tk.Frame(buttons_frame, bg=background_color)

# Create Submenu Buttons
submenu_buttons = [
    create_rounded_button(submenu_frame, "Advanced Boot Option", "Access Windows Advanced Boot Options Menu. Click to access advanced boot options.", open_advanced_boot_options),
    create_rounded_button(submenu_frame, "Remote Shutdown Dialog", "Open the Remote Shutdown Dialog. Click to initiate remote shutdown.", open_remote_shutdown_dialog),
    create_rounded_button(submenu_frame, "Slide to Shutdown", "Initiate Slide to Shutdown feature.", slide_to_shutdown)
]

for button in submenu_buttons:
    button.pack(pady=5)

root.mainloop()


