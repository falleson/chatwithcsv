import datetime
import asyncio
from semantic_kernel.skill_definition import sk_function,sk_function_context_parameter


class SQLSkill:

    @sk_function(
        description="get records count"
    )
    def get_records_count(self) -> str:
        return "10"
    
    @sk_function(description="list tables",name="listtable")
    def listtable(self) -> str:
        return "blogs,posts"
        # now = datetime.datetime.now()
        # return now.strftime("%A, %d %B, %Y")
    
    
    @sk_function(description="Wait for a certain number of seconds.")
    async def wait(self, seconds_text: str):
        try:
            seconds = max(float(seconds_text), 0)
        except ValueError:
            raise ValueError("seconds text must be a number")
        await asyncio.sleep(seconds)
    
    @sk_function(description="Get the current date.")
    def date(self) -> str:
        """
        Get the current date

        Example:
            {{time.date}} => Sunday, 12 January, 2031
        """
        now = datetime.datetime.now()
        return now.strftime("%A, %d %B, %Y")