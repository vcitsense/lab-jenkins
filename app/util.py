# pylint: disable=no-else-return
def convert_to_number(operand):
    try:
        # Convierte a cadena para realizar la comprobación
        operand_str = str(operand)
        
        if "." in operand_str:  # Verifica si es un número decimal
            return float(operand)
        else:  # Si no tiene punto, trata de convertirlo como entero
            return int(operand)

    except ValueError:
        raise TypeError("Operator cannot be converted to number")


def InvalidConvertToNumber(operand):
    try:
        if "." in operand:
            return (float(operand))

        return int(operand)

    except ValueError:
        raise TypeError("Operator cannot be converted to number")


def validate_permissions(operation, user):
    print(f"checking permissions of {user} for operation {operation}")
    return user == "user1"
