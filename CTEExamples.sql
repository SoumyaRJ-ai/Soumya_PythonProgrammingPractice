INSERT INTO orders (id, date, customer_id, store, employee_id, amount)
values 
	(101, '2021-07-01', 234, 'East', 11, 198.00 ),
	(102, '2021-07-01', 675, 'West', 13, 799.00 ),
	(103, '2021-07-01', 456, 'West', 14, 698.00 ),
 	(104, '2021-07-01', 980, 'Center', 15, 99.00 ),
	(105, '2021-07-02', 594, 'Center', 16, 1045.45 ),
	(106, '2021-07-02', 435, 'East', 11, 599.00 ),
	(107, '2021-07-02', 246, 'West', 14, 678.89 ),
	(108, '2021-07-03', 256, 'East', 12, 458.80 ),
	(109, '2021-07-03', 785, 'East', 12, 99.00),
	(110, '2021-07-03', 443, 'Center', 16, 325.50 )

SELECT * from orders

--In our first example, we want to compare the total amount of each order with the average order 
--amount at the corresponding store.

WITH avg_per_store AS
(select AVG(amount) as avg_amount, store 
	from orders 
	group by store)

select o.id, o.store, o.amount, avgs.avg_amount
	from orders as o
	inner join
	avg_per_store as avgs
	on o.store = avgs.store

-- we want to see how the average order amount for each store compares to the 
-- minimum and the maximum of the average order amount among all stores.

WITH avg_amount_store AS 
(SELECT AVG(amount) as avg_amount, store 
	FROM ORDERS
	GROUP BY store
),
max_min_avg AS  
(SELECT MAX(avgs.avg_amount) as max_avg, MIN(avgs.avg_amount) as min_avg
	FROM avg_amount_store as avgs)

SELECT avgs.store, avgs.avg_amount, mm.max_avg, mm.min_avg
	FROM avg_amount_store as avgs
	CROSS JOIN
	max_min_avg as mm


-- Let’s say our company considers orders below $200 to be small and orders equal or above $200 to be big. 
-- Now, we want to calculate how many big orders and small orders each store had.

WITH stores AS 
(
	SELECT store from ORDERS
	GROUP BY store
),
big AS
(
	select store, count(id) as huge from orders
	where amount >= 200
	group by store
),
small AS
(
	select store, count(id) as less from orders
	where amount < 200
	group by store
)

select st.store as store, bg.huge as big_orders, sl.less as small_orders
from stores as st
FULL JOIN big as bg
ON st.store = bg.store
FULL JOIN small as sl
ON bg.store = sl.store






