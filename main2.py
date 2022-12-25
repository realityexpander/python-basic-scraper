# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import requests
from bs4 import BeautifulSoup

url = 'https://subslikescript.com/movies'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
ul_scripts_list = soup.find('ul', class_='scripts-list')

for a in ul_scripts_list.find_all('a'):
    print(a.text)

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/