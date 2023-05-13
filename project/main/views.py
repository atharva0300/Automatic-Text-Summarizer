from django.shortcuts import render
import matplotlib.pyplot as plt

from django.http import HttpResponse


# importing the algo selector form
from .forms import AlgoSelectorForm, ChangeAlgoForm, OptionsSelectorForm, PDFForm, CloudAbbreviation

# importing rest frameork API views 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# from algo folder calling all the algorithms 
from .algo import word_cloud, lsa, lexrank, kl_sum


fileName = ""

# Create your views here.
def home_view(request) :
    
    return render(request , 'home.html' , {})


def try_view(request) :

    if request.method=='POST' : 
        form = AlgoSelectorForm(request.POST)
    
        if form.is_valid() : 
            selected = form.cleaned_data.get("algo_name")

            print('form : ' , form.cleaned_data)


            print(selected)
            selected = int(selected)

            document_text = form.cleaned_data.get("document_text")

            algo_name = ""
            
            # create a text file 
            f = open('./project/main/documents/one.txt' , 'w')
            f.write(document_text)
            f.close()

            if (selected is 1) : 
                # executing the kl_sum python file 
                # importing the kl_sum.py file 
                print('inside if 1')
                document_output = kl_sum.execute(document_text , True)
                directory  = "/home/atharva007/Documents/GitHub/Automatic-Text-Summarizer/project/main/algo/output1.txt"
                algo_name = "KL Sum ALgorithm"    

            elif (selected is 2) : 
                # executing the kl_sum python file 
                # importing the kl_sum.py file 
                print('inside if 2')
                document_output = lexrank.execute(document_text , True)
                directory  = "/home/atharva007/Documents/GitHub/Automatic-Text-Summarizer/project/main/algo/output2.txt"
                algo_name = "LexRank Algorithm"
            elif (selected is 3) : 
                # executing the kl_sum python file 
                # importing the kl_sum.py file
                print('inside if 3 ') 
                document_output = lsa.execute(document_text , True)
                directory  = "/home/atharva007/Documents/GitHub/Automatic-Text-Summarizer/project/main/algo/output3.txt"
                algo_name = "LSA Algorithm"


            form2 = ChangeAlgoForm()
            # initializing a form to change the algo

            convertionForm = CloudAbbreviation()


            total = {
                'algo_name' : algo_name,
                'document_text' : document_text,
                'document_output' : document_output,
                'form' : form2,
                'form2' : convertionForm
            }

            return render(request , 'summarizer.html' , {'total' : total})
    
        else : 
            return render(request , 'summarizer.html' , {"algo_name" : "Form is not valid"})
    
    elif request.method=='GET' : 
        form = AlgoSelectorForm()

        # getting the form layout 
        # and passing it to the html page 

        return render(request , 'summarizer.html' , {'form' : form})


