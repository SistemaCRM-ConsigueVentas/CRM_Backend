from enum import Enum

class PaymentMethodEnums(Enum):
    CREDIT_CARD = 0 #'Tarjeta de Crédito'
    DEBIT_CARD = 1 #'Tarjeta de Débito'
    CASH = 2 #'Efectivo'
    BANK_TRANSFER = 3 #'Transferencia Bancaria'
    OTHER = 4 #'Otro'