import unittest
from selenium import webdriver

class WebsiteLoadingTest(unittest.TestCase):
    def setUp(self):
        # Set up the browser driver (assuming you have WebDriver installed)
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Close the browser window after the test
        self.driver.quit()

    def test_website_loading(self):
        # Open the atg.world website
        self.driver.get("https://www.atg.world")

        # Get the current page title
        page_title = self.driver.title

        # Print the page title for debugging
        print(f"Page Title: {page_title}")

        # Check if the page title contains expected text
        self.assertIn("Across The Globe", page_title)

if __name__ == '__main__':
    unittest.main()