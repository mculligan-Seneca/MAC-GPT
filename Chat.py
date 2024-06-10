from llama_index.core import SimpleDirectoryReader
from MacGPT import MacGPT
import time



def main():
    #docs=SimpleDirectoryReader('input_data',filename_as_id=True).load_data()
    model=MacGPT()
    #model.add_documents(docs)
    print("---------Question 1---------")
    query="What is the symmetric key encryption?"
    print(query)
    response=model.query(query)
   
    print(f"{response}")
    
    r_sources={response.metadata[doc_id]['file_name'].rsplit('\\')[-1].rsplit('_')[0] for doc_id in response.metadata}
 
    print(f"Sources={r_sources}")
  
    
    query2="How does it compare to asymmetric key encryption?Please include page numbers and file names for references."
    print("---------Question 2---------")
    print(query2)
    response=model.query(query2)
    print(f"{response}")
    
    r_sources={response.metadata[doc_id]['file_name'].rsplit('\\')[-1].rsplit('_')[0] for doc_id in response.metadata}
   
    print(f"Sources={r_sources}")
    
    print("-----Question 3-------")
    query3="What are some security risks to the diffie hellman key exchange?"
    print(query3)
    response=model.query(query3)
    print(response)

    r_sources={response.metadata[doc_id]['file_name'].rsplit('\\')[-1].rsplit('_')[0] for doc_id in response.metadata}
   
    print(f"Sources={r_sources}")
    avg_time=model.avg_response_time()
    print(f"Average response time = {avg_time} seconds")
    
   




if __name__=="__main__":
    main()