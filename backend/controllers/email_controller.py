from flask import jsonify, request
from services.email_service import EmailService

class EmailController:
    def __init__(self):
        self.svc = EmailService()

    def list_emails(self):
        limit = int(request.args.get("limit", 100))
        emails = self.svc.list_emails(limit=limit)
        return jsonify([e.to_dict() for e in emails])
