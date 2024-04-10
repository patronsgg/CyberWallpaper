import sqlite3
import os
import shutil
import random
import hashlib


class SqlMethods:
    def __init__(self):
        self.con = sqlite3.connect('cyber_wallpapper.db')
        self.cur = self.con.cursor()

    def close_connect(self, cur, con):
        cur.close()
        con.close()

    def log_in_user(self, data):
        value = self.cur.execute('''SELECT login, password FROM users WHERE login=?''', (data[0],)).fetchall()

        if '' in data:
            return 'The fields are empty.'
        if len(value) == 0:
            return 'This user does not exist'
        if value[0][1] == hashlib.sha1(data[1].encode()).hexdigest():
            return 'Log in complete.'
        return 'Invalid password.'

    def registration_new_user(self, data):
        if '' in data:
            return 'The fields are empty.'
        if data[1] != data[2]:
            return 'Password disagree.'
        if len(data[1]) < 8:
            return 'Password is too short'
        if data[1].islower() or data[1].isupper() or data[1].isdigit():
            return 'Invalid password for registration'
        if len(data[0]) < 5:
            return 'Login is short'
        if len(data[3]) < 5:
            return 'Code word is short'
        con = sqlite3.connect('cyber_wallpapper.db')
        cur = con.cursor()
        value = cur.execute('''SELECT login FROM users WHERE login=?''', (data[0], )).fetchall()

        if value != []:
            return 'The user with this username is already registered.'

        cur.execute('''INSERT INTO users (login, password, code_word, icon) VALUES(?, ?, ?, ?)''',
                    (data[0], hashlib.sha1(data[1].encode()).hexdigest(),
                     hashlib.sha1(data[3].encode()).hexdigest(), 'image_program\\profile.png'))
        con.commit()
        return 'Ok. Wait about five seconds. We are cooking cakes.'

    def change_password_user(self, data):
        if '' in data:
            return 'The fields are empty.'
        if data[3] != data[2]:
            return 'Password disagree.'
        if len(data[2]) < 8:
            return 'Password is too short'
        if data[2].islower() or data[2].isupper() or data[2].isdigit():
            return 'Invalid password for registration'
        con = sqlite3.connect('cyber_wallpapper.db')
        cur = con.cursor()
        value = [x[0] for x in cur.execute('''SELECT login FROM users WHERE login=?''', (data[0],)).fetchall()]

        if data[0] not in value:
            return 'There is no such user.'

        if hashlib.sha1(data[1].encode()).hexdigest() != cur.execute('''SELECT code_word 
        FROM users WHERE login=?''', (data[0],)).fetchall()[0][0]:
            return 'Invalid code word.'

        cur.execute('''UPDATE users SET password=? WHERE login=?''', (hashlib.sha1(data[2].encode()).hexdigest(), data[0],))
        con.commit()
        return 'Ok. Wait about five seconds. We are cooking cakes.'

    def check_last_login(self, login):
        value = self.cur.execute('''SELECT last_login FROM users WHERE login=?''', (login, )).fetchall()
        if value[0][0] is None:
            self.add_last_login(login, self.con, self.cur)
            return False
        else:
            self.add_last_login(login, self.con, self.cur)
            return True

    def add_last_login(self, login, con, cur):
        cur.execute('''UPDATE users SET last_login=? WHERE login=?''', ('+', login,))
        con.commit()

    def get_count_photos(self):
        value = self.cur.execute('''SELECT url FROM images''').fetchall()
        return (len(value), value)

    def copy_and_add_new_image(self, way, login_user, tag, title):
        name_file = 'image/' + str(random.randint(10 ** 3, 10 ** 4 - 1)) + way[way.rfind('.'):]
        shutil.copy(way, name_file)
        if len(self.cur.execute('''SELECT * FROM tags WHERE title=?''', (tag,)).fetchall()) == 0:
            self.cur.execute('''INSERT INTO tags (title) VALUES(?)''', (tag,))
        self.cur.execute('''INSERT INTO images (url, count_like, author, title) VALUES(?, ?, ?, ?)''',
                    (name_file, 0, login_user, title))
        id_img = self.cur.execute('''SELECT id FROM images WHERE url = ?''', (name_file,)).fetchall()[0][0]
        id_tag = self.cur.execute('''SELECT id FROM tags WHERE title=?''', (tag,)).fetchall()[0][0]
        self.cur.execute('''INSERT INTO images_tags (id_img, id_tag) VALUES(?, ?)''', (id_img, id_tag))
        self.con.commit()
        return name_file

    def add_like(self, way, login_user):
        id_img = self.cur.execute('''SELECT id FROM images WHERE url=?''', (way,)).fetchall()[0][0]
        if self.cur.execute('''SELECT * FROM users_likes WHERE id_img=? AND login_user=?''', (id_img, login_user,)).fetchall() == list():
            self.cur.execute('''UPDATE images SET count_like=count_like + 1 WHERE url=?''', (way,))
            self.cur.execute('''INSERT INTO users_likes (login_user, id_img) VALUES(?, ?)''', (login_user, id_img))
            self.con.commit()
            return True
        else:
            self.cur.execute('''UPDATE images SET count_like=count_like - 1 WHERE url=?''', (way,))
            self.cur.execute('''DELETE FROM users_likes WHERE login_user=? AND id_img=?''', (login_user, id_img))
            self.con.commit()
            return False

    def who_author(self, way):
        return self.cur.execute('''SELECT author FROM images WHERE url=?''', (way,)).fetchall()[0][0]

    def return_tags(self, way):
        value = self.cur.execute('''SELECT title FROM tags 
        WHERE id in (SELECT id_tag FROM images_tags 
        WHERE id_img in (SELECT id FROM images WHERE url=?))''', (way,)).fetchall()
        return value

    def return_tags_all(self):
        value = self.cur.execute('''SELECT title FROM tags''').fetchall()
        return value

    def check_like(self, way, login_user):
        if len(self.cur.execute('''SELECT * FROM users_likes 
        WHERE login_user=? AND id_img in (SELECT id FROM images WHERE url=?)''', (login_user, way)).fetchall()) == 0:
            return 'image_program/notlike.png'
        else:
            return 'image_program/like.png'

    def return_way_images(self, tag, author):
        if tag == 'all' and author == 'all':
            return self.cur.execute('''SELECT url FROM images''').fetchall()
        elif tag != 'all' and author == 'all':
            return self.cur.execute('''SELECT url FROM images WHERE id in (SELECT id_img FROM images_tags 
            WHERE id_tag in (SELECT id FROM tags WHERE title=?))''', (tag,)).fetchall()
        elif tag == 'all' and author != 'all':
            return self.cur.execute('''SELECT url FROM images WHERE author=?''', (author,)).fetchall()
        else:
            return self.cur.execute('''SELECT url FROM images WHERE author=? AND id in (SELECT id_img FROM images_tags 
                    WHERE id_tag in (SELECT id FROM tags WHERE title=?))''', (author, tag,)).fetchall()

    def get_images_with_like(self, login_user):
        value = self.cur.execute('''SELECT url FROM images WHERE id in (SELECT id_img FROM users_likes 
        WHERE login_user=?)''', (login_user,)).fetchall()
        return (len(value), value)

    def return_title(self, way):
        return self.cur.execute('''SELECT title FROM images WHERE url=?''', (way,)).fetchall()[0][0]

    def return_comments(self, way):
        return [': '.join(x) for x in self.cur.execute('''SELECT login_user, text FROM comments 
        WHERE id in (SELECT id_comment FROM images_comments 
        WHERE id_img in (SELECT id FROM images WHERE url=?))''', (way,)).fetchall()]

    def add_comment(self, way, login_user, comment):
        id_img = self.cur.execute('''SELECT id FROM images WHERE url=?''', (way,)).fetchall()[0][0]
        self.cur.execute('''INSERT INTO comments (text, login_user) VALUES (?, ?)''', (comment, login_user,))
        id_comment = self.cur.execute('''SELECT id FROM comments WHERE text=? AND login_user=?''',
                                 (comment, login_user, )).fetchall()[0][0]
        self.cur.execute('''INSERT INTO images_comments (id_img, id_comment) VALUES (?, ?)''', (id_img, id_comment))
        self.con.commit()
        return login_user + ': ' + comment

    def return_authors_all(self):
        return self.cur.execute('''SELECT DISTINCT author FROM images''').fetchall()

    def return_icon(self, login_user):
        return self.cur.execute('''SELECT icon FROM users WHERE login=?''', (login_user,)).fetchall()[0][0]

    def new_icon(self, path, login_user):
        name_file = 'image/' + str(random.randint(10 ** 3, 10 ** 4 - 1)) + path[path.rfind('.'):]
        shutil.copy(path, name_file)
        self.cur.execute('''UPDATE users SET icon=? WHERE login=?''', (name_file, login_user,))
        self.con.commit()

    def return_author_image(self, login_user):
        return self.cur.execute('''SELECT url FROM images WHERE author=?''', (login_user,)).fetchall()

    def change_title(self, title, path):
        self.cur.execute('''UPDATE images SET title=? WHERE url=?''', (title, path))
        self.con.commit()

    def delete_img(self, path):
        os.remove(path)
        id_img = self.cur.execute('''SELECT id FROM images WHERE url=?''', (path,)).fetchall()[0][0]
        self.cur.execute('''DELETE FROM images_comments WHERE id_img=?''', (id_img,))
        self.cur.execute('''DELETE FROM images_tags WHERE id_img=?''', (id_img,))
        self.cur.execute('''DELETE FROM users_likes WHERE id_img=?''', (id_img,))
        self.cur.execute('''DELETE FROM images WHERE id=?''', (id_img,))
        self.con.commit()
