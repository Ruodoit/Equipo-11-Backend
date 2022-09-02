import mysql.connector, json
from flask import Flask, request, Response, render_template, jsonify

mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'
app=Flask(__name__)
cursor=mydb.cursor()
cursor.execute("select * from ventiladores;")
resultados=cursor.fetchall()

@app.route('/dispositivos/ventiladores',methods=['GET'])
def Ventiladores():
    resultado={"ventiladores":[]}
    i=0 
    while i <len(resultados):
        ventilador={"id":resultados[i][0],"estado":resultados[i ][1],"conexion":resultados[i][2],"nombre":resultados[i][3],"velocidad":resultados[i][4],"timer":resultados[i][5],"sleep":resultados[i][6],"swin":resultados[i][7]}
        i+=1
        resultado["ventiladores"].append(ventilador)
        print(ventilador)
    return resultado    
    
@app.route('/dispositivos/ventiladores/cambiarestado',methods=['GET','POST'])
def estado():
    global estado
    global ida
    mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'
    estado=request.args.get('estado')
    ida=request.args.get('id')
    cursor=mydb.cursor()
    sql=("UPDATE ventiladores SET estado = '"+estado+"' WHERE id = '"+ida+"';")
    cursor.execute(sql)
    resultado=cursor.fetchall() 
    mydb.commit()   
    
    if estado=='si':   
        return { "status": 200, "state": 'PRENDIDO'}
    elif estado=='no':
        return { "status": 200, "state":'APAGADO'}
    else:
        return 'OLEEEE!!!, PROBA DE NUEVO'
    
@app.route('/dispositivos/ventiladores/verificarconexion',methods=['GET','POST'])
def conexion():
    global conexion
    global idv
    mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'
    conexion=request.args.get('conexion')
    idv=request.args.get('id')
    cursor=mydb.cursor()
    sql=("UPDATE ventiladores SET conexion = '"+conexion+"' WHERE id = '"+idv+"';")
    cursor.execute(sql)
    resultado=cursor.fetchall() 
    mydb.commit()   
    
    if conexion=='si':   
        return { "status": 200, "state": 'CONECTADO'}
    elif conexion=='no':
        return { "status": 200, "state":'DESCONECTADO'}
    else:
        return 'OLEEEE!!!, PROBA DE NUEVO'

@app.route('/dispositivos/ventiladores/editarnombre',methods=['GET','POST'])
def nombre():
    global nombre
    global idv
    mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'
    nombre=request.args.get('nombre')
    idv=request.args.get('id')
    cursor=mydb.cursor()
    sql=("UPDATE ventiladores SET nombre = '"+nombre+"' WHERE id = '"+idv+"';")
    cursor.execute(sql)
    resultado=cursor.fetchall() 
    mydb.commit()   
    
    print(nombre)
    return { "status": 200, "state": "OK" }
        
@app.route('/dispositivos/ventiladores/cambiarvelocidad',methods=['GET','POST'])
def velocidad():
    global velocidad
    global idv
    mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'
    velocidad=request.args.get('velocidad')
    idv=request.args.get('id')
    cursor=mydb.cursor()
    sql=("UPDATE ventiladores SET velocidad = '"+velocidad+"' WHERE id = '"+idv+"';")
    cursor.execute(sql)
    resultado=cursor.fetchall() 
    mydb.commit()   
    
    if velocidad=='0':
        return { "status": 200, "state": "APAGADO" }
    elif velocidad=='1':
        return { "status": 200, "state": "VELOCIDAD 1" }
    elif velocidad=='2':
        return { "status": 200, "state": "VELOCIDAD 2" }
    elif velocidad=='3':
        return { "status": 200, "state": "VELOCIDAD 3" }
    elif velocidad=='4':
        return { "status": 200, "state": "VELOCIDAD 4" }
    elif velocidad=='5':
        return { "status": 200, "state": "VELOCIDAD 5" }                
    else:
        return 'OLEEEE!!!, PROBA DE NUEVO'

@app.route('/dispositivos/ventiladores/activartimer',methods=['GET','POST'])
def timer():
    global timer
    global idv
    mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'
    timer=request.args.get('timer')
    idv=request.args.get('id')
    cursor=mydb.cursor()
    sql=("UPDATE ventiladores SET timer = '"+timer+"' WHERE id = '"+idv+"';")
    cursor.execute(sql)
    resultado=cursor.fetchall() 
    mydb.commit()   
    
    
    print(timer)
    return { "status": 200, "state": "OK" }

@app.route('/dispositivos/ventiladores/activarsleep',methods=['GET','POST'])
def sleep():
    global sleep
    global idv
    mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'
    sleep=request.args.get('sleep')
    idv=request.args.get('id')
    cursor=mydb.cursor()
    sql=("UPDATE ventiladores SET sleep = '"+sleep+"' WHERE id = '"+id+"';")
    cursor.execute(sql)
    resultado=cursor.fetchall() 
    mydb.commit()   
        
    print(sleep)
    return { "status": 200, "state": "OK" }

@app.route('/dispositivos/ventiladores/activarswin',methods=['GET','POST'])
def swin():
    global swin
    global idv
    mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'
    swin=request.args.get('swin')
    idv=request.args.get('id')
    cursor=mydb.cursor()
    sql=("UPDATE ventiladores SET swin = '"+swin+"' WHERE id = '"+idv+"';")
    cursor.execute(sql)
    resultado=cursor.fetchall() 
    mydb.commit()   
        
    if swin=='si':   
        return { "status": 200, "state": 'ACTIVADO'}
    elif swin=='no':
        return { "status": 200, "state":'DESACTIVADO'}
    else:
        return 'OLEEEE!!!, PROBA DE NUEVO'

cursor.close()
mydb.close()

if __name__=='__main__':
    app.run(debug=True)   

