from dataclasses import dataclass


@dataclass(frozen=True)
class Persona:
    nombre: str

    def saludo(self) -> str:
        return f"Hola {self.nombre}"