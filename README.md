# Practical Data Wrangling
This is the code repository for [Practical Data Wrangling](https://www.packtpub.com/big-data-and-business-intelligence/practical-data-wrangling?utm_source=github&utm_medium=repository&utm_campaign=9781787286139), published by [Packt](https://www.packtpub.com/?utm_source=github). It contains all the supporting project files necessary to work through the book from start to finish.
## About the Book
Around 80% of time in data analysis is spent on cleaning and preparing data for analysis. This is, however, an important task, and is a prerequisite to the rest of the data analysis workflow, including visualization, analysis and reporting. Python and R are considered a popular choice of tool for data analysis, and have packages that can be best used to manipulate different kinds of data, as per your requirements. This book will show you the different data wrangling techniques, and how you can leverage the power of Python and R packages to implement them.
## Instructions and Navigation
All of the code is organized into folders. Each folder starts with a number followed by the application name. For example, Chapter02.



The code will look like the following:
```
fin = open('data/fake_weather_data.csv','r',newline='')
reader = csv.reader(fin)
for row in reader:
    myData.append(row)
```

You will need a Python 3 installation on your computer, and you will need to be able to execute Python from your operating system’s command-line interface. In addition, the following external Python modules will be used:

pandas (Chapters 4 and 5)
requests (Chapter 8)
PyMongo (Chapter 9)
For Chapter 9, you will need to install MongoDB and set up your own local MongoDB server.
For Chapters 6 and 7, you will need RStudio and Rbase. Additionally, for Chapter 7, you will need the dplyr and tibble libraries.

## Related Products
* [Practical Big Data Analytics](https://www.packtpub.com/big-data-and-business-intelligence/practical-big-data-analytics?utm_source=github&utm_medium=repository&utm_campaign=9781783554393)

* [Practical Real-time Data Processing and Analytics](https://www.packtpub.com/big-data-and-business-intelligence/practical-real-time-data-processing-and-analytics?utm_source=github&utm_medium=repository&utm_campaign=9781787281202)

* [Practical Data Science Cookbook - Second Edition](https://www.packtpub.com/big-data-and-business-intelligence/practical-data-science-cookbook-second-edition?utm_source=github&utm_medium=repository&utm_campaign=9781787129627)

### Suggestions and Feedback
[Click here](https://docs.google.com/forms/d/e/1FAIpQLSe5qwunkGf6PUvzPirPDtuy1Du5Rlzew23UBp2S-P3wB-GcwQ/viewform) if you have any feedback or suggestions.
