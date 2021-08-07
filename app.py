# doing necessary imports
import threading

import os
from flask import Flask, render_template, request, url_for, redirect
from flask_cors import cross_origin
import pandas as pd
from FlipkratScrapping import FlipkratScrapper
from selenium import webdriver
from CassandraDBOperations import cassandraDBManagement


from plotly_dashboard import plotly_dashboard



path = 'secure-connect-FlipkartScrapper.zip'
user_id = 'EyeOFNUtvBEWdsuTcwTjqLQQ'
secure_key = 'K,Xh4igbTq5ZCvRK,_q5u6qieJXwZXpS5dszUGz1Kf1HvBv-HDA,NPvreG.dN4RzYDL0ixBTsnlfzffdSpZIaUKHgshvYgc,x.mj+h8jauSlS.u06nbJFXmnxsTZ9rky'
key_space = 'tj'
table_name = 'flipkart_heroku1'





rows = {}

collection_name = None


free_status = True

app = Flask(__name__)  # initialising the flask app with the name 'app'

#For selenium driver implementation on heroku
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)








#To avoid the time out issue on heroku
class threadClass:

    def __init__(self, expected_review, searchString, scrapper_object, review_count):
        self.expected_review = expected_review
        self.searchString = searchString
        self.scrapper_object = scrapper_object
        self.review_count = review_count
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True  # Daemonize thread
        thread.start()  # Start the execution

    def run(self):
        global collection_name, free_status
        free_status = False
        collection_name = self.scrapper_object.getReviewsToDisplay(expected_review=self.expected_review,
                                                                   searchString=self.searchString,
                                                                   review_count=self.review_count)
        free_status = True






@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def index():
    if request.method == 'POST':
        global free_status
        ## To maintain the internal server issue on heroku
        if free_status != True:
            return "This website is executing some process. Kindly try after some time..."
        else:
            free_status = True

        searchString = request.form['content'].replace(" ", "")  # obtaining the search string entered in the form
        expected_review = int(request.form['expected_review'])
        try:


            review_count = 0
            scrapper_object = FlipkratScrapper(executable_path=os.environ.get("CHROMEDRIVER_PATH"),
                                               chrome_options=chrome_options)

            cassandra_obj = cassandraDBManagement(path, user_id, secure_key, key_space, table_name)
            cassandra_obj.create_table()

            response = cassandra_obj.findAllRecords()

            if len(response) > 1:
                cassandra_obj.deleteRecords()

            scrapper_object.openUrl("https://www.flipkart.com/")
            scrapper_object.login_popup_handle()
            scrapper_object.searchProduct(searchString=searchString)


            if cassandra_obj.isconnectionestablished():
                response = cassandra_obj.findAllRecords()

                if len(response) > expected_review:
                    scrapper_object.saveDataFrameToFile(file_name="static/scrapper_data.csv",
                                                        dataframe=pd.DataFrame(response))



                    return render_template('results.html', rows=response)  # show the results to user

                else:
                    review_count = len(response)
                    threadClass(expected_review=expected_review, searchString=searchString,
                                scrapper_object=scrapper_object, review_count=review_count)


                    return redirect(url_for('feedback'))

            else:
                threadClass(expected_review=expected_review, searchString=searchString, scrapper_object=scrapper_object,
                            review_count=review_count)
                return redirect(url_for('feedback'))

        except Exception as e:
            raise Exception("(app.py) - Something went wrong while rendering all the details of product.\n" + str(e))

    else:
        return render_template('index.html')








@app.route('/feedback', methods=['POST', 'GET'])
@cross_origin()
def feedback():
    try:
        global collection_name
        if collection_name is not None:
            scrapper_object = FlipkratScrapper(executable_path=os.environ.get("CHROMEDRIVER_PATH"),
                                               chrome_options=chrome_options)
            cassandra_obj = cassandraDBManagement(path, user_id, secure_key, key_space, table_name)
            rows = cassandra_obj.findAllRecords()

            dataframe = pd.DataFrame(rows)

            scrapper_object.saveDataFrameToFile(file_name="static/scrapper_data.csv", dataframe=dataframe)

            collection_name = None

            return render_template('results.html', rows=rows)
        else:
            return render_template('results.html', rows=None)
    except Exception as e:
        raise Exception("(feedback) - Something went wrong on retrieving feedback.\n" + str(e))





@app.route("/dashboard", methods=['GET'])
@cross_origin()
def viewdashboard():
    obj = plotly_dashboard(path="static/scrapper_data.csv")
    obj.view_all_plots()
    return render_template('dashboard.html')




@app.route('/logs', methods=['GET'])
@cross_origin()
def viewlogs():
    obj = plotly_dashboard(path="static/scrapper_data.csv")
    obj.save_log_html()
    return render_template('Log.html')






if __name__ == "__main__":
    app.run()  # running the app on the local machine on port 8000
