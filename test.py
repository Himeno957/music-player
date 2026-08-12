# test.py - 测试 PyQt5 是否正常
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

print("1. 创建 QApplication...")
app = QApplication(sys.argv)

print("2. 创建窗口...")
window = QWidget()
window.setWindowTitle("测试窗口")
window.setGeometry(100, 100, 400, 300)

label = QLabel("✅ PyQt5 工作正常！\n如果能看见这个窗口，说明没问题", window)
label.move(50, 80)
label.setStyleSheet("font-size: 16px;")

print("3. 显示窗口...")
window.show()
window.raise_()  # 强制置顶
window.activateWindow()  # 激活窗口

print("4. 进入事件循环...")
print("窗口应该已经显示了，如果没看到请检查任务栏")
sys.exit(app.exec_())