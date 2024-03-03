import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap, QWheelEvent, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QFileDialog, QGraphicsView, QGraphicsScene, QLabel, QMessageBox

import fitz  # PyMuPDF

class FeatherPDF(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('FeatherPDF')
        self.setGeometry(100, 100, 800, 600)
        
        # Agrega el ícono a la ventana
        icon = QIcon("fpdf-iconlogo.png")
        self.setWindowIcon(icon)

        layout = QVBoxLayout()

        self.pdf_view = QGraphicsView()
        layout.addWidget(self.pdf_view)

        self.scene = QGraphicsScene()
        self.pdf_view.setScene(self.scene)

        button_layout = QHBoxLayout()

        open_button = QPushButton('Open')
        open_button.clicked.connect(self.openPDF)
        open_button.setFixedSize(40, 20)
        button_layout.addWidget(open_button)

        home_button = QPushButton('Home')
        home_button.clicked.connect(self.goHome)
        home_button.setFixedSize(40, 20)
        button_layout.addWidget(home_button)

        zoom_in_button = QPushButton('+')
        zoom_in_button.clicked.connect(self.zoomIn)
        zoom_in_button.setFixedSize(20, 20)
        button_layout.addWidget(zoom_in_button)

        zoom_out_button = QPushButton('-')
        zoom_out_button.clicked.connect(self.zoomOut)
        zoom_out_button.setFixedSize(20, 20)
        button_layout.addWidget(zoom_out_button)
        
        reset_zoom_button = QPushButton('Reset Zoom')
        reset_zoom_button.clicked.connect(self.resetZoom)
        reset_zoom_button.setFixedSize(80, 20)
        button_layout.addWidget(reset_zoom_button)

        prev_page_button = QPushButton('<')
        prev_page_button.clicked.connect(self.prevPage)
        prev_page_button.setFixedSize(20, 20)
        button_layout.addWidget(prev_page_button)

        next_page_button = QPushButton('>')
        next_page_button.clicked.connect(self.nextPage)
        next_page_button.setFixedSize(20, 20)
        button_layout.addWidget(next_page_button)

        self.page_label = QLabel()
        button_layout.addWidget(self.page_label)

        credits_button = QPushButton('Credits')
        credits_button.clicked.connect(self.showCredits)
        credits_button.setFixedSize(80, 20)
        button_layout.addWidget(credits_button)

        layout.addLayout(button_layout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.doc = None
        self.current_page = 0
        self.zoom_factor = 1.0

    def openPDF(self):
        options = QFileDialog()
        file_name, _ = options.getOpenFileName(self, "Open PDF File", "", "PDF Files (*.pdf);;All Files (*)")
        if file_name:
            self.doc = fitz.open(file_name)
            self.current_page = 0
            self.showPage()

    def showPage(self):
        if self.doc is not None and 0 <= self.current_page < self.doc.page_count:
            page = self.doc[self.current_page]
            image = page.get_pixmap(matrix=fitz.Matrix(self.zoom_factor, self.zoom_factor), alpha=False)
            image_data = image.samples

            qimage = QImage(image_data, image.width, image.height, image.stride, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(qimage)
            self.scene.clear()
            self.scene.addPixmap(pixmap)

            self.page_label.setText(f"Page {self.current_page + 1} / {self.doc.page_count}")

            self.pdf_view.setScene(self.scene)

    def goHome(self):
        self.zoom_factor = 1.0
        self.current_page = 0
        self.showPage()

    def zoomIn(self):
        self.zoom_factor *= 1.25
        self.showPage()

    def zoomOut(self):
        self.zoom_factor *= 0.8
        self.showPage()
        
    def resetZoom(self):
        self.zoom_factor = 1.0
        self.showPage()

    def prevPage(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.showPage()

    def nextPage(self):
        if self.doc is not None and self.current_page < self.doc.page_count - 1:
            self.current_page += 1
            self.showPage()

    def wheelEvent(self, event: QWheelEvent):
        num_degrees = event.angleDelta().y() / 8
        num_steps = num_degrees / 15
        
        if num_steps > 0:
            self.prevPage()
        else:
            self.nextPage()

    def showCredits(self):
        credits_text = (
            "Created by Felipe Alfonso Gonzalez\n"
            "Computer Science Engineer\n"
            "Chile, 2023\n\n"
            "Licensed under the MIT License\n\n"
            "MIT License:\n\n"
            "Permission is hereby granted, free of charge, to any person obtaining a copy of this software and "
            "associated documentation files (the 'Software'), to deal in the Software without restriction, "
            "including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,"
            " and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,"
            " subject to the following conditions:\n\n"
            "The above copyright notice and this permission notice shall be included in all copies or substantial "
            "portions of the Software.\n\n"
            "THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT"
            " LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN "
            "NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,"
            " WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE "
            "SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."
        )
        QMessageBox.information(self, "Credits", credits_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FeatherPDF()
    window.show()
    sys.exit(app.exec_())
