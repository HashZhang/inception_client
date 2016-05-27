import MySQLdb
import logging
import json
from main.models import Inception

def max(numbers):
    ret = 0
    for number in numbers:
        if number > ret:
            ret = number
    return ret


def printResult(fields, results):
    numOfFields = len(fields);
    lengths = [];
    for i in range(0, 11, 1):
        numbers = []
        for result in results:
            numbers.append(len(str(result[i])))
        numbers.append(len(str(fields[i])))
        lengths.append(max(numbers));
    return str(printField(lengths, fields)) + str(printValue(lengths, results))


def printSeparator(lengths):
    str1 = "";
    for i in lengths:
        str1 += "+"
        for j in range(0, i + 1, 1):
            str1 += "-"
    str1 += "+\r\n"
    return str1


def printField(lengths, fields):
    leng = len(lengths)
    str1 = "";
    str1 += printSeparator(lengths)
    for i in range(0, leng, 1):
        str1 += "|"
        val1 = lengths[i]
        val2 = len(str(fields[i]))
        for j in range(0, val1 - val2 + 1, 1):
            str1 += " "
        str1 = str1 + str(fields[i])
    str1 += "|\r\n"
    return str1


def printValue(lengths, values):
    leng = len(lengths)
    str2 = ""
    str2 += printSeparator(lengths)
    for value in values:
        str1 = "";
        for i in range(0, leng, 1):
            str1 += "|"
            val1 = lengths[i]
            val2 = len(str(value[i]))
            for j in range(0, val1 - val2 + 1, 1):
                str1 += " "
            str1 = str1 + str(value[i])
        str1 += "|"
        str1.replace("\r", "")
        str1.replace("\n", "")
        str1 += "\r\n" + printSeparator(lengths)
        str2 += str1
    return str2


def convertJson(fields,values):
    length = len(fields)
    length2 = len(values)
    result = []
    for i in range(0,length2,1):
        a = []
        for j in range(0,length,1):
            b={}
            b[fields[j]]=values[i][j]
            a.append(b)
        result.append(a)
    return result;


def processSQL(sql):
    try:
        p = Inception.objects.get(isSelected=1)
        inceptionHost = p.address
        inceptionPort = p.port;
        inceptionUser = p.username
        inceptionpasswd = p.password
        conn = MySQLdb.connect(host=inceptionHost, user=inceptionUser, passwd=inceptionpasswd, db='', port=inceptionPort)
        cur = conn.cursor()
        ret = cur.execute(sql)
        result = cur.fetchall()
        num_fields = len(cur.description)
        field_names = [i[0] for i in cur.description]
        cur.close()
        conn.close()
        log = logging.getLogger('test1')
        log.info(printResult(field_names, result))
        ret = convertJson(field_names,result)
        return json.dumps(ret)
    except MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def checkSQL(sql):
    sql2 = str(sql).strip()
    sql2 = sql2.replace('\n','')
    if sql2=='':
        return 'None'
    else:
        return processSQL(sql);
#
# print processSQL('/*--user=root;--password=sf123456;--host=10.202.4.39;--execute=1;--port=3306;*/\
# inception_magic_start;\
# use db1;\
# insert into hotnews(id,title)values("19","title2");\
# inception_magic_commit;')