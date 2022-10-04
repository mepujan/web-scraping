import urllib.request
from bs4 import BeautifulSoup as soup
import csv

def main():
    release_date_list=[]
    release=[]
    movie_list=[]
    url='https://en.wikipedia.org/wiki/List_of_Blumhouse_Productions_projects'
    request=urllib.request.urlopen(url)
    print('status code: ',str(request.getcode()))
    data=request.read()
    page_soup=soup(data,'html.parser')
    table_data=page_soup.find_all('td')
    for movie in table_data:
        release_date_list.append(movie.get_text())
        a_data=movie.find_all('a')
        for m_data in a_data:
            if m_data !=None:
                movie_list.append(m_data.get('title'))
    print(len(release_date_list))
    for release_date in range(387):
        if release_date %3 ==0:
            if release_date_list[release_date] != None :
                release.append(release_date_list[release_date])
        # if release_date % 2 == 0:
        #     if release_date_list[release_date] != None :
        #         print(release_date_list[release_date])
        #         release.append(release_date_list[release_date])
    print(release_date_list)

    for i in range(len(release_date_list)):
        if i % 2 ==0:
            print(release_date_list[i])
        
    
    with open('moviedb.csv','w',newline='') as movie:
        writer=csv.writer(movie,escapechar='\n')
        row_list=zip(release,movie_list)
        writer.writerow(['Release Date','Title'])
        for row in row_list:
            writer.writerow(row)
       
    
    
            
        

if __name__== '__main__':
    main()