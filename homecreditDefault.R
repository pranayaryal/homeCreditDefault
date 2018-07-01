library(tidyverse)

setwd('~/.kaggle/competitions/home-credit-default-risk/')

credit_card_balance = read_csv('credit_card_balance.csv')

credit_card_balance %>% group_by(SK_ID_PREV) %>% mutate(count = n()) %>% head()
