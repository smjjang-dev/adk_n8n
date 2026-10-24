from google.adk.agents import Agent
from tools.time_tool import get_current_time
from tools.calculator_tool import calculate
from tools.dice_tool import roll_dice
from tools.weather_tool import get_current_weather

root_agent = Agent(
    model="gemini-3.1-flash-lite",
    name="multi_tool_agent",
    description="여러 Tool을 사용하는 Agent",
    instruction="""
    사용자의 질문에 적절한 Tool을 선택하여 답변하세요.
    """,
    tools=[
        get_current_time,
        calculate,
        roll_dice,
        get_current_weather
    ]
)