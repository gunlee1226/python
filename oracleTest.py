import cx_Oracle

# [아이디]/[비밀번호]@[서버 주소]/[SID] 형태로 들어가야 합니다.
connection = cx_Oracle.connect("gunlee/0000@localhost/orcl")

cursor = connection.cursor()


#query = ''' select date, name, content from sample_table where date between %s and %s ''' % (startDate, endDate)
query = ''' select KINDS_CODE, KINDS_NUM, KINDS_name from KINDS '''

# 실행을 시킵니다.
cursor.execute(query)
rows = cursor.fetchall()

print(rows)

connection.close

