import datetime
import uuid

import factory
from moneyed.classes import Money
from djmoney.models.fields import currency_field_name

from paypaladaptive.models import Payment, Preapproval, PaypalAdaptive


class PaypalAdaptiveFactory(factory.DjangoModelFactory):
    FACTORY_FOR = PaypalAdaptive

    created_date = datetime.datetime.now()

    @classmethod
    def _create(cls, *args, **kwargs):
        money = kwargs.get('money', None)
        instance = super(PaypalAdaptiveFactory, cls)._create(*args, **kwargs)
        instance.money = money or Money(1400, 'SEK')
        return instance


class PaymentFactory(PaypalAdaptiveFactory):
    FACTORY_FOR = Payment
    transaction_id = str(uuid.uuid4())[0:17]


class PreapprovalFactory(PaypalAdaptiveFactory):
    FACTORY_FOR = Preapproval
