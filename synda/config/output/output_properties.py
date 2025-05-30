from abc import ABC, abstractmethod

from pydantic import BaseModel, ConfigDict, model_validator


class OutputProperties(BaseModel, ABC):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    @abstractmethod
    @model_validator(mode="after")
    def validate_properties(self) -> "OutputProperties":
        pass
