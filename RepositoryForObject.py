from logger1 import App_Logger




class ObjectRepository:
    """
        This class shall be used for fetching the data from the html page source.

        Written By: Tejas Jay (TJ)
        Version: 1.0
        Revisions: None

    """

    def __init__(self):
        self.logging = App_Logger()




    def getUsernameforMongoDB(self):
        self.logging.log('Entered the get UsernameforMongoDB method of the ObjectRepository class')
        try:
           username = "kavimaurya1997@gmail.com"
           self.logging.log('Exited UsernameforMongoDB method of the ObjectRepository class successfully')
           return username
        except Exception as e:
            self.logging.log('Unsuccessful in executing UsernameforMongoDB method of the ObjectRepository class: The exception error is: ' +str(e))
            raise e





    def getPasswordforMongoDB(self):
        self.logging.log('Entered the get getPasswordforMongoDB method of the ObjectRepository class')
        try:
            password = "Kavita@123"
            self.logging.log('Exited getPasswordforMongoDB method of the ObjectRepository class successfully')
            return password
        except Exception as e:
            self.logging.log('Unsuccessful in executing getPasswordforMongoDB method of the ObjectRepository class: The exception error is: ' +str(e))
            raise e





    def getLoginCloseButton(self):
        self.logging.log('Entered the get getLoginCloseButton method of the ObjectRepository class')
        try:
            login_close_button = "//body[1]/div[2]/div[1]/div[1]/button[1]"
            self.logging.log('Exited getLoginCloseButton method of the ObjectRepository class successfully')
            return login_close_button
        except Exception as e:
            self.logging.log('Unsuccessful in executing getLoginCloseButton method of the ObjectRepository class: The exception error is: ' +str(e))
            raise e





    def getInputSearchArea(self):
        self.logging.log('Entered the get getInputSearchArea method of the ObjectRepository class')
        try:
            search_inputarea = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/input[1]"
            self.logging.log('Exited getInputSearchArea method of the ObjectRepository class successfully')
            return search_inputarea
        except Exception as e:
            self.logging.log('Unsuccessful in executing getInputSearchArea method of the ObjectRepository class: The exception error is: ' +str(e))
            raise e




    def getElementTobeSearched(self):
        self.logging.log('Entered the get getElementTobeSearched method of the ObjectRepository class')
        try:
            element = "_10Ermr"
            self.logging.log('Exited getElementTobeSearched method of the ObjectRepository class successfully')
            return element
        except Exception as e:
            self.logging.log('Unsuccessful in executing getElementTobeSearched method of the ObjectRepository class: The exception error is: ' +str(e))
            raise e




    def getSearchButton(self):
        self.logging.log('Entered the get getSearchButton method of the ObjectRepository class')
        try:
            search_button = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/button[1]"
            self.logging.log('Exited getSearchButton method of the ObjectRepository class successfully')
            return search_button
        except Exception as e:
            self.logging.log('Unsuccessful in executing getSearchButton method of the ObjectRepository class: The exception error is: ' +str(e))
            raise e




    def getRatingandReviewsText(self):
        self.logging.log('Entered the get getRatingandReviewsText method of the ObjectRepository class')
        try:
            rating_and_review_text = "//div[contains(text(),'Ratings & Reviews')]"
            self.logging.log('Exited getRatingandReviewsText method of the ObjectRepository class successfully')
            return rating_and_review_text
        except Exception as e:
            self.logging.log('Unsuccessful in executing getRatingandReviewsText method of the ObjectRepository class: The exception error is: ' +str(e))
            raise e




    def getProductNameByXpath(self):
        self.logging.log('Entered the get getProductNameByXpath method of the ObjectRepository class')
        try:
            product_name = "//body[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/h1[1]/span[2]"
            self.logging.log('Exited getProductNameByXpath method of the ObjectRepository class successfully')
            return product_name
        except Exception as e:
            self.logging.log('Unsuccessful in executing getProductNameByXpath method of the ObjectRepository class: The exception error is: ' +str(e))
            raise e




    def getProductNameByClass(self):
        self.logging.log('Entered the get getProductNameByClass method of the ObjectRepository class')
        try:
            product_name = "B_NuCI"
            self.logging.log('Exited getProductNameByClass method of the ObjectRepository class successfully')
            return product_name
        except Exception as e:
            self.logging.log('Unsuccessful in executing getProductNameByClass method of the ObjectRepository class: The exception error is: ' +str(e))
            raise e



    def getProductSearchedByXpath(self):
        self.logging.log('Entered the get getProductSearchedByXpath method of the ObjectRepository class')
        try:
            product_searched = "//body[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/h1[1]/span[1]"
            self.logging.log('Exited getProductSearchedByXpath method of the ObjectRepository class successfully')
            return product_searched
        except Exception as e:
            self.logging.log('Unsuccessful in executing getProductSearchedByXpath method of the ObjectRepository class: The exception error is: ' +str(e))
            raise e




    def getProductSearchedByClass(self):
        self.logging.log('Entered the get getProductSearchedByClass method of the ObjectRepository class')
        try:
            product_searched = "G6XhRU"
            self.logging.log('Exited getProductSearchedByClass method of the ObjectRepository class successfully')
            return product_searched
        except Exception as e:
            self.logging.log('Unsuccessful in executing getProductSearchedByClass method of the ObjectRepository class: The exception error is: ' +str(e))
            raise e




    def getOriginalPriceUsingClass(self):
        self.logging.log('Entered the get getOriginalPriceUsingClass method of the ObjectRepository class')
        try:
            original_price = "_30jeq3"
            self.logging.log('Exited getProductSearchedByClass method of the ObjectRepository class successfully')
            return original_price
        except Exception as e:
            self.logging.log('Unsuccessful in executing getOriginalPriceUsingClass method of the ObjectRepository class: The exception error is: ' +str(e))
            raise e



    def getOriginalPriceUsingXpath(self):
        self.logging.log('Entered the get getOriginalPriceUsingXpath method of the ObjectRepository class')
        try:
            original_price = "//body[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]"
            self.logging.log('Exited getOriginalPriceUsingXpath method of the ObjectRepository class successfully')
            return original_price
        except Exception as e:
            self.logging.log('Unsuccessful in executing getOriginalPriceUsingXpath method of the ObjectRepository class: The exception error is: ' +str(e))
            raise e



    def getDiscountPercent(self):
        self.logging.log('Entered the get getDiscountPercent method of the ObjectRepository class')
        try:
            discount_percent = "_3Ay6Sb"
            self.logging.log('Exited getDiscountPercent method of the ObjectRepository class successfully')
            return discount_percent
        except Exception as e:
            self.logging.log('Unsuccessful in executing getDiscountPercent method of the ObjectRepository class: The exception error is: ' +str(e))
            raise e



    def getEMIDetail(self):
        self.logging.log('Entered the get getEMIDetail method of the ObjectRepository class')
        try:
            emi_detail = "//body[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/span[3]/li[1]/span[1]"
            self.logging.log('Exited getEMIDetail method of the ObjectRepository class successfully')
            return emi_detail
        except Exception as e:
            self.logging.log('Unsuccessful in executing getEMIDetail method of the ObjectRepository class: The exception error is: ' +str(e))
            raise e



    def getViewPlanLinkUsingClass(self):
        self.logging.log('Entered the get getViewPlanLinkUsingClass method of the ObjectRepository class')
        try:
            viewPlan = "_3IATq1"
            self.logging.log('Exited getViewPlanLinkUsingClass method of the ObjectRepository class successfully')
            return viewPlan
        except Exception as e:
            self.logging.log('Unsuccessful in executing getViewPlanLinkUsingClass method of the ObjectRepository class: The exception error is: ' +str(e))
            raise e




    def getAvailableOffers(self):
        self.logging.log('Entered the get getAvailableOffers method of the ObjectRepository class')
        try:
            available_offers1 = "_3TT44I"
            available_offers2 = "WT_FyS"
            self.logging.log('Exited getAvailableOffers method of the ObjectRepository class successfully')
            return available_offers1, available_offers2
        except Exception as e:
            self.logging.log('Unsuccessful in executing getAvailableOffers method of the ObjectRepository class: The exception error is: ' +str(e))
            raise e




    def getMoreOffers(self):
        self.logging.log('Entered the get getMoreOffers method of the ObjectRepository class')
        try:
            more_offer = "IMZJg1"
            self.logging.log('Exited getMoreOffers method of the ObjectRepository class successfully')
            return more_offer
        except Exception as e:
            self.logging.log('Unsuccessful in executing getMoreOffers method of the ObjectRepository class: The exception error is: ' +str(e))
            raise e




    def getMoreOffersUsingClass(self):
        self.logging.log('Entered the get getMoreOffersUsingClass method of the ObjectRepository class')
        try:
            more_offer = "IMZJg1 Okf99z"
            self.logging.log('Exited getMoreOffersUsingClass method of the ObjectRepository class successfully')
            return more_offer
        except Exception as e:
            self.logging.log('Unsuccessful in executing getMoreOffersUsingClass method of the ObjectRepository class: The exception error is: ' +str(e))
            raise e




    def getRatings(self):
        self.logging.log('Entered the get getRatings method of the ObjectRepository class')
        try:
            rating = "div._3LWZlK._1BLPMq"
            self.logging.log('Exited getRatings method of the ObjectRepository class successfully')
            return rating
        except Exception as e:
            self.logging.log('Unsuccessful in executing getRatings method of the ObjectRepository class: The exception error is: ' +str(e))
            raise e




    def getComment(self):
        self.logging.log('Entered the get getComment method of the ObjectRepository class')
        try:
            comment1 = "_6K-7Co"
            comment2 = "_2-N8zT"
            self.logging.log('Exited getComment method of the ObjectRepository class successfully')
            return comment1,comment2
        except Exception as e:
            self.logging.log('Unsuccessful in executing getComment method of the ObjectRepository class: The exception error is: ' +str(e))
            raise e



    def getCustomerName(self):
        self.logging.log('Entered the get getCustomerName method of the ObjectRepository class')
        try:
            comment_date = "_2sc7ZR"
            self.logging.log('Exited getCustomerName method of the ObjectRepository class successfully')
            return comment_date
        except Exception as e:
            self.logging.log('Unsuccessful in executing getCustomerName method of the ObjectRepository class: The exception error is: ' +str(e))
            raise e



    def getTotalReviewPage(self):
        self.logging.log('Entered the get getTotalReviewPage method of the ObjectRepository class')
        try:
            total_page_1 = "_2MImiq"
            #total_page_2 ="//body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[13]/div[1]/div[1]/span[1]"
            self.logging.log('Exited getTotalReviewPage method of the ObjectRepository class successfully')
            return total_page_1
        except Exception as e:
            self.logging.log('Unsuccessful in executing getTotalReviewPage method of the ObjectRepository class: The exception error is: ' +str(e))
            raise e



    def getMoreReviewUsingClass(self):
        self.logging.log('Entered the get getMoreReviewUsingClass method of the ObjectRepository class')
        try:
            more_review_1 = "_3at_-o"
            more_review_2 = "_3UAT2v"
            self.logging.log('Exited getMoreReviewUsingClass method of the ObjectRepository class successfully')
            return more_review_1, more_review_2
        except Exception as e:
            self.logging.log('Unsuccessful in executing getMoreReviewUsingClass method of the ObjectRepository class: The exception error is: ' +str(e))
            raise e
#



    def getNextFromTotalReviewPage(self):
        self.logging.log('Entered the get getNextFromTotalReviewPage method of the ObjectRepository class')
        try:
            next_button = "_1LKTO3"
            self.logging.log('Exited getNextFromTotalReviewPage method of the ObjectRepository class successfully')
            return next_button
        except Exception as e:
            self.logging.log('Unsuccessful in executing getNextFromTotalReviewPage method of the ObjectRepository class: The exception error is: ' +str(e))
            raise e

