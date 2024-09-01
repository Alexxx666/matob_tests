import requests
from bs4 import BeautifulSoup
from functools import wraps


def request_and_parse(url):
    def decorator(func):
        @wraps(func)
        def wrapper():
            response = requests.get(url)
            response.encoding = 'utf8'
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                return func(soup, url)
            else:
                print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
                return None
        return wrapper
    return decorator


@request_and_parse("https://matob.ru")
def homePageContainsDownloadAllIssuesLink(soup, url):
    link_to_check = "files/math_edu_journal_full_archive.zip"
    links = soup.find_all('a', href=True)

    if any(link['href'] == link_to_check for link in links):
        print(f"Success - the link '{link_to_check}' is present on the page '{url}'")
    else:
        print(f"Failure - the link '{link_to_check}' is NOT present on the page.")


@request_and_parse("https://matob.ru")
def homePageContainsMCCMELink(soup, url):
    link_to_check = "https://www.mccme.ru/"
    target_to_check = "_blank"
    links = soup.find_all('a', href=True)

    if any(link['href'] == link_to_check and link.get('target') == target_to_check for link in links):
        print(f"Success - the link '{link_to_check}' with target='{target_to_check}' is present on the page '{url}'")
    else:
        print(f"Failure - the link '{link_to_check}' with target='{target_to_check}' is NOT present on the page.")


@request_and_parse("https://matob.ru/archive.html")
def archivePageContainsDownloadAllIssuesLink(soup, url):
    link_to_check = "files/math_edu_journal_full_archive.zip"
    links = soup.find_all('a', href=True)

    if any(link['href'] == link_to_check for link in links):
        print(f"Success - the link '{link_to_check}' is present on the page '{url}'")
    else:
        print(f"Failure - the link '{link_to_check}' is NOT present on the page.")


@request_and_parse("https://matob.ru/archive.html")
def archivePageContainsLinksForAllIssues(soup, url):
    file = open("issues_link_list.txt", "r")
    links_to_check = file.readlines()

    current_links = soup.find_all('a', download=True)

    if links_to_check[0] == str(current_links):
        print(f"Success - link list on the archive page corresponds to previous version.")
    else:
        print(f"Failure - link list on the archive page DOES NOT correspond to previous version.")


# Run the tests
homePageContainsDownloadAllIssuesLink()
homePageContainsMCCMELink()
archivePageContainsDownloadAllIssuesLink()
archivePageContainsLinksForAllIssues()