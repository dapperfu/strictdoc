from PySide2.QtWidgets import (QHBoxLayout, QHeaderView, QSizePolicy,
                               QTableView, QWidget)

from strictdoc.gui.document.document_item_delegate import DocumentItemDelegate
from strictdoc.gui.document.document_model import DocumentTableModel
from strictdoc.gui.styles import STRICTDOC_QT_STYLES


class Widget(QWidget):
    def __init__(self, rst_document):
        QWidget.__init__(self)

        # Getting the Model
        self.model = DocumentTableModel(rst_document)

        # Creating a QTableView
        table_delegate = DocumentItemDelegate()
        self.table_view = QTableView()
        self.table_view.setModel(self.model)
        self.table_view.setItemDelegate(table_delegate)
        # TODO: table_delegate retains table_view
        # TODO: check if it causes any issues with reference cycles.
        table_delegate.table_view = self.table_view
        self.table_view.verticalHeader().setVisible(False)
        self.table_view.horizontalHeader().setVisible(False)

        # Styles
        self.table_view.setStyleSheet(STRICTDOC_QT_STYLES)

        # QTableView Headers
        self.horizontal_header = self.table_view.horizontalHeader()

        self.vertical_header = self.table_view.verticalHeader()
        self.vertical_header.setSectionResizeMode(QHeaderView.ResizeToContents)

        self.horizontal_header.setSectionResizeMode(QHeaderView.Stretch)
        self.horizontal_header.setStretchLastSection(True)

        # QWidget Layout
        self.main_layout = QHBoxLayout()
        size = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        ## Left layout
        size.setHorizontalStretch(1)
        self.table_view.setSizePolicy(size)
        self.main_layout.addWidget(self.table_view)

        # Set the layout to the QWidget
        self.setLayout(self.main_layout)