from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.document_loaders import PyPDFLoader


class ChromaQA:
    def __init__(self, input_path, input_text):
        self.pdf_path = input_path
        self.input_text = input_text
        self.docs = None
        self.db = None
        self.create_chromadb()

    def create_chromadb(self):
        loader = PyPDFLoader(self.pdf_path)
        text_spliter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        chunks = loader.load_and_split(text_spliter)
        embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        self.db = Chroma.from_documents(chunks, embedding_function)

    def get_result(self):
        self.docs = self.db.similarity_search(self.input_text)
        combine_question = f'Please summarize a short answer for my question based on the following information. ' \
                           f'This is my Question: {self.input_text}. ' \
                           f'The following information: ' + self.docs[0].page_content
        temp = '\n------\n'.join([str(x) for x in self.docs])
        return combine_question, temp
