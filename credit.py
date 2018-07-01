
from __future__ import division
import pandas as pd
import numpy as np

import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import missingno as msno
import xgboost
import numpy as np
import lightgbm

from imblearn.over_sampling import SMOTE

print 'Reading train ...'
train = pd.read_csv('application_train.csv')
print 'Shape of train is %s'%(str(train.shape))
bureau_balance = pd.read_csv('bureau_balance.csv')
print 'The shape of bureau_balance is %s'%(str(bureau_balance.shape))
credit_card_balance = pd.read_csv('credit_card_balance.csv')
print 'The shape of creditcard_balance is %s'%(str(credit_card_balance.shape))
installments_payments = pd.read_csv('installments_payments.csv')
print 'The shape of installments_payments is %s'%(str(installments_payments.shape))
pos_cash_balance = pd.read_csv('POS_CASH_balance.csv')
print 'The shape of pos_cash_balance is %s'%(str(pos_cash_balance.shape))
previous_application = pd.read_csv('previous_application.csv')
print 'The shape of previous_application is %s'%(str(previous_application.shape))
descriptions = pd.read_csv('HomeCredit_columns_description.csv')
print 'The shape of descriptions is %s'%(str(descriptions.shape))
bureau = pd.read_csv('bureau.csv')
print 'The shape of bureau is %s'%(str(bureau.shape))
print 'Done!'