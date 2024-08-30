# Form implementation generated from reading ui file 'index.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        MainWindow.resize(1199, 767)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 1161, 825))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.icon_only_widget = QtWidgets.QWidget(parent=self.layoutWidget)
        self.icon_only_widget.setMinimumSize(QtCore.QSize(71, 0))
        self.icon_only_widget.setMaximumSize(QtCore.QSize(71, 99999))
        self.icon_only_widget.setStyleSheet("QWidget{\n"
"    background-color: rgb(0, 0, 0);\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color:white;\n"
"    border-radius:3px;\n"
"}")
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_12.setContentsMargins(-1, 9, -1, 20)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 35, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(parent=self.icon_only_widget)
        self.label_4.setMinimumSize(QtCore.QSize(40, 40))
        self.label_4.setMaximumSize(QtCore.QSize(40, 40))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Icons/shopping-cart.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        spacerItem1 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_12.addLayout(self.horizontalLayout_2)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_9.setSpacing(20)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.dashboard_btn1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.dashboard_btn1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/dashboard.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon.addPixmap(QtGui.QPixmap("Icons/dashboard-color.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.dashboard_btn1.setIcon(icon)
        self.dashboard_btn1.setIconSize(QtCore.QSize(20, 20))
        self.dashboard_btn1.setCheckable(True)
        self.dashboard_btn1.setAutoExclusive(True)
        self.dashboard_btn1.setObjectName("dashboard_btn1")
        self.verticalLayout_9.addWidget(self.dashboard_btn1)
        self.order_btn1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.order_btn1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icons/checkout.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon1.addPixmap(QtGui.QPixmap("Icons/checkout-color.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.order_btn1.setIcon(icon1)
        self.order_btn1.setIconSize(QtCore.QSize(20, 20))
        self.order_btn1.setCheckable(True)
        self.order_btn1.setAutoExclusive(True)
        self.order_btn1.setObjectName("order_btn1")
        self.verticalLayout_9.addWidget(self.order_btn1)
        self.delivery_btn1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.delivery_btn1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/delivery.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon2.addPixmap(QtGui.QPixmap("Icons/delivery-color.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.delivery_btn1.setIcon(icon2)
        self.delivery_btn1.setIconSize(QtCore.QSize(24, 24))
        self.delivery_btn1.setCheckable(True)
        self.delivery_btn1.setAutoExclusive(True)
        self.delivery_btn1.setObjectName("delivery_btn1")
        self.verticalLayout_9.addWidget(self.delivery_btn1)
        self.finance_btn1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.finance_btn1.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/profits.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon3.addPixmap(QtGui.QPixmap("Icons/profits-color.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.finance_btn1.setIcon(icon3)
        self.finance_btn1.setIconSize(QtCore.QSize(24, 24))
        self.finance_btn1.setCheckable(True)
        self.finance_btn1.setAutoExclusive(True)
        self.finance_btn1.setObjectName("finance_btn1")
        self.verticalLayout_9.addWidget(self.finance_btn1)
        self.products_btn1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.products_btn1.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icons/product.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon4.addPixmap(QtGui.QPixmap("Icons/product-color.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.products_btn1.setIcon(icon4)
        self.products_btn1.setIconSize(QtCore.QSize(24, 24))
        self.products_btn1.setCheckable(True)
        self.products_btn1.setAutoExclusive(True)
        self.products_btn1.setObjectName("products_btn1")
        self.verticalLayout_9.addWidget(self.products_btn1)
        self.verticalLayout_12.addLayout(self.verticalLayout_9)
        spacerItem2 = QtWidgets.QSpacerItem(20, 293, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_12.addItem(spacerItem2)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setContentsMargins(-1, -1, -1, 15)
        self.verticalLayout_10.setSpacing(20)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.settings_btn1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.settings_btn1.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Icons/settings.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon5.addPixmap(QtGui.QPixmap("Icons/settings-color.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.settings_btn1.setIcon(icon5)
        self.settings_btn1.setIconSize(QtCore.QSize(20, 20))
        self.settings_btn1.setCheckable(True)
        self.settings_btn1.setAutoExclusive(True)
        self.settings_btn1.setObjectName("settings_btn1")
        self.verticalLayout_10.addWidget(self.settings_btn1)
        self.logout_btn1 = QtWidgets.QPushButton(parent=self.icon_only_widget)
        self.logout_btn1.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Icons/logout.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon6.addPixmap(QtGui.QPixmap("Icons/logout-color.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.logout_btn1.setIcon(icon6)
        self.logout_btn1.setIconSize(QtCore.QSize(20, 20))
        self.logout_btn1.setCheckable(True)
        self.logout_btn1.setAutoExclusive(True)
        self.logout_btn1.setObjectName("logout_btn1")
        self.verticalLayout_10.addWidget(self.logout_btn1)
        self.verticalLayout_12.addLayout(self.verticalLayout_10)
        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)
        self.icon_text_widget = QtWidgets.QWidget(parent=self.layoutWidget)
        self.icon_text_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.icon_text_widget.setMaximumSize(QtCore.QSize(999999, 999999))
        self.icon_text_widget.setStyleSheet("QWidget{\n"
"    background-color: rgb(0, 0, 0);\n"
"    color: white;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    height:30px;\n"
"    border:none;\n"
"}")
        self.icon_text_widget.setObjectName("icon_text_widget")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.icon_text_widget)
        self.verticalLayout_11.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 35, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.icon_text_widget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_2.setMaximumSize(QtCore.QSize(40, 40))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Icons/shopping-cart.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.icon_text_widget)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(16)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout_11.addLayout(self.horizontalLayout)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.dashboard_btn2 = QtWidgets.QPushButton(parent=self.icon_text_widget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        font.setBold(True)
        self.dashboard_btn2.setFont(font)
        self.dashboard_btn2.setStyleSheet("QPushButton{\n"
"    padding-left: -25px\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color:white;\n"
"    border-radius:3px;\n"
"}")
        self.dashboard_btn2.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Icons/dashboard2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon7.addPixmap(QtGui.QPixmap("Icons/dashboard1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.dashboard_btn2.setIcon(icon7)
        self.dashboard_btn2.setIconSize(QtCore.QSize(200, 20))
        self.dashboard_btn2.setCheckable(True)
        self.dashboard_btn2.setAutoExclusive(True)
        self.dashboard_btn2.setObjectName("dashboard_btn2")
        self.verticalLayout_7.addWidget(self.dashboard_btn2)
        self.order_btn2 = QtWidgets.QPushButton(parent=self.icon_text_widget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        font.setBold(True)
        self.order_btn2.setFont(font)
        self.order_btn2.setStyleSheet("QPushButton{\n"
"    padding-left: -27px\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color:white;\n"
"    border-radius:3px;\n"
"}")
        self.order_btn2.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("Icons/orders2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon8.addPixmap(QtGui.QPixmap("Icons/orders1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.order_btn2.setIcon(icon8)
        self.order_btn2.setIconSize(QtCore.QSize(200, 20))
        self.order_btn2.setCheckable(True)
        self.order_btn2.setAutoExclusive(True)
        self.order_btn2.setObjectName("order_btn2")
        self.verticalLayout_7.addWidget(self.order_btn2)
        self.delivery = QtWidgets.QFrame(parent=self.icon_text_widget)
        self.delivery.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.delivery.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.delivery.setObjectName("delivery")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.delivery)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.delivery_btn2 = QtWidgets.QPushButton(parent=self.delivery)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        font.setBold(True)
        self.delivery_btn2.setFont(font)
        self.delivery_btn2.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("Icons/delivery4.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon9.addPixmap(QtGui.QPixmap("Icons/delivery3.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.delivery_btn2.setIcon(icon9)
        self.delivery_btn2.setIconSize(QtCore.QSize(200, 24))
        self.delivery_btn2.setCheckable(True)
        self.delivery_btn2.setAutoExclusive(True)
        self.delivery_btn2.setObjectName("delivery_btn2")
        self.verticalLayout_5.addWidget(self.delivery_btn2)
        self.delivery_dropdown = QtWidgets.QFrame(parent=self.delivery)
        self.delivery_dropdown.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.delivery_dropdown.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.delivery_dropdown.setObjectName("delivery_dropdown")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.delivery_dropdown)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.deliveredOrders_btn = QtWidgets.QPushButton(parent=self.delivery_dropdown)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.deliveredOrders_btn.setFont(font)
        self.deliveredOrders_btn.setStyleSheet("QPushButton{\n"
"    padding-left: 12px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:#12B298;\n"
"}")
        self.deliveredOrders_btn.setCheckable(True)
        self.deliveredOrders_btn.setObjectName("deliveredOrders_btn")
        self.verticalLayout_2.addWidget(self.deliveredOrders_btn)
        self.paidOrders_btn = QtWidgets.QPushButton(parent=self.delivery_dropdown)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.paidOrders_btn.setFont(font)
        self.paidOrders_btn.setStyleSheet("QPushButton{\n"
"    padding-left: -14px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:#12B298;\n"
"}")
        self.paidOrders_btn.setCheckable(True)
        self.paidOrders_btn.setObjectName("paidOrders_btn")
        self.verticalLayout_2.addWidget(self.paidOrders_btn)
        self.paiements_btn = QtWidgets.QPushButton(parent=self.delivery_dropdown)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.paiements_btn.setFont(font)
        self.paiements_btn.setStyleSheet("QPushButton{\n"
"    padding-left: -22px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:#12B298;\n"
"}")
        self.paiements_btn.setCheckable(True)
        self.paiements_btn.setObjectName("paiements_btn")
        self.verticalLayout_2.addWidget(self.paiements_btn)
        self.verticalLayout_5.addWidget(self.delivery_dropdown)
        self.verticalLayout_7.addWidget(self.delivery)
        self.finances = QtWidgets.QFrame(parent=self.icon_text_widget)
        self.finances.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.finances.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.finances.setObjectName("finances")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.finances)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.finance_btn2 = QtWidgets.QPushButton(parent=self.finances)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        font.setBold(True)
        self.finance_btn2.setFont(font)
        self.finance_btn2.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("Icons/profits4.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon10.addPixmap(QtGui.QPixmap("Icons/profits3.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.finance_btn2.setIcon(icon10)
        self.finance_btn2.setIconSize(QtCore.QSize(200, 24))
        self.finance_btn2.setCheckable(True)
        self.finance_btn2.setAutoExclusive(True)
        self.finance_btn2.setObjectName("finance_btn2")
        self.verticalLayout_6.addWidget(self.finance_btn2)
        self.finance_dropdown = QtWidgets.QFrame(parent=self.finances)
        self.finance_dropdown.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.finance_dropdown.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.finance_dropdown.setObjectName("finance_dropdown")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.finance_dropdown)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.expenses_btn = QtWidgets.QPushButton(parent=self.finance_dropdown)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.expenses_btn.setFont(font)
        self.expenses_btn.setStyleSheet("QPushButton{\n"
"    padding-left: -25px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:#12B298;\n"
"}")
        self.expenses_btn.setCheckable(True)
        self.expenses_btn.setObjectName("expenses_btn")
        self.verticalLayout_3.addWidget(self.expenses_btn)
        self.cash_btn = QtWidgets.QPushButton(parent=self.finance_dropdown)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.cash_btn.setFont(font)
        self.cash_btn.setStyleSheet("QPushButton{\n"
"    padding-left: -48px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:#12B298;\n"
"}")
        self.cash_btn.setCheckable(True)
        self.cash_btn.setObjectName("cash_btn")
        self.verticalLayout_3.addWidget(self.cash_btn)
        self.revenues_btn = QtWidgets.QPushButton(parent=self.finance_dropdown)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.revenues_btn.setFont(font)
        self.revenues_btn.setStyleSheet("QPushButton{\n"
"    padding-left: -22px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:#12B298;\n"
"}")
        self.revenues_btn.setCheckable(True)
        self.revenues_btn.setObjectName("revenues_btn")
        self.verticalLayout_3.addWidget(self.revenues_btn)
        self.verticalLayout_6.addWidget(self.finance_dropdown)
        self.verticalLayout_7.addWidget(self.finances)
        self.products = QtWidgets.QFrame(parent=self.icon_text_widget)
        self.products.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.products.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.products.setObjectName("products")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.products)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.products_btn2 = QtWidgets.QPushButton(parent=self.products)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        font.setBold(True)
        self.products_btn2.setFont(font)
        self.products_btn2.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("Icons/product4.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon11.addPixmap(QtGui.QPixmap("Icons/product3.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.products_btn2.setIcon(icon11)
        self.products_btn2.setIconSize(QtCore.QSize(200, 24))
        self.products_btn2.setCheckable(True)
        self.products_btn2.setAutoExclusive(True)
        self.products_btn2.setObjectName("products_btn2")
        self.verticalLayout_4.addWidget(self.products_btn2)
        self.products_dropdown = QtWidgets.QFrame(parent=self.products)
        self.products_dropdown.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.products_dropdown.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.products_dropdown.setObjectName("products_dropdown")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.products_dropdown)
        self.verticalLayout.setObjectName("verticalLayout")
        self.allProducts_btn = QtWidgets.QPushButton(parent=self.products_dropdown)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.allProducts_btn.setFont(font)
        self.allProducts_btn.setStyleSheet("QPushButton{\n"
"    padding-left: -2px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:#12B298;\n"
"}")
        self.allProducts_btn.setCheckable(True)
        self.allProducts_btn.setObjectName("allProducts_btn")
        self.verticalLayout.addWidget(self.allProducts_btn)
        self.addProduct_btn = QtWidgets.QPushButton(parent=self.products_dropdown)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.addProduct_btn.setFont(font)
        self.addProduct_btn.setStyleSheet("QPushButton{\n"
"    padding-left: -2px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:#12B298;\n"
"}")
        self.addProduct_btn.setCheckable(True)
        self.addProduct_btn.setObjectName("addProduct_btn")
        self.verticalLayout.addWidget(self.addProduct_btn)
        self.inventory_btn = QtWidgets.QPushButton(parent=self.products_dropdown)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(8)
        self.inventory_btn.setFont(font)
        self.inventory_btn.setStyleSheet("QPushButton{\n"
"    padding-left: -17px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color:#12B298;\n"
"}")
        self.inventory_btn.setCheckable(True)
        self.inventory_btn.setObjectName("inventory_btn")
        self.verticalLayout.addWidget(self.inventory_btn)
        self.verticalLayout_4.addWidget(self.products_dropdown)
        self.verticalLayout_7.addWidget(self.products)
        self.verticalLayout_11.addLayout(self.verticalLayout_7)
        spacerItem3 = QtWidgets.QSpacerItem(20, 29, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_11.addItem(spacerItem3)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(-1, -1, -1, 15)
        self.verticalLayout_8.setSpacing(15)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.settings_btn2 = QtWidgets.QPushButton(parent=self.icon_text_widget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        font.setBold(True)
        self.settings_btn2.setFont(font)
        self.settings_btn2.setStyleSheet("QPushButton{\n"
"    padding-left: -27px\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color:white;\n"
"    border-radius:3px;\n"
"}")
        self.settings_btn2.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("Icons/settings2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon12.addPixmap(QtGui.QPixmap("Icons/settings1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.settings_btn2.setIcon(icon12)
        self.settings_btn2.setIconSize(QtCore.QSize(200, 20))
        self.settings_btn2.setCheckable(True)
        self.settings_btn2.setAutoExclusive(True)
        self.settings_btn2.setObjectName("settings_btn2")
        self.verticalLayout_8.addWidget(self.settings_btn2)
        self.logout_btn2 = QtWidgets.QPushButton(parent=self.icon_text_widget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        font.setBold(True)
        self.logout_btn2.setFont(font)
        self.logout_btn2.setStyleSheet("QPushButton{\n"
"    padding-left: -27px\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color:white;\n"
"    border-radius:3px;\n"
"}")
        self.logout_btn2.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("Icons/logout2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon13.addPixmap(QtGui.QPixmap("Icons/logout1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
        self.logout_btn2.setIcon(icon13)
        self.logout_btn2.setIconSize(QtCore.QSize(200, 20))
        self.logout_btn2.setCheckable(True)
        self.logout_btn2.setAutoExclusive(True)
        self.logout_btn2.setObjectName("logout_btn2")
        self.verticalLayout_8.addWidget(self.logout_btn2)
        self.verticalLayout_11.addLayout(self.verticalLayout_8)
        self.gridLayout.addWidget(self.icon_text_widget, 0, 1, 1, 1)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.header_widget = QtWidgets.QWidget(parent=self.layoutWidget)
        self.header_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.header_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.header_widget.setObjectName("header_widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.header_widget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtWidgets.QPushButton(parent=self.header_widget)
        self.pushButton.setStyleSheet("border:none;")
        self.pushButton.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("Icons/menu.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon14)
        self.pushButton.setIconSize(QtCore.QSize(29, 35))
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setContentsMargins(-1, 35, -1, 35)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label = QtWidgets.QLabel(parent=self.header_widget)
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_13.addWidget(self.label)
        self.label_5 = QtWidgets.QLabel(parent=self.header_widget)
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(70, 70, 70);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_13.addWidget(self.label_5)
        self.horizontalLayout_4.addLayout(self.verticalLayout_13)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        spacerItem4 = QtWidgets.QSpacerItem(311, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.header_widget)
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    padding-left: 10px;\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.label_6 = QtWidgets.QLabel(parent=self.header_widget)
        self.label_6.setMaximumSize(QtCore.QSize(40, 40))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("Icons/man.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_14.addWidget(self.header_widget)
        self.main_screen_widget = QtWidgets.QWidget(parent=self.layoutWidget)
        self.main_screen_widget.setMinimumSize(QtCore.QSize(850, 650))
        self.main_screen_widget.setMaximumSize(QtCore.QSize(850, 650))
        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        self.main_screen_widget.setFont(font)
        self.main_screen_widget.setStyleSheet("")
        self.main_screen_widget.setObjectName("main_screen_widget")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.main_screen_widget)
        self.stackedWidget.setGeometry(QtCore.QRect(30, 0, 811, 571))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_7 = QtWidgets.QLabel(parent=self.page)
        self.label_7.setGeometry(QtCore.QRect(370, 220, 161, 101))
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(19)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_8 = QtWidgets.QLabel(parent=self.page_2)
        self.label_8.setGeometry(QtCore.QRect(370, 190, 161, 101))
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(19)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_9 = QtWidgets.QLabel(parent=self.page_3)
        self.label_9.setGeometry(QtCore.QRect(310, 250, 161, 101))
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(19)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_10 = QtWidgets.QLabel(parent=self.page_4)
        self.label_10.setGeometry(QtCore.QRect(300, 270, 161, 101))
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(19)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.label_11 = QtWidgets.QLabel(parent=self.page_5)
        self.label_11.setGeometry(QtCore.QRect(490, 290, 161, 101))
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(19)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.label_12 = QtWidgets.QLabel(parent=self.page_6)
        self.label_12.setGeometry(QtCore.QRect(360, 260, 161, 101))
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(19)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.label_13 = QtWidgets.QLabel(parent=self.page_7)
        self.label_13.setGeometry(QtCore.QRect(440, 300, 161, 101))
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(19)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.label_14 = QtWidgets.QLabel(parent=self.page_8)
        self.label_14.setGeometry(QtCore.QRect(510, 300, 161, 101))
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(19)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.stackedWidget.addWidget(self.page_8)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.label_15 = QtWidgets.QLabel(parent=self.page_9)
        self.label_15.setGeometry(QtCore.QRect(460, 300, 161, 101))
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(19)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.stackedWidget.addWidget(self.page_9)
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.label_16 = QtWidgets.QLabel(parent=self.page_10)
        self.label_16.setGeometry(QtCore.QRect(280, 310, 161, 101))
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(19)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.stackedWidget.addWidget(self.page_10)
        self.page_11 = QtWidgets.QWidget()
        self.page_11.setObjectName("page_11")
        self.label_17 = QtWidgets.QLabel(parent=self.page_11)
        self.label_17.setGeometry(QtCore.QRect(310, 320, 161, 101))
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(19)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.stackedWidget.addWidget(self.page_11)
        self.page_12 = QtWidgets.QWidget()
        self.page_12.setObjectName("page_12")
        self.label_18 = QtWidgets.QLabel(parent=self.page_12)
        self.label_18.setGeometry(QtCore.QRect(320, 280, 161, 101))
        font = QtGui.QFont()
        font.setFamily("Poppins SemiBold")
        font.setPointSize(19)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.stackedWidget.addWidget(self.page_12)
        self.verticalLayout_14.addWidget(self.main_screen_widget)
        self.gridLayout.addLayout(self.verticalLayout_14, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.delivery_btn2.toggled['bool'].connect(self.delivery_dropdown.hide) # type: ignore
        self.products_btn2.toggled['bool'].connect(self.products_dropdown.lower) # type: ignore
        self.finance_btn2.toggled['bool'].connect(self.finance_dropdown.hide) # type: ignore
        self.delivery_btn2.toggled['bool'].connect(self.delivery_dropdown.setHidden) # type: ignore
        self.products_btn2.toggled['bool'].connect(self.products_dropdown.setHidden) # type: ignore
        self.finance_btn2.toggled['bool'].connect(self.finance_dropdown.setHidden) # type: ignore
        self.dashboard_btn2.toggled['bool'].connect(self.dashboard_btn1.setChecked) # type: ignore
        self.delivery_btn2.toggled['bool'].connect(self.delivery_btn1.setChecked) # type: ignore
        self.order_btn2.toggled['bool'].connect(self.order_btn1.setChecked) # type: ignore
        self.finance_btn2.toggled['bool'].connect(self.finance_btn1.setChecked) # type: ignore
        self.products_btn2.toggled['bool'].connect(self.products_btn1.setChecked) # type: ignore
        self.settings_btn2.toggled['bool'].connect(self.settings_btn1.setChecked) # type: ignore
        self.logout_btn2.toggled['bool'].connect(self.logout_btn1.setChecked) # type: ignore
        self.logout_btn2.toggled['bool'].connect(MainWindow.close) # type: ignore
        self.logout_btn1.toggled['bool'].connect(MainWindow.close) # type: ignore
        self.pushButton.clicked['bool'].connect(self.icon_text_widget.setHidden) # type: ignore
        self.pushButton.toggled['bool'].connect(self.icon_only_widget.setVisible) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "E-Commerce"))
        self.deliveredOrders_btn.setText(_translate("MainWindow", "Delivered Orders"))
        self.paidOrders_btn.setText(_translate("MainWindow", "Paid Orders"))
        self.paiements_btn.setText(_translate("MainWindow", "Paiements"))
        self.expenses_btn.setText(_translate("MainWindow", "Expenses"))
        self.cash_btn.setText(_translate("MainWindow", "Cash"))
        self.revenues_btn.setText(_translate("MainWindow", "Revenues"))
        self.allProducts_btn.setText(_translate("MainWindow", "All Products"))
        self.addProduct_btn.setText(_translate("MainWindow", "Add Product"))
        self.inventory_btn.setText(_translate("MainWindow", "Inventory"))
        self.label.setText(_translate("MainWindow", "Hello, Imad"))
        self.label_5.setText(_translate("MainWindow", "Welcome to your page."))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Search here ..."))
        self.label_7.setText(_translate("MainWindow", "Dashboard"))
        self.label_8.setText(_translate("MainWindow", "Orders"))
        self.label_9.setText(_translate("MainWindow", "Delivred orders"))
        self.label_10.setText(_translate("MainWindow", "Paid Orders"))
        self.label_11.setText(_translate("MainWindow", "Paiments"))
        self.label_12.setText(_translate("MainWindow", "Expenses"))
        self.label_13.setText(_translate("MainWindow", "Cash"))
        self.label_14.setText(_translate("MainWindow", "Revenues"))
        self.label_15.setText(_translate("MainWindow", "All products"))
        self.label_16.setText(_translate("MainWindow", "Add product"))
        self.label_17.setText(_translate("MainWindow", "Invertory"))
        self.label_18.setText(_translate("MainWindow", "Settings"))
