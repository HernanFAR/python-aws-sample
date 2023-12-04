from dataclasses import dataclass
from typing import List

import boto3
import os


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


class GetAllQuestionRepository:
  def __init__(self) -> None:
    self.dynamodb = boto3.resource('dynamodb')
    self.table = self.dynamodb.Table(f'Questions-{os.getenv("PY-ENV")}')

  def getAll(self) -> List[Question]:
    items = []
    baseResponse = self.table.scan()
    items.extend(baseResponse.get('Items', []))

    print(items)

    return []


class GetAllQuestionHandler:
  def __init__(self, repository: GetAllQuestionRepository) -> None:
    self.repository = repository

  def handle(self) -> GetAllQuestionResponse:
    return self.repository.getAll()
