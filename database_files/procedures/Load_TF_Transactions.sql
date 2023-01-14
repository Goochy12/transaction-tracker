CREATE PROCEDURE `Load_TF_Transactions` ()
BEGIN
INSERT INTO TF_Transactions (id, TD_Salary_id, TD_Rent_id, date, cost, description)
SELECT
tf.id
, IFNULL(salary.id, -1) AS TD_Salary_id
, IFNULL(rent.id, -1) AS TD_Rent_id
, tf.date
, tf.cost
, tf.description
FROM tmp_TF_Transactions tf
LEFT JOIN TD_Salary salary
ON tf.date between salary.effective_from AND salary.effective_to
LEFT JOIN TD_Rent rent
ON tf.date between rent.effective_from AND rent.effective_to
;

Truncate tmp_TF_Transactions;
END