

class MyUtils:
    
    def __init__(self, df):
        self.df = df
        
    def get_nulls(self):
        nulls = self.df.isnull().sum() * 100/self.df.shape[0]
        return nulls
    
    #checking if writing works
    def get_nas(self):
        nulls = self.df.isna().sum() * 100/self.df.shape[0]
        return nulls
    
    def train_ensembled(self):
        train_zeros = self.df[self.df.TARGET == 0]
        train_ones = self.df[self.df.TARGET == 1]
        sampled_indices = np.random.choice(train_zeros.index, size=[11, train_ones.shape[0]], replace=False)
        print 'shape of sampled indices is %s'%(str(sampled_indices.shape))
        ensembled = np.zeros([11, test.shape[0]])
        preds_list = []
        for i in range(11):
            print 'starting %s th sample'%(str(i))
            new_train = pd.concat([train_zeros.loc[sampled_indices[i]], train_ones])
            train_y = new_train.TARGET
            train_x = new_train.drop(['TARGET', 'SK_ID_CURR'], axis=1)
            test_dropid = test.drop(['SK_ID_CURR'], axis=1)
            concatted = pd.concat([train_x, test_dropid])
            concatted_dummied = pd.get_dummies(concatted)
            imputed_concatted = my_imputer.fit_transform(concatted_dummied)
            imputed_concatted_df = pd.DataFrame(imputed_concatted)
            imputed_concatted_df.columns = concatted_dummied.columns
            #split them back to train and test
            train_x_after_impute = imputed_concatted_df[:train_x.shape[0]]
            test_x = imputed_concatted_df[train_x.shape[0]:]
            clf.fit(train_x_after_impute, train_y)
            preds = clf.predict_proba(test_x)
            pred_actual = preds[:,1]
            ensembled[i] = pred_actual
        return ensembled
    
    
    def getSkidCount(self):
        count_skid_prev = self.df.SK_ID_CURR.value_counts()
        count_skid_df = count_skid_prev.to_frame()
        count_skid_df['count'] = count_skid_prev.values
        count_skid_df['SK_ID_CURR'] = count_skid_df.index
        count_skid_df = count_skid_df.rename_axis(None)
        return count_skid_df
    
    def randomChoice(self):
        sampled_indices = np.random.choice(self.df.index, size=[11, self.df.shape[0]], replace=False)
        print 'The shape of sampled_indices array is %s'%(str(sampled_indices.shape))
        return sampled_indices
    
    def createEnsemblesUndersample(self):
        test_merged = test.merge(count_skid_df, on='SK_ID_CURR')
        not_included = [ ind for ind in test.index if ind not in test_merged.index ]
        not_included_in_merge = test.loc[not_included]
        not_included_in_merge['count_cc'] = test_merged['count_cc'].median()
        test_merged_imputed = pd.concat([test_merged, not_included_in_merge])

        ensembled = np.zeros([11, test.shape[0]])
        preds_list = []
        for i in range(11):
            print 'starting %s th sample'%(str(i))
            new_train = pd.concat([train_zeros.loc[sampled_indices[i]], train_ones])
            new_train_merged = new_train.merge(count_skid_df, on='SK_ID_CURR')
            train_y = new_train_merged.TARGET
            train_x = new_train_merged.drop(['TARGET', 'SK_ID_CURR'], axis=1)
            test_dropid = test_merged_imputed.drop(['SK_ID_CURR'], axis=1)
            concatted = pd.concat([train_x, test_dropid])
            concatted_dummied = pd.get_dummies(concatted)
            imputed_concatted = my_imputer.fit_transform(concatted_dummied)
            imputed_concatted_df = pd.DataFrame(imputed_concatted)
            imputed_concatted_df.columns = concatted_dummied.columns
            #split them back to train and test
            train_x_after_impute = imputed_concatted_df[:train_x.shape[0]]
            test_x = imputed_concatted_df[train_x.shape[0]:]
            clf.fit(train_x_after_impute, train_y)
            preds = clf.predict_proba(test_x)
            pred_actual = preds[:,1]
            ensembled[i] = pred_actual
        #     preds_list.append(pred_actual)
        print 'Done!!'
        
    
    def printColDesc(self, descr):
        for col in self.df.columns:
            if col not in ['SK_ID_CURR', 'SK_ID_PREV']:
                print col, descr[descr.Row == str(col)].Description.unique()
    
    def computeInstallPaymentColumns(self):
        print 'you are here'
        self.df['diff_amount'] = self.df.AMT_INSTALMENT - self.df.AMT_PAYMENT
        self.df['diff_days'] = self.df.DAYS_INSTALMENT - self.df.DAYS_ENTRY_PAYMENT
    