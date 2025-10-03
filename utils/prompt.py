def build_prompt(content: str) -> str:
    prompt = f"""
    You are an expert at summarizing PDF documents and reviewing CVs
    Your task is to read the content of the PDF and provide a concise summary,
    and explain the candidate suitability for a senior software engineer role for an AWS event driven system.
    Explain your reasoning in bullet points. make sure to extract relevant name, email, skills and experiences from the CV.

    Here is the content of the PDF:
    <content>
    {content}
    </content>
    
    <example>
    the candidate is good/excellent  fit for the role, he  has the required skills for the position, my reason for my decision is based on: 
    - he has React.js, which will support the front end developing
    - he has experience with event driven system proved by his previous projects
    </example>

    Please provide a summary that captures the main points and key information from the document.
    """
    return prompt.strip()
