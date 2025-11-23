from flask import Flask, request,make_response
from flask_cors import CORS
import json,sys,configparser
from flask_sqlalchemy import SQLAlchemy
from gevent import pywsgi

import os
config = configparser.ConfigParser()
config_file = os.environ.get('CONFIG_FILE', 'config.dev.ini')
config.read(config_file, encoding='utf-8')

app = Flask(__name__)
#browser security protocal
CORS(app, supports_credentials=True)

#initialize database
mysql=SQLAlchemy()
#database type+drive type://username:password@database address:API/database used
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://%s:%s@%s:%d/%s' %(
    config.get('mysql','user'),
    config.get('mysql','password'),
    config.get('mysql','host'),
    config.getint('mysql','port'),
    config.get('mysql','database')
)
app.config['SQLALCHEMY_ECHO'] = config.getboolean('mysql','debug')
mysql.init_app(app)

@app.after_request
def after_request(resp):
    resp.headers['Content-Type'] = 'application/json'
    return resp

@app.before_request
def before_request():
    if request.path=='/login' :
        return None
    if request.cookies.get('id') is None:
        return response(999,'please re-login')
    return None

@app.route('/teacher_lists',methods=['Get'] )
def teacher_lists():
    teachers_list=[]
    sql='select * from teachers'
    rets=query(sql)
    if len(rets)>0:
        for idx, row in enumerate(rets):
            teachers_list.append({'id':row['id'],'name':row['name']})
    return response(0,'ok',teachers_list)
@app.route('/teacher_add',methods=['POST'] )
def teacher_add():
    feild=[]
    vals={}
    if str(request.data)=='':
        return response(1,'index error')
    data=json.loads(request.data)
    if 'name' not in data:
        if data['name']=='':
            return response(1,'enter name')
    feild.append('name')
    vals['name']=data['name']
    if 'password' not in data:
        if data['password'] == '':
            return response(1,'enter password')
    feild.append('password')
    vals['password']=data['password']

    usql='select * from teachers where name=:name'
    rets=query(usql,{'name':data['name']})
    if len(rets)>0:
        return response(1,'duplicate name, please enter new name')

    sql='insert into teachers (%s) values (:%s)' % (','.join(feild),',:'.join(feild))
    print(sql)
    execute(sql,vals)
    return response(0,'ok')

@app.route('/teacher_delete',methods=['POST'] )
def teacher_delete():
    if str(request.data)=='':
        return response(1,'index error')
    param=json.loads(request.data)
    if 'id' not in param:
        return response(1,'index error')
    sql='delete from teachers where id=:id'
    execute(sql,{'id':param['id']})
    return response(0,'Deleted')
@app.route('/teacher_edit',methods=['POST'] )
def teacher_edit():
    field=[]
    vals={}

    if str(request.data)=='':
        return response(1,'index error')
    param=json.loads(request.data)
    if 'id' not in param:
        return response(1,'index error')
    vals['id']=param['id']

    usql='select * from teachers where id=:id'
    rets=query(usql,{'id':param['id']})
    if len(rets)==0:
        return response(1,'does not exist')


    nsql='select * from teachers where name=:name'
    nets=query(nsql,{'name':param['name']})
    if len(nets)>0 and nets[0]['id']!=param['id']:
        return response(1,'duplicate name, please enter new name')

    if 'name' in param:
        if param['name'] =='':
            return response(1,'name cannot be empty')
        field.append('name')
        vals['name']=param['name']


    if 'password' in param:
        if param['password'] =='':
            return response(1,'password cannot be empty')
        field.append('password')
        vals['password']=param['password']



    sets=[]
    [sets.append("%s=:%s" %(f,f)) for f in field]
    sql='update teachers set %s where id=:id' %(','.join(sets))
    execute(sql,vals)
    return response(0,'updated')




def searchdata(list,id):
    for i in range(len(list)):
        if list[i]['id'] == id:
            return list[i]
    return None
def editdata(list,id,data):
    for i in range(len(list)):
        if list[i]['id'] == id:
            list[i] = data
            return
    return

def deletedata(list,id):
    for i in range(len(list)):
        if list[i]['id'] == id:
            del list[i]
            return
    return
