WITH total_by_nomenclature AS (
    SELECT
        orders2nomenclature.orders_id, orders2nomenclature.nomenclature_id,
        orders.clients_id,
        nomenclature.cost * orders2nomenclature.count AS total_by_nomenclature
    FROM orders2nomenclature
    JOIN public.nomenclature ON orders2nomenclature.nomenclature_id = nomenclature.id
    JOIN public.orders ON orders2nomenclature.orders_id = orders.id
),
total_by_orders AS (
    SELECT
        SUM(total_by_nomenclature.total_by_nomenclature) AS total_by_orders,
        total_by_nomenclature.orders_id, total_by_nomenclature.clients_id
    FROM total_by_nomenclature
    GROUP BY total_by_nomenclature.orders_id, total_by_nomenclature.clients_id
)
SELECT clients.name AS name, SUM(total_by_orders.total_by_orders) AS total
FROM clients
JOIN orders ON clients.id = orders.clients_id
JOIN total_by_orders ON total_by_orders.orders_id = orders.id
GROUP BY clients.name
ORDER BY total DESC
