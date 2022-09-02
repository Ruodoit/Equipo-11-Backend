import mysql.connector
from flask import Flask, request, Response, jsonify, render_template

mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",
user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'

app=Flask(__name__)
cursor=mydb.cursor()
cursor.execute("select * from aireacondicionado;")
resultados=cursor.fetchall()

@app.route('/dispositivos/aireacondicionado',methods=['GET'])
def aires():
    resultado={"aires":[]}
    i=0
    while i <len(resultados):
        aire={"id":resultados[i][0],"estado":resultados[i ][1],"conexion":resultados[i][2],"nombre":resultados[i][3],"temperatura":resultados[i][4],"fan":resultados[i][5],"swin":resultados[i][6],"timer":resultados[i][7],"sleep":resultados[i][8],"modo":resultados[i][9],"direccion":resultados[i][10]}
        i+=1
        resultado["aires"].append(aire)
        print(aire)
      
    return resultado

@app.route('/dispositivos/aireacondicionado/cambiarestado',methods=['GET','POST'])
def estado():
    global estado
    global ida
    mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",
user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'
    ida=request.args.get('id')
    estado=request.args.get('estado')
    cursor=mydb.cursor()
    sql=("UPDATE aireacondicionado SET estado = '"+estado+"' WHERE id = '"+ida+"';")
    cursor.execute(sql)
    resultado=cursor.fetchall() 
    mydb.commit()   

    if estado=='si':   
        return { "status": 200, "state": 'PRENDIDO'}
    elif estado=='no':
        return { "status": 200, "state":'APAGADO'}
    else:
        return 'OLEEEE!!!, PROBA DE NUEVO'

@app.route('/dispositivos/aireacondicionado/verificarconexion',methods=['GET','POST'])
def conexion():
    global conexion
    global ida
    mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",
user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'
    ida=request.args.get('id')
    conexion=request.args.get('conexion')   
    cursor=mydb.cursor()
    sql=("UPDATE aireacondicionado SET conexion='"+conexion+"'  WHERE id='"+ida+"';")
    cursor.execute(sql)
    resultado=cursor.fetchall() 
    mydb.commit()   
    
    if conexion=='si':   
        return { "status": 200, "state": 'CONECTADO'}
    elif conexion=='no':
        return { "status": 200, "state":'DESCONECTADO'}
    else:
        return 'OLEEEE!!!, PROBA DE NUEVO'

@app.route('/dispositivos/aireacondicionado/editarnombre',methods=['GET','POST'])
def nombre():
    global nombre
    global ida
    mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",
user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'
    ida=request.args.get('id')
    nombre=request.args.get('nombre')   
    cursor=mydb.cursor()
    sql=("UPDATE aireacondicionado SET nombre='"+nombre+"' WHERE id='"+ida+"';")
    cursor.execute(sql)
    resultado=cursor.fetchall() 
    mydb.commit()   
    
    print(nombre)
    return { "status": 200, "state": "OK" }

@app.route('/dispositivos/aireacondicionado/cambiartemperatura',methods=['GET','POST'])
def temperatura():
    global temperatura
    global ida
    mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",
user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'
    temperatura=request.args.get('temperatura')
    ida=request.args.get('id')
    cursor=mydb.cursor()
    sql=("UPDATE aireacondicionado SET temperatura='"+temperatura+"' WHERE id='"+ida+"';")
    cursor.execute(sql)
    resultado=cursor.fetchall() 
    mydb.commit()   
    
    if '16'<=temperatura<='31':
        return { "status": 200, "state": temperatura }
    else:
        return 'OLEEEE!!!, PROBA DE NUEVO'      

@app.route('/dispositivos/aireacondicionado/activarfan',methods=['GET','POST'])
def fan():
    global fan
    global ida
    mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",
user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'
    fan=request.args.get('fan')
    ida=request.args.get('id')
    cursor=mydb.cursor()
    sql=("UPDATE aireacondicionado SET fan='"+fan+"' WHERE id='"+ida+"';")
    cursor.execute(sql)
    resultado=cursor.fetchall() 
    mydb.commit()   
    
    if fan=='0':
        return { "status": 200, "state": 'DESACTVADO'}    
    elif fan=='1':   
        return { "status": 200, "state": 'VELOCIDAD 1'}
    elif fan=='2':
        return { "status": 200, "state":'VELOCIDAD 2'}
    elif fan=='3':
        return {"status": 200, "state": "VELOCIDAD 3"}
    else:
        return 'OLEEEE!!!, PROBA DE NUEVO'        


