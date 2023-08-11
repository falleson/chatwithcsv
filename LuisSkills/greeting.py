import os
from semantic_kernel.skill_definition import sk_function,sk_function_context_parameter


class GreetingSkill:
    """
    Description: say hello to others
    """

    @sk_function(
        description="say hello in the morning"
    )
    def hello_morning(self) -> str:
        return "hello morning!"
    
    @sk_function(
        description="say hello in the afternoon"
    )
    def hello_afternoon(self)-> str:
        return "hello afternoon!"
    
    @sk_function(
        description="say hello in the evening"
    )
    def hello_evening(self)-> str:
        return "hello evening!"
