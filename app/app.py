import jsonpickle
from core.useCases.getAllQuestion import GetAllQuestionHandler, GetAllQuestionRepository

def lambda_handler(event, context):
    handler = GetAllQuestionHandler(GetAllQuestionRepository())

    response = handler.handle()

    return {
        "statusCode": 200,
        "body": jsonpickle.encode(response, unpicklable=False),
    }
