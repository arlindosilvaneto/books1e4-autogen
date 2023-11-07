import autogen

config_list = [
    {
        "model": 'gpt-3.5-turbo-16k',
        "api_key": '',
    }
]

llm_config = {
    "request_timeout": 600,
    "seed": 42,
    "config_list": config_list,
    "temperature": 0,
}

assistant = autogen.AssistantAgent(
    name ="Assistant",
    llm_config = llm_config,
    system_message = "I am Assistant",
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    llm_config=llm_config,
    code_execution_config={
        "work_dir": "coding",
        "use_docker": False,  # set to True or image name like "python:3" to use docker
    },
    system_message = "Reply TERMINATE if the task has been solved for your full satisfaction. Or reply CONTINUE if the task is not solved yet",
)

user_proxy.initiate_chat(
   assistant,
   message="""From the ./images folder, take all images with 'Front' name suffix, and .jpeg extension, and create an html page with a 
   table of images. The table should have 3 columns and as many rows as needed. The images should be 
   shown with 200x300 pixels dimentions, but let unchanged. The table should be centered on the page and use div with styles to
   set border, padding, and margin. 
   """
)
