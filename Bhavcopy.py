import requests
import datetime
import html5lib
from bs4 import BeautifulSoup
import pandas as pd
from pymysql import *
from pygubu import *


class Records :


    # def download(self):
    #     url="https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx"
    #     r=requests.get(url)
    #     print(r.status_code)
    #     soup = BeautifulSoup(r.content,"html5lib")
    #     print ( soup.prettify() )

    def Store(self) :
        conn = connect ( host = 'Localhost' , database = 'code' , user = 'root' , password = '' )
        cur = conn.cursor ()
        data = pd.read_csv ( 'EQ310720.CSV' )
        df = pd.DataFrame ( data = data )
        print ( df.keys () )
        for rows in df.itertuples () :
            query='insert into store1(code,name,open,high,low,close) values("%s","%s","%s","%s","%s","%s")'
            args=(str(rows.SC_CODE ), str(rows.SC_NAME) , str(rows.OPEN) , str(rows.HIGH) , str(rows.LOW) , str(rows.CLOSE))
            cur.execute(query % args)
        conn.commit ()
        conn.close ()


    def view(self) :
        conn = connect ( host = 'Localhost' , database = 'code' , user = 'root' , password = '' )
        cur = conn.cursor ()
        query = "Select * from Store1 order by high limit 10"
        cur.execute( query )
        # result=cur.fetchall()
        print('code name open high low close')
        for code,name,open,high,low,close in cur.fetchall():
            print("{} {} {} {} {} {}".format(code,name,open,high,low,close))
        conn.commit ()
        conn.close ()

    def view_by_name(self , name) :
        conn = connect ( host = 'Localhost' , database = 'code' , user = 'root' , password = '' )
        cur = conn.cursor ()
        self.name = name
        query = "Select * from Store1 where name=%s"
        args = (self.name)
        cur.execute ( query , args )
        for code,name,open,high,low,close in cur.fetchall():
            print("{} {} {} {} {} {}".format(code,name,open,high,low,close))
        conn.commit ()
        conn.close ()



while True :
    record = Records ()
    print (
        """1.Download Today's File and Save the Records in DB \n2.View top 10 Stock Entries\n3.View Records\n4.Exit""" )
    option = int ( input ( "Enter the option" ) )
    if option == 1 :
        # record.download()
        record.Store ()
    elif option == 2 :
        record.view ()
    elif option == 3 :
        name = input ( "Enter name of enitity" )
        record.view_by_name ( name )

    elif option == 4 :
        quit ()
