#ola simon, intentare explicarte las barrabasadas que haga en esye codgio cfcfcfcf

import sys
from  PyQt6.QtWidgets import (QWidget,QApplication,QLineEdit,QPushButton,
        QTableWidget,QTableWidgetItem,QMessageBox,QHBoxLayout,QVBoxLayout,QGridLayout,QLabel,QGroupBox,QDoubleSpinBox,QHeaderView,QComboBox)
from PyQt6.QtGui import QFont

class MainView(QWidget):
    def __init__(self):
        super().__init__()
        self.ventana_principal()

    def ventana_principal(self):
        self.setGeometry(100,100,800,650)
# layout_principal es nuestro layout vetical principal con el que se organizaran los datos.
#qgropbox nos vsirve para poner un margen al rededor de los datos desdeados, un detallito
        
        layout_principal = QVBoxLayout(self)
        
        grupo_entradas = QGroupBox('Entradas principales')
        
        layout_entradas = QHBoxLayout()

#QDoubleSpinbox es un metodo que funciona parecido a QLineEdit pero solo funciona con numeros
#tiene flechitas para subir o bajar el valor ingresado, funciona con datos float
        
        layout_entradas.addWidget(QLabel('Caudal Total (L/s):'))
        spin_caudal = QDoubleSpinBox()
        spin_caudal.setValue(2.5)
        layout_entradas.addWidget(spin_caudal)

        layout_entradas.addWidget(QLabel('Presión Requerida Emisor (m):'))
        spin_presion = QDoubleSpinBox()
        spin_presion.setValue(10)
        layout_entradas.addWidget(spin_presion)

#aqui asigno layout_entradas (el horizontal) a grupo_entradas para que seconvierta en widget
# y luego ese widget lo agrego a layout_principal, un layout anidado basicamente        
        
        grupo_entradas.setLayout(layout_entradas)
        layout_principal.addWidget(grupo_entradas)

#el usuario sera capaz de ingresar los datos en tablas, funcionaran como tramos de todos los datos

        grupo_tuberias = QGroupBox('Configuración de Tramos de Tubería y Accesorios')
        layout_tabla = QVBoxLayout()

        self.tabla_tramos = QTableWidget()
        self.tabla_tramos.setColumnCount(5)
        self.tabla_tramos.setHorizontalHeaderLabels(['Tramo', 'Logitud (m)', 'Diámetro (m)',
                                    'Coeficiente C', 'Accesorios K'])

        self.tabla_tramos.setRowCount(0)

        largo_tabla = self.tabla_tramos.horizontalHeader()
        largo_tabla.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        layout_tabla.addWidget(self.tabla_tramos)

        layout_botones_tabla = QHBoxLayout()

        self.boton_agregar = QPushButton('Agregar Tramo')
        self.boton_eliminar = QPushButton('Eliminar Tramo')

        layout_botones_tabla.addWidget(self.boton_agregar)
        layout_botones_tabla.addWidget(self.boton_eliminar)

        layout_tabla.addLayout(layout_botones_tabla)

        grupo_tuberias.setLayout(layout_tabla)

        layout_principal.addWidget(grupo_tuberias)

       #PARTE INFERIOR, ULTIMO GROUPBOX
       
        grupo_resultados = QGroupBox('Resultados y Recomendaciones')
        layout_rr = QGridLayout()

        layout_rr.addWidget(QLabel('Seleccionar tramo a consultar'),0,0)
        self.combo_select_tramo = QComboBox()

        self.combo_select_tramo.addItem('-- Seleccione un tramo --')
        layout_rr.addWidget(self.combo_select_tramo,0,1)

        layout_rr.addWidget(QLabel('Tramo Crítico'),1,0)
        self.txt_tramocritico = QLineEdit()
        self.txt_tramocritico.setReadOnly(True)
        layout_rr.addWidget(self.txt_tramocritico,1,1)

        layout_rr.addWidget(QLabel('Pérdida de Carga Total (m)'))
        self.txt_perdidatotal = QLineEdit()
        self.txt_perdidatotal.setReadOnly(True)
        negrita = QFont()    
        negrita.setBold(True)
        self.txt_perdidatotal.setFont(negrita)
        layout_rr.addWidget(self.txt_perdidatotal,2,1)

        layout_rr.addWidget(QLabel('Presión de Bombeo Requerida (m)'),3,0)
        self.txt_presionbombeo = QLineEdit()
        self.txt_presionbombeo.setReadOnly(True)
        self.txt_presionbombeo.setFont(negrita)
        layout_rr.addWidget(self.txt_presionbombeo,3,1)

        self.lbl_recomendacion = QLabel('Recomendación de Diseño:')
        self.lbl_recomendacion.setStyleSheet('background-color: yellow; color: black; font-weight: bold; padding: 6px;')

        layout_rr.addWidget(self.lbl_recomendacion,4,0,1,2)

        grupo_resultados.setLayout(layout_rr)
        layout_principal.addWidget(grupo_resultados)  

        
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    iu = MainView()
    sys.exit(app.exec())

