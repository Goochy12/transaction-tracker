CREATE PROCEDURE `Load_tmp_TF_Trancactions` ()
BEGIN
    INSERT INTO tmp_TF_Transactions (id, date, cost, description)
    select
    id
    , date
    , cost
    , description
    from tblStg_Transactions
;
END