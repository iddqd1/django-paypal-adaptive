from paypaladaptive.models import Payment, Preapproval, PaypalAdaptive
import factory
import uuid
from moneyed.classes import Money
from djmoney.models.fields import currency_field_name
import datetime


class PaypalAdaptiveFactory(factory.DjangoModelFactory):
    FACTORY_FOR = PaypalAdaptive

    money = 1400
    created_date = datetime.datetime.now()

setattr(PaypalAdaptiveFactory, currency_field_name('money'), 'SEK')


class PaymentFactory(PaypalAdaptiveFactory):
    FACTORY_FOR = Payment
    transaction_id = str(uuid.uuid4())[0:17]


class PreapprovalFactory(PaypalAdaptiveFactory):
    FACTORY_FOR = Preapproval
