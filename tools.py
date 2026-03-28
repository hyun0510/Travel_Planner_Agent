from langchain_core.tools import tool
from models import UserInformation, TravelPlan
from mock_db import get_store

@tool
def save_information(
    departure_date: str,
    departure: str,
    destination: str,
    period: int,
    budget: int, 
    style: str,
    personnel: int
)->UserInformation:
    """여행자 정보를 저장합니다

    Args:
        departure_date: 출발일
        departure: 출발지
        destination: 목적지
        period: 여행기간
        buget: 예산
        style: 여행 스타일
        personnel: 여행 인원
        
    Returns:
        UserInformation: 출발일, 출발지, 목적지, 기간, 예산, 스타일, 인원을 포함한 여행자 정보
    """
    
    infor = UserInformation(
        departure_date = departure_date,
        departure = departure,
        destination = destination,
        period = period,
        budget = budget,
        style = style,
        personnel = personnel
    )

    store = get_store()
    store["information"].append(infor)

    return infor

@tool
def save_plan(plan_content: str) -> TravelPlan:
    """모델이 생성한 항공, 호텔, 관광지 계획을 저장합니다.

    Args:
        plan_content: 저장할 게획의 내용

    Returns:
        TravelPlan: 저장된 여행계획
    """

    plan = TravelPlan(
        plan_content=plan_content
    )

    store = get_store()
    store["saved_plans"].append(plan)

    return plan



@tool
def get_saved_information()->str:
    """저장된 여행자 정보를 불러옵니다
    
    Returns:
        여행자의 여행정보
    """
    store = get_store()

    infor = store.get("information", [])

    if not infor:
        return "등록된 사용자가 없습니다. 사용자에게 여행자 정보 등록을 요청하세요"
    

    result = f"""
    여행자 정보
    - 출발일: {infor[-1].departure_date}
    - 출발지: {infor[-1].departure}
    - 목적지: {infor[-1].destination}
    - 기간: {infor[-1].period}
    - 예산: {infor[-1].budget}
    - 스타일: {infor[-1].style}
    - 인원: {infor[-1].personnel}
    """

    return result

@tool
def get_saved_plan(plan_type:str) -> TravelPlan:
    """저장된 여행계획을 불러옵니다.
    
    Returns:
        저장되어 있는 여행계획 정보
    """

    store = get_store()
    plan = store.get("saved_plans")[-1]




