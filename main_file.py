import sys
from PyQt5.Qt import Qt
from PyQt5.QtCore import QTimer, QSize, pyqtSignal
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QToolTip, QMainWindow, QFileDialog, QLabel
from sqlmethods import SqlMethods
from loading_ui import Ui_loading_page
from log_in_ui import Ui_MainWindow
from register_ui import Ui_register_pool
from change_password_ui import Ui_change_password
from main_ui import Ui_Work_page


class QLableСlickable(QLabel):
    clicked = pyqtSignal()

    def __init__(self, widget, size, path):
        super().__init__(widget)
        self.setMaximumSize(QSize(size[0], size[1]))
        self.setCursor(Qt.PointingHandCursor)
        self.setPixmap(QPixmap(path))
        self.setScaledContents(True)
        self.setStyleSheet('border-style: solid; border-width: 3px; border-color: black;')

    def mousePressEvent(self, event):
        self.clicked.emit()


class MainWorkWindow(QMainWindow, Ui_Work_page):
    def __init__(self, tool):
        super().__init__()
        self.setupUi(self)

        self.tool = tool
        self.login_user = self.tool.login_user

        if not self.tool.sql_methods.check_last_login(self.tool.login_user):
            self.stackedWidget.setCurrentWidget(self.hello_new_user_page)
        else:
            self.stackedWidget.setCurrentWidget(self.welcome_back_page)

        self.load_window()

    def to_get_like_page_load(self):
        # load info page
        self.stackedWidget.setCurrentWidget(self.info_image_page)

        self.comments_view.clear()

        image = self.sender()

        if image in self.path_and_pixmap.keys():
            self.way = self.path_and_pixmap[image]
        elif image in self.path_and_pixmap_search.keys():
            self.way = self.path_and_pixmap_search[image]
        else:
            self.way = self.favorite_images[image]

        self.like_button.setIcon(QIcon(QPixmap(self.tool.sql_methods.check_like(self.way, self.login_user))))
        self.like_button.setIconSize(QSize(35, 35))

        self.tags_image.setText('tag: ' + '\n'.join(*self.tool.sql_methods.return_tags(self.way)))
        self.author_image.setText('author: ' + self.tool.sql_methods.who_author(self.way))
        self.title_image.setText('title: ' + self.tool.sql_methods.return_title(self.way))

        self.image.setPixmap(image.pixmap())
        self.comments_view.addItems(self.tool.sql_methods.return_comments(self.way))

    def to_search_page_load(self):
        # load search page
        self.stackedWidget.setCurrentWidget(self.search_page)

        self.tags.clear()
        self.authors.clear()

        self.tags.addItem('all')
        self.authors.addItem('all')
        tags = self.tool.sql_methods.return_tags_all()
        for x in tags:
            self.tags.addItem(x[0])

        authors = self.tool.sql_methods.return_authors_all()
        for x in authors:
            self.authors.addItem(x[0])

    def to_profile_page_load(self):
        # load profile page
        self.stackedWidget.setCurrentWidget(self.profile_page)

        self.frame_2.hide()

        self.comboBox.clear()
        images = self.tool.sql_methods.return_author_image(self.login_user)
        for x in images:
            self.comboBox.addItem(x[0])

    def add_image(self):
        """
        This method upload new image to database.
        """
        if self.choose_path_line.text() == '':
            self.verdict.setText('verdict: you didnt choose a photo')
        elif self.write_tags_line.text() == '':
            self.verdict.setText('verdict: you didnt write a tag')
        elif self.write_title_line.text() == '':
            self.verdict.setText('verdict: you didnt write a title')
        else:
            self.verdict.setText('verdict: ok!')

            path = self.tool.sql_methods.copy_and_add_new_image(self.choose_path_line.text(), self.login_user,
                                                                self.write_tags_line.text(),
                                    self.write_title_line.text())

            self.load_images([(path,)], self.layout_for_img, self.path_and_pixmap, (350, 200))

    def choose_image(self):
        """
        This method takes the path to the image.
        """
        path = QFileDialog.getOpenFileName(self, 'Выбрать картинку', './', "Image (*.png *.jpg *jpeg)")[0]
        self.choose_path_line.setText(path)
        self.view_image.setPixmap(QPixmap(path))

    def add_like(self):
        """
        This method check status, change icon QPushButton and add new info to database.
        """
        value = self.tool.sql_methods.add_like(self.way, self.login_user)
        self.like_button.setIcon(QIcon(QPixmap(self.tool.sql_methods.check_like(self.way, self.login_user))))
        self.like_button.setIconSize(QSize(35, 35))
        if value:
            self.load_images([(self.way,)], self.gridLayout, self.favorite_images, (350, 200))
        else:
            self.close_object(self.favorite_images, self.way, 'image_program/not found.png')

    def search_images(self):
        """
        This method displays photos based on the specified parameters.
        """
        images = self.tool.sql_methods.return_way_images(self.tags.currentText(), self.authors.currentText())

        for x in self.path_and_pixmap_search.keys():
            self.verticalLayout_3.removeWidget(x)
            x.close()
        self.path_and_pixmap_search.clear()

        self.load_images(images, self.verticalLayout_3, self.path_and_pixmap_search, (860, 450), 1)

    def change_title_image(self):
        """
        This method changes the existing name.
        """
        self.tool.sql_methods.change_title(self.title_line.text(), self.comboBox.currentText())

    def add_comment(self):
        """
        This method adds a comment to the database.
        """
        self.comments_view.addItem(self.tool.sql_methods.add_comment(self.way, self.login_user,
                                                                     self.comment_line.text()))
        self.comment_line.clear()

    def upload_icon_profile(self):
        """
        This method upload a new profile icon
        """
        path = QFileDialog.getOpenFileName(self, 'Выбрать картинку', './', "Image (*.png *.jpg *jpeg)")[0]
        if path != '':
            self.tool.sql_methods.new_icon(path, self.login_user)
            self.load_profile_icon()

    def delete_image(self):
        """
        This method deletes photos on uploaded pages and from the database.
        """
        count, all_photos_favorite = self.tool.sql_methods.get_images_with_like(self.login_user)
        delete_path = self.comboBox.currentText()
        if delete_path in [x[0] for x in all_photos_favorite]:
            self.close_object(self.favorite_images, delete_path, 'image_program\delete_pic.png')

        self.tool.sql_methods.delete_img(delete_path)
        self.comboBox.clear()
        images = self.tool.sql_methods.return_author_image(self.login_user)
        for x in images:
            self.comboBox.addItem(x[0])

        self.close_object(self.path_and_pixmap, delete_path, 'image_program\delete_pic.png')

    def close_object(self, path_and_image, delete_path, path):
        """
        This method closes the object.
        """
        for key, item in path_and_image.items():
            if path_and_image[key] == delete_path:
                key.setPixmap(QPixmap(path))
                key.setEnabled(False)

    def load_image_on_profile_page(self):
        """
        This method load image on profile page.
        """
        self.image_on_profile_page.setPixmap(QPixmap(self.comboBox.currentText()))
        self.image_on_profile_page.setScaledContents(True)

    def load_images(self, photos, layout, path_and_image, size, type=0):
        """
        This method uploads photos on the main pages.
        """
        for x in photos:
            label = QLableСlickable(self, size, x[0])
            label.clicked.connect(self.to_get_like_page_load)
            path_and_image[label] = x[0]
            if type:
                layout.addWidget(label)
            else:
                layout.addWidget(label, layout.count() // 3, layout.count() % 3)

    def load_profile_icon(self):
        """
        This method load profile icon.
        """
        icon = QPixmap(self.tool.sql_methods.return_icon(self.login_user))
        self.to_profile_page.setIcon(QIcon(QPixmap(self.tool.sql_methods.return_icon(self.login_user))))
        self.to_profile_page.setIconSize(QSize(35, 35))
        self.avatar.setPixmap(icon)
        self.avatar.setScaledContents(True)

    def load_window(self):
        # buttons on command_frame
        self.to_profile_page.clicked.connect(self.to_profile_page_load)
        self.to_search_page.clicked.connect(self.to_search_page_load)
        self.add_new_image.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.add_new_image_page))
        self.to_home_page.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.home_page))
        self.to_favorite_page.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.favorite_page))
        # buttons on add_new_image_page
        self.choose_path_button.clicked.connect(self.choose_image)
        self.add_image_button.clicked.connect(self.add_image)
        # button on search_page
        self.search_button.clicked.connect(self.search_images)
        # buttons on info_image_page
        self.like_button.clicked.connect(self.add_like)
        self.add_comment_button.clicked.connect(self.add_comment)
        # buttons on profile_page
        self.upload_icon.clicked.connect(self.upload_icon_profile)
        self.delete_button.clicked.connect(self.delete_image)
        self.change_title_button.clicked.connect(lambda: self.frame_2.show())
        self.accept_button.clicked.connect(self.change_title_image)
        self.comboBox.currentIndexChanged[str].connect(self.load_image_on_profile_page)
        # create arrays
        self.path_and_pixmap = {}
        self.path_and_pixmap_search = {}
        self.favorite_images = {}
        # load home_page and favorites_page
        count, all_photos = tool.sql_methods.get_images_with_like(self.login_user)
        self.load_images(all_photos, self.gridLayout, self.favorite_images, (350, 200))
        count, all_photos = tool.sql_methods.get_count_photos()
        self.load_images(all_photos, self.layout_for_img, self.path_and_pixmap, (350, 200))
        # load profile icon
        self.load_profile_icon()
        # set text
        self.login_label.setText(self.login_user)
        # load QLable on info page
        self.image.setStyleSheet('border-style: solid; border-width: 3px; border-color: black;')
        self.image.setScaledContents(True)
        # Set layout to scrollareas
        self.scrollAreaWidgetContents_4.setLayout(self.verticalLayout_3)
        self.scrollAreaWidgetContents_3.setLayout(self.gridLayout)
        self.scrollAreaWidgetContents_2.setLayout(self.layout_for_img)


