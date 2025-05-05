import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QVBoxLayout, QWidget, QLineEdit, QPushButton, QToolBar, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView

def add_tab():
    new_tab = QWidget()
    layout = QVBoxLayout(new_tab)

    browser = QWebEngineView()
    layout.addWidget(browser)

    tabs.addTab(new_tab, "New Tab")
    tabs.setCurrentWidget(new_tab)

    browser.setUrl(QUrl("https://www.google.com"))

    # Connect the urlChanged signal to update_url_bar slot
    browser.urlChanged.connect(lambda url, browser=browser: update_url_bar(url, browser))

def close_tab(index):
    if tabs.count() > 1:
        tabs.removeTab(index)

def navigate_to_url():
    current_tab_index = tabs.currentIndex()
    current_tab_widget = tabs.widget(current_tab_index)
    browser = current_tab_widget.findChild(QWebEngineView)

    url = url_bar.text()
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
    browser.setUrl(QUrl(url))

def update_url_bar(url, browser=None):
    if browser is None:
        browser = tabs.currentWidget().findChild(QWebEngineView)
    if browser.url() != url:
        browser.setUrl(url)
    url_bar.setText(url.toString())

def go_back():
    current_tab_index = tabs.currentIndex()
    current_tab_widget = tabs.widget(current_tab_index)
    browser = current_tab_widget.findChild(QWebEngineView)
    browser.back()

def go_forward():
    current_tab_index = tabs.currentIndex()
    current_tab_widget = tabs.widget(current_tab_index)
    browser = current_tab_widget.findChild(QWebEngineView)
    browser.forward()

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Professional PyQt5 Web Browser")
window.setGeometry(100, 100, 800, 600)

tabs = QTabWidget()
tabs.setTabsClosable(True)
tabs.tabCloseRequested.connect(close_tab)

add_tab_button = QPushButton("+")
add_tab_button.clicked.connect(add_tab)

url_bar = QLineEdit()
url_bar.returnPressed.connect(navigate_to_url)

navigation_bar = QToolBar()
navigation_bar.addWidget(url_bar)
navigation_bar.addWidget(add_tab_button)

back_button = QAction("Back", window)
back_button.triggered.connect(go_back)

forward_button = QAction("Forward", window)
forward_button.triggered.connect(go_forward)

navigation_bar.addAction(back_button)
navigation_bar.addAction(forward_button)

window.setCentralWidget(tabs)
window.addToolBar(navigation_bar)

# Open initial tab
add_tab()

window.show()
sys.exit(app.exec_())
