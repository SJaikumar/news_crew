from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

search = SerperDevTool()

researcher= Agent(
    role ="Search the web",
    goal="Find the top trending tech new stories ",
    backstory="You should be able to classify the top trending tech stories that "
    "catches the attention of tech enthusiasts",
    tools=[search],
    verbose ="True",
)

writer=Agent(
    role="Write the story in a attractive way interesting for the tech enthusiasts ",
    goal= "The writing should be very professional",
    backstory="You are an experience writer who have written similar stories in tha past that has " \
    "reasonable reach with the community",
    Verbose=True,
    
)

find= Task(description="The top trending tech stories", 
           expected_output="A short reference of a story." \
           " Example: Nvidia CEO launched a laptop that self-cools by itself",
           agent=researcher
           )
            
write=Task(description=" The story should be in a language connect with the Tech community. Only 3 stories are required followed by Why it matters",
           expected_output="A summary one line statement that gives an initial idea about the story." \
           "This should follow this pattern. Why it matters also should be a one liner 1.First story - First story is about the very story," \
           "2. Second story - This is about the second story" \
           "3. Third story - This is about the third story" \
           "Why it matters: It matters due to these reasons",
           agent=writer,
           context=[find]
           )

crew= Crew(agents =[researcher,writer], tasks=[find,write], process =Process.sequential, verbose=True)

print(crew.kickoff())