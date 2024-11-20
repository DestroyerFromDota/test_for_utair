Напишите следующие SQL-запросы:
1. возвращающий пользователей, у которых суммарно размер транзакций списаний превышает 500;

SELECT a.id
FROM account a
JOIN transaction t ON a.id = t.account
JOIN transaction_balance tb ON t.id = tb.transaction_id
WHERE tb.amount < 0  
GROUP BY a.id
HAVING SUM(tb.amount) < -500;  
===============================================================================================================
2. возвращающий отсортированный по дате список всех транзакций только начислений для учётных
записей, созданных с 2020 года;

SELECT t.id, t.created_at, tb.amount
FROM transaction t
JOIN account a ON a.id = t.account
JOIN transaction_balance tb ON t.id = tb.transaction_id
WHERE tb.amount > 0 
AND a.created_id >= '2020-01-01'  -- если поддерживает лексографическое сравнение времени и даты как строк. Если нет AND a.created_id >= '2020-01-01'
								  -- AND a.created_id >= TO_DATE('2020-01-01') Если не поддерживает. Но если не поддерживает, то это большая боль, честно говоря, работать так с датой и временем
                                  -- просто в примере указан тип данных TIMESTAMP
ORDER BY t.created_at;  

===============================================================================================================
3. возвращающий всех пользователей, у которых не было ни одной транзакции в 2020 году.
SELECT a.id
FROM account a
LEFT JOIN transaction t ON a.id = t.account AND YEAR(t.created_at) = 2020
WHERE t.id IS NULL;  