class ChangePasswordWindow(QMainWindow, Ui_change_password):
    def __init__(self, tool):
        super().__init__()
        self.setupUi(self)

        self.tool = tool

        self.timer = QTimer()
        self.tool.load_hints(self.password_line)

        self.buttons_load()

        self.mistacke_frame.hide()
        self.style_for_ok_verdict, self.style_for_not_ok_verdict = return_styles()

    def change_password(self):
        data = [self.login_line.text(), self.code_word_line.text(),
                self.password_line.text(), self.repeat_password_line.text()]
        verdict = self.tool.sql_methods.change_password_user(data)
        if verdict == 'Ok. Wait about five seconds. We are cooking cakes.':
            self.tool.show_verdict(self.mistacke_frame, self.style_for_ok_verdict, self.name_error, verdict)

            self.timer.start(3000)
            self.timer.timeout.connect(lambda: self.tool.change_page(MainWindow, self.timer))
        else:
            self.tool.show_verdict(self.mistacke_frame, self.style_for_not_ok_verdict, self.name_error, verdict)

    def buttons_load(self):
        self.back.clicked.connect(lambda: self.tool.change_page(MainWindow))
        self.hide_error.clicked.connect(lambda: self.mistacke_frame.hide())
        self.change_password_butn.clicked.connect(self.change_password)


