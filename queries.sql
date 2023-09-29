SELECT
    c.login,
    COUNT(*) ordersQnt
FROM "Couriers" c
    JOIN "Orders" o ON o."courierId" = c.id
WHERE o."inDelivery" = TRUE
GROUP BY c.login;

SELECT track,
    CASE
        WHEN finished = TRUE THEN 2
        WHEN cancelled = TRUE THEN -1
        WHEN "inDelivery" = TRUE THEN 1
        ELSE 0
    END status
FROM "Orders";
