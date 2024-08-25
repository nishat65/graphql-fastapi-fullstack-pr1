from typing import TypeVar, Generic, Optional
from pydantic import BaseModel, Field

T = TypeVar("T")


class ServiceResponse(BaseModel, Generic[T]):
    result: Optional[T] = Field(default=None, title="Result", description="API result")
    error: Optional[str] = Field(default=None, title="Error", description="API error")
    status_code: Optional[int] = Field(
        default=200, title="Status code", description="API status code"
    )
    message: Optional[str] = Field(
        default="OK", title="Message", description="API message"
    )

    def __init__(
        self,
        result: T = None,
        error: str = None,
        status_code: int = 200,
        message: str = "OK",
    ) -> None:
        super().__init__()
        self.result = result
        self.error = error
        self.status_code = status_code
        self.message = message

    def set_data(self, data):
        self.data = data
