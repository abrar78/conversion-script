    #Pass the parameters with the source (docx)file absolute location ,and the target file(pdf) absolute location where you want to save the file including its name on your machine
    # example:-
    #source_file='~/test.docx'
    #target_file='~/converted/test.pdf
    #note :- send complete file path with the proper extension
    #Function returns dict type with status and conversion credit cost, if file converted and Downloaded successfully
    #module require requests,json,time can be installed using pip command

import requests,json,time
from requests.auth import HTTPBasicAuth 
       
def convert_zamzarApi(source_file,target_file):

        is_converted=False
        api_key = '2de37843cd4370359dcd7a93d59b79cf0b41bdd8' #Put your API key here
        endpoint = "https://sandbox.zamzar.com/v1/jobs"
        target_format = "pdf"
        file_content = {'source_file': open(source_file, 'rb')}
        data_content = {'target_format': target_format}
        response_upload = requests.post(endpoint, data=data_content, files=file_content, auth=HTTPBasicAuth(api_key, ''))
        response_upload=response_upload.json()
        #Convert
        job_id = response_upload['id']
        endpoint = "https://sandbox.zamzar.com/v1/jobs/"+str(job_id)
        endpoint=endpoint.format(job_id)
        response_convert = requests.get(endpoint, auth=HTTPBasicAuth(api_key, ''))
        response_convert=response_convert.json()
        status=response_convert['status']
        time.sleep(1)
        while status!='successful':
            time.sleep(1)
            response_convert = requests.get(endpoint, auth=HTTPBasicAuth(api_key, ''))
            response_convert=response_convert.json()
            status=response_convert['status']
        credit_cost=response_convert['credit_cost']
        #Download Request
        file_id = response_convert['target_files'][0]['id']
        local_filename = target_file
        endpoint = "https://sandbox.zamzar.com/v1/files/"+str(file_id)+"/content".format(file_id)
        response = requests.get(endpoint, stream=True, auth=HTTPBasicAuth(api_key, ''))
        try:
         with open(local_filename, 'wb') as f:
             for chunk in response.iter_content():
              if chunk:
                f.write(chunk)
                f.flush()

             print("File downloaded")
             is_converted=True
            #Uncomment this if you want to delete file from zamzar server imidietely after conversion by default it will be deleted after 2 days in paid plan 
             endpoint = "https://api.zamzar.com/v1/files/"+str(file_id)  
             endpoint=endpoint.format(file_id)
             res = requests.delete(endpoint, auth=HTTPBasicAuth(api_key, ''))
         return {'status':is_converted,'credit_cost':credit_cost}

        except IOError:
            print("Error")
            return {'status':is_converted}
            

