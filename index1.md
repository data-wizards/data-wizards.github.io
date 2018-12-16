---
title: Judging Covers
---

December is always a busy month. Are you late for Christmas presents again this year? Do you have a lot of young nephew and nieces, and do not know how to choose from the million of books found online?


PICTURES ON TWO BOOKCOVERS ( Many and Pandy visit the Zoo 9024, the lord of the hat 6752)


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



Lets go back and look at our initial proposed book covers. The above mentioned visual features are all resulting in the following measures for the two books:


| Title        | Mandy and Pandy visit the Zoo | The Lord of the hat |
| ------------ | ----------------------------- | ------------------- |
| ID           | 9024                          | 6752                |
| ------------ | ----------------------------- | ------------------- |
| Brightness   | 0.6929143                     | 0.57373714          |
| ------------ | ----------------------------- | ------------------- |
| Colorfulness | 56.011766869752854            | 81.67765304315728   |
| ------------ | ----------------------------- | ------------------- |
| Entropy      | 6.860396400000001             | 6.765961            |
| ------------ | ----------------------------- | ------------------- |
| UniqueColors | 64144                         | 52475               |
| ------------ | ----------------------------- | ------------------- |
| Keypoints    | 0.01810313901345292           | 0.0268821752265861  |
| ------------ | ----------------------------- | ------------------- |
| Color1R      | 243                           | 199                 |
| ------------ | ----------------------------- | ------------------- |
| Color1G      | 236                           | 208                 |
| ------------ | ----------------------------- | ------------------- |
| Color1B      | 183                           | 236                 |
| ------------ | ----------------------------- | ------------------- |
| Color2R      | 125                           | 82                  |
| ------------ | ----------------------------- | ------------------- |
| Color2G      | 109                           | 42                  |
| ------------ | ----------------------------- | ------------------- |
| Color2B      | 160                           | 129                 |


Before going directly to the interesting results, let's first get a closer look of data.


## Exploratory Analysis

As the first exploratory plot we will examine the distribution of our initial response variable, `Sales Rank`, and also of the other possible response variable, `Review Score`.

<div>
    <a href="https://plot.ly/~PernilleLindvang/27/?share_key=2F33uwz7SnUQan0gwmrWYZ" target="_blank" title="Plot 27" style="display: block; text-align: center;"><img src="https://plot.ly/~PernilleLindvang/27.png?share_key=2F33uwz7SnUQan0gwmrWYZ" alt="Plot 27" style="max-width: 100%;width: 600px;"  width="600" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="PernilleLindvang:27" sharekey-plotly="2F33uwz7SnUQan0gwmrWYZ" src="https://plot.ly/embed.js" async></script>
</div>



As seen in the above plot, our response variable follow a power-log distribution. Just as the literature says, plotting the distribution on a log-log scale the plot distribution becomes linear.

In the plot below we examine the correlation between the response variable, `Sales Rank` and the continuous variable, `Review Score`.

<div>
    <a href="https://plot.ly/~PernilleLindvang/21/?share_key=FP97Hq2PBdXv7oo9009m5H" target="_blank" title="Plot 21" style="display: block; text-align: center;"><img src="https://plot.ly/~PernilleLindvang/21.png?share_key=FP97Hq2PBdXv7oo9009m5H" alt="Plot 21" style="max-width: 100%;width: 600px;"  width="600" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="PernilleLindvang:21" sharekey-plotly="FP97Hq2PBdXv7oo9009m5H" src="https://plot.ly/embed.js" async></script>
</div>


From this plot you can see each book with the `Title` and the corresponding `Review Score` and `Score Rank` when hovering over the datapoints.
As seen in the above scatterplot the `Review Score` is not a categorical variable, but it does to a large extent act like one. We have taken out the books with a review score of 0 since this is due to the book not being reviewed. As it is seen from the above plot there are very limited reviews between the rest of the integers in the 1-5 scale. This might be due to the reviewers finding it too difficult to judge a book to be 3,6 instead of just 4.

Furthermore, since we wish to explore the ability of predicting the `Sales Rank` or the `Review Score` based on visual features, `Entropy`, `Brightness`, and `Keypoints` are visualised against the two proposed response variables.

<div>
    <a href="https://plot.ly/~PernilleLindvang/23/?share_key=K1Xfpn9oSEHqQQsvlrhDzW" target="_blank" title="Plot 23" style="display: block; text-align: center;"><img src="https://plot.ly/~PernilleLindvang/23.png?share_key=K1Xfpn9oSEHqQQsvlrhDzW" alt="Plot 23" style="max-width: 100%;width: 800px;"  width="800" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="PernilleLindvang:23" sharekey-plotly="K1Xfpn9oSEHqQQsvlrhDzW" src="https://plot.ly/embed.js" async></script>
</div>


From this we actually see that some of these visual features have some kind of explanatory relationship with the `Sales Rank`. More specifically we see for `Entropy` that higher values of entropy score tends to give higher sales rank. For `brightness` it seems neither too bright or too dark will give a high sales rank. Lastly, for keypoints, which is another way of calculating a measure of complexity, the less complex the lower the sales rank. Especially the keypoints make sense when we take into account that this is for children's books - the simpler the cover, the better the sales rank.
Let's examine the same for `Review Score`.

<div>
    <a href="https://plot.ly/~PernilleLindvang/25/?share_key=N8cmRiV22Bf1rLlnT6KJjY" target="_blank" title="Plot 25" style="display: block; text-align: center;"><img src="https://plot.ly/~PernilleLindvang/25.png?share_key=N8cmRiV22Bf1rLlnT6KJjY" alt="Plot 25" style="max-width: 100%;width: 800px;"  width="800" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="PernilleLindvang:25" sharekey-plotly="N8cmRiV22Bf1rLlnT6KJjY" src="https://plot.ly/embed.js" async></script>
</div>


Here, we see a very different pattern for the visual features and the response variable. Again, the plot is very affected by `Review Score` being a bit categorical in nature.

Based on the two plots above it seems like the visual features alone might be better at predicting the `Sales Rank`than the `Review Score` since there were at least some kind of correlation.

## Analysis

In this section we will present to you the results of the boosted ensemble of trees from *CatBoost* together with the SciKit learn Random Forest model. The CatBoost is chosen due to better performance compared to the other libraries working with *SHAP*.



## Conclusion

In this project we have seen that ...