@app.route('/dispositivos/aireacondicionado/activarswin',methods=['GET','POST'])
def swin():
    global swin
    global ida
    mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",
user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'
    swin=request.args.get('swin')
    ida=request.args.get('id')
    cursor=mydb.cursor()
    sql=("UPDATE aireacondicionado SET swin='"+swin+"' WHERE id='"+ida+"';")
    cursor.execute(sql)
    resultado=cursor.fetchall() 
    mydb.commit()   
    
    if swin=='si':
        return {"status": 200, "state": "ACTIVADO"}
    elif swin=='no':
        return {"status": 200, "state": "DESACTIVADO"}    
    else :
        return 'OLEEEE!!!, PROBA DE NUEVO'

@app.route('/dispositivos/aireacondicionado/activartimer',methods=['GET','POST'])
def timer():
    global timer
    global ida
    mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",
user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'
    timer=request.args.get('timer')
    ida=request.args.get('id')
    cursor=mydb.cursor()
    sql=("UPDATE aireacondicionado SET timer='"+timer+"' WHERE id='"+ida+"';")
    cursor.execute(sql)
    resultado=cursor.fetchall() 
    mydb.commit()   
    
    print(timer)
    return { "status": 200, "state": "OK" }

@app.route('/dispositivos/aireacondicionado/activarsleep',methods=['GET','POST'])
def sleep():
    global sleep
    global ida
    mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",
user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'
    sleep=request.args.get('sleep')
    ida=request.args.get('id')
    cursor=mydb.cursor()
    sql=("UPDATE aireacondicionado SET sleep='"+sleep+"' WHERE id='"+ida+"';")
    cursor.execute(sql)
    resultado=cursor.fetchall() 
    mydb.commit()   
    
    print(sleep)
    return { "status": 200, "state": "OK" }

@app.route('/dispositivos/aireacondicionado/cambiarmodo',methods=['GET','POST'])
def modo():
    global modo
    global ida
    mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",
user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'
    modo=request.args.get('modo')
    ida=request.args.get('id')
    cursor=mydb.cursor()
    sql=("UPDATE aireacondicionado SET modo='"+modo+"' WHERE id='"+ida+"';")
    cursor.execute(sql)
    resultado=cursor.fetchall() 
    mydb.commit()   
    
    if modo=='frio':
        return { "status": 200, "state": "FRIO" }
    elif modo=='calor':
        return { "status": 200, "state": "CALOR" }
    elif modo=='ventilacion':
        return { "status": 200, "state": "VENTILACION" }
    else:
        return 'OLEEEE!!!, PROBA DE NUEVO'        

@app.route('/dispositivos/aireacondicionado/cambiardireccion',methods=['GET','POST'])
def direccion():
    global direccion
    global ida
    mydb=mysql.connector.connect(host="b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com",database="b0zrkz2xyg7u8afh6has",
user="ui6majbcugnjjink",password="sNHVs7AyLnUbsimZIKWG", port='3306')
# connectionURI='mysql://ui6majbcugnjjink:sNHVs7AyLnUbsimZIKWG@b0zrkz2xyg7u8afh6has-mysql.services.clever-cloud.com:3306/b0zrkz2xyg7u8afh6has'
    direccion=request.args.get('direccion')
    ida=request.args.get('id')
    cursor=mydb.cursor()
    sql=("UPDATE aireacondicionado SET direccion='"+direccion+"' WHERE id='"+ida+"';")
    cursor.execute(sql)
    resultado=cursor.fetchall() 
    mydb.commit()   
    
    if direccion=='1':
        return { "status": 200, "state": "Posicion 1" }
    elif direccion=='2':
        return { "status": 200, "state": "Posicion 2" }    
    elif direccion=='3':
        return { "status": 200, "state": "Posicion 3" }    
    elif direccion=='4':
        return { "status": 200, "state": "Posicion 4" }    
    elif direccion=='5':
        return { "status": 200, "state": "Posicion 5" }    
    else:
        return 'OLEEEE!!!, PROBA DE NUEVO'
cursor.close()
mydb.close()
    
if __name__=='__main__':
    app.run(debug=True)
