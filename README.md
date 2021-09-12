# Global News Highlight
An application that will help users to list and preview news articles from various sources.   

## Built By [Hannah Waruguru](https://github.com/HWaruguru/)

## Description
Global News Highlight is a web application that displays a list of various news sources like BBC and CNN. On choosing a news source, it will preview the top news articles of the day. Clicking a news article will redirect the user to read it fully from the news source. It achieves this by using the [News API](https://newsapi.org/).

You can view the site at: 

## User Stories
These are the behaviours/features that the application implements for use by a user.

A user will be able to:
* See various news sources 
* Select the ones they prefer
* See the top news articles from that news source
* See the image, description and time the news article was created
* Click on an article and read it fully from the news source

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display news sources | **On page load** | List of various news sources is displayed per category |
| Display articles from a news source | **Click on a news source** | Redirected to a page with a list of articles from the source |
| Display the preview of an article | **On page load** | Each article displays an image, title, description and publication date |
| Read an entire article | **Click on the Article** | Redirected to the news source's site to read the entire article |
| Go back to news sources | **Click on Global-News-Highlight** | Redirected to the homepage |
## SetUp / Installation Requirements
### Prerequisites
* python3.9
* pip
* virtualenv

### Cloning
* In your terminal:
        
        $ git clone https://github.com/HWaruguru/Global-News-Highlight/
        $ cd Global-News-Highlight

## Running the Application
* Setting up the application

        $ python3 -m venv virtual
        $ source virtual/bin/env
        $ pip install -r requirements.txt
        
* Setting up the API Key
        
        To be able to gather article info from the News API you will need an API Key.
        
        * Visit https://newsapi.org/ and register for an API key.
        * Insert the API Key you received from News API where <Your-API-Key> is.
        
* To run the application, in your terminal:
        $ python run.py

## Testing the Application
* To run the tests for the class files:

        $ python -m unittest discover -s tests
   
## Technologies Used
* Python3.9
* Flask

## License
MIT &copy;2021 [Hannah Waruguru](https://github.com/HWaruguru/)