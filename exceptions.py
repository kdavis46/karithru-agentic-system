class FulfillAIException(Exception):
    pass

class CustomerValidationError(FulfillAIException):
    pass

class InventoryError(FulfillAIException):
    pass

class RiskEscalation(FulfillAIException):
    pass
