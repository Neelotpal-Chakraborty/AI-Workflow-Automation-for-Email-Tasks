from flask import Flask
from flask_cors import CORS
from config import Config
from db import db
from routes import register_routes
from handlers.error_handler import register_error_handlers
from handlers.health_handler import register_health
from services.sched_service import SchedulerService

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    print("Loaded OpenAI key:", app.config.get("OPENAI_API_KEY"))
    CORS(app)

    db.init_app(app)
    with app.app_context():
        from models import EmailMessage, ActionLog, TaskLink  # noqa
        db.create_all()

    register_routes(app)
    register_error_handlers(app)
    register_health(app)

    # Background scheduler (ingest + process)
    SchedulerService(app).start()
    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
