---
title: Judging Covers
---

December is always a busy month. Are you late for Christmas presents again this year? Do you have a lot of young nephew and nieces, and do not know how to choose from the million of books found online?


PICTURES ON TWO BOOKCOVERS


So, based on the looks of these two book covers, which one would you buy? Which one would you think had the highest review score? Take your time to think....


 Buckle up and get ready to go through the data story which will uncover the scientific answer to the questions above, and will make sure you are on the same _page_ as the younger ones for the holiday seasons in the years to come.




## Introduction
We would like to judge books by their covers and tell the story of how the aesthetics of a book's cover can influence its reception by the general public, as measured by its sales and reviews.

Originally, [the suggested project idea](https://dlab.epfl.ch/teaching/fall2018/cs401/projects/) was whether the reviews of a book would be affected by the aesthetics of its cover but we expanded our investigation to also look into book sales. To write a review, buyers must first read the book so their reviews will presumably be more dependent on the content that they went through, rather than the cover. Whereas while buying a book, one has access to less information that can be used to decide whether to make a purchase or not, and we believe the cover is among the most important of those pieces of information. Hence we hypothesize that we will see a more pronounced correlation between the visual features of the cover of a book and its sales, as opposed to its reviews.

In this project we also restricted our problem to the domain of children's books. Different types of covers may work better for different categories of books, and we may see effects in specific categories that are not observable when looking at all of them (and vice versa). We intuitively believe children's books will be the category that is most dependent on the visual features of their covers, so we focus on them for this project. This specification also allows us to account for the changes in sales and reviews between different categories so all our samples now come from the same distribution (more or less).

In this project we have examined the sale rate of the children's book and the relationship to XX, YY, together with semantically meaningful features extracted from the book covers. In this data story we will guide you throw the most interesting of our findings. Let's judge some books by their cover....

## Research questions
How important are the aesthetics of a children's book cover? Are there good/bad cover practices?
- How can we find and extract semantically meaningful/interpretable features of book covers?
- How can we fit a good model that uses these features to predict sales/reviews?
- How can we analyze which of the features were the most important ones in this model?
- How can we specify and interpret the effects of changing each of these important features on the output variables?


## Data Processing
One of the main challenges of this project has been that all data had to be scraped from Amazon directly, since the data which was publicly available was mainly reviews. We start the project with [this publicly available dataset](https://github.com/uchidalab/book-dataset). It has the following columns:

| ID | Filename | Image URL | Title | Author | Category ID | Category |
| -- | -------- | --------- | ----- | ------ | ----------- | -------- |
| ID | Filename | Image URL | Title | Author | Category ID | Category |

In order to answer the research questions, we need a dataset that looks more like:

| ID | Review Score | Sales Rank | Title | Author | Date    | Visual Features |
| -- | ------------ | ---------- | ----- | ------ | ------- | --------------- |
| ID | Review Score | Sales Rank | Title | Author | Date    | Visual Features |

The `ID` column in the data can be used to access the webpage of each book, by connecting to https://www.amazon.com/dp/book-id. This allows us to scrape any data that is missing directly from Amazon.

The columns we are missing are `Review Score`, `Sales Rank`, `Date` and `Visual Features`. We scrape the first three directly from the product pages from Amazon and download the cover images using the URLs in the dataset. We then extract the visual features from each image using [OpenCV](https://opencv.org/) and other methods, completing our dataset.

[//]: # The `Title`, `Author` and `Date` columns don't directly relate to the research questions, but can allow some interesting further analysis if time allows. For example, do good/bad cover practices change over time?


The visual semantically meaningful features we have chosen to work with in this project are highlighted in the below interactive tree plot. By clicking the circles, information about the features will appear.


<iframe src="https://github.com/data-wizards/data-wizards.github.io/blob/master/dendogram.html" width="100%" height="400px"></iframe>


## Exploratory Analysis

As the first exploratory plot we will examine the distribution of our initial response variable, `Sales Rank`, and also of the other possible response variable, `Review Score`.

<div>
    <a href="https://plot.ly/~PernilleLindvang/15/?share_key=QMvfYzETSaLhbU5wCN9LPB" target="_blank" title="Plot 15" style="display: block; text-align: center;"><img src="https://plot.ly/~PernilleLindvang/15.png?share_key=QMvfYzETSaLhbU5wCN9LPB" alt="Plot 15" style="max-width: 100%;width: 800px;"  width="800" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="PernilleLindvang:15" sharekey-plotly="QMvfYzETSaLhbU5wCN9LPB" src="https://plot.ly/embed.js" async></script>
</div>



As seen in the above plot, our response variable follow a power-log distribution. Just as the literature says, plotting the distribution on a log-log scale the plot distribution becomes linear.

In the plot below we examine the correlation between the response variable, `Sales Rank` and the continuous variable, `Review Score`.

<div>
    <a href="https://plot.ly/~PernilleLindvang/13/?share_key=8Slp6SgnHXutG1W6uRYTx3" target="_blank" title="Plot 13" style="display: block; text-align: center;"><img src="https://plot.ly/~PernilleLindvang/13.png?share_key=8Slp6SgnHXutG1W6uRYTx3" alt="Plot 13" style="max-width: 100%;width: 600px;"  width="600" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="PernilleLindvang:13" sharekey-plotly="8Slp6SgnHXutG1W6uRYTx3" src="https://plot.ly/embed.js" async></script>
</div>


From this plot you can see each book with the `Title` and the corresponding `Review Score` and `Score Rank` when hovering over the datapoints.
As seen in the above scatterplot the `Review Score` is not a categorical variable, but it does to a large extent act like one. We have taken out the books with a review score of 0 since this is due to the book not being reviewed. As it is seen from the above plot there are very limited reviews between the rest of the integers in the 1-5 scale. This might be due to the reviewers finding it too difficult to judge a book to be 3,6 instead of just 4.

Furthermore, since we wish to explore the ability of predicting the `Sales Rank` or the `Review Score` based on visual features, `Entropy`, `Brightness`, and `Keypoints` are visualised against the two proposed response variables.

<div>
    <a href="https://plot.ly/~PernilleLindvang/9/?share_key=M1ua1WqFPxRxKrRNfNlSgu" target="_blank" title="Plot 9" style="display: block; text-align: center;"><img src="https://plot.ly/~PernilleLindvang/9.png?share_key=M1ua1WqFPxRxKrRNfNlSgu" alt="Plot 9" style="max-width: 100%;width: 800px;"  width="800" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="PernilleLindvang:9" sharekey-plotly="M1ua1WqFPxRxKrRNfNlSgu" src="https://plot.ly/embed.js" async></script>
</div>


From this we actually see that some of these visual features have some kind of explanatory relationship with the `Sales Rank`. More specifically we see for `Entropy` that higher values of entropy score tends to give higher sales rank. For `brightness` it seems neither too bright or too dark will give a high sales rank. Lastly, for keypoints, which is another way of calculating a measure of complexity, the less complex the lower the sales rank. Especially the keypoints make sense when we take into account that this is for children's books - the simpler the cover, the better the sales rank.
Let's examine the same for `Review Score`.

<div>
    <a href="https://plot.ly/~PernilleLindvang/19/?share_key=uNWfeF3g0yH5ylV9kCgxLS" target="_blank" title="Plot 19" style="display: block; text-align: center;"><img src="https://plot.ly/~PernilleLindvang/19.png?share_key=uNWfeF3g0yH5ylV9kCgxLS" alt="Plot 19" style="max-width: 100%;width: 800px;"  width="800" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="PernilleLindvang:19" sharekey-plotly="uNWfeF3g0yH5ylV9kCgxLS" src="https://plot.ly/embed.js" async></script>
</div>


Here, we see a very different pattern for the visual features and the response variable. Again, the plot is very affected by `Review Score` being a bit categorical in nature.

## Analysis

In this section we will present to you the results of the boosted ensemble of tree model from *CatBoost*.
This one is chosen due to better performance compared to the other libraries working with *SHAP*.


## Conclusion

In this project we have seen that ...



NOTES:

## Challenges
We could approach the problem in two ways, each with its unique set of challenges.
1. Using Interpretable Features
    - Fitting a simple model would let us interpret the results (e.g. look at the weights of each feature given by linear regression), but such a simple model probably would not get a good enough accuracy to make a good analysis.
    - If we make a complex model (e.g. a neural network or an   ensemble of trees) from these features, we would have a well-fitting model but then we would again get uninterpretable combinations of the features—even though the initial features were meaningful.

2. Using Complex Non-Interpretable Features
    - We could get a well-fitting model perhaps even with simpler models, but we would be unable to interpret which features affect the sales and reviews and how they affect them.
    - Methods such as K-means clustering or PCA could help us visually identify certain features of books, but this might be a subjective analysis. Even if there are clearly observable features, they may not translate to an effect on sales/reviews.

## Method
To tackle the challenges above, we bring together the best of both worlds: start with interpretable features, fit a complex model, use state-of-the-art research to interpret the model.

In more specific steps:
1. Scrape the missing parts of the dataset from Amazon, download cover images for each book,
2. Decide on a number of semantically meaningful features and extract these features from the covers,
3. Build an ensemble of trees such as a Random Forest that can model the data well using these features,
4. Use [SHAP](https://github.com/slundberg/shap) to analyze the model and learn which features are the most important and how they affect the output of the model,
5. Use the analysis results to draw conclusions about the importance of cover aesthetics.

## Internal Milestones
Week 1 (Nov 26):
- Further work on building meaningful visual features
- Further work on scraping more data from Amazon
- Build an initial Random Forest model

Week 2 (Dec 3):
- Improve and expand the Random Forest model
- Start examining the influence of the visual features

Week 3 (Dec 10):
- Finish the modelling and start building a data story
- Draw conclusion on the visual features and compare with already published papers on book covers

**Report Deadline:** December 16

Until the presentation:
- Prepare the project poster
- Prepare for the presentation

**Presentation Deadline:** Jan 21

## The Repository
1. `Data Collection.ipynb` starts from the original dataset and creates `scraped.csv` which holds the scraped features. It also downloads all the cover images to a folder. Finally, it gives an initial exploration of the newly scraped data.
2. `Exploratory Analysis.ipynb` uses the outputs of the last step to complete the dataset. It extracts the visual features of each image by using the methods in `feature_extraction.py`. As its name suggests, this notebook continues to do the exploratory analysis on the whole dataset, doing the descriptive statistics tasks, investigating distributions, etc. It ends with a plan for the upcoming steps of the project.

## Contributions of Group Members
