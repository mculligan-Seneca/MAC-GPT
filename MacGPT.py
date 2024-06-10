#Main module for backend chatbot
import chromadb
from llama_index.core import VectorStoreIndex, SummaryIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core import Settings, StorageContext,get_response_synthesizer
from llama_index.core.schema import MetadataMode
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.llms.ollama import Ollama
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.llms.ollama import Ollama
from llama_index.core.evaluation import SemanticSimilarityEvaluator
from llama_index.core.evaluation import FaithfulnessEvaluator
from llama_index.core.evaluation import RelevancyEvaluator
from llama_index.core.query_engine.retriever_query_engine import (
    RetrieverQueryEngine,
)
from llama_index.core.response_synthesizers import ResponseMode
import os
class MacGPT:
    
    __CHROMADB_PATH="./chroma_db"
    __TOP_K=5
    __RESPONSE_MODES={
        "compact":ResponseMode.COMPACT,
        "refine":ResponseMode.REFINE,
        "tree_summarize":ResponseMode.TREE_SUMMARIZE
      }
    __EMBED_MODEL="BAAI/bge-base-en-v1.5"
    __CHUNK_SIZE=250
    __CHUNK_OVERLAP=30
    #TODO: check if documents have already been added to vector store and not add them again if so
    def __init__(self,**kwargs) -> None:
        db=chromadb.PersistentClient(self.__CHROMADB_PATH)
        chroma_collection=db.get_or_create_collection("quickstart")
        vector_store=ChromaVectorStore(chroma_collection=chroma_collection)
        llm=Ollama(model="llama3")
        storage_context=StorageContext.from_defaults(vector_store=vector_store)
        docs=kwargs.get("docs",None)
        embed_model=HuggingFaceEmbedding(model_name=kwargs.get("embed_model",self.__EMBED_MODEL))
        text_splitter=SentenceSplitter(
            chunk_size=kwargs.get("chunk_size",self.__CHUNK_SIZE),
            chunk_overlap=kwargs.get("chunk_overlap",self.__CHUNK_OVERLAP))
        if docs is not None and len(docs)>0:
            self.__index=VectorStoreIndex.from_documents(
                docs,storage_context=storage_context,
                embed_model=embed_model,
                transformations=[text_splitter],
               
            )
            
        else:
            self.__index=VectorStoreIndex.from_vector_store(
                vector_store=vector_store,
                storage_context=storage_context,
                embed_model=embed_model,
                transformations=[text_splitter],
            
                )
        # Query Data from the persisted index
        # https://docs.llamaindex.ai/en/stable/module_guides/indexing/vector_store_guide/
        # query_engine = index.as_query_engine(similarity_top_k=10, vector_store_query_mode="default",)
        # response = query_engine.query("Which Senator was McMasters University named after?")
        # print(response)

        # index = VectorStoreIndex.from_documents(docs, transformations=[text_splitter], embed_model=MACGPT_embeddingModel)
        # https://www.restack.io/docs/llamaindex-knowledge-llamaindex-similarity-score-analysis
        # configure retriever
        # https://docs.llamaindex.ai/en/v0.9.48/api_reference/query/retrievers/vector_store.html#llama_index.vector_stores.types.VectorStoreQueryMode
        self.__retriever= VectorIndexRetriever(
            index=self.__index, 
            similarity_top_k=kwargs.get("top_k",self.__TOP_K), 
            vector_store_query_mode="default",
            llm=llm
            )
        
        # https://docs.llamaindex.ai/en/stable/module_guides/evaluating/usage_pattern/
        # define a Faithfulness evaluator (Hallucination)
        # The FaithfulnessEvaluator evaluates if the answer is faithful to the retrieved contexts (in other words, whether if there's hallucination).
        self.__evaluator_f = FaithfulnessEvaluator(llm=llm)
        # define a Relevancy evaluator
        # The RelevancyEvaluator evaluates if the retrieved context and the answer is relevant and consistent for the given query.
        # Note that this evaluator requires the query to be passed in, in addition to the Response object.
        self.__evaluator_r = RelevancyEvaluator(llm=llm)
        # configure response synthesizer
        # https://www.bluelabellabs.com/blog/llamaindex-response-modes-explained/
        response_synthesizer = get_response_synthesizer(
            response_mode=self.__RESPONSE_MODES.get(kwargs.get("response_mode","refine")),
            llm=llm,
            streaming=True
            )
        # https://docs.llamaindex.ai/en/stable/module_guides/deploying/query_engine/usage_pattern/
        # chat_engine = index.as_chat_engine(streaming=True, similarity_top_k=1)

        # assemble chat engine
        """self.__chat_engine=self.__index.as_chat_engine(
            streaming=True,
            llm=llm,
            similarity_top_k=self.__TOP_K,
            response_synthesizer=response_synthesizer)"""
        
        self.__chat_engine=RetrieverQueryEngine(
            retriever=self.__retriever,
            response_synthesizer=response_synthesizer,
          
            # node_postprocessors=[SimilarityPostprocessor(similarity_cutoff=0.7)],   #Only use with documents directly and not database
        )
     

    def query(self,prompt):
        response=self.__chat_engine.query(prompt)
        faithfulness="Faithful"#self.__evaluator_f.evaluate_response(response=response)
        relevance="Relevance"#self.__evaluator_r.evaluate_response(query=prompt,response=response)
        return dict({'response': response,'faithfulness':faithfulness,'relevance':relevance})

    def add_documents(self, documents):
        self.__index.refresh_ref_docs(documents)



#TODO: Improve LLM model performance 
#TODO: TAG node chuncks with metadata for nodes
#TODO: Investigate Summary index for improving query retrieval
