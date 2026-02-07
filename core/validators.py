def count_check(src_df, tgt_df): return len(src_df) == len(tgt_df)
def duplicate_check(df, pk): return df[pk].is_unique
def incremental_check(src_df, tgt_df, inc_col):
    if not inc_col: return True
    return tgt_df[inc_col].max() >= src_df[inc_col].max()
