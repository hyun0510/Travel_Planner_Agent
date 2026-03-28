from agents import get_travel_planner_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b" 
)

coach_agent = get_travel_planner_agent(model)

result = coach_agent.invoke({
    "messages":[
        {
            "role": "user",
            "content": "저는 4일 후에 인천에서 출발해서 일본을 3박 4일 동안 여행할 것입니다. 예산은 200만원 이고 여행 인원은 2명입니다. 저의 여행스타일은 힐링여행을 좋아합니다. 일본에 가면 도톤보리는 꼭 가보고 싶어요."
        }
    ]
})

print(result['messages'][-1].content)