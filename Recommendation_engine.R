# Install packages
install.packages("readr")
install.packages("arules")

# load libraries
library(plyr)
library("arules")
library(readr)

# Set current working director
setwd("C:/Users/Chandler/Desktop/FtechX/Recomendation Engine Demo")
# load data
input <- read_csv("Transaction_file.csv")
# Get the list of merchants/items
merchant <- unique(input$individual_merchant)
merchant <- merchant[order(merchant)]
target_merchants <- merchant
sno <- 1:length(target_merchants)
merchant_ident <-cbind(target_merchants,sno)






View(merchant_ident)
