CREATE PROCEDURE `LoadTblStg_Transactions` ()
BEGIN
insert into tblStg_Transactions (date, cost, description)
(
	SELECT 
    STR_TO_DATE(date, "%d/%m/%Y") AS date
    , CONVERT(cost, DECIMAL(12,2)) AS cost
    , description
    FROM tblLnd_Transactions
);
END