Title: Quality Basic Terms
Date: 2014-09-16
intro: Introduce some base terms in quality.
Tags: 
Status: public

## Measures of Location

Two commonly used measures of location are the mean and the median.

### Mean

The **mean** describes an entire set of observations with a single value representing the center of the data. 

The mean of the entire population is represented by $\mu$. The mean of the sample is represented by $\bar{X}$. 

The sample mean

\begin{equation}
  \bar{X}=\frac{sum}{count}=\sum_{i=1}^{n}\frac{x_i}{n}
\end{equation}

### Median

The **median** is the middle of the range of data. Half the data points are greater than, or equal to, the median, and half are smaller than, or equal to, the median. When there is an even number of observations, as in this example showing four data points, to find the median we average the middle two numbers.

## Measures of spread

There are three measures of spread: range, variance, and standard deviation.

### Range

**Range** represented by $R$, is the difference between the largest and smallest
values.

\begin{equation}
  R=\max\{data\}-\min\{data\}
\end{equation}

### Variance

**Variance** is a measure of dispersion, which is the extent to which a data set or distribution is scattered around its mean. The formula goes like this: 

\begin{equation}
  S^2=\frac{\sum_{i=1}^{n}(x_i-\bar{X})^2}{n-1}
\end{equation}

### Standard Deviation
Standard Deviation is the most common measure of dispersion, or how spread out the data are from the mean.

The standard deviation for a population is represented by $\sigma$. The standard deviation for a sample is indicated by $S$.

The standard deviation is the square root of the variance:

\begin{equation}
  S=\sqrt{S^2}
\end{equation}

> Note: The standard deviation uses the same units as the data.

## Caculate above Data from Minitab

**Stat** -- **Basic Statistics** -- **Display Descriptive Statistics...**

A great tool to get a quick, birds-eye view of your measurement data is Minitab’s Graphical Summary (**Stat** > **Basic Statistics** > **Graphical Summary**). 

![enter image description here][1]

Visual representations help us quickly understand the distribution of data. Also, help us quickly compare different sets of data.

But visual representations are interpretations of data, we still must analyze the data to make sure any perceived differences are statistically significant.

### Graphical Analysis Tool

Two basic tools for graphical analysis are the histogram and the boxplot.

#### Histogram

We can also plot the histogram of data by:

**Graph** > **Histogram...**

![enter image description here][2]

A histogram is a graph used to assess the shape and spread of continuous sample data. To draw a histogram Minitab divides sample values into many intervals called **bins**. By default, bars represent the number of observations falling within each bin (or its frequency). Minitab automatically determines an optimal number of bins (in this example, 12), but you can edit the number of bins as well as the intervals covered by each. This histogram also includes a fit curve to convey the shape of the data’s distribution.

We can get more information for each bar in the graph by rolling our cursor over the bar.

#### Boxplot

**Graph** > **Boxplot...**

![enter image description here][3]

A boxplot is graphical summary of the distribution of a sample that shows its shape, central tendency, and variability. Boxplots use what is called a “box and whiskers” format, with the box in the center and two whiskers extending out from the box. This boxplot is displayed horizontally to align with the histogram above it, but boxplots also can be displayed vertically.

For larger data sets, use boxplots to informally compare the spread of data in different groups (**Graph** > **Boxplot** > **Multiple Ys**).

![enter image description here][4]

## Normal distribution

Normal distribution is the most common continuous distribution. Normal distribution describes many phenomena that occur in nature and industry. For example, the weight of apples from a recent harvest, or the amount of voltage in a new battery. Many statistical analyses require that the data come from normally distributed populations.

A normal distribution is completely described by mean and standard deviation of the data.

Many statistical methods are developed under the normality assumption, that is, the assumption that the data from the population fall into a normal distribution. But the assumption of normality is just that—an assumption. Therefore, testing the normality of the data is very important.

### Normality Testing

Doing the normality test in Minitab:

**Stat** > **Basic Statistics** > **Normality Test...**

![enter image description here][5]

If the P-Value is bigger than 0.05, we can see the data meet normal distribution.


  [1]: https://cdn2.content.compendiumblog.com/uploads/user/458939f4-fe08-4dbc-b271-efca0f5a2682/ba6a552e-3bc0-4eed-9c9a-eae3ade49498/Image/e5973cf36ebc52f58039d0e40b51dbd2/graphical_summary_w640.gif
  [2]: http://sites.stat.psu.edu/~ajw13/stat200/Fall06/00_courseIntro/graphics/minitab_plot.gif
  [3]: http://wps.prenhall.com/wps/media/objects/3550/3635712/Image58.gif
  [4]: https://cdn2.content.compendiumblog.com/uploads/user/458939f4-fe08-4dbc-b271-efca0f5a2682/ba6a552e-3bc0-4eed-9c9a-eae3ade49498/Image/0e068bdad01c167e1e29ce2f6ec0aa30/boxplot_of_group_1__group_2__group_3__group_4__group_5.jpg
  [5]: http://farm4.staticflickr.com/3040/2433059563_28c35e958b_o.jpg