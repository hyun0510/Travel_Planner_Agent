from pydantic import BaseModel, Field


class UserInformation(BaseModel):
    departure_date: str = Field(description="여행 출발일")
    departure: str = Field(description="여행 출발지")
    destination: str = Field(description="여행의 목적지")
    period: int = Field(description="여행 기간(일)") 
    budget: int = Field(description="여행 예산")
    style: str = Field(description="여행 스타일")
    personnel: int = Field(description="여행인원")

class TravelPlan(BaseModel):
    plan_content: str = Field(description="계획의 내용")