#search in sql
def query(sql,param=None):
    ress=mysql.session.execute(sql,param)
    data=[dict(zip(result.keys(),result)) for result in ress]
    return data

#write in sql
def execute(sql,param=None):
    result=mysql.session.execute(sql,param)
    mysql.session.commit()
    return result
@app.route('/login',methods=['POST'] )
def login():

    param=json.loads(request.data)
    if 'name' not in param:
        return response(1000,'enter your name')
    if 'password' not in param:
        return response(1001,'enter your password')
    sql="SELECT * FROM `teachers` WHERE name=:name"
    ret=query(sql,{'name':param['name']})
    if len(ret)>0 and ret[0]['password']==param['password']:
        resp = response(0, 'ok', {'id':ret[0]['id'], 'name': ret[0]['name']})
        resp.set_cookie('id',str(ret[0]['id']), max_age=3600)
        return resp
    return response(2000,'unauthorized')

@app.route('/logout',methods=['POST'] )
def logout():
    resp=response(0,'logged out')
    resp.delete_cookie('id')
    return resp

def response(code,message,data:any=None):
    res={'code':code,'message':message,'data':{}}
    if data is not None:
        if hasattr(data,'__dict__'):
            res['data']=data.__dict__
        else:
            res['data']=data
    return make_response(json.dumps(res,sort_keys=True,ensure_ascii=False),200)


@app.route('/student_lists',methods=['Get'] )
def student_lists():
    student_list = []
    sql = 'select * from students'
    rets = query(sql)
    if len(rets) > 0:
        for idx, row in enumerate(rets):
            student_list.append({'id': row['id'], 'name': row['name'],'english':float(row['english']),'physics':float(row['physics']),'math':float(row['math'])})
    return response(0,'ok',student_list)


@app.route('/student_add',methods=['POST'] )
def student_add():
    field=[]
    vals={}
    if str(request.data)=='':
        return response(1,'index error')

    data=json.loads(request.data)
    if 'name' not in data:
        return response(1,'enter name')
    field.append('name')
    vals['name']=data['name']

    usql = 'select * from students where name=:name'
    rets= query(usql,{'name':data['name']})
    if len(rets)>0:
        return response(1,'duplicate name, please enter new name')
    if 'math' in data:
        field.append('math')
        vals['math']=float(data['math'])
    if 'english' in data:
        field.append('english')
        vals['english']=float(data['english'])
    if 'physics' in data:
        field.append('physics')
        vals['physics']=float(data['physics'])

    sql='insert into students (%s) values (:%s)' % (', '.join(field),',:'.join(field))
    execute(sql,vals)
    return response(0,'ok')

@app.route('/student_delete',methods=['POST'] )
def student_delete():

    if str(request.data)=='':
        return response(1,'index error')
    param=json.loads(request.data)
    if 'id' not in param:
        return response(1,'index error')
    sql='delete from students where id=:id'
    execute(sql,{'id':param['id']})
    return response(0,'Deleted')

@app.route('/student_edit',methods=['POST'] )
def student_edit():
    field=[]
    vals={}
    if str(request.data)=='':
        return response(1,'index error')
    param=json.loads(request.data)
    if 'id' not in param:
        return response(1,'index error')
    vals['id']=param['id']

    if 'name' not in param:
        return response(1,'name cannot be empty')
    field.append('name')
    vals['name']=param['name']

    usql='select * from students where id=:id'
    rets= query(usql,{'id':param['id']})
    if len(rets)==0:
        return response(1,'student not found')


    if 'math' in param:
        field.append('math')
        vals['math']=float(param['math'])
    if 'english' in param:
        field.append('english')
        vals['english']=float(param['english'])
    if 'physics' in param:
        field.append('physics')
        vals['physics']=float(param['physics'])

    sets = []
    [sets.append("%s=:%s" % (f, f)) for f in field]
    sql = 'update students set %s where id=:id' % (','.join(sets))
    execute(sql, vals)


    return response(0,'updated')

if __name__ == '__main__':
    #app.run(port=9000)
    server=pywsgi.WSGIServer(("0.0.0.0", config.getint('server','port')), app)
    server.serve_forever()