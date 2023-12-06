import jsonpickle
from core.useCases.getAllQuestion import Handler as GetAllQuestionHandler, define_dependency_container as define_get_all_question_dependency_container

def lambda_handler(event, context):
    container = define_get_all_question_dependency_container()

    handler = container[GetAllQuestionHandler]
    response = handler.handle()

    return {
        "statusCode": 200,
        "body": jsonpickle.encode(response, unpicklable=False),
    }
