from voyager import Voyager

mc_port=0000
openai_api_key = "YOUR_API_KEY"



action_agent_model_name="llama2"

critic_agent_model_name=action_agent_model_name
skill_manager_model_name="llama2"

curriculum_agent_model_name=skill_manager_model_name
curriculum_agent_qa_model_name=skill_manager_model_name

voyager = Voyager(
    mc_port=34293,
    openai_api_key=openai_api_key,
    action_agent_model_name=action_agent_model_name,
    critic_agent_model_name=critic_agent_model_name,
    skill_manager_model_name=skill_manager_model_name,
    curriculum_agent_model_name=curriculum_agent_model_name,
    curriculum_agent_qa_model_name=curriculum_agent_qa_model_name,
    # skill_library_dir="./skill_library/trial1", # Load a learned skill library.
    # ckpt_dir="checkpoints", # Feel free to use a new dir. Do not use the same dir as skill library because new events will still be recorded to ckpt_dir. 
    # resume=False, 
)

# start lifelong learning
voyager.learn()