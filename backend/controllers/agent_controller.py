from flask import jsonify
from services.agent_service import AgentService
from flask import current_app

class AgentController:
    def ingest(self):
        svc = AgentService(current_app.config)
        return jsonify({"ingested": svc.ingest()})

    def process(self):
        svc = AgentService(current_app.config)
        return jsonify({"processed": svc.process()})

    def execute(self):
        svc = AgentService(current_app.config)
        return jsonify({"executed": svc.execute()})
