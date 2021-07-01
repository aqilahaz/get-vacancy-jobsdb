
import ast
from bs4 import BeautifulSoup
import requests
import json

def make_dictionary(soup):
    lib = {}
    lib['platform'] = 'jobsdb'
    for tanggal in soup.find_all('p', {"class":"data-timestamp"}):
    	lib['tanggal'] = tanggal.text
    for pekerjaan in soup.find_all('h1', {"class":"general-pos"}):
        lib['pekerjaan'] = pekerjaan.text
    for job in soup.find_all('h2', {"class":"jobad-header-company"}):
        lib['perusahaan'] = job.text
    for pnglaman in soup.find_all('b', {"class":"primary-meta-exp"}):
        lib['pengalaman'] = pnglaman.text
    for pend in soup.find_all('p', {"class":"meta-item primary-meta-edu col-xs-9"}):
        lib['pendidikan'] = pend.text
    for loc in soup.find_all('a', {"class":"loc-link"}):
        lib['lokasi'] = loc.text
    for gaj in soup.find_all('span', {"id":"salaryTooltip"}):
        lib['gaji'] = gaj.text
    for tipe in soup.find_all('div', {"class":"primary-meta-box row meta-employmenttype"}):
        lib['tipe'] = tipe.text
    for inds in soup.find_all('div', {"class":"primary-meta-box row meta-industry"}):
        lib['industri'] = inds.text
    for lev in soup.find_all('div', {"class":"primary-meta-box row meta-lv"}):
        lib['level'] = lev.text   
    for spec in soup.find_all('div', {"class":"jobad-primary-details"}):
        lib['kualifikasi'] = spec.text
    return lib


a_list = [] 
with open('one_list.txt', 'r') as f:
    mylist = ast.literal_eval(f.read())

print("Job Start")
num = 0
for link in mylist:
    html_doc = requests.get(link).text
    soup = BeautifulSoup(html_doc, 'html.parser')
    kamus=make_dictionary(soup)
    dictionary_copy = kamus.copy()
    a_list.append(dictionary_copy)
    num+=1
    print(num)


with open('jobsdb.json', 'w') as fp:
    json.dump(a_list, fp)
print("Job Finished")