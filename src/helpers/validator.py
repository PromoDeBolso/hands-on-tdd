class Validator(object):
    @staticmethod
    def cpf_validator(cpf):
        cpf = ''.join([i for i in cpf if i.isdigit()])

        return len(cpf) == 11

    @staticmethod
    def pincode_validator(pincode):
        return len(pincode) == 10
