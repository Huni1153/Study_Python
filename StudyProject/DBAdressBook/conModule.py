from db.mdba import getConn

# conn = getConn()

def create_table():
    conn = getConn()
    cur = conn.cursor()
    cur.execute('''
    create table person (
     name varchar(20),
     age int,
     tel varchar(30))
     ''')

    conn.commit()
    conn.close()

def drop_talbe():
    conn = getConn()
    cur = conn.cursor()
    strSql = 'drop table person'
    cur.execute(strSql)

def insert_data():
    conn = getConn()
    cur = conn.cursor()
    strSql = 'insert into person (name, age, tel) values (%s,%s,%s)'
    strVal = '박세훈', 30, '010-5516-1153'
    cur.execute(strSql, strVal)
    conn.commit()
    conn.close()

def delete_data():
    conn = getConn()
    cur = conn.cursor()
    sql = 'delete from person where name = "test" '
    cur.execute(sql)
    conn.commit()
    conn.close()

def select_table():
    conn = getConn()
    cur = conn.cursor()
    strSql = "select * person"
    cur.execute(strSql)

    rs = cur.f



if __name__ == '__main__':
    pass
    #create_table()
    #drop_talbe()
    #insert_table()
    delete_data()