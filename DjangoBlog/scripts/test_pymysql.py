#coding=utf-8

import pymysql



def main():
    conn = pymysql.connections.Connection(host="mysql", 
                                          user="zhouxin", 
                                          password="782744680", 
                                          database="djangoblog", 
                                          port=3306)

    conn.begin()
    print(conn.open)
    print(conn.ping())


if __name__ == "__main__":
    main()