class RegisterWindow(QMainWindow, Ui_register_pool):
    def __init__(self, tool):
        super().__init__()
        self.setupUi(self)

        self.tool = tool

        self.timer = QTimer()

        self.buttons_load()

        self.mistacke_frame.hide()

        self.tool.load_hints(self.password_line, self.login_line, self.code_word_line)
        self.style_for_ok_verdict, self.style_for_not_ok_verdict = return_styles()

    def registration(self):
        data = [self.login_line.text(), self.password_line.text(),
                self.repeat_pass_line.text(), self.code_word_line.text()]
        verdict = self.tool.sql_methods.registration_new_user(data)
        if verdict == 'Ok. Wait about five seconds. We are cooking cakes.':
            self.tool.show_verdict(self.mistacke_frame, self.style_for_ok_verdict, self.name_error, verdict)

            self.timer.start(3000)
            self.timer.timeout.connect(lambda: self.tool.change_page(MainWindow, self.timer))
        else:
            self.tool.show_verdict(self.mistacke_frame, self.style_for_not_ok_verdict, self.name_error, verdict)

    def buttons_load(self):
        self.register_3.clicked.connect(self.registration)
        self.back.clicked.connect(lambda: self.tool.change_page(MainWindow))
        self.hide_error.clicked.connect(lambda: self.mistacke_frame.hide())


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, tool):
        super().__init__()
        self.setupUi(self)

        self.timer = QTimer()
        self.tool = tool
        self.buttons_load()
        self.mistacke.hide()
        self.style_for_ok_verdict, self.style_for_not_ok_verdict = return_styles()

    def logs_in(self):
        data = [self.login_line.text(), self.password_line.text()]
        verdict = self.tool.sql_methods.log_in_user(data)
        if verdict == 'Log in complete.':
            self.tool.show_verdict(self.mistacke, self.style_for_ok_verdict, self.name_error, verdict)

            self.timer.start(2000)
            self.tool.remember_login(self.login_line.text())
            self.timer.timeout.connect(lambda: self.tool.change_page(MainWorkWindow, self.timer))
        else:
            self.tool.show_verdict(self.mistacke, self.style_for_not_ok_verdict, self.name_error, verdict)

    def buttons_load(self):
        self.hide_error.clicked.connect(lambda: self.mistacke.hide())
        self.log_in.clicked.connect(self.logs_in)
        self.register_2.clicked.connect(lambda: self.tool.change_page(RegisterWindow))
        self.forgotpass.clicked.connect(lambda: self.tool.change_page(ChangePasswordWindow))


