# -*- coding: utf-8 -*-
"""merve bağçiçek.ipynb adlı dosyanın kopyası

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G4YIaLgYGQS-f9UWKerw0LxCCgfmuY97

*Hello*, please change the file name as your name_surname_MIDTERM.ipynb and upload to the folder 'DROP MIDTERMS HERE' on Drive.
ex: atay_ilgun_MIDTERM.ipynb

*Describe* what ML is in 50 words.

*Machine Learning is the sub-branch of artificial intelligence. defined as data interpretation tools that can be used in any case where the data.*

Give 3 examples of ML in practical use in todays world - also, meditate on how it is being utilised as well.

*FACEBOOK, NETFLIX, GOOGLE*
*One of the Facebook and google's using purposes is that knowing what people need and use ML to show commercials to what people need.*

*Netflix is using ML for showing users one of the film/series scenes as a picture. Because they try to use it to attract people's attention to the movie of series.*

In ML terminology what is an 'example', 'feature', 'label' and 'feature vector'?

**Samples**
– A sample is an item to process (e.g. classify). It can be a document, a
picture, a sound, a video, a row in database or CSV file, or whatever you
can describe with a fixed set of quantitative traits.
**Features**
– The number of features or distinct traits that can be used to describe
each item in a quantitative manner. •
The label is the final choice of your inputs such as Golden, Chiwawa.
**Feature vector**
– is an n-dimensional vector of numerical features that represent some
object.

In 100 words meditate on how future advancements on AI could affect your work practice as a communication designer.

*For communication designers we can say the following for the effects of AI use;* 

*Communication designers can produce faster jobs by wasting less time. For example, when the customer wants to make logo, we can get the ideal logo with artificial Intelligence by making the customer's job description. Or Artificial Intelligence change communication designers interest areas and designers try to improve AI looks. *

Try to describe how you learn in algorithmic terms.

*first we learn basic words and then our brain bring them together and then we use them to make sentences*

Create a python dictionary for your name surname and year of birth.
"""

whoami= {'name':'merve','surname':'bağçiçek','birth':'1995'}

"""Write a conditional so If the first letter of your name is 'a' print 'my initial is a!'"""

if whoami['name'][0] =='a':
  print("my initial is a")

"""Write a conditional so If your surnames letter count is divisable by 3 print 'it is divisible' if not 'not divisible'."""

if len(whoami['surname']) % 3 ==0:
 print('it is divisible')
else:
    print('not divisible')

"""Change your year of birth to 2678."""

whoami["birth"]=2678
print (whoami)

"""Create a loop that goes through 20 to 40 and prints out the numbers that are divisble by 5."""

list_1 = range(20,40)

for everynumber in list_1:
 if everynumber % 5==0:
    print(everynumber)

"""Check the PDF on the Drive and calculate the neurons. Put all neurons and weights in python and do the calculation with them."""

x=(0.87*0.12) + (0.12*0.54) + (0.62*0.61)

a=0.87
b=0.12
c=0.62

x=0.12
y=0.54
z=0.61

soruisareti = (a*b)+(b*y)+(c*z)

print (soruisareti)

"""Using the code here:
https://github.com/anishathalye/neural-style
create a ***style transfer*** image.

Upload it along with this file.

You might need a file while doing this, it also is on the Drive!
"""