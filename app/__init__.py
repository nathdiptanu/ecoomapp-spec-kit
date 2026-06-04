from pathlib import Path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(test_config=None):
    project_root = Path(__file__).resolve().parent.parent
    app = Flask(
        __name__,
        instance_relative_config=True,
        template_folder=str(project_root / "templates"),
        static_folder=str(project_root / "static"),
    )
    app.config.from_mapping(
        SECRET_KEY="dev-secret-key-change-me",
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{Path(app.instance_path) / 'ecommerce.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if test_config:
        app.config.update(test_config)

    Path(app.instance_path).mkdir(parents=True, exist_ok=True)

    db.init_app(app)

    from app.routes import bp

    app.register_blueprint(bp)

    with app.app_context():
        from app.seed import seed_database

        db.create_all()
        seed_database()

    return app