def change_algo(request) : 

    
    # handling get request 
    if request.method=='POST' : 
        print('POST request received')


        form = ChangeAlgoForm(request.POST)

        if form.is_valid() : 

            print('form : ' , form)

            selected = form.cleaned_data.get('algo_name')
        
            print('Algo Changed to : ' , selected)

            selected = int(selected)

            algo_name = ""

            directory  = "/home/atharva007/Documents/GitHub/Automatic-Text-Summarizer/project/main/algo/output.txt"


            if (selected is 1) : 
                # executing the kl_sum python file 
                # importing the kl_sum.py file 
                print('inside if 1')
                kl_sum.execute()
                algo_name = "KL Sum ALgorithm"    
                directory  = "/home/atharva007/Documents/GitHub/Automatic-Text-Summarizer/project/main/algo/output1.txt"

            elif (selected is 2) : 
                # executing the kl_sum python file 
                # importing the kl_sum.py file 
                print('inside if 2')
                lexrank.execute()

                algo_name = "LexRank Algorithm"
                directory  = "/home/atharva007/Documents/GitHub/Automatic-Text-Summarizer/project/main/algo/output2.txt"

            elif (selected is 3) : 
                # executing the kl_sum python file 
                # importing the kl_sum.py file 
                print('inside if 3')
                lsa.execute()
                algo_name = "LSA Algorithm"
                directory  = "/home/atharva007/Documents/GitHub/Automatic-Text-Summarizer/project/main/algo/output3.txt"


            print('Algo name : ' , algo_name)

            
            # after the ewxecution, get the output file and display it 
            file1 = open(directory , 'r')
            document_output = file1.read()
            # reading all the lines

            # execute the python file 
            print(document_output)

            form2 = ChangeAlgoForm()
            # initializing a form to change the algo

            directory2  = "/home/atharva007/Documents/GitHub/Automatic-Text-Summarizer/project/main/documents/one.txt"
            
            # opening the file 
            file1 = open(directory2 , "r")
            document_text = file1.read()

            total = {
                'algo_name' : algo_name,
                'document_text' : document_text,
                'document_output' : document_output,
                'form' : form2
            }




            return render(request , 'summarizer.html' , {'total' : total})

        else : 
            print('Form is not Valid')
            # if the form is not valid then 
            return render(request , 'summarizer.html' , {})

    elif request.method=='GET' : 
        print('GET method received')

        return render(request , 'summarizer.html' , {})


def about(request) : 
    if request.method=='GET' : 
        # hadnling the get request here
        print('Inside the about get')

        return render(request , 'about.html' , {})
    

def options_view(request) : 
    if request.method =='GET' : 
        print('Handling the get request')

        # obtain an empty form and display it
        optionsForm = OptionsSelectorForm()
        

        return render(request,  'options.html' , {'form' : optionsForm , 'heading' : 'What do want to do?' , 'action' : 'options'})
    
    elif request.method=='POST' : 
        print('Handling the post request')

        # obtain the contents of the post form 
        receivedForm = OptionsSelectorForm(request.POST)

        print('received Form : ' , receivedForm)

        if receivedForm.is_valid() : 
            option = receivedForm.cleaned_data.get('option')

            print('option selected : ' , option)

            if(option=='1') : 
                # extracting the text from the pdf and then summariing the text 
                print('inside option 1')
                
                pdfForm = PDFForm()
                return render(request , 'extractpdf.html' , {'form' : pdfForm , 'heading' : 'Upload a PDF File'})

            elif(option=='2') :
                # sumzrization from an input text
                print('inside option 2')

                summarizer = AlgoSelectorForm()

                return render(request , 'summarizer.html' , {'form' : summarizer})
        
  
            




def extractPDF_view(request) : 
    if request.method == 'GET' : 
        print('inside the get method of the extract pdf')

        return render(request , 'summarizer.html' , {'form' : ''} )
    
    elif request.method =='POST' : 
        print('handling the file')

        pdfForm = PDFForm(request.FILES)

        print('pdfForm : '  , pdfForm)

        if pdfForm.is_valid () : 
            print('the pdf form is valid')
            file  = pdfForm.cleaned_data.get('file')

            print('file : ' , file)

            # pass the file in the summarizer function 
            

            return render(request , 'summarizer.html'  , {'form'  : ''})
    
        else :
            print("The pdfFrom is not valid")
        


def convertionView(request) : 
    print('inside the convertion view')

    if request.method=='POST': 
        print('inside the post of convertionView')

        receivedForm = CloudAbbreviation(request.POST)

        if receivedForm.is_valid() : 
            print('form is valid')

            option = receivedForm.cleaned_data.get('option')

            if( option=='1') : 
                print('selected option 1')

                # calling the cloud program, passing teh output file in the program and taking the output and pasting it on the page 
                result = word_cloud.execute('output1.txt')

                # obtaining the image from the stored file 
                if result : 
                    print('the image file has been saved')

                    # sending the file to the website

                    
                else : 
                    print('The image file has not been saved')



            elif (option=='2') : 
                print('selectedd option 2')