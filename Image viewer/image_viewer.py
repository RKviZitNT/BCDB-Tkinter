import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QVBoxLayout, QWidget, QHBoxLayout, QSpinBox
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import Qt

# основного класс приложения
class ImageEditor(QMainWindow):
    # конструктора класса
    def __init__(self):
        super().__init__()
        self.initUI()
        self.scale_factor = 1.0

    # пользовательский интерфейс
    def initUI(self):
        self.setWindowTitle('Редактор изображений')
        self.setGeometry(100, 100, 800, 600)

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)

        self.zoom_in_button = QPushButton('Увеличить')
        self.zoom_in_button.clicked.connect(self.zoom_in)

        self.zoom_out_button = QPushButton('Уменьшить')
        self.zoom_out_button.clicked.connect(self.zoom_out)

        self.rotate_left_button = QPushButton('Повернуть влево')
        self.rotate_left_button.clicked.connect(self.rotate_left)

        self.rotate_right_button = QPushButton('Повернуть вправо')
        self.rotate_right_button.clicked.connect(self.rotate_right)

        self.load_button = QPushButton('Загрузить изображение')
        self.load_button.clicked.connect(self.load_image)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addLayout(QHBoxLayout())
        layout.addWidget(self.load_button)
        layout.addWidget(self.rotate_left_button)
        layout.addWidget(self.rotate_right_button)
        layout.addWidget(self.zoom_in_button)
        layout.addWidget(self.zoom_out_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    # загрузка изображения
    def load_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Выбор изображения', '', 'Изображения (*.jpg *.jpeg *.png *.bmp *.gif)')
        if file_name:
            self.pixmap = QPixmap(file_name)
            self.scale_image()

    # поворот изображения влево на 90'
    def rotate_left(self):
        if hasattr(self, 'pixmap'):
            transform = QTransform().rotate(-90)
            self.pixmap = self.pixmap.transformed(transform)
            self.scale_image()

    # поворот изображения вправо на 90'
    def rotate_right(self):
        if hasattr(self, 'pixmap'):
            transform = QTransform().rotate(90)
            self.pixmap = self.pixmap.transformed(transform)
            self.scale_image()

    # масштабирование изображения, увеличение на 10%
    def zoom_in(self):
        self.scale_factor *= 1.1
        self.scale_image()

    # масштабирование изображения, уменьшение на 10%
    def zoom_out(self):
        self.scale_factor *= 0.9
        self.scale_image()

    # изменение изображения, позволяющее не допустить пояевления графических артефактов при изменении масштаба изображения
    def scale_image(self):
        if hasattr(self, 'pixmap'):
            scaled_width = int(self.pixmap.width() * self.scale_factor)
            scaled_height = int(self.pixmap.height() * self.scale_factor)
            scaled_pixmap = self.pixmap.scaled(scaled_width, scaled_height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image_label.setPixmap(scaled_pixmap)

# запуск программы
if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = ImageEditor()
    editor.show()
    sys.exit(app.exec_())