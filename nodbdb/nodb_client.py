import sys, csv, time 
from multiprocessing import Pool
from os.path import splitext as get_ext
from azure.storage.blob import BlobServiceClient, ContainerClient, BlobClient, DelimitedTextDialect, DelimitedJsonDialect, BlobQueryError

def get_explanations():
    return "Sorry human, I thought 'twas a good idea"

def query(a_query, a_blob_url, a_sas_key):
    #Get the file extension/type 
    a_file_name, a_file_type = get_ext(a_blob_url)

    blob_client = BlobClient.from_blob_url(blob_url= a_blob_url + a_sas_key)

    if a_file_type      == '.csv':
        qa_reader = blob_client.query_blob(a_query, blob_format=DelimitedTextDialect(has_header=True), encoding='utf-8')
    elif a_file_type    == '.json':
        qa_reader = blob_client.query_blob(a_query, blob_format=DelimitedJsonDialect(delimeter=' '), encoding='utf-8',output_format = DelimitedJsonDialect(delimiter='\n'))
    elif a_file_type    == '.parquet':
        qa_reader = "We'll do something about this"
    else:
        print(f"Sorry, can't query a {a_file_type} file type")

    blob_reader = qa_reader.records()
    return blob_reader
        

def query_a_dir():
    # Should it have to have a recursive option, a starmap_async exec?
    # some_args = []
    # pool = Pool()
    # result = pool.starmap(query, some_args)
    # print("main script")
    # print(result.get())
    # print("end main script")
    return "TBI (to be implemented) :D"

def read_the_news():
    return "This would read the change feed. TBI (to be implemented) :D"
#In the future refactor to class