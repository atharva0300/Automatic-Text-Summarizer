from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render


# importing the algo selector form
from .forms import AlgoSelectorForm, ChangeAlgoForm



# Create your views here.
def home_view(request) :
    
    return render(request , 'home.html' , {})


def try_view(request) :

    if request.method=='POST' : 
        form = AlgoSelectorForm(request.POST)
    
        if form.is_valid() : 
            selected = form.cleaned_data.get("algo_name")

            print(selected)
            selected = int(selected)

            document_text = form.cleaned_data.get("document_text")

            algo_name = ""

            if (selected is 1) : 
                algo_name = "KL Sum ALgorithm"    
            elif (selected is 2) : 
                algo_name = "LexRank Algorithm"
            elif (selected is 3) : 
                algo_name = "LSA Algorithm"


            

            directory  = "/home/atharva007/Documents/GitHub/Automatic-Text-Summarizer/project/main/algo/output.txt"

            # executing the kl_sum python file 
            # importing the kl_sum.py file 
            from .algo import kl_sum

            # after the ewxecution, get the output file and display it 
            file1 = open(directory , 'r')
            document_output = file1.read()
            # reading all the lines

            # execute the python file 
            print(document_output)

            form2 = ChangeAlgoForm()
            # initializing a form to change the algo

            total = {
                'algo_name' : algo_name,
                'document_text' : document_text,
                'document_output' : document_output,
                'form' : form2
            }




            return render(request , 'try.html' , {'total' : total})
    
        else : 
            return render(request , 'try.html' , {"algo_name" : "Form is not valid"})
    
    elif request.method=='GET' : 
        form = AlgoSelectorForm()

        # getting the form layout 
        # and passing it to the html page 

        return render(request , 'try.html' , {'form' : form})


def change_algo(request) : 

    
    # handling get request 
    if request.method=='POST' : 
        print('POST request received')


        form = ChangeAlgoForm(request.POST)

        if form.is_valid() : 

            selected = form.cleaned_data.get('algo_name')
        
            print('Algo Changed to : ' , selected)

            selected = int(selected)

            algo_name = ""

            if (selected is 1) : 
                algo_name = "KL Sum ALgorithm"    
            elif (selected is 2) : 
                algo_name = "LexRank Algorithm"
            elif (selected is 3) : 
                algo_name = "LSA Algorithm"


            print('Algo name : ' , algo_name)

            

            directory  = "/home/atharva007/Documents/GitHub/Automatic-Text-Summarizer/project/main/algo/output.txt"

            # executing the kl_sum python file 
            # importing the kl_sum.py file 
            from .algo import kl_sum

            # after the ewxecution, get the output file and display it 
            file1 = open(directory , 'r')
            document_output = file1.read()
            # reading all the lines

            # execute the python file 
            print(document_output)

            form2 = ChangeAlgoForm()
            # initializing a form to change the algo

            directory  = "/home/atharva007/Documents/GitHub/Automatic-Text-Summarizer/project/main/documents/one.txt"
            
            # opening the file 
            file1 = open(directory , "r")
            document_text = file1.read()

            total = {
                'algo_name' : algo_name,
                'document_text' : document_text,
                'document_output' : document_output,
                'form' : form2
            }




            return render(request , 'try.html' , {'total' : total})

        else : 
            print('Form is not Valid')
            # if the form is not valid then 
            return render(request , 'try.html' , {})

    elif request.method=='GET' : 
        print('GET method received')

        return render(request , 'try.html' , {})


