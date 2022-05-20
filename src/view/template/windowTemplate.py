# Tutorial: https://realpython.com/python-menus-toolbars/
# Tutorail2: https://realpython.com/python-pyqt-gui-calculator/
import random
import sys
import PySide6

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (QLabel, QMainWindow, )


class WindowTemplate(QMainWindow):
    """Main Window."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        # chamando metodo criado para reinderiza os opções do menuBar
        self._createActions()
        # chamando metodo criado para reinderiza o menuBar
        self._createMenuBar()
        # chamando metodo criado para reinderiza o toolbar
        self._createToolBars()
        # metodos referente a janela
        self.setWindowTitle("Python Menus & Toolbars")
        self.resize(1200, 800)
        self.centralWidget = QLabel("Hello, World")
        self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.centralWidget)

    def _createMenuBar(self):
        menuBar = self.menuBar()
        # & ativa tecla de atalho, correspondente a primeira letra da string
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(self.containerAction)
        fileMenu.addAction(self.imageAction)
        fileMenu.addAction(self.configAction)
        fileMenu.addAction(self.exitAction)
        searchMenu = menuBar.addMenu('&Search')
        #Submenu example
        actionsHub = searchMenu.addMenu('&Actions Hub')
        actionsHub.addAction("&Pull")
        actionsHub.addAction("&Search")
        #end submenu
        aboutMenu = menuBar.addMenu('&About')
        aboutMenu.addAction(self.helpAction)
        aboutMenu.addAction(self.aboutAction)
        '''
        Na maneira a cima, a classe QMainWindow possui um espaço padrão para o objeto QMenuBar, sendo apenas acessado pelo metodo menuBar()
        ou usando de objetos:
        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)
        '''

    def _createToolBars(self):
        fileToolBar = self.addToolBar('File')
        configToolBar = self.addToolBar('Configuration')
        aboutToolBar = self.addToolBar('About')

    def _createActions(self):
        self.containerAction = QAction("&Containers", self)
        self.imageAction = QAction("&Images", self)
        self.exitAction = QAction("&Exit", self)
        self.hubAction = QAction("&Docker Hub", self)
        self.configAction = QAction("&Settings", self)
        self.helpAction = QAction("&Help", self)
        self.aboutAction = QAction("&About", self)
