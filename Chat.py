from llama_index.core import SimpleDirectoryReader
from MacGPT import MacGPT
import time



def main():
    #docs=SimpleDirectoryReader('input_data',filename_as_id=True).load_data()
    model=MacGPT(response_mode="tree_summarize",top_k=3)
    #model.add_documents(docs)
    query="What is the symmetric key encryption?"
    print(query)
    response=model.query(query)
   
    print(f"{response['response']}")
    """
    r_sources={response['response'].metadata[doc_id]['file_name'].rsplit('\\')[-1].rsplit('_')[0] for doc_id in response['response'].metadata}
 
    print(f"Sources={r_sources}")
    print(f"Faithfulness={response['faithfulness'].score}")
    print(f"Relevance={response['relevance'].score}")
    """
    query2="How does it compare to asymmetric key encryption?Please include page numbers and file names for references."
    print()
    print(query2)
    response=model.query(query2)
    print(f"{response['response']}")
    """
    r_sources={response['response'].metadata[doc_id]['file_name'].rsplit('\\')[-1].rsplit('_')[0] for doc_id in response['response'].metadata}
   
    print(f"Sources={r_sources}")
    print(f"Faithfulness={response['faithfulness'].score}")
    print(f"Relevance={response['relevance'].score}")
    print("-------Faithfulness OUTPUT------")
    print(f"faithfulness={response['faithfulness']}")
    """
   




if __name__=="__main__":
    main()