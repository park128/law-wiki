import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

#데이터 베이스를 불러온다

def namecheck(nick_name):
    #대충 여기서 있는지 없는지를 확인한다.
    #불러와서 확인하는 방법으로 그리고 정렬까지
    conn_string="dbname='ddtk33j69v200c' host='ec2-54-225-234-165.compute-1.amazonaws.com' user='uxweficayqkvnb' password='191795f6687a563f2d49dd25fa1d4a3b481604b2bfb416f11811f430377a463f'"
    conn=db.connect(conn_string)
    script = 'SELECT * FROM public."user"'
    df = pd.read_sql(script, conn)
    print(df.head())

    sql = "SELECT * FROM user;"
    result = cursor.excute(sql)
    result = pd.DataFrame(result)
    #불러왔다.
    if result.find(nickname) == -1:
        sql = "INSERT INTO user(이름, 점수) VALUES ("+ nickname + ", 0)"
        cursor.excute(sql)

   
def countingstar():
    print("Tlqkf")   

def rankup():
    top5 = result.sort_values("점수", ascending=False)
    return top5.head