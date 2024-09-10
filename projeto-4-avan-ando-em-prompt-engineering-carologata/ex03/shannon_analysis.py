import re
from model_api import get_response

def extract_content(text, tag):
    pattern = f"<{tag}>(.*?)</{tag}>"
    match = re.search(pattern, text, re.DOTALL)
    return match.group(1).strip() if match else ""

def get_response(prompt, previous_response, previous_tag, current_tag):
    formatted_prompt = f""" 
        <instruction>
            - The question that should be answered is this:
                <question>{prompt}</question>
            - The answer must not be have any instruction.
            - Answer exactly in the format requested.
            - The answer should be answered inside the <{current_tag}></{current_tag}> 
            - Follow the example below:
                <{current_tag}>{{RESPONSE}}</{current_tag}>
            """
    if previous_response is not None:
        formatted_prompt += f""" - The question must be answered based on the information 
            inside the <{previous_tag}></{previous_tag}> tag:
                {previous_response}"""
    formatted_prompt += f"""
        </instruction>
        """
    return formatted_prompt

def run_prompt_chain():
    # Prompt 1: Biografia
    prompt = "Forneça uma breve biografia de Claude Shannon, focando em sua vida pessoal."
    prompt1 = construct_prompt(prompt, None, None, "biography")
    print("************* PROMPT 1 *****************\n")
    print(prompt1)
    print("****************************************\n")
    response1 = get_response(prompt1)
    biography = extract_content(response1, "biography")
    print("************* RESPONSE 1 ***************\n")
    print(response1)
    print("****************************************\n")

    # Prompt 2: ...
    prompt = "Descreva as contribuições principais de Claude Shannon"
    prompt2 = construct_prompt(prompt, response1, "biography", "analysis")
    print("************* PROMPT 2 *****************\n")
    print(prompt2)
    print("****************************************\n")
    response2 = get_response(prompt2)
    analysis = extract_content(response2, "analysis")
    print("************* RESPONSE 2 ***************\n")
    print(response2)
    print("****************************************\n")

    # Prompt 3: ...
    prompt = "Informe o histórico profissional de Claude Shannon"
    prompt3 = construct_prompt(prompt, response2, "biography", "analysis")
    print("************* PROMPT 3 *****************\n")
    print(prompt3)
    print("****************************************\n")
    response3 = get_response(prompt3)
    professional = extract_content(response3, "professional")
    print("************* RESPONSE 3 ***************\n")
    print(response3)
    print("****************************************\n")

if __name__ == "__main__":
    run_prompt_chain()