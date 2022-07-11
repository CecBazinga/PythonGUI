        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_10 = QVBoxLayout(self.page_home)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_6 = QLabel(self.page_home)
        self.label_6.setObjectName(u"label_6")
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(40)
        self.label_6.setFont(font5)
        self.label_6.setStyleSheet(u"")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_6)

        self.label = QLabel(self.page_home)
        self.label.setObjectName(u"label")
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(14)
        self.label.setFont(font6)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label)

        self.label_7 = QLabel(self.page_home)
        self.label_7.setObjectName(u"label_7")
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(15)
        self.label_7.setFont(font7)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_7)

        self.stackedWidget.addWidget(self.page_home)







        self.page_widgets = QWidget()
        self.page_widgets.setObjectName(u"page_widgets")
        self.verticalLayout_6 = QVBoxLayout(self.page_widgets)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.page_widgets)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.frame)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        #self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        #self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        #self.labelBoxBlenderInstalation.setFont(font1)
        #self.labelBoxBlenderInstalation.setStyleSheet(u"")

        #self.verticalLayout_8.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_7.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        #self.lineEdit = QLineEdit(self.frame_content_wid_1)
        #self.lineEdit.setObjectName(u"lineEdit")
        #self.lineEdit.setMinimumSize(QSize(0, 30))
        #self.lineEdit.setStyleSheet(u"QLineEdit {\n"
        #                            "	background-color: rgb(27, 29, 35);\n"
        #                            "	border-radius: 5px;\n"
        #                            "	border: 2px solid rgb(27, 29, 35);\n"
        #                            "	padding-left: 10px;\n"
        #                            "}\n"
        #                            "QLineEdit:hover {\n"
        #                            "	border: 2px solid rgb(64, 71, 88);\n"
        #                            "}\n"
        #                            "QLineEdit:focus {\n"
        #                            "	border: 2px solid rgb(91, 101, 124);\n"
        #                            "}")

        #self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton2")
        self.pushButton.setMaximumWidth(250)
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(45)
        self.pushButton.setFont(font8)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
                                       "	border: 2px solid rgb(52, 59, 72);\n"
                                       "	border-radius: 5px;	\n"
                                       "	background-color: rgb(52, 59, 72);\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "	background-color: rgb(57, 65, 80);\n"
                                       "	border: 2px solid rgb(61, 70, 86);\n"
                                       "}\n"
                                       "QPushButton:pressed {	\n"
                                       "	background-color: rgb(35, 40, 49);\n"
                                       "	border: 2px solid rgb(43, 50, 61);\n"
                                       "}")




        #self.pushButton = QPushButton(self.frame_content_wid_1)
        #self.pushButton.setObjectName(u"pushButton")
        #self.pushButton.setMinimumSize(QSize(150, 30))
        #font8 = QFont()
        #font8.setFamily(u"Segoe UI")
        #font8.setPointSize(9)
        #self.pushButton.setFont(font8)
        #self.pushButton.setStyleSheet(u"QPushButton {\n"
        #                           "	border: 2px solid rgb(52, 59, 72);\n"
        #                            "	border-radius: 5px;	\n"
        #                            "	background-color: rgb(52, 59, 72);\n"
        #                            "}\n"
        #                            "QPushButton:hover {\n"
        #                            "	background-color: rgb(57, 65, 80);\n"
        #                            "	border: 2px solid rgb(61, 70, 86);\n"
        #                            "}\n"
        #                            "QPushButton:pressed {	\n"
        #                            "	background-color: rgb(35, 40, 49);\n"
        #                            "	border: 2px solid rgb(43, 50, 61);\n"
        #                            "}")
        #icon3 = QIcon()
        #icon3.addFile(u":/16x16/icons/16x16/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        #self.pushButton.setIcon(icon3)



        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        #self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        #self.labelVersion_3.setObjectName(u"labelVersion_3")
        #self.labelVersion_3.setStyleSheet(u"color: rgb(98, 103, 111);")
        #self.labelVersion_3.setLineWidth(1)
        #self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        #self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_7.addWidget(self.frame_content_wid_1)


        self.verticalLayout_15.addWidget(self.frame_div_content_1)


        self.verticalLayout_6.addWidget(self.frame)

        #self.frame_2 = QFrame(self.page_widgets)
        #self.frame_2.setObjectName(u"frame_2")
        #self.frame_2.setMinimumSize(QSize(0, 150))
        #self.frame_2.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
        #                            "border-radius: 5px;")
        #self.frame_2.setFrameShape(QFrame.StyledPanel)
        #self.frame_2.setFrameShadow(QFrame.Raised)
        #self.verticalLayout_11 = QVBoxLayout(self.frame_2)
        #self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        #self.gridLayout_2 = QGridLayout()
        #self.gridLayout_2.setObjectName(u"gridLayout_2")
        #self.checkBox = QCheckBox(self.frame_2)
        #self.checkBox.setObjectName(u"checkBox")
        #self.checkBox.setAutoFillBackground(False)
        #self.checkBox.setStyleSheet(u"")

        #self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        #self.radioButton = QRadioButton(self.frame_2)
        #self.radioButton.setObjectName(u"radioButton")
        #self.radioButton.setStyleSheet(u"")

        #self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        #self.verticalSlider = QSlider(self.frame_2)
        #self.verticalSlider.setObjectName(u"verticalSlider")
        #self.verticalSlider.setStyleSheet(u"")
        #self.verticalSlider.setOrientation(Qt.Vertical)

        #self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        #self.verticalScrollBar = QScrollBar(self.frame_2)
        #self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        #self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical {\n"
        #                                        "	border: none;\n"
        #                                        "    background: rgb(52, 59, 72);\n"
        #                                        "    width: 14px;\n"
        #                                        "    margin: 21px 0 21px 0;\n"
        #                                        "	border-radius: 0px;\n"
        #                                        " }")
        #self.verticalScrollBar.setOrientation(Qt.Vertical)

        #self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        #self.scrollArea = QScrollArea(self.frame_2)
        #self.scrollArea.setObjectName(u"scrollArea")
        #self.scrollArea.setStyleSheet(u"QScrollArea {\n"
        #                                "	border: none;\n"
        #                                "	border-radius: 0px;\n"
        #                                "}\n"
        #                                "QScrollBar:horizontal {\n"
        #                                "    border: none;\n"
        #                                "    background: rgb(52, 59, 72);\n"
        #                                "    height: 14px;\n"
        #                                "    margin: 0px 21px 0 21px;\n"
        #                                "	border-radius: 0px;\n"
        #                                "}\n"
        #                                " QScrollBar:vertical {\n"
        #                                "	border: none;\n"
        #                               "    background: rgb(52, 59, 72);\n"
        #                                "    width: 14px;\n"
        #                                "    margin: 21px 0 21px 0;\n"
        #                                "	border-radius: 0px;\n"
        #                                " }\n"
        #                                "")
        #self.scrollArea.setFrameShape(QFrame.NoFrame)
        #self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        #self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        #self.scrollArea.setWidgetResizable(True)
        #self.scrollAreaWidgetContents = QWidget()
        #self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        #self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 274, 218))
        #self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        #self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        #self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        #self.plainTextEdit.setObjectName(u"plainTextEdit")
        #self.plainTextEdit.setMinimumSize(QSize(200, 200))
        #self.plainTextEdit.setStyleSheet(u"QPlainTextEdit {\n"
        #                                    "	background-color: rgb(27, 29, 35);\n"
        #                                    "	border-radius: 5px;\n"
        #                                    "	padding: 10px;\n"
        #                                    "}\n"
        #                                    "QPlainTextEdit:hover {\n"
        #                                    "	border: 2px solid rgb(64, 71, 88);\n"
        #                                    "}\n"
        #                                    "QPlainTextEdit:focus {\n"
        #                                    "	border: 2px solid rgb(91, 101, 124);\n"
        #                                    "}")

        #self.horizontalLayout_11.addWidget(self.plainTextEdit)

        #self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        #self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        #self.comboBox = QComboBox(self.frame_2)
        #self.comboBox.addItem("")
        #self.comboBox.addItem("")
        #self.comboBox.addItem("")
        #self.comboBox.setObjectName(u"comboBox")
        #self.comboBox.setFont(font8)
        #self.comboBox.setAutoFillBackground(False)
        #self.comboBox.setStyleSheet(u"QComboBox{\n"
        #                            "	background-color: rgb(27, 29, 35);\n"
        #                            "	border-radius: 5px;\n"
        #                            "	border: 2px solid rgb(27, 29, 35);\n"
        #                            "	padding: 5px;\n"
        #                            "	padding-left: 10px;\n"
        #                            "}\n"
        #                            "QComboBox:hover{\n"
        #                            "	border: 2px solid rgb(64, 71, 88);\n"
        #                            "}\n"
        #                            "QComboBox QAbstractItemView {\n"
        #                            "	color: rgb(85, 170, 255);	\n"
        #                            "	background-color: rgb(27, 29, 35);\n"
        #                            "	padding: 10px;\n"
        #                            "	selection-background-color: rgb(39, 44, 54);\n"
        #                            "}")
        #self.comboBox.setIconSize(QSize(16, 16))
        #self.comboBox.setFrame(True)

        #self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        #self.horizontalScrollBar = QScrollBar(self.frame_2)
        #self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        #sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        #sizePolicy5.setHorizontalStretch(0)
        #sizePolicy5.setVerticalStretch(0)
        #sizePolicy5.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        #self.horizontalScrollBar.setSizePolicy(sizePolicy5)
        #self.horizontalScrollBar.setStyleSheet(u"QScrollBar:horizontal {\n"
        #                                       "    border: none;\n"
        #                                        "    background: rgb(52, 59, 72);\n"
        #                                        "    height: 14px;\n"
        #                                        "    margin: 0px 21px 0 21px;\n"
        #                                        "	border-radius: 0px;\n"
        #                                        "}\n"
        #                                        "")
        #self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        #self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        #self.commandLinkButton = QCommandLinkButton(self.frame_2)
        #self.commandLinkButton.setObjectName(u"commandLinkButton")
        #self.commandLinkButton.setStyleSheet(u"QCommandLinkButton {	\n"
        #                                        "	color: rgb(85, 170, 255);\n"
        #                                        "	border-radius: 5px;\n"
        #                                        "	padding: 5px;\n"
        #                                        "}\n"
        #                                        "QCommandLinkButton:hover {	\n"
        #                                        "	color: rgb(210, 210, 210);\n"
        #                                        "	background-color: rgb(44, 49, 60);\n"
        #                                        "}\n"
        #                                        "QCommandLinkButton:pressed {	\n"
        #                                        "	color: rgb(210, 210, 210);\n"
        #                                        "	background-color: rgb(52, 58, 71);\n"
        #                                        "}")
        #icon4 = QIcon()
        #icon4.addFile(u":/16x16/icons/16x16/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        #self.commandLinkButton.setIcon(icon4)

        #self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        #self.horizontalSlider = QSlider(self.frame_2)
        #self.horizontalSlider.setObjectName(u"horizontalSlider")
        #self.horizontalSlider.setStyleSheet(u"")
        #self.horizontalSlider.setOrientation(Qt.Horizontal)

        #self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        #self.verticalLayout_11.addLayout(self.gridLayout_2)


        #self.verticalLayout_6.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.page_widgets)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 150))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.frame_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 100):
            self.tableWidget.setRowCount(100)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font2);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush15 = QBrush(QColor(39, 44, 54, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush15)
        brush16 = QBrush(QColor(210, 210, 210, 128))
        brush16.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush16)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        brush17 = QBrush(QColor(210, 210, 210, 128))
        brush17.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        brush18 = QBrush(QColor(210, 210, 210, 128))
        brush18.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.tableWidget.setPalette(palette1)
        self.tableWidget.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        #self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_widgets)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_toggle_menu)
        QWidget.setTabOrder(self.btn_toggle_menu, self.tableWidget)
        #QWidget.setTabOrder(self.checkBox, self.comboBox)
        #QWidget.setTabOrder(self.comboBox, self.radioButton)
        #QWidget.setTabOrder(self.radioButton, self.horizontalSlider)
        #QWidget.setTabOrder(self.horizontalSlider, self.verticalSlider)
        #QWidget.setTabOrder(self.verticalSlider, self.scrollArea)
        #QWidget.setTabOrder(self.scrollArea, self.plainTextEdit)
        #QWidget.setTabOrder(self.plainTextEdit, self.tableWidget)
        #QWidget.setTabOrder(self.tableWidget, self.commandLinkButton)






        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QMetaObject.connectSlotsByName(MainWindow)


    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"Main Window - Base", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText(QCoreApplication.translate("MainWindow", u"C:\\Program Files\\Blender Foundation\\Blender 2.82", None))
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| HOME", None))
        self.label_user_icon.setText(QCoreApplication.translate("MainWindow", u"WM", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Let's have some tests! ", None))
        #self.label_7.setText(QCoreApplication.translate("MainWindow", u"Page Index 0", None))
        #self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"BLENDER INSTALLATION", None))
        #self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your Password", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"START", None))
        #self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Ex: C:Program FilesBlender FoundationBlender 2.82 blender.exe", None))
        #self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        #self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        #self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        #self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        #self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        #self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"CommandLinkButton", None))
        #self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Open External Link", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Username", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Password", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)




        #self.label_credits.setText(QCoreApplication.translate("MainWindow", u"Registered by: Wanderson M. Pimenta", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi