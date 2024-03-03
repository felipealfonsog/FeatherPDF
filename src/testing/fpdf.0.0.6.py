import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap, QWheelEvent, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QFileDialog, QGraphicsView, QGraphicsScene, QLabel, QMessageBox, QSizePolicy, QTabWidget, QTabBar

import fitz  # PyMuPDF

class PDFViewer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        layout = QVBoxLayout()

        self.pdf_view = QGraphicsView()
        self.pdf_scene = QGraphicsScene()
        self.pdf_view.setScene(self.pdf_scene)
        self.pdf_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.pdf_view.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.pdf_view)

        self.setLayout(layout)

        self.doc = None
        self.current_page = 0
        self.zoom_factor = 1.0

    def openPDF(self, file_name):
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
            self.pdf_scene.setSceneRect(0, 0, image.width, image.height)
            self.pdf_scene.clear()
            self.pdf_scene.addPixmap(pixmap)

    def goHome(self):
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

class FeatherPDF(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('FeatherPDF')
        self.setGeometry(100, 100, 620, 700)  # Ajusta las dimensiones de la ventana
        
        # Agrega el ícono a la ventana
        icon = QIcon("fpdf-iconlogo.png")
        self.setWindowIcon(icon)

        layout = QVBoxLayout()

        self.tab_widget = QTabWidget()
        layout.addWidget(self.tab_widget)

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

        quit_button = QPushButton('Quit')
        quit_button.clicked.connect(self.quitApp)
        quit_button.setFixedSize(60, 20)
        button_layout.addWidget(quit_button)

        layout.addLayout(button_layout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.current_tab = None

    def openPDF(self):
        options = QFileDialog()
        file_name, _ = options.getOpenFileName(self, "Open PDF File", "", "PDF Files (*.pdf);;All Files (*)")
        if file_name:
            self.createTab(file_name)

    def createTab(self, file_name=None):
        pdf_tab = PDFViewer()
        if file_name:
            pdf_tab.openPDF(file_name)
        self.tab_widget.addTab(pdf_tab, "Untitled")
        if file_name:
            self.tab_widget.setTabText(self.tab_widget.indexOf(pdf_tab), file_name)
        pdf_tab.close_button = QPushButton('x')
        pdf_tab.close_button.setFixedSize(20, 20)
        pdf_tab.close_button.clicked.connect(lambda: self.closeTab(pdf_tab))
        self.tab_widget.tabBar().setTabButton(self.tab_widget.indexOf(pdf_tab), QTabBar.LeftSide, pdf_tab.close_button)
        self.tab_widget.setCurrentWidget(pdf_tab)
        self.current_tab = pdf_tab
        self.updatePageLabel()

    def closeTab(self, tab):
        self.tab_widget.removeTab(self.tab_widget.indexOf(tab))

    def goHome(self):
        if self.current_tab:
            self.current_tab.goHome()

    def zoomIn(self):
        if self.current_tab:
            self.current_tab.zoomIn()

    def zoomOut(self):
        if self.current_tab:
            self.current_tab.zoomOut()

    def resetZoom(self):
        if self.current_tab:
            self.current_tab.resetZoom()

    def prevPage(self):
        if self.current_tab:
            self.current_tab.prevPage()
            self.updatePageLabel()

    def nextPage(self):
        if self.current_tab:
            self.current_tab.nextPage()
            self.updatePageLabel()
    
    def updatePageLabel(self):
        if self.current_tab:
            self.page_label.setText(f"Page {self.current_tab.current_page + 1} of {self.current_tab.doc.page_count}")

    def showCredits(self):
        credits_text = (
            "Feather PDF: A PDF Viewer with a simple UI and very lightweight. Developed with love from Santiago, Chile.\n\n"
            "Created by Felipe Alfonso Gonzalez\n"
            "Computer Science Engineer\n"
            "Email: f.alfonso@res-ear.ch\n"
            "GitHub: github.com/felipealfonsog\n\n"
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

    def quitApp(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # Cambia el estilo a 'Fusion'
    window = FeatherPDF()
    window.show()
    sys.exit(app.exec_())
