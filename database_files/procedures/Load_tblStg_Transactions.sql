CREATE PROCEDURE `Load_tblStg_Transactions` ()
BEGIN
insert into tblStg_Transactions (id, date, cost, description, meta_hash)
(
	SELECT 
    id
    , STR_TO_DATE(date, "%d/%m/%Y") AS date
    , CONVERT(cost, DECIMAL(12,2)) AS cost
    , description
    , MD5(CONCAT(date, cost, description)) AS meta_hash
    FROM tblLnd_Transactions
);
END