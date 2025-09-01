from flask import Flask, request, jsonify

def create_app():
    app = Flask(__name__)
    app.config["WORKOUTS"] = []

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"}), 200

    @app.get("/workouts")
    def list_workouts():
        return jsonify(app.config["WORKOUTS"]), 200

    @app.post("/workouts")
    def add_workout():
        data = request.get_json(silent=True) or {}
        workout = data.get("workout")
        duration = data.get("duration")
        if not workout or duration is None:
            return jsonify({"error": "Please enter both workout and duration."}), 400
        try:
            duration_int = int(duration)
        except (TypeError, ValueError):
            return jsonify({"error": "Duration must be a number."}), 400
        entry = {"workout": workout, "duration": duration_int}
        app.config["WORKOUTS"].append(entry)
        return jsonify({"message": f"'{workout}' added successfully!", "entry": entry}), 201

    return app

# For local run
if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
