from langchain_ollama import ChatOllama

def run_model(promt:str = "")-> str:
    model_name="llama3.2:1b"
    model = ChatOllama(model=model_name)
    return model.invoke(promt)

if __name__=="__main__":
    query ="테스트 자동화 엔지니어의 역할은 무엇인가요?"
    result = run_model(query)
    print(result)