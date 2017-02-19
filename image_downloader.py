import requests
from bs4 import BeautifulSoup as bs
url='https://www.google.co.in/search?q='
urladd='&espv=2&biw=1366&bih=662&tbm=isch&tbo=u&source=univ&sa=X&ved=0ahUKEwirtI-kspvSAhXMLY8KHRsqAlYQsAQIHw'
q=input('enter the tag of images')
u=url+q+urladd
r=requests.get(u)
soup=bs(r.text,'html.parser')
soup.find_all('img')
images=soup.find_all('img')
result=[]
for image in images:
	result.append(image.get('src'))
i=0
for result in result:
    with open('C:/Users/Hp/Desktop/dwnimg/'+q+str(i)+'.jpg','wb') as f:
        r=requests.get(result,stream=True)
        f.write(r.content)
    i+=1
          
          
