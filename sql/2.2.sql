WITH first_categories AS (
    SELECT
        categories.id, categories.materialize_path
    FROM categories
    WHERE categories.materialize_path LIKE '_'
    ORDER BY materialize_path
),
first_categories_sum AS(
    SELECT
        first_categories.materialize_path,
        SUM(nomenclature.count) AS total
    FROM nomenclature
    JOIN categories ON nomenclature.categories_id = categories.id
    JOIN
        first_categories
        ON categories.materialize_path
        LIKE CONCAT(first_categories.materialize_path, '%')
    GROUP BY first_categories.materialize_path
)
SELECT
    categories.name, first_categories_sum.total
FROM categories
JOIN
    first_categories_sum
    ON first_categories_sum.materialize_path = categories.materialize_path