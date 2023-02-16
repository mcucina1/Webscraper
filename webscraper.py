from bs4 import BeautifulSoup
import requests
import time

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

def find_jobs():
    index = 1
    with open('job_postings.txt', 'w') as file:
        for job in jobs:
            published_date = job.find('span', class_='sim-posted').span.text
            if 'few' in published_date:
                company_name=job.find('h3', class_= 'joblist-comp-name').text.replace(' ','')
                skills = job.find('span', class_= 'srp-skills').text.replace(' ', '')
                link = job.header.h2.a['href']
                file.write(f'Job Posting #{index}\n\n')
                file.write(f'Company Name: {company_name.strip()}\n')
                file.write(f'Skills: {skills.strip()}\n')
                file.write(f'Link: {link}\n\n')
                index+=1


if __name__ == '__main__':
    while True:
        find_jobs()
        print('Waiting 10 minutes...')
        time.sleep(600)
