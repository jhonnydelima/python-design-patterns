from typing import Dict
from flask import request as FlaskRequest

class Calculator1:
  '''
  The first part is divided by 4 and then increased by 7.
  After that, the result is powered by 2 and then multiplied by 0,257.

  The second part is powered by 2,121, then divided by 5, and finally increased by 1.

  And the last part should keep the number as it is.
  '''

  def calculate(self, request: FlaskRequest) -> Dict:
    body = request.json
    input_data = self.__validate_body(body)
    splitted_number = input_data / 3

    first_process_result = self.__first_process(splitted_number)


  def __validate_body(self, body: Dict) -> float:
    if "number" not in body:
      raise Exception("Missing 'number' in request body")
    input_data = body["number"]
    return input_data
  
  def __first_process(self, number: floar) -> float:
    first_part = (number / 4) + 7
    second_part = (first_part ** 2) * 0.257
    return second_part