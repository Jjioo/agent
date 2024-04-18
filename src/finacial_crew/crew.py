from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


from langchain_groq import ChatGroq




import yaml

@CrewBase
class UniversityCrew():
  def __init__(self) -> None:
        with open('src/finacial_crew/config/agents.yaml', 'r') as agents_file:
            self.agents = yaml.safe_load(agents_file)

        with open('src/finacial_crew/config/tasks.yaml', 'r') as tasks_file:
            self.tasks = yaml.safe_load(tasks_file)

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
        return Task(
            config=self.tasks.get('research_university_task', {}),  # Use .get() to handle missing keys
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
