import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("PyQt 練習")
        self.setGeometry(100, 100, 300, 200)

        # Layout
        layout = QVBoxLayout()

        # Input Field
        self.input_field = QLineEdit(self)
        layout.addWidget(self.input_field)

        # Label
        self.label = QLabel("輸入後顯示這裡", self)
        layout.addWidget(self.label)

        # Reverse Button
        self.reverse_button = QPushButton("反轉文字", self)
        self.reverse_button.clicked.connect(self.reverse_text)
        layout.addWidget(self.reverse_button)

        # Check Length Button
        self.check_length_button = QPushButton("檢查文字長度", self)
        self.check_length_button.clicked.connect(self.check_length)
        layout.addWidget(self.check_length_button)

        # Set Layout
        self.setLayout(layout)

    def reverse_text(self):
        text = self.input_field.text()
        if text:
            self.label.setText(text[::-1])
        else:
            QMessageBox.warning(self, "提示", "請輸入文字！")

    def check_length(self):
        text = self.input_field.text()
        if len(text) > 10:
            QMessageBox.warning(self, "提示", "文字太長！")
        else:
            self.label.setText("文字長度符合要求")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())