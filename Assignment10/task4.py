from flask import Flask, jsonify

app = Flask(__name__)

AIRPORTS = {
    "LFLL": {"name": "Lyon Saint-Exupery Airport", "city": "Lyon", "country": "FR"},
    "EGLL": {"name": "Heathrow Airport", "city": "London", "country": "GB"},
    "EFHK": {"name": "Helsinki Airport", "city": "Helsinki", "country": "FI"}
}

@app.route('/airport/<icao>')
def get_airport_info(icao):
    icao_upper = icao.upper()
    
    airport = AIRPORTS.get(icao_upper)

    if airport:
        return jsonify({"icao": icao_upper, **airport}), 200
    
    return jsonify({
        "status": "error",
        "message": f"Airport with ICAO '{icao_upper}' not found"
    }), 404

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)