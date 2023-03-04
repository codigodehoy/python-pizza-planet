from app.plugins import ma
from ..repositories.models.orderDetail import OrderDetail
from ..repositories.models.ingredient import Ingredient
from ..repositories.models.size import Size
from ..repositories.models.order import Order
from ..repositories.models.beverage import Beverage
from ..repositories.models.beverageDetail import BeverageDetail


class IngredientSerializer(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Ingredient
        load_instance = True
        fields = ('_id', 'name', 'price')


class SizeSerializer(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Size
        load_instance = True
        fields = ('_id', 'name', 'price')


class BeverageSerializer(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Beverage
        load_instance = True
        fields = ('_id', 'name', 'price')


class OrderDetailSerializer(ma.SQLAlchemyAutoSchema):

    ingredient = ma.Nested(IngredientSerializer)

    class Meta:
        model = OrderDetail
        load_instance = True
        fields = (
            'ingredient_price',
            'ingredient',
        )


class BeverageDetailSerializer(ma.SQLAlchemyAutoSchema):

    beverage = ma.Nested(BeverageSerializer)

    class Meta:
        model = BeverageDetail
        load_instance = True
        fields = (
            'beverage_price',
            'beverage',
        )


class OrderSerializer(ma.SQLAlchemyAutoSchema):
    size = ma.Nested(SizeSerializer)
    detail = ma.Nested(OrderDetailSerializer, many=True)
    beverage = ma.Nested(BeverageDetailSerializer, many=True)

    class Meta:
        model = Order
        load_instance = True
        fields = (
            '_id',
            'client_name',
            'client_dni',
            'client_address',
            'client_phone',
            'date',
            'total_price',
            'size',
            'detail',
            'beverage',
        )

class SerializerFactory:
    serializers = {
        Ingredient: IngredientSerializer,
        Size: SizeSerializer,
        Beverage: BeverageSerializer,
        OrderDetail: OrderDetailSerializer,
        BeverageDetail: BeverageDetailSerializer,
        Order: OrderSerializer
    }

    @staticmethod
    def get_serializer(model_class):
        serializer_class = SerializerFactory.serializers.get(model_class)
        if serializer_class is None:
            raise ValueError(f"No serializer found for {model_class}")
        return serializer_class;
