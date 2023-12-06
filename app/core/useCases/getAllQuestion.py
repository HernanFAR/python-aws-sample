from dataclasses import dataclass
from typing import List
from kink import Container, di, inject

import boto3
import os

from mypy_boto3_dynamodb import DynamoDBServiceResource

@dataclass(frozen=True)
class Question:
  id: str
  name: str
  detail: str


@dataclass(frozen=True)
class GetAllQuestionResponse:
  questions: List[Question]


@dataclass(frozen=True)
class GetAllQuestionContract:
  page: int
  items: int


class Repository:
  def __init__(self, dynamoDb: DynamoDBServiceResource) -> None:
    self.table = dynamoDb.Table(f'Question_{os.getenv("PY_ENV")}')

  def getAll(self) -> GetAllQuestionResponse:
    items = []
    baseResponse = self.table.scan()
    items.extend(baseResponse.get('Items', []))

    return GetAllQuestionResponse(
      questions=[
        Question(
          id=item.get('id'),
          name=item.get('name'),
          detail=item.get('detail'),
        ) for item in items
      ]
    )


class Handler:
  def __init__(self, repository: Repository) -> None:
    self.repository = repository

  def handle(self) -> GetAllQuestionResponse:
    return self.repository.getAll()

def define_dependency_container() -> Container:
  di[DynamoDBServiceResource] = boto3.resource('dynamodb')
  di[Repository] = lambda di: Repository(di[DynamoDBServiceResource])
  di[Handler] = lambda di: Handler(di[Repository])

  return di
