from enum import Enum

class PaymentMethodEnums(Enum):
    CREDIT_CARD = 'Tarjeta de Crédito'
    DEBIT_CARD = 'Tarjeta de Débito'
    CASH = 'Efectivo'
    BANK_TRANSFER = 'Transferencia Bancaria'
    OTHER = 'Otro'