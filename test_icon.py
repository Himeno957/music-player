
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon

class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("图标测试")
        self.setGeometry(200, 200, 300, 200)
        
        # 设置图标
        icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")
        print(f"图标路径: {icon_path}")
        print(f"文件存在: {os.path.exists(icon_path)}")
        
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
            print("✅ 图标已设置")
        
        # 显示一个标签
        label = QLabel("查看任务栏图标是否显示", self)
        label.move(50, 80)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestWindow()
    window.show()
    sys.exit(app.exec_())