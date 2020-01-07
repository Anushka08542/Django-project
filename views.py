from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from django.http import HttpResponse
import io
import operator
from appone.forms import new_form
from appone.forms import login_form
from appone.models import Logs
from django.contrib.auth import authenticate

# ----------Q1.1-------
df=pd.read_csv('/home/Anushka/zomato/zomato.csv',encoding="iso-8859-1")
df_=df
df_=df_[df_['Country Code']==1]
df_.reset_index(drop=True,inplace=True)
df1=df_['Cuisines'].str.split(',')
df2=df_['City']
df1.fillna('',inplace=True)
dict1={}
l=['New Delhi', 'Ghaziabad', 'Noida', 'Gurgaon', 'Faridabad']
for i in range(df_.shape[0]):
    city_=df2[i]
    cui=df1[i]
    for a in cui:
        a=(a.strip())
        if a in dict1:
            if city_ in l:
                dict1[a]=1
        else:
            dict1[a]=0
# p is list of cuisines not present in Delhi-NCR
p=[]
for i,j in dict1.items():
    if j==0:
        p.append(i)

def index(request):
    return render(request,'appone/index.html')

def cuisines(requests):
    my_dict={'cuisines':p}
    return render(requests,'appone/cuisines.html',context=my_dict)

#country code :1=India
#----------Q1.2----------

df_=(df_[df_['Country Code']==1])
dict1={'Delhi-NCR':1,'Rest of India':1}
l=['New Delhi', 'Ghaziabad', 'Noida', 'Gurgaon', 'Faridabad']
for i in df_['City']:
    if i in l:
        dict1['Delhi-NCR']+=1
    else:
        dict1['Rest of India']+=1
##graph
x=list(dict1.keys())
y=list(dict1.values())
fig, ax = plt.subplots()
ax.bar(x,y)
    
ax.set(xlabel='location', ylabel='Number of restaurants',title='Case study Q1.2')
#ax.grid()
def restaurants(request):
    buf = io.BytesIO()
    canvas = FigureCanvasAgg(fig)
    canvas.print_png(buf)
    response = HttpResponse(buf.getvalue(),content_type = 'image/png')
    return response


#--------- Q1.3---------
dict2={}
dict3={}
for i in range(df_.shape[0]):
    city=df2[i]
    cui=df1[i]
    for a in cui:
        a=(a.strip())
        if city in l:
            if a in dict3:
                dict3[a]+=1
            else:
                dict3[a]=1
        else:
            if a in dict2:
                dict2[a]+=1
            else:
                dict2[a]=1

dict2=sorted(dict2.items(),key=operator.itemgetter(1),reverse=True)
dict3=sorted(dict3.items(),key=operator.itemgetter(1),reverse=True)
# DELHI-NCR
#print("TOP 10 CUISINES IN DELHI NCR \n")
count=0
x1=[]
y1=[]
for i in dict3:
    if count==10:
        break
    x1.append(i[0])
    y1.append(i[1])
    count+=1
# REST OF INDIA
#print("\nTOP 10 CUISINES IN REST OF INDIA \n")
count=0
x2=[]
y2=[]
for i in dict2:
    if count==10:
        break
    x2.append(i[0])
    y2.append(i[1])
    count+=1
# GRAPH: DELHI-NCR
fig1,ax=plt.subplots(figsize=(11, 5))
ax.bar(x1,y1)
ax.set(title='DELHI NCR')
#plt.xticks(rotation=25)
plt.xlabel('Cuisines',color="green")
plt.ylabel('Number',color="green")
def dgraph(request):
    buf=io.BytesIO()
    canvas = FigureCanvasAgg(fig1)
    canvas.print_png(buf)
    response=HttpResponse(buf.getvalue(),content_type='image/png')
    return response

#GRAPH: REST OF INDIA
fig2,ax2=plt.subplots(figsize=(11, 5))
ax2.bar(x2,y2)
ax2.set(title='REST OF INDIA')
plt.xlabel('Cuisines',color="green")
plt.ylabel('Number',color="green")
def rgraph(request):
    buf=io.BytesIO()
    canvas = FigureCanvasAgg(fig2)
    canvas.print_png(buf)
    response=HttpResponse(buf.getvalue(),content_type='image/png')
    return response


