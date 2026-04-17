from flask import Flask, json
app = Flask(__name__)
@app.route('/prime_number/<int:number>')
def is_prime_endpoint(number):
    result = {
        "Number": number,
        "isPrime": check_prime(number)
    }

    return json.dumps(result)

def check_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)