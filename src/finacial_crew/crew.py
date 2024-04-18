from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


from langchain_groq import ChatGroq


@CrewBase
class UniversityCrew():
  agents = 'config/agents.yaml'
  tasks = 'config/tasks.yaml'

  def __init__(self)->None:
    self.groq_llm = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")

  @agent
  def university_researcher(self) -> Agent:
    return Agent(
        config=self.agents['university_researcher'],
        llm=self.groq_llm
    )

  @agent
  def university_analyser(self) -> Agent:
    return Agent(
        config=self.agents['university_analyser'],
        llm=self.groq_llm
    )

  @task
  def research_university_task(self) -> Task:
        # Access task description and expected output directly from tasks.yaml
        description = self.tasks['research_university_task']['description']
        expected_output = self.tasks['research_university_task']['expected_output']
        return Task(
            config={  # No separate config dictionary needed here
                "description": description,
                "expected_output": expected_output
            },
            agent=self.university_researcher()
        )


  @task
  def analyse_university_task(self) -> Task:
    return Task(
        config=self.tasks["analyse_university_task"],  # Access with double quotes
        agent=self.university_analyser()
    )

  @crew
  def crew(self) -> Crew:
    return Crew(
        agents=self.agents,
        tasks=self.tasks,
        process=Process.sequential,
        verbose=2
    )
