---
title: Judging Covers
---

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


<html lang="en">
  <head>
    <meta charset="utf-8">

    <title>Tree Example</title>

    <style>

	.node {
		cursor: pointer;
	}

	.node circle {
	  fill: #fff;
	  stroke: steelblue;
	  stroke-width: 3px;
	}

	.node text {
	  font: 12px sans-serif;
	}

	.link {
	  fill: none;
	  stroke: #ccc;
	  stroke-width: 2px;
	}

    </style>

  </head>

  <body>

<!-- load the d3.js library -->
<script src="http://d3js.org/d3.v3.min.js"></script>

<script>

var treeData = [
  {
    "name": "Visual Features",
    "parent": "null",
    "children": [
      {
        "name": "Brightness",
        "parent": "Visual Features"
      },
      {
        "name": "Entropy",
        "parent": "Visual Features"
      },
      {
        "name": "Keypoints",
        "parent": "Visual Features"
      },
      {
        "name": "Colorfullness",
        "parent": "Visual Features"
      },
      {
        "name": "Top Color #1",
        "parent": "Visual Features",
        "children": [
          {
            "name": "The red color value of RGB",
            "parent": "Top Color #1"
          },
          {
            "name": "The green color value of RGB",
            "parent": "Top Color #1"
          },
          {
            "name": "The blue color value of RGB",
            "parent": "Top Color #1"
          }
        ]
      },
      {
        "name": "Top Color #2",
        "parent": "Visual Features",
        "children": [
          {
            "name": "The red color value of RGB",
            "parent": "Top Color #2"
          },
          {
            "name": "The green color value of RGB",
            "parent": "Top Color #2"
          },
          {
            "name": "The blue color value of RGB",
            "parent": "Top Color #2"
          }
        ]
      },
      {
        "name": "Unique Colors",
        "parent": "Visual Features"
      },
    ]
  }
];


// ************** Generate the tree diagram	 *****************
var margin = {top: 20, right: 120, bottom: 20, left: 120},
	width = 960 - margin.right - margin.left,
	height = 500 - margin.top - margin.bottom;

var i = 0,
	duration = 750,
	root;

var tree = d3.layout.tree()
	.size([height, width]);

var diagonal = d3.svg.diagonal()
	.projection(function(d) { return [d.y, d.x]; });

var svg = d3.select("body").append("svg")
	.attr("width", width + margin.right + margin.left)
	.attr("height", height + margin.top + margin.bottom)
  .append("g")
	.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

root = treeData[0];
root.x0 = height / 2;
root.y0 = 0;

update(root);

d3.select(self.frameElement).style("height", "500px");

function update(source) {

  // Compute the new tree layout.
  var nodes = tree.nodes(root).reverse(),
	  links = tree.links(nodes);

  // Normalize for fixed-depth.
  nodes.forEach(function(d) { d.y = d.depth * 180; });

  // Update the nodes…
  var node = svg.selectAll("g.node")
	  .data(nodes, function(d) { return d.id || (d.id = ++i); });

  // Enter any new nodes at the parent's previous position.
  var nodeEnter = node.enter().append("g")
	  .attr("class", "node")
	  .attr("transform", function(d) { return "translate(" + source.y0 + "," + source.x0 + ")"; })
	  .on("click", click);

  nodeEnter.append("circle")
	  .attr("r", 1e-6)
	  .style("fill", function(d) { return d._children ? "lightsteelblue" : "#fff"; });

  nodeEnter.append("text")
	  .attr("x", function(d) { return d.children || d._children ? -13 : 13; })
	  .attr("dy", ".35em")
	  .attr("text-anchor", function(d) { return d.children || d._children ? "end" : "start"; })
	  .text(function(d) { return d.name; })
	  .style("fill-opacity", 1e-6);

  // Transition nodes to their new position.
  var nodeUpdate = node.transition()
	  .duration(duration)
	  .attr("transform", function(d) { return "translate(" + d.y + "," + d.x + ")"; });

  nodeUpdate.select("circle")
	  .attr("r", 10)
	  .style("fill", function(d) { return d._children ? "lightsteelblue" : "#fff"; });

  nodeUpdate.select("text")
	  .style("fill-opacity", 1);

  // Transition exiting nodes to the parent's new position.
  var nodeExit = node.exit().transition()
	  .duration(duration)
	  .attr("transform", function(d) { return "translate(" + source.y + "," + source.x + ")"; })
	  .remove();

  nodeExit.select("circle")
	  .attr("r", 1e-6);

  nodeExit.select("text")
	  .style("fill-opacity", 1e-6);

  // Update the links…
  var link = svg.selectAll("path.link")
	  .data(links, function(d) { return d.target.id; });

  // Enter any new links at the parent's previous position.
  link.enter().insert("path", "g")
	  .attr("class", "link")
	  .attr("d", function(d) {
		var o = {x: source.x0, y: source.y0};
		return diagonal({source: o, target: o});
	  });

  // Transition links to their new position.
  link.transition()
	  .duration(duration)
	  .attr("d", diagonal);

  // Transition exiting nodes to the parent's new position.
  link.exit().transition()
	  .duration(duration)
	  .attr("d", function(d) {
		var o = {x: source.x, y: source.y};
		return diagonal({source: o, target: o});
	  })
	  .remove();

  // Stash the old positions for transition.
  nodes.forEach(function(d) {
	d.x0 = d.x;
	d.y0 = d.y;
  });
}

// Toggle children on click.
function click(d) {
  if (d.children) {
	d._children = d.children;
	d.children = null;
  } else {
	d.children = d._children;
	d._children = null;
  }
  update(d);
}

</script>

  </body>
</html>



## Exploratory Analysis

As the first exploratory plot we will examine the distribtion of our response variable, `Sales Rank`.

<div>
    <a href="https://plot.ly/~PernilleLindvang/1/?share_key=regkrHjAbQB1byAT7K6pl1" target="_blank" title="Plot 1" style="display: block; text-align: center;"><img src="https://plot.ly/~PernilleLindvang/1.png?share_key=regkrHjAbQB1byAT7K6pl1" alt="Plot 1" style="max-width: 100%;width: 600px;"  width="600" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="PernilleLindvang:1" sharekey-plotly="regkrHjAbQB1byAT7K6pl1" src="https://plot.ly/embed.js" async></script>
</div>


As seen in the above plot, our response variable follow a power-log distribution. Just as the literature says, plotting the distribution on a log-log scale the plot distribution becomes linear.

In the plot below we examine the correlation between the response variable, `Sales Rank` and the continuous variable, `Review Score`.

<div>
    <a href="https://plot.ly/~PernilleLindvang/5/?share_key=WKlsCjldxGdTfVWEQzrEez" target="_blank" title="Plot 5" style="display: block; text-align: center;"><img src="https://plot.ly/~PernilleLindvang/5.png?share_key=WKlsCjldxGdTfVWEQzrEez" alt="Plot 5" style="max-width: 100%;width: 600px;"  width="600" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="PernilleLindvang:5" sharekey-plotly="WKlsCjldxGdTfVWEQzrEez" src="https://plot.ly/embed.js" async></script>
</div>


As seen in the above scatterplot the `Review Score` is not a categorical variable, but it does to a large extent act like one. We have taken out the books with a review score of 0 since this is due to the book not being reviewed. As it is seen from the above plot there are very limited reviews between the rest of the integers in the 1-5 scale. This might be due to the reviewers finding it too difficult to judge a book to be 3,6 instead of just 4.

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
