from dataclasses import dataclass

@dataclass(frozen=True)
class Command:
  name: str
  detail: str

class Handler:
  def handle(self, command: Command):
    print(command.name)
    print(command.detail)
