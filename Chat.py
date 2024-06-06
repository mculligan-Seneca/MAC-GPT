from llama_index.core import SimpleDirectoryReader
from MacGPT import MacGPT



def main():
    docs=SimpleDirectoryReader('input_data').load_data()
    model=MacGPT()
    model.add_documents(docs)
    response=model.query("What is the Diffie Helman key Exchange?")['response']

    r_sources={response.metadata[doc_id]['file_name'].rsplit('\\')[-1].rsplit('_')[0] for doc_id in response.metadata}
    print(response)
    print(f"Sources={r_sources}")
   




if __name__=="__main__":
    main()