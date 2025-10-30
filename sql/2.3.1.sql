CREATE VIEW report AS
WITH first_categories AS (
    SELECT categories.id, categories.materialize_path, categories.name
    FROM categories
    WHERE categories.materialize_path LIKE '_'
    ORDER BY materialize_path
),
first_categories_name AS(
    SELECT
        first_categories.materialize_path,
        first_categories.name, categories.id
    FROM categories
    JOIN
        first_categories
        ON categories.materialize_path
        LIKE CONCAT(first_categories.materialize_path, '%')
),
total_by_nomenclature AS (
    SELECT
        orders2nomenclature.nomenclature_id,
        SUM(orders2nomenclature.count) AS total_by_nomenclature
    FROM orders2nomenclature
    JOIN public.nomenclature ON orders2nomenclature.nomenclature_id = nomenclature.id
    GROUP BY orders2nomenclature.nomenclature_id
    ORDER BY total_by_nomenclature DESC
    LIMIT 5
)
SELECT first_categories_name.name AS category_name, nomenclature.name, nomenclature.id, total_by_nomenclature.total_by_nomenclature
FROM total_by_nomenclature
JOIN nomenclature ON total_by_nomenclature.nomenclature_id = nomenclature.id
JOIN categories ON nomenclature.categories_id = categories.id
JOIN first_categories_name ON first_categories_name.id = categories.id
ORDER BY total_by_nomenclature.total_by_nomenclature DESC