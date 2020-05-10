
print("job_search Execution Starts Here!")

import job_scraper
from job_scraper import find_jobs_from

desired_characs = ['titles', 'companies', 'links', 'date_listed']

find_jobs_from('Indeed', 'data scientist', 'london', desired_characs)

print("job_search Execution Ends Here!")

