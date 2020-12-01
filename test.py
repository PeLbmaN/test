from flask import Flask


app = Flask(__name__)

client = app.test_client()

x = int(input())
y = int(input()) 

def multiplication(x, y):
    result = 0
    i = 0 
    for i in range(y):
        result += x 
        i += 1 
    return result

a = multiplication( x, y ) 


@app.route('/', methods=['GET'])
def index():   
    return "Your number is " + str(a)


@app.route('/<int:numb1>/<int:numb2>')
def index1(numb1, numb2):   
    a = multiplication(numb1, numb2)
    return 'Your number is ' + str(a)



if __name__ == '__main__':
    app.run()
