    import os
    my_secret = os.environ['OPENAI_API_KEY']

    from langchain.chains import LLMChain
    from langchain.llms import OpenAI
    from langchain.prompts import PromptTemplate

    # temperature lies between 0 and 1
    # higher the temperature more random or creative the response
    # default Open AI model is text-davinci-003
    llm = OpenAI(api_key=my_secret)

    prompt = ("""
    What is the capital of France? What are the 3 most popular places to visit in Paris?

    Limit your response to 500 words.
    """)

    try:
      response = llm(prompt)
      print(response)
    except Exception as e:
      if "429" in str(e):
          #print("Too many requests. Waiting and retrying...")
          #time.sleep(60)  # Wait for 60 seconds
          #response = llm(prompt)
          print("Too many requests. Cancelling the job.")
          #print(response)
          print(f"Error: {e}")
      else:
          print(f"Error: {e}")