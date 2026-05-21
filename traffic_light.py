import tkinter as tk

class TrafficLight:
    def __init__(self, root):
        self.root = root
        self.root.title("紅綠燈 GUI")
        self.root.geometry("200x450")
        self.root.configure(bg="#f0f0f0")

        # 建立畫布來繪製紅綠燈
        self.canvas = tk.Canvas(root, width=150, height=400, bg="#f0f0f0", highlightthickness=0)
        self.canvas.pack(pady=20)

        # 畫紅綠燈的黑色外框
        self.canvas.create_rectangle(25, 25, 125, 375, fill="#333333", outline="black", width=2)

        # 建立三個燈 (預設為暗色)
        self.red_light = self.canvas.create_oval(40, 45, 110, 115, fill="#550000", outline="black")
        self.yellow_light = self.canvas.create_oval(40, 150, 110, 220, fill="#554400", outline="black")
        self.green_light = self.canvas.create_oval(40, 255, 110, 325, fill="#003300", outline="black")

        self.state = "red"
        
        # 啟動自動切換燈號的迴圈
        self.update_light()

    def update_light(self):
        # 先將所有燈設為暗色
        self.canvas.itemconfig(self.red_light, fill="#550000")
        self.canvas.itemconfig(self.yellow_light, fill="#554400")
        self.canvas.itemconfig(self.green_light, fill="#003300")

        # 根據狀態點亮對應的燈，並設定下一次切換的時間
        if self.state == "red":
            self.canvas.itemconfig(self.red_light, fill="#ff0000")  # 亮紅燈
            self.state = "green"
            self.root.after(3000, self.update_light)  # 3秒後換綠燈
            
        elif self.state == "green":
            self.canvas.itemconfig(self.green_light, fill="#00ff00")  # 亮綠燈
            self.state = "yellow"
            self.root.after(3000, self.update_light)  # 3秒後換黃燈
            
        elif self.state == "yellow":
            self.canvas.itemconfig(self.yellow_light, fill="#ffff00")  # 亮黃燈
            self.state = "red"
            self.root.after(1000, self.update_light)  # 1秒後換紅燈

if __name__ == "__main__":
    root = tk.Tk()
    app = TrafficLight(root)
    root.mainloop()