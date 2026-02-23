from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# EQUIPOS DE LA NBA
equipos = [
    {"id": 1, "nombre": "Lakers", "ciudad": "Los Angeles"},
    {"id": 2, "nombre": "Warriors", "ciudad": "Golden State"},
    {"id": 3, "nombre": "Bulls", "ciudad": "Chicago"},
    {"id": 4, "nombre": "Celtics", "ciudad": "Boston"},
    {"id": 5, "nombre": "Heat", "ciudad": "Miami"},
    {"id": 6, "nombre": "Nets", "ciudad": "Brooklyn"},
    {"id": 7, "nombre": "Knicks", "ciudad": "New York"},
    {"id": 8, "nombre": "Suns", "ciudad": "Phoenix"},
    {"id": 9, "nombre": "Mavericks", "ciudad": "Dallas"},
    {"id": 10, "nombre": "Spurs", "ciudad": "San Antonio"},
    {"id": 11, "nombre": "Raptors", "ciudad": "Toronto"},
    {"id": 12, "nombre": "76ers", "ciudad": "Philadelphia"},
    {"id": 13, "nombre": "Clippers", "ciudad": "Los Angeles"},
    {"id": 14, "nombre": "Nuggets", "ciudad": "Denver"},
    {"id": 15, "nombre": "Timberwolves", "ciudad": "Minnesota"},
    {"id": 16, "nombre": "Thunder", "ciudad": "Oklahoma City"},
    {"id": 17, "nombre": "Kings", "ciudad": "Sacramento"},
    {"id": 18, "nombre": "Pelicans", "ciudad": "New Orleans"},
    {"id": 19, "nombre": "Magic", "ciudad": "Orlando"},
    {"id": 20, "nombre": "Hawks", "ciudad": "Atlanta"}
]
@csrf_exempt
def equipos_view(request):

    # GET
    if request.method == "GET":
        response = json.dumps({"equipos": equipos})
        return HttpResponse(response, content_type="application/json", status=200)

    # POST
    elif request.method == "POST":
        data = json.loads(request.body)

        nuevo_equipo = {
            "id": len(equipos) + 1,
            "nombre": data.get("nombre"),
            "ciudad": data.get("ciudad")
        }

        equipos.append(nuevo_equipo)

        response = json.dumps({
            "mensaje": "Equipo creado",
            "equipo": nuevo_equipo
        })

        return HttpResponse(response, content_type="application/json", status=201)

    # PUT
    elif request.method == "PUT":
        data = json.loads(request.body)
        equipo_id = data.get("id")

        for equipo in equipos:
            if equipo["id"] == equipo_id:
                equipo["nombre"] = data.get("nombre", equipo["nombre"])
                equipo["ciudad"] = data.get("ciudad", equipo["ciudad"])

                response = json.dumps({
                    "mensaje": "Equipo actualizado",
                    "equipo": equipo
                })

                return HttpResponse(response, content_type="application/json", status=200)

        return HttpResponse(
            json.dumps({"error": "Equipo no encontrado"}),
            content_type="application/json",
            status=404
        )

    # DELETE
    elif request.method == "DELETE":
        data = json.loads(request.body)
        equipo_id = data.get("id")

        for equipo in equipos:
            if equipo["id"] == equipo_id:
                equipos.remove(equipo)

                return HttpResponse(
                    json.dumps({"mensaje": "Equipo eliminado"}),
                    content_type="application/json",
                    status=200
                )

        return HttpResponse(
            json.dumps({"error": "Equipo no encontrado"}),
            content_type="application/json",
            status=404
        )

    return HttpResponse(
        json.dumps({"error": "Método no permitido"}),
        content_type="application/json",
        status=405
    )