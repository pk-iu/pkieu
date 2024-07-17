import tkinter as tk

def update_status(status):
    pause_status.pack_forget()
    start_status.pack_forget()
    end_status.pack_forget()
    if status == "pause":
        pause_status.pack(pady=5)
    elif status == "start":
        start_status.pack(pady=5)
    elif status == "end":
        end_status.pack(pady=5)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Frame Recorder")
root.geometry("600x300")
root.configure(bg='#e9a9e0')

# Tạo nhãn tiêu đề
title_label = tk.Label(root, text="Frame Recorder", font=("Helvetica", 24), bg='#e9a9e0')
title_label.pack(pady=20)

# Tạo khung cho đầu vào FPS
fps_frame = tk.Frame(root, bg='#e9a9e0')
fps_frame.pack(pady=10)

fps_label = tk.Label(fps_frame, text="create an", font=("Helvetica", 12), bg='#e9a9e0')
fps_label.pack(side=tk.LEFT)

fps_entry = tk.Entry(fps_frame, width=5, font=("Helvetica", 12))
fps_entry.pack(side=tk.LEFT, padx=5)
fps_entry.insert(0, "100")

fps_label_2 = tk.Label(fps_frame, text="fps video", font=("Helvetica", 12), bg='#e9a9e0')
fps_label_2.pack(side=tk.LEFT)

# Tạo khung cho các nút
button_frame = tk.Frame(root, bg='#e9a9e0')
button_frame.pack(pady=20)

pause_button = tk.Button(button_frame, text="Pause", font=("Helvetica", 12), 
                         command=lambda: update_status("pause"))
pause_button.pack(side=tk.LEFT, padx=10)

start_button = tk.Button(button_frame, text="Start", font=("Helvetica", 12), 
                         command=lambda: update_status("start"))
start_button.pack(side=tk.LEFT, padx=10)

end_button = tk.Button(button_frame, text="End", font=("Helvetica", 12), 
                       command=lambda: update_status("end"))
end_button.pack(side=tk.LEFT, padx=10)

# Tạo nhãn trạng thái cho từng nút
pause_status = tk.Label(root, text="Recording Paused", font=("Helvetica", 12), bg='#e9a9e0')
start_status = tk.Label(root, text="Recording Started", font=("Helvetica", 12), bg='#e9a9e0')
end_status = tk.Label(root, text="Recording Ended", font=("Helvetica", 12), bg='#e9a9e0')

# Bắt đầu vòng lặp sự kiện chính
root.mainloop()
