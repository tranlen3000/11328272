import sys
import json
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget,
    QPushButton, QLineEdit, QInputDialog, QMessageBox, QLabel
)

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do App")
        self.resize(400, 300)

        # Main layout
        self.layout = QVBoxLayout(self)

        # Task list
        self.task_list = QListWidget()
        self.layout.addWidget(self.task_list)

        # Input field
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Enter a task...")
        self.layout.addWidget(self.input_field)

        # Add task button
        self.add_button = QPushButton("Add Task")
        self.add_button.clicked.connect(self.add_task)
        self.layout.addWidget(self.add_button)

        # Delete task button
        self.delete_button = QPushButton("Delete Task")
        self.delete_button.clicked.connect(self.delete_task)
        self.layout.addWidget(self.delete_button)

        # Mark as complete button
        self.complete_button = QPushButton("Mark as Complete")
        self.complete_button.clicked.connect(self.mark_complete)
        self.layout.addWidget(self.complete_button)

        # Save and load buttons
        self.save_button = QPushButton("Save Tasks")
        self.save_button.clicked.connect(self.save_tasks)
        self.layout.addWidget(self.save_button)

        self.load_button = QPushButton("Load Tasks")
        self.load_button.clicked.connect(self.load_tasks)
        self.layout.addWidget(self.load_button)

        # Add deadline button
        self.deadline_button = QPushButton("Add Deadline")
        self.deadline_button.clicked.connect(self.add_deadline)
        self.layout.addWidget(self.deadline_button)

    def add_task(self):
        task = self.input_field.text()
        if task:
            self.task_list.addItem(task)
            self.input_field.clear()
        else:
            QMessageBox.warning(self, "Error", "Please enter a task.")

    def delete_task(self):
        selected_task = self.task_list.currentItem()
        if selected_task:
            self.task_list.takeItem(self.task_list.row(selected_task))
        else:
            QMessageBox.warning(self, "Error", "No task selected.")

    def mark_complete(self):
        selected_task = self.task_list.currentItem()
        if selected_task:
            selected_task.setText(f"{selected_task.text()} (Completed)")
        else:
            QMessageBox.warning(self, "Error", "No task selected.")

    def add_deadline(self):
        selected_task = self.task_list.currentItem()
        if selected_task:
            deadline, ok = QInputDialog.getText(self, "Add Deadline", "Enter deadline (dd/mm/yyyy):")
            if ok and deadline:
                selected_task.setText(f"{selected_task.text()} - Deadline: {deadline}")
        else:
            QMessageBox.warning(self, "Error", "No task selected.")

    def save_tasks(self):
        tasks = []
        for i in range(self.task_list.count()):
            tasks.append(self.task_list.item(i).text())
        with open("tasks.json", "w", encoding="utf-8") as file:
            json.dump(tasks, file, ensure_ascii=False, indent=4)
        QMessageBox.information(self, "Success", "Tasks saved successfully.")

    def load_tasks(self):
        try:
            with open("tasks.json", "r", encoding="utf-8") as file:
                tasks = json.load(file)
                self.task_list.clear()
                self.task_list.addItems(tasks)
        except FileNotFoundError:
            QMessageBox.warning(self, "Error", "No saved file found.")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec())