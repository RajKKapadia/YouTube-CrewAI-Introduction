from crewai import Crew

from agents import *
from tasks import *

crew = Crew(
    agents=[planner, writer, editor],
    tasks=[plan, write, edit],
    verbose=2
)

result = crew.kickoff(
    inputs={"topic": "benifits of artificial intelligence"}
)

print(result)
