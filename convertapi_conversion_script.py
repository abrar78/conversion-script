    #Pass the parameters with the source (docx)file absolute location ,and the target file(pdf) absolute location where you want to save the file including its name on your machine
    # example:-
    #source_file='~/test.docx'
    #target_file='~/converted/test.pdf
    #note :- send complete file path with the proper extension
    #Function returns dict type with status and conversion credit cost, if file converted and Downloaded successfully
    #module require convertapi can be installed using pip3 install convertapi 


import convertapi

def convert_convertApi(source_file,target_file):
    #Pass the parameters with the source file absolute location and the target file absolute location where you want to save the file example:-
    #source_file='~/test.docx'
    #target_file='~/converted/test.pdf
    #note :- send complete file path with the proper extension
    is_converted=False

    convertapi.api_secret = 'Vm0zyKIXYRRAv1dC' #Your convert api secret key , you will get it from the convertapi acccount , here this key is for testing purpose only
    result = convertapi.convert('pdf', { 'File': source_file })
    result.file.save(target_file)
    is_converted=True	
    conversion_cost = result.conversion_cost
    return {'status':is_converted,'conversion_cost':conversion_cost}
