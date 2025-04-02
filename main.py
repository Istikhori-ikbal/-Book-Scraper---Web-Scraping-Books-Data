from bs4 import BeautifulSoup 
import requests
import csv 

def scrape_books():
    url = 'http://books.toscrape.com/'
    response = requests.get(url)
    
    if response.status_code != 200:
        print('Failed to retrieve the page')
        return
    
    soup = BeautifulSoup(response.text, 'lxml')
    books = soup.find_all('article', class_='product_pod')

    book_data = []
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text.strip()
        rating = book.p['class'][1] #Extracting star rating
        availability = book.find('p', class_='instock availability').text.strip()
        book_data.append([title, price, rating, availability])

    # Save to csv
    with open('books.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'Price', 'Rating', 'Availability'])
        writer.writerows(book_data)
    
    print("Scraping complete! Data saved to books.csv")


if __name__ == '__main__' :
    scrape_books()