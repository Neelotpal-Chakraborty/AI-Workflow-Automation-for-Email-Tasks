def register_health(app):
    @app.get("/health")
    def health():
        return {"ok": True}
