import plotly
import pandas as pd
from datetime import date
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from wordcloud import WordCloud, STOPWORDS
import plotly.graph_objs as go
import os
from logger1 import App_Logger






path = "static/scrapper_data.csv"





class plotly_dashboard:
    """
        This class shall be used for creating dynamic plotly plots.

        Written By: Tejas Jay (TJ)
        Version: 1.0
        Revisions: None

    """

    def __init__(self, path):
        self.path = path
        self.logging = App_Logger()



    def data_input_transformation(self):
        """
                Method Name: data_input_transformation
                Description: This method is used for pre-process the csv data.
                Output: None
                On Failure: Raise Exception

                Written By: Tejas Jay (TJ)
                Version: 1.0
                Revisions: None
                """
        self.logging.log('Entered the data_input_transformation method of plotly_dashboard class')

        data = pd.read_csv(self.path)

        data['review_count'] = data['Unnamed: 0']

        x = list(data['product_name'])

        cleaned_product_names = []

        for i in x:
            if len(i) >= 21:
                cleaned_product_names.append(i[:20])
            else:
                cleaned_product_names.append(i)

        data['product_name'] = cleaned_product_names

        data.drop(axis=1, inplace=True,
                  columns=['Unnamed: 0', 'emi', 'Unnamed: 0', 'id', 'offer_details', 'customer_name',
                           'discount_percent'])

        new = data["review_age"].str.split(" ", n=3, expand=True)
        data["First"] = new[0]
        data["second"] = new[1]
        data["third"] = new[2]

        x = list(data['second'])

        todays_date = date.today()

        year = todays_date.year

        new_list = []

        for i in x:
            if i == 'days':
                new_list.append(1)
            elif i == 'months':
                new_list.append(30)
            elif i == 'month':
                new_list.append(30)
            elif i == None:
                new_list.append(0)
            else:
                a = int(i)
                b = (year - a) * 365
                new_list.append(b)

        data['new_second'] = new_list

        y = list(data['First'])

        final_numbers = []

        for i in y:
            try:
                c = int(i)
                final_numbers.append(c)
            except:
                final_numbers.append(1)

        data['new_first'] = final_numbers

        data['review_days_ago'] = data['new_second'] * data['new_first']

        data.drop(axis=1, inplace=True, columns=['First', 'second', 'third', 'new_second', 'new_first'])

        data['review_months_ago'] = round(data['review_days_ago'] / 30, ndigits=1)

        return data




    def create_sunburst_plot(self):
        """
                        Method Name: create_sunburst_plot
                        Description: This method is used to create sunburst plot.
                        Output: saves image and loads dynamic plot
                        On Failure: Raise Exception

                        Written By: Tejas Jay (TJ)
                        Version: 1.0
                        Revisions: None
                        """
        self.logging.log('Entered the create_sunburst_plot method of plotly_dashboard class')

        fig = px.sunburst(self.data_input_transformation(), path=['product_name', 'rating'],
                          color='rating')

        fig.write_image("static\images\sunburstfig.png")

        result = plotly.offline.plot(fig,
                                     filename='static\images\sunburst.png')

        return result






    def create_line_plot(self):
        """
                                Method Name: create_line_plot
                                Description: This method is used to create line plot.
                                Output: saves image and loads dynamic plot
                                On Failure: Raise Exception

                                Written By: Tejas Jay (TJ)
                                Version: 1.0
                                Revisions: None
                                """
        self.logging.log('Entered the create_line_plot method of plotly_dashboard class')

        data = self.data_input_transformation()

        # Create figure with secondary y-axis
        fig = make_subplots(specs=[[{"secondary_y": True}]])

        # Add traces
        fig.add_trace(
            go.Scatter(x=list(data['review_count']), y=list(data['review_months_ago']), name="Months ago"),
            secondary_y=False,
        )

        fig.add_trace(
            go.Scatter(x=list(data['review_count']), y=list(data['rating']), name="Rating"),
            secondary_y=True,
        )

        # Set x-axis title
        fig.update_xaxes(title_text="<b>number of reviews</b>")

        # Set y-axes titles
        fig.update_yaxes(title_text="<b>Months ago</b>", secondary_y=False)
        fig.update_yaxes(title_text="<b>Rating</b>", secondary_y=True)

        fig.write_image("static\images\lineplotfig.png")

        result = plotly.offline.plot(fig,
                                     filename='static\images\lineplot.png')

        return result






    def plotly_wordcloud(self, text):
        wc = WordCloud(stopwords=set(STOPWORDS),
                       max_words=5000,
                       max_font_size=50)
        wc.generate(text)

        word_list = []
        freq_list = []
        fontsize_list = []
        position_list = []
        orientation_list = []
        color_list = []

        for (word, freq), fontsize, position, orientation, color in wc.layout_:
            word_list.append(word)
            freq_list.append(freq)
            fontsize_list.append(fontsize)
            position_list.append(position)
            orientation_list.append(orientation)
            color_list.append(color)

        # get the positions
        x = []
        y = []
        for i in position_list:
            x.append(i[0])
            y.append(i[1])

        # get the relative occurence frequencies
        new_freq_list = []
        for i in freq_list:
            new_freq_list.append(i * 100)

        trace = go.Scatter(x=x,
                           y=y,
                           textfont=dict(size=new_freq_list,
                                         color=color_list),
                           hoverinfo='text',
                           hovertext=['{0}{1}'.format(w, f) for w, f in zip(word_list, freq_list)],
                           mode='text',
                           text=word_list
                           )

        layout = go.Layout({'xaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False},
                            'yaxis': {'showgrid': False, 'showticklabels': False, 'zeroline': False}}
                           )

        fig = go.Figure(data=[trace], layout=layout)

        return fig





    def cloud_plot(self):
        """
                    Method Name: cloud_plot
                    Description: This method is used to create word-cloud plot.
                    Output: saves image and loads dynamic plot
                    On Failure: Raise Exception

                    Written By: Tejas Jay (TJ)
                    Version: 1.0
                    Revisions: None
        """
        self.logging.log('Entered the cloud_plot method of plotly_dashboard class')

        data = self.data_input_transformation()

        review_list = []
        x = list(data['comment'])
        for i in x:
            if len(i) >= 21:
                review_list.append(i[:20])
            else:
                review_list.append(i)

        cloud_words = (' '.join(review_list))

        fig = self.plotly_wordcloud(text=cloud_words)

        fig.write_image("static\images\cloudplotfig.png")

        result = plotly.offline.plot(fig,
                                     filename='static\images\cloudplot.png')

        return result




    def view_all_plots(self):
        """
                            Method Name: view_all_plots
                            Description: This method is used to create all the plots.
                            Output: saves all images and loads all dynamic plots
                            On Failure: Raise Exception

                            Written By: Tejas Jay (TJ)
                            Version: 1.0
                            Revisions: None
        """
        self.logging.log('Entered the view_all_plots method of plotly_dashboard class')

        r1 = self.create_sunburst_plot()
        r2 = self.create_line_plot()
        r3 = self.cloud_plot()

        return r1, r2, r3



    def save_log_html(self):

        """
        Method Name: save_log_html
        Description: Loads the model with csv and saves it as html in template directory
        Output: html file
        On Failure: Raise Exception

        Written By: Tejas Jay
        Version: 1.0
        Revisions: None
        """
        try:
            df = pd.read_csv("logs.txt", sep='\t', header=None)
            column = ['Date', 'Time', 'Log_Status']
            df.columns = column
            result = df.to_html(index=False)
            html = result
            text_file = open("templates\Log.html", "w")
            text_file.write(html)
            text_file.close()

        except Exception as e:
            raise e






