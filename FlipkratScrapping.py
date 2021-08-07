import random
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from RepositoryForObject import ObjectRepository
from selenium.webdriver.common.by import By
import pandas as pd
import uuid
from CassandraDBOperations import cassandraDBManagement
from logger1 import App_Logger





path = 'secure-connect-flipkartscrapper.zip'
user_id = 'EyeOFNUtvBEWdsuTcwTjqLQQ'
secure_key = 'K,Xh4igbTq5ZCvRK,_q5u6qieJXwZXpS5dszUGz1Kf1HvBv-HDA,NPvreG.dN4RzYDL0ixBTsnlfzffdSpZIaUKHgshvYgc,x.mj+h8jauSlS.u06nbJFXmnxsTZ9rky'
key_space = 'tj'
table_name = 'flipkart_heroku1'





class FlipkratScrapper:

    def __init__(self, executable_path, chrome_options):
        """
            This class shall  be used for initializing the web browser driver.

            Written By: Tejas Jay (TJ)
            Version: 1.0
            Revisions: None
        """
        self.logging = App_Logger()
        self.logging.log('Entered the __init__ method of get FlipkratScrapper class')
        try:
            self.driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)
        except Exception as e:
            self.logging.log('Unsuccessful in executing class FlipkratScrapper __init__ method, error message is: '+ str(e))
            raise e




    def waitExplicitlyForCondition(self, element_to_be_found):

        """
                Method Name: waitExplicitlyForCondition
                Description: This method explicitly waits for condition to satisfy.
                Output: None
                On Failure: Raise Exception

                Version: 1.0
                Revisions: None
        """
        self.logging.log('Entered the waitExplicitlyForCondition method of get FlipkratScrapper class')
        try:
            ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
            WebDriverWait(self.driver, 2, ignored_exceptions=ignored_exceptions).until(
                expected_conditions.presence_of_element_located((By.CLASS_NAME, element_to_be_found)))
            self.logging.log('Exited waitExplicitlyForCondition method of the FlipkratScrapper class successfully')
            return True
        except Exception as e:
            self.logging.log('Unsuccessful in executing waitExplicitlyForCondition method of the FlipkratScrapper class: error message is: '+ str(e))
            return e




    def getCurrentWindowUrl(self):
        """
                Method Name: getCurrentWindowUrl
                Description: This method returns the url of current window.
                Output: current_window_url
                On Failure: Raise Exception

                Version: 1.0
                Revisions: None
        """
        self.logging.log('Entered the getCurrentWindowUrl method of get FlipkratScrapper class')
        try:
            current_window_url = self.driver.current_url
            self.logging.log('Exited getCurrentWindowUrl method of the FlipkratScrapper class successfully')
            return current_window_url
        except Exception as e:
            self.logging.log('Unsuccessful in executing getCurrentWindowUrl method of the FlipkratScrapper class: error message is: '+ str(e))
            raise e




    def getLocatorsObject(self):
        """
                Method Name: getLocatorsObject
                Description: This method initializes the Locator object and returns the locator object.
                Output: Locator
                On Failure: Raise Exception

                Version: 1.0
                Revisions: None
        """
        self.logging.log('Entered the getLocatorsObject method of get FlipkratScrapper class')
        try:
            locators = ObjectRepository()
            self.logging.log('Exited getLocatorsObject method of the FlipkratScrapper class successfully')
            return locators
        except Exception as e:
            self.logging.log('Unsuccessful in executing getLocatorsObject method of the FlipkratScrapper class: error message is: '+ str(e))
            raise e




    def findElementByXpath(self, xpath):
        """
            Method Name: findElementByXpath
            Description: This method finds the web element using xpath passed.
            Output: element
            On Failure: Raise Exception

            Version: 1.0
            Revisions: None
        """
        self.logging.log('Entered the findElementByXpath method of get FlipkratScrapper class')
        try:
            element = self.driver.find_element(By.XPATH, value=xpath)
            self.logging.log('Exited findElementByXpath method of the FlipkratScrapper class successfully')
            return element
        except Exception as e:
            # self.driver.refresh()
            self.logging.log('Unsuccessful in executing findElementByXpath method of the FlipkratScrapper class: error message is: '+ str(e))
            raise e




    def findElementByClass(self, classpath):
        """
            Method Name: findElementByClass
            Description: This method finds web element using Classpath provided.
            Output: element
            On Failure: Raise Exception

            Version: 1.0
            Revisions: None
        """
        self.logging.log('Entered the findElementByClass method of get FlipkratScrapper class')
        try:
            element = self.driver.find_element(By.CLASS_NAME, value=classpath)
            self.logging.log('Exited findElementByClass method of the FlipkratScrapper class successfully')
            return element
        except Exception as e:
            # self.driver.refresh()
            self.logging.log('Unsuccessful in executing findElementByClass method of the FlipkratScrapper class: error message is: '+ str(e))
            raise e




    def findElementByTag(self, tag_name):
        """
            Method Name: findElementByTag
            Description: This method finds web element using tag_name provided.
            Output: element
            On Failure: Raise Exception

            Version: 1.0
            Revisions: None
        """
        self.logging.log('Entered the findElementByTag method of get FlipkratScrapper class')
        try:
            element = self.driver.find_elements_by_tag_name(tag_name)
            self.logging.log('Exited findElementByTag method of the FlipkratScrapper class successfully')
            return element
        except Exception as e:
            self.logging.log('Unsuccessful in executing findElementByTag method of the FlipkratScrapper class: error message is: '+ str(e))
            raise e




    def findingElementsFromPageUsingClass(self, element_to_be_searched):
        """
        Method Name: findingElementsFromPageUsingClass
        Description: This method finds all element from the page.
        Output: element
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the findingElementsFromPageUsingClass method of get FlipkratScrapper class')
        try:
            result = self.driver.find_elements(By.CLASS_NAME, value=element_to_be_searched)
            self.logging.log('Exited findingElementsFromPageUsingClass method of the FlipkratScrapper class successfully')
            return result
        except Exception as e:
            self.logging.log('Unsuccessful in executing findingElementsFromPageUsingClass method of the FlipkratScrapper class: error message is: '+ str(e))
            raise e




    def findingElementsFromPageUsingCSSSelector(self, element_to_be_searched):
        """
        Method Name: findingElementsFromPageUsingCSSSelector
        Description: This method finds all element from the page.
        Output: element
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the findingElementsFromPageUsingCSSSelector method of get FlipkratScrapper class')
        try:
            result = self.driver.find_elements(By.CSS_SELECTOR, value=element_to_be_searched)
            self.logging.log('Exited findingElementsFromPageUsingCSSSelector method of the FlipkratScrapper class successfully')
            return result
        except Exception as e:
            self.logging.log('Unsuccessful in executing findingElementsFromPageUsingCSSSelector method of the FlipkratScrapper class: error message is: '+ str(e))
            raise e




    def openUrl(self, url):
        """
        Method Name: openUrl
        Description: This method open the particular url passed.
        Output: None
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the openUrl method of get FlipkratScrapper class')
        try:
            if self.driver:
                self.driver.get(url)
                self.logging.log('Exited openUrl method of the FlipkratScrapper class successfully')
                return True
            else:
                return False
        except Exception as e:
            self.logging.log('Unsuccessful in executing openUrl method of the FlipkratScrapper class: error message is: '+ str(e))
            raise e




    def login_popup_handle(self):
        """
        Method Name: login_popup_handle
        Description: This method closes the login popup displayed.
        Output: None
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the login_popup_handle method of get FlipkratScrapper class')
        try:
            self.wait()
            locator = self.getLocatorsObject()
            self.findElementByXpath(xpath=locator.getLoginCloseButton()).click()
            self.logging.log('Exited login_popup_handle method of the FlipkratScrapper class successfully')
            return True
        except Exception as e:
            self.logging.log('Unsuccessful in executing login_popup_handle method of the FlipkratScrapper class: error message is: '+ str(e))
            raise e




    def searchProduct(self, searchString):
        """
        Method Name: searchProduct
        Description: This method searches product using search string provided by the user.
        Output: None
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the searchProduct method of get FlipkratScrapper class')
        try:
            locator = self.getLocatorsObject()
            search_box_path = self.findElementByXpath(xpath=locator.getInputSearchArea())
            search_box_path.send_keys(searchString)
            search_button = self.findElementByXpath(xpath=locator.getSearchButton())
            search_button.click()
            self.logging.log('Exited searchProduct method of the FlipkratScrapper class successfully')
            return True
        except Exception as e:
            # self.driver.refresh()
            self.logging.log('Unsuccessful in executing searchProduct method of the FlipkratScrapper class: error message is: '+ str(e))
            raise e




    def generateTitle(self, search_string):
        """
        Method Name: generateTitle
        Description: This method generates Title for the products searched using search string.
        Output: title
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the generateTitle method of get FlipkratScrapper class')
        try:
            title = search_string + "- Buy Products Online at Best Price in India - All Categories | Flipkart.com"
            self.logging.log('Exited generateTitle method of the FlipkratScrapper class successfully')
            return title
        except Exception as e:
            self.logging.log('Unsuccessful in executing generateTitle method of the FlipkratScrapper class: error message is: '+ str(e))
            raise e




    def getProductLinks(self):
        """
        Method Name: getProductLinks
        Description: This method returns all the product's list of links.
        Output: list of links
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the getProductLinks method of get FlipkratScrapper class')
        try:
            links = []
            all_links = self.findElementByTag('a')
            for link in all_links:
                links.append(link.get_attribute('href'))
            count = 0
            for i in links:
                if count > 15: break
                if '?pid=' in i:
                    print(i)
                    count = count + 1
                    yield str(i)
        except Exception as e:
            self.logging.log('Unsuccessful in executing getProductLinks method of the FlipkratScrapper class: error message is: '+ str(e))
            raise e





    def actualProductLinks(self):
        """
        Method Name: actualProductLinks
        Description: This method returns the actual product links after filtering.
        Output: individual product link
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the actualProductLinks method of get FlipkratScrapper class')
        try:
            productLinks = []
            count = 0
            for link in self.getProductLinks():
                if count > 15: break
                if '?pid=' in link:
                    print(link)
                    productLinks.append(link)
                    count = count + 1
                else:
                    continue
            self.logging.log('Exited actualProductLinks method of the FlipkratScrapper class successfully')
            return productLinks
        except Exception as e:
            self.logging.log('Unsuccessful in executing actualProductLinks method of the FlipkratScrapper class: error message is: '+ str(e))
            raise e




    def getLinkForExpectedReviewCount(self, expected_review, searchString):
        """
        Method Name: getLinkForExpectedReviewCount
        Description: This method extracts the link of product having more than expected count.
        Output: None
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the getLinkForExpectedReviewCount method of get FlipkratScrapper class')
        try:
            product_links = self.actualProductLinks()
            count = 0
            expected_count = self.getExpectedCountForLooping(expected_review=expected_review)
            while count < expected_count:
                url_to_hit = product_links[random.randint(0, len(product_links) - 1)]
                self.openUrl(url=url_to_hit)
                total_review_page = self.getTotalReviewPage()
                count = total_review_page

            url_to_hit = product_links[random.randint(0, len(product_links) - 1)]
            self.openUrl(url=url_to_hit)
            self.logging.log('Exited getLinkForExpectedReviewCount method of the FlipkratScrapper class successfully')
            return True
        except Exception as e:
            self.logging.log('Unsuccessful in executing getLinkForExpectedReviewCount method of the FlipkratScrapper class: error message is: '+ str(e))
            raise e





    def checkVisibilityOfElement(self, element_to_be_checked):
        """
        Method Name: checkVisibilityOfElement
        Description: This method checks the visibility of element on the webpage.
        Output: None
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the checkVisibilityOfElement method of get FlipkratScrapper class')
        try:
            if element_to_be_checked in self.driver.page_source:
                self.logging.log('Exited checkVisibilityOfElement method of the FlipkratScrapper class successfully')
                return True
            else:
                return False
        except Exception as e:
            self.logging.log('Unsuccessful in executing checkVisibilityOfElement method of the FlipkratScrapper class: error message is: '+ str(e))
            raise e




    def getProductName(self):
        """
        Method Name: getProductName
        Description: This method retrieves actual name of the product.
        Output: product name
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the getProductName method of get FlipkratScrapper class')
        try:
            locator = self.getLocatorsObject()
            element = locator.getProductNameByClass()
            if self.checkVisibilityOfElement(element_to_be_checked=element):
                product_name = self.findElementByClass(classpath=locator.getProductNameByClass()).text
            else:
                product_name = self.findElementByXpath(xpath=locator.getProductNameByXpath()).text
            print(product_name)
            self.logging.log('Exited getProductName method of the FlipkratScrapper class successfully')
            return product_name
        except Exception as e:
            self.logging.log('Unsuccessful in executing getProductName method of the FlipkratScrapper class: error message is: '+ str(e))
            raise e




    def getProductSearched(self, search_string):
        """
        Method Name: getProductSearched
        Description: This method returns the name of product searched.
        Output: string searched
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the getProductSearched method of get FlipkratScrapper class')
        try:
            self.logging.log('Exited getProductSearched method of the FlipkratScrapper class successfully')
            return search_string
        except Exception as e:
            return search_string





    def getPrice(self):
        """
        Method Name: getPrice
        Description: This method retrieves the original price of the product.
        Output: string searched
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the getPrice method of get FlipkratScrapper class')
        try:
            locator = self.getLocatorsObject()
            original_price = self.findElementByClass(classpath=locator.getOriginalPriceUsingClass()).text
            print(original_price)
            self.logging.log('Exited getPrice method of the FlipkratScrapper class successfully')
            return original_price
        except Exception as e:
            self.logging.log('Unsuccessful in executing getPrice method of the FlipkratScrapper class: Not able to get the price of product: error message is: '+ str(e))
            raise e




    def getDiscountedPercent(self):
        """
        Method Name: getDiscountedPercent
        Description: This method returns discounted percent for the product.
        Output: discounted price
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the getDiscountedPercent method of get FlipkratScrapper class')
        try:
            locator = self.getLocatorsObject()
            discounted_price = self.findElementByClass(classpath=locator.getDiscountPercent()).text
            print(discounted_price)
            self.logging.log('Exited getPrice method of the getDiscountedPercent class successfully')
            return discounted_price
        except Exception as e:
            return "No Discount"





    def checkMoreOffer(self):
        """
        Method Name: checkMoreOffer
        Description: This method checks whether more offer links is provided for the product or not.
        Output: None
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the checkMoreOffer method of get FlipkratScrapper class')
        try:
            locator = self.getLocatorsObject()
            if locator.getMoreOffersUsingClass() in self.driver.page_source:
                return True
            else:
                return False
        except Exception as e:
            self.logging.log('Unsuccessful in executing checkMoreOffer method of the FlipkratScrapper class: Trouble in finding more offer link: error message is: '+ str(e))
            raise e





    def clickOnMoreOffer(self):
        """
        Method Name: clickOnMoreOffer
        Description: This method clicks on more offer button.
        Output: None
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the clickOnMoreOffer method of get FlipkratScrapper class')
        try:
            status = self.checkMoreOffer()
            if status:
                locator = self.getLocatorsObject()
                more_offer = self.findElementByClass(classpath=locator.getMoreOffers())
                more_offer.click()
                return True
            else:
                return False
        except Exception as e:
            self.logging.log('Unsuccessful in executing clickOnMoreOffer method of the FlipkratScrapper class: error message is: '+ str(e))
            raise e





    def getAvailableOffer(self):
        """
        Method Name: getAvailableOffer
        Description: This method returns offers available.
        Output: Available offer
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the getAvailableOffer method of get FlipkratScrapper class')
        try:
            status = self.checkMoreOffer()
            locator = self.getLocatorsObject()
            if status:
                self.clickOnMoreOffer()
            if locator.getAvailableOffers()[0] in self.driver.page_source:
                offer_details = self.findElementByClass(classpath=locator.getAvailableOffers()[0]).text
            elif locator.getAvailableOffers()[1] in self.driver.page_source:
                offer_details = self.findElementByClass(classpath=locator.getAvailableOffers()[1]).text
            else:
                offer_details = "No Offer For the product"
            return offer_details
        except Exception as e:
            self.logging.log('Unsuccessful in executing getAvailableOffer method of the FlipkratScrapper class: error message is: '+ str(e))
            raise e




    def getOfferDetails(self):
        """
        Method Name: getOfferDetails
        Description: This method returns the offers in formatted way.
        Output: formatted offers
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the getOfferDetails method of get FlipkratScrapper class')
        try:
            available_offers = self.getAvailableOffer()
            split_offers = available_offers.split("\n")
            print(split_offers[1:])
            return split_offers[1:]
        except Exception as e:
            return "No offer Available"





    def checkViewPlanForEMI(self):
        """
        Method Name: checkViewPlanForEMI
        Description: This method returns boolean value for EMI is available or not.
        Output: None
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the checkViewPlanForEMI method of get FlipkratScrapper class')
        try:
            # status = self.checkMoreOffer()
            locator = self.getLocatorsObject()
            # if status:
            #     self.clickOnMoreOffer()
            if locator.getViewPlanLinkUsingClass() in self.driver.page_source:
                return True
            else:
                return False
        except Exception as e:
            self.logging.log('Unsuccessful in executing checkViewPlanForEMI method of the FlipkratScrapper class: error message is: '+ str(e))
            raise e





    def getEMIDetails(self):
        """
        Method Name: getEMIDetails
        Description: This method returns EMI details of the product.
        Output: emi details
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the getEMIDetails method of get FlipkratScrapper class')
        try:
            locator = self.getLocatorsObject()
            status = self.checkViewPlanForEMI()
            # if status:
            if locator.getViewPlanLinkUsingClass() in self.driver.page_source:
                emi_detail = self.findElementByXpath(xpath=locator.getEMIDetail()).text
                return emi_detail
            else:
                return "NO EMI Plans"
        except Exception as e:
            return "NO EMI Plans"





    def getTotalReviewPage(self):
        """
        Method Name: getTotalReviewPage
        Description: This method retrieves total number of pages available for review.
        Output: count of pages
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the getTotalReviewPage method of get FlipkratScrapper class')
        try:
            locator = self.getLocatorsObject()
            if locator.getMoreReviewUsingClass()[0] in self.driver.page_source:
                self.findElementByClass(classpath=locator.getMoreReviewUsingClass()[0]).click()
            elif locator.getMoreReviewUsingClass()[1] in self.driver.page_source:
                self.findElementByClass(classpath=locator.getMoreReviewUsingClass()[1]).click()
            else:
                return int(1)
            total_review_page = [self.findElementByClass(classpath=locator.getTotalReviewPage()).text][0]
            split_values = total_review_page.split("\n")
            value = str(split_values[0]).split()[-1]
            return int(value)
        except Exception as e:
            return int(1)





    def wait(self):
        """
        Method Name: wait
        Description: This method waits for the given time.
        Output: None
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the wait method of get FlipkratScrapper class')
        try:
            self.driver.implicitly_wait(2)
        except Exception as e:
            self.logging.log('Unsuccessful in executing wait method of the FlipkratScrapper class: error message is: '+ str(e))
            raise e





    def getRatings(self):
        """
        Method Name: getRatings
        Description: This method gets rating for the product.
        Output: rating
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the getRatings method of FlipkratScrapper class')
        try:
            locator = self.getLocatorsObject()
            rating = self.findingElementsFromPageUsingCSSSelector(locator.getRatings())
            return rating
        except Exception as e:
            self.logging.log('Unsuccessful in executing getRatings method of the FlipkratScrapper class: error message is: '+ str(e))
            raise e





    def getComments(self):
        """
        Method Name: getComments
        Description: This method gets review comment for the product.
        Output: comment
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the getComments method of FlipkratScrapper class')
        try:
            locator = self.getLocatorsObject()
            comment_object = locator.getComment()
            if comment_object[0] in self.driver.page_source:
                comment = self.findingElementsFromPageUsingClass(comment_object[0])
            else:
                comment = self.findingElementsFromPageUsingClass(comment_object[1])
            return comment
        except Exception as e:
            self.logging.log('Unsuccessful in executing getComments method of the FlipkratScrapper class: error message is: '+ str(e))
            raise e




    def getCustomerNamesAndReviewAge(self):
        """
        Method Name: getCustomerNamesAndReviewAge
        Description: This method gets the customername for the review.
        Output: customer name
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the getCustomerNamesAndReviewAge method of FlipkratScrapper class')
        try:
            locator = self.getLocatorsObject()
            customer_name = self.findingElementsFromPageUsingClass(locator.getCustomerName())
            return customer_name
        except Exception as e:
            self.logging.log('Unsuccessful in executing getCustomerNamesAndReviewAge method of the FlipkratScrapper class: error message is: '+ str(e))
            raise e





    def checkForNextPageLink(self):
        """
        Method Name: checkForNextPageLink
        Description: This method clicks on the next page for the review.
        Output: None
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the checkForNextPageLink method of FlipkratScrapper class')
        try:
            locator = self.getLocatorsObject()
            if locator.getNextFromTotalReviewPage() in self.driver.page_source:
                return True
            else:
                return False
        except Exception as e:
            self.logging.log('Unsuccessful in executing checkForNextPageLink method of the FlipkratScrapper class: error message is: '+ str(e))
            raise e





    def getExpectedCountForLooping(self, expected_review):
        """
        Method Name: getExpectedCountForLooping
        Description: This method retrives the total number of pages which should be searched for review.
        Output: count of pages
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the getExpectedCountForLooping method of FlipkratScrapper class')
        try:
            expected_count = expected_review / 10
            return int(expected_count)
        except Exception as e:
            self.logging.log('Unsuccessful in executing getExpectedCountForLooping method of the FlipkratScrapper class: error message is: '+ str(e))
            raise e





    def getReviewDetailsForProduct(self):
        """
        Method Name: getReviewDetailsForProduct
        Description: This method gets all Review Details for the product.
        Output: review details
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the getReviewDetailsForProduct method of FlipkratScrapper class')
        try:
            ratings, comment, customer_name, review_age = [], [], [], []
            ratings.append([i.text for i in self.getRatings()])
            comment.append([i.text for i in self.getComments()])
            cust_name_and_review_age = [i.text for i in self.getCustomerNamesAndReviewAge()]
            customer_name.append(
                self.separateCustomernameAndReviewAge(list_of_custname_and_reviewage=cust_name_and_review_age)[0])
            review_age.append(
                self.separateCustomernameAndReviewAge(list_of_custname_and_reviewage=cust_name_and_review_age)[1])
            yield ratings, comment, customer_name, review_age
        except Exception as e:
            # self.driver.refresh()
            self.logging.log('Unsuccessful in executing getReviewDetailsForProduct method of the FlipkratScrapper class: error message is: '+ str(e))
            raise e





    def separateCustomernameAndReviewAge(self, list_of_custname_and_reviewage):
        """
        Method Name: separateCustomernameAndReviewAge
        Description: This method separates the review age and customer name.
        Output: customer name and review age
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the separateCustomernameAndReviewAge method of FlipkratScrapper class')
        try:
            customer_name = list_of_custname_and_reviewage[0::2]
            review_age = list_of_custname_and_reviewage[1::2]
            return customer_name, review_age
        except Exception as e:
            self.logging.log('Unsuccessful in executing separateCustomernameAndReviewAge method of the FlipkratScrapper class: error message is: '+ str(e))
            raise e





    def generatingResponse(self, product_searched, product_name, price, discount_percent, offer_details, EMI, result):
        """
        Method Name: generatingResponse
        Description: This method generates the final response to send.
        Output: dictonary of final response
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the generatingResponse method of FlipkratScrapper class')
        try:
            response_dict = {"product_searched": [], "product_name": [], "price": [], "discount_percent": [],
                             "offer_details": [], "EMI": [], "ratings": [], "comments": [], "customer_name": [],
                             "review_Age": []}
            rating, comments, cust_name, review_age = result[0], result[1], result[2], result[3]
            response_dict["ratings"] = rating
            response_dict["comments"] = comments
            response_dict["customer_name"] = cust_name
            response_dict["review_Age"] = review_age
            response_dict["product_name"] = product_name
            response_dict["product_searched"] = product_searched
            response_dict["offer_details"] = offer_details
            response_dict["EMI"] = EMI
            response_dict["price"] = price
            response_dict["discount_percent"] = discount_percent
            return response_dict
        except Exception as e:
            self.logging.log('Unsuccessful in executing generatingResponse method of the FlipkratScrapper class: error message is: '+ str(e))
            raise e




    def generateDataForColumnAndFrame(self, response):
        """
        Method Name: generateDataForColumnAndFrame
        Description: This method generates data for the column where only single data is presented. And then frames it into a data frame.
        Output: dataframe
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the generateDataForColumnAndFrame method of FlipkratScrapper class')
        try:
            data_frame1 = pd.DataFrame()
            flatten_rating = [j for i in response['ratings'] for j in i]
            for column_name, value in response.items():
                if column_name == 'product_searched' or column_name == 'product_name' or column_name == 'price' or column_name == 'discount_percent' or column_name == 'offer_details' or column_name == 'EMI':
                    list_value = []
                    for i in range(0, len(flatten_rating)):
                        list_value.append(response[column_name])
                    data_frame1.insert(0, column_name, list_value)
            print(data_frame1)
            return data_frame1
        except Exception as e:
            self.logging.log(
                'Unsuccessful in executing generateDataForColumnAndFrame method of the FlipkratScrapper class: error message is: ' + str(
                    e))
            raise e




    def frameToDataSet(self, response):
        """
        Method Name: frameToDataSet
        Description: This method frames the column to dataframe.
        Output: dataframe
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the frameToDataSet method of FlipkratScrapper class')
        try:
            data_frame2 = pd.DataFrame()
            for column_name, value in response.items():
                if column_name == 'product_searched' or column_name == 'product_name' or column_name == 'price' or column_name == 'discount_percent' or column_name == 'offer_details' or column_name == 'EMI':
                    continue
                else:
                    flatten_result = [values for lists in response[column_name] for values in lists]
                    data_frame2.insert(0, column_name, flatten_result)
            return data_frame2
        except Exception as e:
            self.logging.log(
                'Unsuccessful in executing frameToDataSet method of the FlipkratScrapper class: error message is: ' + str(
                    e))
            raise e





    def createDataFrameIncludingAllColumn(self, response):
        """
        Method Name: createDataFrameIncludingAllColumn
        Description: This method creates dataframe from given data.
        Output: dataframe
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the createDataFrameIncludingAllColumn method of FlipkratScrapper class')
        try:
            data_frame1 = self.generateDataForColumnAndFrame(response=response)
            data_frame2 = self.frameToDataSet(response=response)
            frame = [data_frame1, data_frame2]
            data_frame = pd.concat(frame, axis=1)
            return data_frame
        except Exception as e:
            self.logging.log(
                'Unsuccessful in executing createDataFrameIncludingAllColumn method of the FlipkratScrapper class: error message is: ' + str(
                    e))
            raise e




    def saveDataFrameToFile(self, dataframe, file_name):
        """
        Method Name: saveDataFrameToFile
        Description: This method saves dataframe into filename given.
        Output: csv file
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the saveDataFrameToFile method of FlipkratScrapper class')
        try:
            self.logging.log('Exited saveDataFrameToFile method of the ObjectRepository class successfully')
            self.logging.log('The file is Successfully saved!!!')
            dataframe.to_csv(file_name)
        except Exception as e:
            self.logging.log(
                'Unsuccessful in executing saveDataFrameToFile method of the FlipkratScrapper class: error message is: ' + str(
                    e))
            raise e




    def closeConnection(self):
        """
        Method Name: closeConnection
        Description: This method closes the connection.
        Output: None
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the closeConnection method of FlipkratScrapper class')
        try:
            self.driver.close()
        except Exception as e:
            self.logging.log(
                'Unsuccessful in executing closeConnection method of the FlipkratScrapper class: error message is: ' + str(
                    e))
            raise e




    def getReviewsToDisplay(self, searchString, expected_review,review_count):
        """
        Method Name: getReviewsToDisplay
        Description: This method returns the review and other detials of product.
        Output: final output
        On Failure: Raise Exception

        Version: 1.0
        Revisions: None
        """
        self.logging.log('Entered the getReviewsToDisplay method of FlipkratScrapper class')
        try:
            search = searchString
            cassandra_obj = cassandraDBManagement(path, user_id, secure_key, key_space, table_name)
            locator = self.getLocatorsObject()

            for link in self.getProductLinks():
                print('reviewing: ' + str(review_count))

                if review_count <= expected_review:
                    self.openUrl(url=link)

                    if locator.getCustomerName() in self.driver.page_source:
                        product_name = self.getProductName()

                        print(product_name)

                        product_searched = self.getProductSearched(search_string=searchString)

                        print(product_searched)
                        price = self.getPrice()
                        offer_details = self.getOfferDetails()
                        discount_percent = self.getDiscountedPercent()
                        EMI = self.getEMIDetails()
                        total_review_page = self.getTotalReviewPage()
                        count = 0
                        while count <= total_review_page:
                            if review_count > expected_review:
                                return search
                            count = count + 1
                            new_url = self.driver.current_url + "&page=" + str(count + 1)
                            for i in self.getReviewDetailsForProduct():
                                ratings = i[0][0]
                                comment = i[1][0]
                                customer_name = i[2][0]
                                review_age = i[3][0]

                                if len(ratings) > 0:

                                    for i in range(0, len(ratings)):

                                        if review_count > expected_review:
                                            return search

                                    result = {'ID': str(uuid.uuid4()),
                                              'product_name': product_name,
                                              'product_searched': product_searched,
                                              'price': price,
                                              'offer_details': offer_details[0],
                                              'discount_percent': discount_percent,
                                              'EMI': EMI,
                                              'rating': ratings[i],
                                              'comment': comment[i],
                                              'customer_name': customer_name[i],
                                              'review_age': review_age[i]
                                              }

                                    convert = list(result.values())

                                    cassandra_obj.insert_in_table(convert)

                                    print(convert)
                                    print(result)

                                    review_count = review_count + 1

                                    print(review_count)

                            self.openUrl(url=new_url)
            return search

        except Exception as e:
            self.logging.log('Unsuccessful in executing getReviewsToDisplay method of the FlipkratScrapper class: error message is: ' + str(e))
            raise e
