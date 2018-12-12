---
title: Judging Covers
---

## Abstract
We would like to judge books by their covers and tell the story of how the aesthetics of a book's cover can influence its reception by the general public, as measured by its sales and reviews.

Originally, [the suggested project idea](https://dlab.epfl.ch/teaching/fall2018/cs401/projects/) was whether the reviews of a book would be affected by the aesthetics of its cover but we expanded our investigation to also look into book sales. To write a review, buyers must first read the book so their reviews will presumably be more dependent on the content that they went through, rather than the cover. Whereas while buying a book, one has access to less information that can be used to decide whether to make a purchase or not, and we believe the cover is among the most important of those pieces of information. Hence we hypothesize that we will see a more pronounced correlation between the visual features of the cover of a book and its sales, as opposed to its reviews.

At this milestone, we also restricted our problem to the domain of children's books. Different types of covers may work better for different categories of books, and we may see effects in specific categories that are not observable when looking at all of them (and vice versa). We intuitively believe children's books will be the category that is most dependent on the visual features of their covers, so we focus on them for this project. This specification also allows us to account for the changes in sales and reviews between different categories so all our samples now come from the same distribution (more or less).

## Research questions
How important are the aesthetics of a children's book cover? Are there good/bad cover practices?
- How can we find and extract semantically meaningful/interpretable features of book covers?
- How can we fit a good model that uses these features to predict sales/reviews?
- How can we analyze which of the features were the most important ones in this model?
- How can we specify and interpret the effects of changing each of these important features on the output variables?

## Dataset
We start the project with [this publicly available dataset](https://github.com/uchidalab/book-dataset). It has the following columns:

| ID | Filename | Image URL | Title | Category ID | Category |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Book ID | bookid.jpg | amazon.com/... | Book Name | Category ID | Children's |

In order to answer the research questions, we need a dataset that looks more like:

| ID | Review Score | Sales Rank | Title | Author | Date    | Visual Features |
| -- | ------------ | ---------- | ----- | ------ | ------- | --------------- |
| ID | Review Score | Sales Rank | Title | Author | Date    | Visual Features |

The `ID` column in the data can be used to access the webpage of each book, by connecting to https://www.amazon.com/dp/book-id. This allows us to scrape any data that is missing directly from Amazon.

The columns we are missing are `Review Score`, `Sales Rank`, `Date` and `Visual Features`. We scrape the first three directly from the product pages from Amazon and download the cover images using the URLs in the dataset. We then extract the visual features from each image using [OpenCV](https://opencv.org/) and other methods, completing our dataset.

The `Title`, `Author` and `Date` columns don't directly relate to the research questions, but can allow some interesting further analysis if time allows. For example, do good/bad cover practices change over time?

## Challenges
We could approach the problem in two ways, each with its unique set of challenges.
1. Using Interpretable Features
    - Fitting a simple model would let us interpret the results (e.g. look at the weights of each feature given by linear regression), but such a simple model probably would not get a good enough accuracy to make a good analysis.
    - If we make a complex model (e.g. a neural network or anensemble of trees) from these features, we would have a well-fitting model but then we would again get uninterpretable combinations of the features—even though the initial features were meaningful.

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
