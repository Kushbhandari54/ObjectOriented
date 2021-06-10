from flask import Flask
from flaskext.mysql import MySQL
import pymysql
from flask import jsonify
from flask import flash, request
#from werkzeug import generate_password_hash, check_password_hash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'migrateIt'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

		
@app.route('/api/temp/save-details', methods=['POST'])
def add_user():
    conn = None
    cursor = None  
    try:
        _json = request.get_json()
        _DomainName=_json['DomainName']
        _SourceServerIp=_json['DomainName']
        _SourceUserName=_json['SourceUserName']
        _SourcePassword=_json['SourcePassword']
        _DatabaseName=_json['DatabaseName']
        _DestinationServerIp=_json['DestinationServerIp']
        _DestinationUserName=_json['DestinationUserName']
        _DestinationPassword=_json['DestinationPassword']

        if request.method == 'POST':
        #do not save password as a plain text
        
            _destinationPasswordhashed = generate_password_hash(_DestinationPassword)
            _sourcePasswordhashed = generate_password_hash(_SourcePassword)
            sql="INSERT INTO migrationdetails(DomainName,SourceServerIp,SourceUserName,SourcePassword,DatabaseName,DestinationServerIp,DestinationUserName,DestinationPassword) VALUES(%s, %s, %s,%s,%s,%s,%s,%s)"
            data = (_DomainName, _SourceServerIp,_SourceUserName,_sourcePasswordhashed,_DatabaseName,_DestinationServerIp,_DestinationUserName,_destinationPasswordhashed)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User added successfully!')
            resp.status_code = 200
            return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

@app.route('/api/temp/delete-details/id', methods=['DELETE'])
def delete_user(id):
	conn = None
	cursor = None
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM  migrationdetails WHERE user_id=%s", (id,))
		conn.commit()
		resp = jsonify('User deleted successfully!')
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
    


if __name__=='__main__':
    app.run(debug=True)
		

