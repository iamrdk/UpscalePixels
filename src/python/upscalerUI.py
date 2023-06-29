import sys
from PIL import Image
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLineEdit, QVBoxLayout, QWidget, QHBoxLayout, QMessageBox, QLabel
from time import time
import os


class ImageUpscalingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Upscaling")
        self.setGeometry(100, 100, 400, 200)

        self.filename = ""
        self.scale_factor = 2

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        line1_layout = QHBoxLayout()
        self.load_button = QPushButton("Load Image")
        self.load_button.setFixedSize(120, 30)
        line1_layout.addWidget(self.load_button)

        line2_layout = QHBoxLayout()
        self.scale_label = QLabel("Scale Factor:")
        self.scale_entry = QLineEdit()
        self.scale_entry.setFixedSize(120, 30)
        self.scale_entry.setText(str(self.scale_factor))
        line2_layout.addWidget(self.scale_label)
        line2_layout.addWidget(self.scale_entry)

        line3_layout = QHBoxLayout()
        self.process_button = QPushButton("Process Image")
        self.process_button.setFixedSize(120, 30)
        line3_layout.addWidget(self.process_button)

        self.layout.addLayout(line1_layout)
        self.layout.addLayout(line2_layout)
        self.layout.addLayout(line3_layout)

        self.load_button.clicked.connect(self.load_image)
        self.process_button.clicked.connect(self.process_image)

    def load_image(self):
        file_dialog = QFileDialog()
        self.filename, _ = file_dialog.getOpenFileName(self, "Select Image", "", "Image files (*.png *.jpg *.jpeg)")

    def process_image(self):
        if self.filename:
            start_time = time()
            img = Image.open(self.filename)
            w, h = img.size
            pixels = np.array(img)
            scale = int(self.scale_entry.text())

            upscaled_img = Image.new(mode="RGB", size=(w * scale, h * scale))
            u_pixels = upscaled_img.load()

            for i in range(h):
                for j in range(w):
                    for dx in range(scale):
                        for dy in range(scale):
                            u_pixels[i * scale + dx, j * scale + dy] = tuple(map(int, pixels[i, j]))

            output_file = os.path.abspath("output/upscaled_{}x.jpg".format(scale))
            upscaled_img.save(output_file)

            QMessageBox.information(self, "Processing Complete", "Image processing complete.\nTime taken: {} seconds.".format(time() - start_time))
        else:
            QMessageBox.warning(self, "Error", "Please load an image first.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageUpscalingApp()
    window.show()
    sys.exit(app.exec_())