class LoadingPage(QMainWindow, Ui_loading_page):
    def __init__(self, tool):
        super().__init__()
        self.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.timer = QTimer()
        self.timer.start(3000)
        self.timer.timeout.connect(lambda: tool.change_page(MainWindow, self.timer))


class MainTool:
    def __init__(self):
        self.sql_methods = SqlMethods()
        self.currentpage = LoadingPage(self)
        self.currentpage.show()

        QToolTip.setFont(QFont('Segoe UI Semibold', 10))

    def change_page(self, name, timer=None):
        if timer is not None:
            timer.stop()
        self.currentpage.close()
        self.currentpage = name(self)
        self.currentpage.show()
        self.currentpage.setWindowTitle('Cyber Wallpaper')
        self.currentpage.setWindowIcon(QIcon('image_program/logo.png'))

    def remember_login(self, login):
        self.login_user = login

    def load_hints(self, password, login=None, code_word=None):
        if code_word is not None:
            code_word.setToolTip('the code word must consist of \n at least 5 characters')
        if login is not None:
            login.setToolTip('the login must consist of \n at least 5 of any characters')
        password.setToolTip('the password must be at least \n 8 characters long'
                            ' and contain \n at least one uppercase and uppercase letter')

    def show_verdict(self, frame, style, name_error, verdict):
        frame.setStyleSheet(style)
        name_error.setText(verdict)
        frame.show()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


def return_styles():
    return (("QFrame{\n"
             "    border-radius: 5px;\n"
             "    background-color: rgb(93, 255, 104);\n"
             "}"),
        ("QFrame{\n"
         "    border-radius: 5px;\n"
         "    background-color: rgb(255, 84, 84);\n"
         "}"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tool = MainTool()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
