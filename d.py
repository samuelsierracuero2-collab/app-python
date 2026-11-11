import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton,
    QTableWidget, QTableWidgetItem, QMessageBox,
    QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QGroupBox, QDoubleSpinBox
)
from PyQt6.QtGui import QFont

class MainView(QWidget):
    def __init__(self):
        super().__init__()
        self.ventana_principal()

    def ventana_principal(self):
        self.setWindowTitle("Sistema de Riego por Goteo - Análisis de Pérdidas")
        self.setGeometry(100, 100, 800, 650)
        
        # Asignar el layout principal directamente a la ventana (self)
        layout_principal = QVBoxLayout(self)

        # 1. Crear el contenedor (QGroupBox) con su título
        grupo_entradas = QGroupBox("Entradas Principales")
        layout_entradas = QHBoxLayout()

        # 2. Agregar los elementos de entrada dentro del layout horizontal
        layout_entradas.addWidget(QLabel("Caudal Total (L/s):"))
        spin_caudal = QDoubleSpinBox()
        spin_caudal.setValue(2.5)
        layout_entradas.addWidget(spin_caudal)

        layout_entradas.addWidget(QLabel("Presión Requerida Emisor (m):"))
        spin_presion = QDoubleSpinBox()
        spin_presion.setValue(10.0)
        layout_entradas.addWidget(spin_presion)

        # Asignar el layout horizontal al QGroupBox
        grupo_entradas.setLayout(layout_entradas)

        # 3. Añadir el grupo AL INICIO del layout principal para que quede arriba del todo
        layout_principal.addWidget(grupo_entradas)
        
        # Mostrar la ventana
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    iu = MainView()
    sys.exit(app.exec())