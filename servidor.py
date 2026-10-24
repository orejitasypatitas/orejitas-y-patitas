from flask import Flask, request, jsonify, send_file, make_response
import json, socket
from pathlib import Path

CARPETA_WEB = Path(__file__).parent
CARPETA_DATOS = CARPETA_WEB / "Datos_Web"
CARPETA_DATOS.mkdir(exist_ok=True)

CLAVES = ['cachorros', 'vehiculos', 'conductores', 'usuarios', 'config',
          'asistencia', 'pagos', 'novedades', 'accesos', 'ruta',
          'mantenimientos', 'combustible', 'documentos', 'planes']

app = Flask(__name__)

def archivo_de(clave):
    return CARPETA_DATOS / f"{clave}.json"

@app.route("/")
def pagina():
    response = make_response(send_file(CARPETA_WEB / "mi1.html"))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route("/api/datos")
def dar_datos():
    response = make_response(jsonify(_leer_todos()))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response

def _leer_todos():
    todo = {}
    for clave in CLAVES:
        a = archivo_de(clave)
        if a.exists():
            try:
                todo[clave] = json.loads(a.read_text(encoding="utf-8"))
            except Exception:
                todo[clave] = None
        else:
            todo[clave] = None
    return todo

@app.route("/api/guardar", methods=["POST"])
def guardar_datos():
    datos = request.get_json(force=True, silent=True) or {}
    clave = datos.get("clave", "")
    if clave not in CLAVES:
        return jsonify({"ok": False}), 400
    archivo_de(clave).write_text(
        json.dumps(datos.get("datos"), ensure_ascii=False, indent=2),
        encoding="utf-8")
    return jsonify({"ok": True})

def ip_local():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except Exception:
        return "127.0.0.1"
    finally:
        s.close()

if __name__ == "__main__":
    ip = ip_local()
    print("=" * 55)
    print("Orejitas y Patitas - SERVIDOR ENCENDIDO")
    print(f"   En este PC:       http://localhost")
    print(f"   En los celulares: http://{ip}")
    print("=" * 55)
    app.run(host="0.0.0.0", port=80, threaded=True)