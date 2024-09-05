import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QLineEdit, QStatusBar
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Barra de navegación
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Botón de retroceso
        back_btn = QAction('Atrás', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # Botón de avance
        forward_btn = QAction('Adelante', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # Botón de recargar
        reload_btn = QAction('Recargar', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        # Botón de inicio
        home_btn = QAction('Inicio', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # Barra de URL
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        # Actualizar la barra de URL
        self.browser.urlChanged.connect(self.update_url)

        # Barra de estado
        self.status = QStatusBar()
        self.setStatusBar(self.status)

    def navigate_home(self):
        self.browser.setUrl(QUrl("http://www.google.com"))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName("Navegador Web")
window = Browser()
app.exec_()
