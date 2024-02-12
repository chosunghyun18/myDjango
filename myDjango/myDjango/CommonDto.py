from myDjango.utils import ResponseDto

class CustomDto:
    def __init__(self, given_result):
        self.result = given_result

    def getDto(self):
        res = ResponseDto(status='success', message='Operation completed', data=self.result)
        return res.get_data()
