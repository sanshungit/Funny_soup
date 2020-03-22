import mysql.connector


class soup_insert():
    def __init__(self, db_name):
        self.cnn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='sanshun_1234',
            charset='utf8'
        )

        mycursor = self.cnn.cursor()
        # 创建数据库db_name并且使用此数据库
        mycursor.execute('create database if not exists ' + db_name + ' Character Set UTF8 COLLATE utf8_general_ci')
        mycursor.execute('use ' + db_name)
        self.cnn.commit()
        mycursor.close()
        print('Database Connected!!!')

    def db_close(self):
        self.cnn.close()

    def create_tab(self, tab_name):
        mycursor = self.cnn.cursor()
        str_sql = 'create table if not exists ' + tab_name + ''' (
        	soup_id int AUTO_INCREMENT PRIMARY KEY,
        	soup_text mediumtext
        	)engine=innodb default charset=utf8mb4'''
        mycursor.execute(str_sql)
        self.cnn.commit()
        mycursor.close()
        print('Table Created!!!')

    def insert_data(self, tab_name):
        mycursor = self.cnn.cursor()
        with open('毒鸡汤.txt', 'r', encoding='utf-8-sig') as f:
            for soup_cell in f.readlines():
                str_sql = 'INSERT INTO ' + tab_name + '(soup_text) values(\"%s\")'
                mycursor.execute(str_sql % soup_cell.splitlines()[0])
            f.close()
        self.cnn.commit()
        mycursor.close()


if __name__ == '__main__':
    in_mydb = soup_insert('soup_db')
    in_mydb.create_tab('soup_tb')
    in_mydb.insert_data('soup_tb')
    in_mydb.db_close()
