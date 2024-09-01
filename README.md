# Automation tests for the redesign of "Mathematical Education" Journal web-site

## Test scenarios

### Home Page Contains "Download All Issues" Link
WHEN  
User opens home page "https://matob.ru"  
THEN  
It should contain a link to download all the issues 
"https://matob.ru/files/math_edu_journal_full_archive.zip"

### Home Page Contains "MCCME" Link
WHEN  
User opens home page "https://matob.ru"  
THEN  
It should contain a link to MCCME site 
"https://mccme.ru" with "target=_blank" parameter

### Archive Page Contains "Download All Issues" Link
WHEN  
User opens page with issues archive "https://matob.ru/archive.html"  
THEN  
It should contain a link to download all the issues 
"https://matob.ru/files/math_edu_journal_full_archive.zip"

### Archive Page Contains Links For All Issues
WHEN  
User opens page with issues archive "https://matob.ru/archive.html"  
THEN  
It should contain the same list of links to download each issue as before the redesign  
+ Get current list of links  
+ Compare it with list of links after redesign


