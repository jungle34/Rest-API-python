from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/api/<classe>/<modulo>', methods=['GET'])
def rest(classe, modulo):    
    root = __import__(classe)
    
    function = getattr(root, modulo)

    response = function()

    return response        

if __name__ == '__main__':                
    print("\n" * 500) 
    print("SERVER HAS BEEN STARTED - PYserver is ON!")
    print("ENDPOINT: http://127.0.0.1:5000/api/<classe>/<modulo>")
    print("\n" * 2)
    print("DESENVOLVIDO POR JOÃO VICTOR ")        
    print("\n" * 10)
    app.run()    
else:
    print("\n" * 500)
    print("NÃO FOI POSSÍVEL INICIALIZAR O SERVIDOR")
    print("\n" * 10)
