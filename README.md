# portfolio_analysis_visualization
A basic analysis and visualization of a portfolio containing several stocks: assigns random weights to each stock, shows progression of individual stock values and total portfolio net-worth over time, and volatility of the portfolio. It is based on [Python for Finance: Portfolio Statistical Data Analysis](https://www.coursera.org/projects/portfolio-assets-allocation-and-statistical-data-analysis).

Visualization is done via `plotly.express`, which is a part of the `plotly` (for `python`) package for interactive plotting. More information can be obtained [here](https://plotly.com/python/).

The csv file `stock_data.csv` contains stock prices for Facebook (FB), Twitter (TWTR), and Netflix (NFLX) from 7th November 2013 to 26th August 2020. This file is used here only for illustrative purposes. With minimal changes, any other stock data can be analyzed as well.

Note that interactive plots are not rendered in the default notebook viewer of GitHub, but can be seen clearly if `portfolio_analysis.ipynb` is opened in [Jupyter nbviewer](https://github.com/jupyter/nbviewer).
