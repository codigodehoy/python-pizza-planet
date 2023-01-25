

import pytest
from flask.cli import FlaskGroup
from flask_migrate import Migrate

from app import flask_app
from app.plugins import db
# flake8: noqa
from app.repositories.models.beverage import Beverage
from app.repositories.models.order import Order
from app.repositories.models.ingredient import Ingredient
from app.repositories.models.size import Size
from app.repositories.models.orderDetail import OrderDetail
from app.repositories.models.beverageDetail import BeverageDetail

manager = FlaskGroup(flask_app)

migrate = Migrate()
migrate.init_app(flask_app, db)


@manager.command('test', with_appcontext=False)
def test():
    return pytest.main(['-v', './app/test'])


if __name__ == '__main__':
    manager()
