import random
import pandas as pd
import numpy as np
import copy


def get_na_idx_by_col(df: pd.DataFrame) -> dict:
    """Return columns with row index of nan values"""
    na_idx_by_col = {}
    df_copy = df.copy()
    cols_with_na_mask = df_copy.apply(lambda col: col.isnull().values.any())
    cols_with_na = cols_with_na_mask[cols_with_na_mask == True].index
    for col in cols_with_na:
        na_idx_by_col[col] = df_copy[df_copy[col].isnull()].index.tolist()
    return na_idx_by_col


def get_imp_cols_accuracy(actual: pd.DataFrame, removed: pd.DataFrame, imputed: pd.DataFrame, ) -> dict:
    """Return imputation accuracy of each column"""
    act_copy = actual.copy().reset_index()
    imp_idx = get_na_idx_by_col(removed)
    cols_acc = {}
    for col, idx_vals in imp_idx.items():
        act = act_copy[col].iloc[idx_vals]
        imp = imputed[col].iloc[idx_vals]
        cols_acc[col] = sum(1 for a, i in zip(act, imp) if a == i) / float(len(act))
    return cols_acc

def remove_data(df: pd.DataFrame, p_rm):
    df_copy = copy.deepcopy(df.reset_index())

    for col in df_copy:
        if col != "index":
            # continue
            n_val = df_copy[col].notna().sum()
            n_rm = int(n_val * p_rm)
            idx_ = np.random.choice(df_copy[col].shape[0], n_rm, replace=False)

            df_copy.loc[idx_, col] = np.nan

    return df_copy 

def impute_cat_weighted_dist(complete_data: pd.DataFrame, amp_data: pd.DataFrame, cat: str) -> pd.Series:
    """
    Returns a list of imputed values based on weighted distribution of categories in complete dataset
    """
    cat_complete_dist = complete_data[cat].value_counts() / len(complete_data)
    cat_amp = amp_data[cat]
    cat_na = cat_amp[cat_amp.isna()]
    result = random.choices(population=cat_complete_dist.index, weights=cat_complete_dist.values, k=cat_na.size)
    return result


def undummify_cols(orig_data: pd.DataFrame, data_to_undummify: pd.DataFrame, dummified_col_list: list) -> pd.DataFrame:
    df_to_undummify = data_to_undummify.copy()
    dummy_cols_to_drop = []
    for col_name in dummified_col_list:
        dummy_col_names = list(set(','.join(orig_data[col_name].unique().tolist()).split(",")))
        dummy_cols_to_drop.extend(dummy_col_names)
        idx_cols_by_col_name = {col:df_to_undummify.columns.get_loc(col) for col in dummy_col_names}
        sorted_dummy_col_names = sorted(dummy_col_names, key=lambda x: idx_cols_by_col_name[x])
        df_to_undummify.loc[:,f"{col_name}_combined_dummies"] = df_to_undummify[sorted_dummy_col_names].apply(lambda x: x.tolist(), axis=1)  #{df_to_undummify.columns.get_loc(col):col for col in dummy_col_names}
        df_to_undummify.loc[:,f"{col_name}_undummified"] = df_to_undummify.loc[:,f"{col_name}_combined_dummies"].apply(lambda x: ','.join([sorted_dummy_col_names[idx] for idx, v in enumerate(x) if v == 1 or v == np.nan]))
    result = df_to_undummify[df_to_undummify.columns.drop(list(df_to_undummify.filter(regex="_combined_dummies")))]
    return result.drop(columns=dummy_cols_to_drop)

