from typing import Protocol


class SaludarUseCase(Protocol):
    def ejecutar(self) -> str:
        ...