def top_cuisines(requests):
    my_dict={'delhi':x1,'rest':x2}
    return render(requests,'appone/top.html',context=my_dict)



#--------- Q1.4 -------
df1=df['Average Cost for two']
df2=df['Aggregate rating']
dict1={}
for i in range(df.shape[0]):
    a=df1[i]
    if a==0:
        continue
    if a >100:
        a=(a-a%100)
    b=df2[i]
    if a in dict1:
        dict1[a]=round((dict1[a]+b)/2,1)
    else:
        dict1[a]=b
dict1=sorted(dict1.items(),key=operator.itemgetter(0))
x=[]
y=[]
for i in dict1:
    x.append(i[0])
    y.append(i[1])

fig3,ax3=plt.subplots(figsize=(11, 5))
ax3.scatter(x,y)
ax3.set(xlabel='Avg Cost',ylabel='Rating',title='For complete range of avg cost')

def avg_cost(request):
    buf=io.BytesIO()
    canvas = FigureCanvasAgg(fig3)
    canvas.print_png(buf)
    response=HttpResponse(buf.getvalue(),content_type='image/png')
    return response

fig4,ax4=plt.subplots(figsize=(11, 5))
ax4.plot(x2,y2)
ax4.set(xlabel='Avg cost',ylabel='Rating',title='For lower range of avg cost')

def avg_cost2(request):
    buf=io.BytesIO()
    canvas = FigureCanvasAgg(fig4)
    canvas.print_png(buf)
    response=HttpResponse(buf.getvalue(),content_type='image/png')
    return response

df_=df[df['Country Code']==216]
df_.reset_index(drop=True,inplace=True)
df1=df_['Cuisines']
df1.fillna("",inplace=True)
dict1={}
for i in range(df1.shape[0]):
    j=df1[i].split(', ')
    for a in j :
        if a=='':
            continue
        if a in dict1:
            dict1[a]+=1
        else:
            dict1[a]=1
dict1=sorted(dict1.items(),key=operator.itemgetter(1),reverse=True)
x=[]
y=[]
for i in dict1[:10]:
    x.append(i[0])
    y.append(i[1])
#plt.pie(y,labels=x)
#plt.axis("equal")
#plt.title('top 10 cuisines present in restaurants in the USA \n',color='green')
#plt.show()
fig5,ax5=plt.subplots(figsize=(11, 5))
ax5.pie(y,labels=x,autopct='%.2f%%')
plt.title('top 10 cuisines present in restaurants in the USA',color="red")

def pie_chart(request):
    buf=io.BytesIO()
    canvas = FigureCanvasAgg(fig5)
    canvas.print_png(buf)
    response=HttpResponse(buf.getvalue(),content_type='image/png')
    return response

def about(requests):
    return render(requests,'appone/about.html')

def my_model(request):
    form=new_form()
    if request.method=='POST':
        form = new_form(request.POST)
        if form.is_valid():
            form.save(commit=True)
#            return index(request)
#            html='<html><body><h2> Successfully submitted, we will revert back shortly. <a href="{% url "appone:about" %}"> HOME </a> </h2> </body></html>'
            return form_page(request)
        else:
            print("Error")
    return render(request,'appone/my_model.html',{'form':form})

def form_page(request):
    return render(request,'appone/form_page.html')

def login(request):
    form=login_form()
    if request.method=='POST':
        #form=login_form(data=request.POST)
        user_name = request.POST.get('name')
        pass_word = request.POST.get('password')
        try:
            web_list=Logs.objects.get(name=user_name,password=pass_word)
        except Logs.DoesNotExist:
            web_list = None
        if web_list!=None:
            return form2(request)
        else:
            print("Error")
    return render(request,'appone/login.html',{'form':form})            

def form2(request):
    return render(request,'appone/form2.html')






