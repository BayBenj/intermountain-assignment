-- declare
--
-- v_id  number := 1 ;
-- v_name varchar2(20) ;
-- v_region varchar2(20);
-- v_pop number ;

-- begin

INSERT INTO customer
(id,name,email)
 values(1,"Bob","bob33@gmail.com");

INSERT INTO customer
(id,name,email)
 values(2,"Hannah","thehannah@gmail.com");

INSERT INTO customer
(id,name,email)
 values(3,"Benjamin","benj@gmail.com");

INSERT INTO item
(id,name,price)
 values(1,"shoes",44.99);

INSERT INTO item
(id,name,price)
 values(2,"sunglasses",24.99);

INSERT INTO item
(id,name,price)
 values(3,"socks",7.99);

INSERT INTO purchase
(id,item_id,the_time)
 values(1,3,datetime('2003/12/13 12:13:00', 'YYYY/MM/DD HH:MI:SS'));

INSERT INTO purchase
(id,item_id,the_time)
 values(2,1,datetime('20013/8/3 10:10:43', 'YYYY/MM/DD HH:MI:SS'));

INSERT INTO purchase
(id,item_id,the_time)
 values(3,2,datetime('2004/7/5 15:56:18', 'YYYY/MM/DD HH:MI:SS'));

INSERT INTO purchase
(id,item_id,the_time)
 values(4,3,datetime('2009/3/22 12:44:06', 'YYYY/MM/DD HH:MI:SS'));

INSERT INTO customer_purchases
(purchaseID,customerID)
 values(1,2);

INSERT INTO customer_purchases
(purchaseID,customerID)
 values(2,2);

INSERT INTO customer_purchases
(purchaseID,customerID)
 values(3,1);

INSERT INTO customer_purchases
(purchaseID,customerID)
 values(4,3);


-- commit;
-- end;













--
