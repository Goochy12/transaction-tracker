CREATE PROCEDURE `Load_TF_Transactions` ()
BEGIN
SELECT
date
, cost
, description
FROM tblStg_Transactions
WHERE cost < 0
END