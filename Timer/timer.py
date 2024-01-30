import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox
from PyQt5.QtCore import QTimer, QTime, Qt

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Вход')
        self.resize(250, 100)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel('Введите логин и пароль')
        layout.addWidget(self.label)

        self.login_edit = QLineEdit()
        self.login_edit.setPlaceholderText('Логин')
        layout.addWidget(self.login_edit)

        self.password_edit = QLineEdit()
        self.password_edit.setPlaceholderText('Пароль')
        self.password_edit.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_edit)

        self.login_button = QPushButton('Войти')
        self.login_button.clicked.connect(self.on_login)
        layout.addWidget(self.login_button)

        # стилизация интерфейса окна, с помощью языка CSS
        self.setStyleSheet("""
            QWidget {
                background-color: #333;
                color: #fff;
            }
            QLineEdit {
                background-color: #444;
                border: 1px solid #555;
                padding: 5px;
            }
            QPushButton {
                background-color: #007BFF;
                color: #fff;
                padding: 10px;
                margin-top: 10px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
    
    # окно для ввода логина и пароля
    def on_login(self):
        # тут будет логика (наверное, если мне будет не лень)
        self.close()
        self.main_window = Timer()
        self.main_window.show()

# основной класс окна и логики таймера
class Timer(QWidget):
    # конструктор класса
    def __init__(self):
        super().__init__()
        self.initUI()

    # пользовательский интерфейс
    def initUI(self):
        self.time_label = QLabel('00:00', self)
        self.time_label.setAlignment(Qt.AlignCenter)

        self.minutes_input = QLineEdit('00', self)
        self.minutes_input.setMaxLength(2)
        self.seconds_input = QLineEdit('00', self)
        self.seconds_input.setMaxLength(2)

        self.start_button = QPushButton('Старт', self)
        self.start_button.clicked.connect(self.startTimer)

        hbox = QHBoxLayout()
        hbox.addWidget(self.minutes_input)
        hbox.addWidget(QLabel(':'))
        hbox.addWidget(self.seconds_input)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        vbox.addLayout(hbox)
        vbox.addWidget(self.start_button)

        self.setLayout(vbox)
        self.setWindowTitle('Таймер')
        self.show()

    # запуска таймера
    def startTimer(self):
        minutes = int(self.minutes_input.text())
        seconds = int(self.seconds_input.text())
        total_seconds = minutes * 60 + seconds

        if total_seconds > 0:
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.updateTimer)
            self.timer.start(1000)
            self.start_button.setEnabled(False)
            self.total_seconds = total_seconds
            self.updateTimer()
        else:
            QMessageBox.warning(self, 'Ошибка', 'Введите значенте времени больше 0!')

    # обновление и подсчёт прошедшего времени
    def updateTimer(self):
        minutes = self.total_seconds // 60
        seconds = self.total_seconds % 60
        self.time_label.setText(f'{minutes:02d}:{seconds:02d}')

        if self.total_seconds == 0:
            self.timer.stop()
            self.start_button.setEnabled(True)
            QMessageBox.information(self, 'Уведомление', 'Время вышло!')
        else:
            self.total_seconds -= 1

# запуск программы
if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())