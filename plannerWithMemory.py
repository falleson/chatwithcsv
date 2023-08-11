from dotenv import load_dotenv
import os
import semantic_kernel as sk
import semantic_kernel.connectors.ai.open_ai as sk_oai

from semantic_kernel.planning import ActionPlanner,SequentialPlanner,BasicPlanner
from semantic_kernel.core_skills import FileIOSkill,MathSkill,TextSkill,TimeSkill
from semantic_kernel.connectors.memory.postgres import PostgresMemoryStore
load_dotenv()
# print(os.environ)
azurecogserviceurl = os.environ["AZURE_COGNITIVE_SEARCH_URL"]
azurecogserviceapikey= os.environ["AZURE_COGNITIVE_SEARCH_API_KEY"]

async def main():
    kernel = sk.Kernel()
    deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
    text_llm = sk_oai.AzureTextCompletion("text-davinci-003", endpoint, api_key)
    embedding_llm = sk_oai.AzureTextEmbedding("text-embedding-ada-002",endpoint, api_key)
    kernel.add_text_completion_service("text_llm",text_llm)
    kernel.add_text_embedding_generation_service("embedding_llm2",embedding_llm)
   
    db_conn = 'postgresql://user:Rpc4d:Q2c4j@talkwithdata.postgres.database.azure.com:5432/cntalkwithdata'
    # db_conn2 = 'postgresql://pwcuser1:P#ssw0rd@luispgserver.postgres.database.azure.com:5432/postgres'
    memoryStore = PostgresMemoryStore(db_conn,1024,1,5)
    kernel.register_memory_store(memoryStore)
 

    # import core skills;
    # kernel.import_skill(MathSkill(), "math")
    # kernel.import_skill(FileIOSkill(), "fileIO")
    # kernel.import_skill(TimeSkill(), "time")
    # kernel.import_skill(TextSkill(), "text")
    # kernel.import_semantic_skill_from_directory("skills","writerskill")

    ask = "how many users there"
    # planner = SequentialPlanner(kernel)
    # plan = await planner.create_plan_async(ask)
    # result = await plan.invoke_async()
    result = await kernel.memory.search_async("users",ask)
    print(result)


if __name__=="__main__":
    import asyncio
    asyncio.run(main())

