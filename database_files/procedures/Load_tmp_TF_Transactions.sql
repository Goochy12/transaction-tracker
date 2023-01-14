CREATE PROCEDURE `Load_tmp_TF_Transactions` ()
BEGIN
    INSERT INTO tmp_TF_Transactions (meta_hash, id, date, cost, description)
    select
    meta_hash
    , id
    , date
    , cost
    , description
    from tblStg_Transactions
;
END