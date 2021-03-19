from pydantic import BaseModel, Field


class Error(BaseModel):
    ok: bool = Field(..., example=False)
    detail: str = Field(
        None, description="Error description", example="Error message")


class User(BaseModel):
    login: str = Field(
        ...,
        description="RADIUS login",
        example="CLIENT_ADHERENT"
    )
